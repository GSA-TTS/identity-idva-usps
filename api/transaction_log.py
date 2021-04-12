""" Transaction Logging functionality """
import logging
import os
import aiohttp
from django.conf import settings
from django.http import JsonResponse

# TRANSACTION_URL = "http://localhost:8000/transaction/"
TRANSACTION_ROUTE = os.environ.get("TRANSACTION_ROUTE")
TRANSACTION_URL = f"http://{TRANSACTION_ROUTE}:8080/transaction/"

DEBUG_RESPONSE = JsonResponse({"record_uuid": "fake-uuid"})

transaction_unavailable_response = JsonResponse(
    {
        "error": "Transaction service temporarily unavailable. Check system logs for more information."
    },
    status=503,
)


async def create_transaction(csp: str, cost=0, result=None) -> JsonResponse:
    """
    Log a transaction to the transaction logging microservice.
    Returns the transaction log information on success, otherwise a 503 response
    defined by transaction_unavailable_response.
    """
    if settings.DEBUG:
        logging.debug("Skipping transaction logging while in debug mode")
        return DEBUG_RESPONSE  # Skip sending a transaction log in debug mode

    payload = {
        "service_type": "PROOFING SERVICE",
        "provider": "idemia",
        "csp": csp,
        "cost": cost,
        "result": result,
    }

    try:
        async with aiohttp.request("POST", TRANSACTION_URL, json=payload) as response:
            transaction_result = await response.json()
    except aiohttp.ClientError as error:
        logging.error("Create transaction request raised exception: %s", error)
        return transaction_unavailable_response

    return JsonResponse(transaction_result)


async def update_transaction_result(record_uuid: str, result: str) -> JsonResponse:
    """
    Update information in an existing transaction record
    Returns the transaction log information on success, otherwise a 503 response
    defined by transaction_unavailable_response.
    """
    if settings.DEBUG:
        logging.debug("Skipping transaction logging update while in debug mode")
        return DEBUG_RESPONSE  # Skip sending a transaction log in debug mode

    url = f"{TRANSACTION_URL}{record_uuid}/"

    try:
        async with aiohttp.request("PATCH", url, json={"result": result}) as response:
            transaction_result = await response.json()
    except aiohttp.ClientError as error:
        logging.error("Update transaction raised exception: %s", error)
        return transaction_unavailable_response

    return JsonResponse(transaction_result)
