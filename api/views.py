""" Views for USPS API """
import json
import base64
import logging
import ssl
import aiohttp
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from api import transaction_log


USPS_UUID = "5738f577-d283-49ec-9695-32b106c049d8"
USPS_URL = "https://cat-aii.usps.gov/"

# Create USPS credentials
credentials = service_account.IDTokenCredentials.from_service_account_info(
    json.loads(base64.b64decode(settings.USPS_SERVICE_INFO)),
    target_audience=settings.USPS_TARGET_AUDIENCE,
)
credentials.refresh(Request())
sslcontext = ssl.create_default_context(cafile="cat-aii-root.cer")
# authed_session = AuthorizedSession(credentials)
# authed_session.verify = "cat-aii-root.cer"


async def confidence_indicator(request):
    """ USPS AII API view """
    # Ensure the request contained the required fields and build the
    # USPS request payload
    try:
        json_body = json.loads(request.body)
        payload = {
            "uid": USPS_UUID,
            "first_name": json_body["first_name"],
            "last_name": json_body["last_name"],
            "middle_name": json_body["middle_name"],
            "suffix": json_body["suffix"],
            "delivery_address": json_body["delivery_address"],
            "address_city_state_zip": json_body["address_city_state_zip"],
        }
    except json.JSONDecodeError as error:
        return JsonResponse({"error": "Request body was not valid JSON"}, status=400)
    except KeyError as error:
        return JsonResponse({"error": f"Missing field: {error}"}, status=400)

    if settings.DEBUG:
        logging.debug("Skipping network requests while in debug mode")
        return JsonResponse({"uid": USPS_UUID, "confidence_indicator": "50.00"})

    # Log the transaction
    csp_id = request.META["HTTP_X_CONSUMER_CUSTOM_ID"]
    log_response = await transaction_log.create_transaction(csp_id)

    if log_response.status_code != 200:
        return log_response

    # Ensure USPS credentials are valid and post to USPS address validation API
    if not credentials.valid:
        credentials.refresh(Request())

    headers = {"authorization": f"bearer {credentials.token}"}

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(USPS_URL, json=payload, ssl=sslcontext) as response:
                # See if you can avoid the json serialization/deserialization here
                body = await response.read()
            return HttpResponse(body, response.status)
    except aiohttp.ClientError as error:
        return JsonResponse(
            {"error": f"aiohttp error while validating address: {error}"}
        )
