""" Views for USPS API """
from django.http import JsonResponse
from api import transaction_log


async def hello_world(request):
    """ Hello world view """
    csp_id = request.META["HTTP_X_CONSUMER_CUSTOM_ID"]
    log_response = await transaction_log.create_transaction(csp_id)

    if log_response.status_code != 200:
        return log_response

    return JsonResponse({"message": "Hello, world!"})
