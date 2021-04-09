""" Views for USPS API """
import uuid
import json
import os
from django.http import JsonResponse, HttpResponseBadRequest
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from api import transaction_log

USPS_UUID = str(uuid.uuid4())

# Create USPS credentials
credentials = service_account.IDTokenCredentials.from_service_account_info(
    json.loads(os.environ["USPS_SERVICE_INFO"]),
    target_audience="270619257825-1lduq3l1s7d2m6tdtjhfd7bi4686s3eu.apps.googleusercontent.com",
)
authed_session = AuthorizedSession(credentials)
authed_session.verify = "cat-aii-root.cer"


async def confidence_indicator(request):
    """ USPS AII API view """
    # Log the transaction
    csp_id = request.META["HTTP_X_CONSUMER_CUSTOM_ID"]
    log_response = await transaction_log.create_transaction(csp_id)

    if log_response.status_code != 200:
        return log_response

    try:
        json_body = json.loads(request.body)
        json_payload = {
            "uid": USPS_UUID,
            "first_name": json_body["first_name"],
            "last_name": json_body["last_name"],
            "middle_name": json_body["middle_name"],
            "suffix": json_body["suffix"],
            "delivery_address": json_body["delivery_address"],
            "address_city_state_zip": json_body["address_city_state_zip"],
        }
    except json.JSONDecodeError as error:
        return HttpResponseBadRequest("Request body was not valid JSON")
    except KeyError as error:
        return HttpResponseBadRequest(f"Missing field: {error}")

    # Send test request to USPS API
    response = authed_session.post("https://cat-aii.usps.gov/", json=json_payload)

    return JsonResponse(response.json())
