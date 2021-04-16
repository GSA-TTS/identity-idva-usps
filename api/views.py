""" Views for USPS API """
import json
import base64
import logging
import ssl
from http import HTTPStatus
from aiohttp import ClientSession, ClientError
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from api import transaction_log


USPS_UUID = "5738f577-d283-49ec-9695-32b106c049d8"
USPS_URL = "https://cat-aii.usps.gov/"

# Create USPS credentials
if not settings.DEBUG:
    credentials = service_account.IDTokenCredentials.from_service_account_info(
        json.loads(base64.b64decode(settings.USPS_SERVICE_INFO)),
        target_audience=settings.USPS_TARGET_AUDIENCE,
    )
    credentials.refresh(Request())
    sslcontext = ssl.create_default_context(cafile="cat-aii-root.cer")


async def confidence_indicator(request):
    """ USPS AII API view """
    if settings.DEBUG:
        logging.debug("Skipping network requests while in debug mode")
        return JsonResponse({"uid": USPS_UUID, "confidence_indicator": "50.00"})

    # Ensure USPS credentials are valid and post to USPS address validation API
    if not credentials.valid:
        credentials.refresh(Request())
        logging.info("Refreshed credentials")

    csp_id = request.META["HTTP_X_CONSUMER_CUSTOM_ID"]

    headers = {
        "authorization": f"bearer {credentials.token}",
        "content-type": "application/json",
    }

    try:
        async with ClientSession(headers=headers) as session:
            log_response = await transaction_log.create_transaction(session, csp_id)
            if log_response.status_code != HTTPStatus.CREATED:
                return transaction_log.transaction_unavailable_response

            async with session.post(
                USPS_URL, data=request.body, ssl=sslcontext
            ) as response:
                return HttpResponse(await response.read(), response.status)
    except ClientError as error:
        logging.error("Aiohttp error: %s", error)
        return JsonResponse({"error": "ClientError while validating address"})
