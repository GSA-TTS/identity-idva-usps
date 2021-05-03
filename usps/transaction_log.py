""" Transaction Logging functionality """
import logging
import aiohttp
from usps import settings
from fastapi.responses import JSONResponse

TRANSACTION_ROUTE = settings.TRANSACTION_ROUTE
TRANSACTION_URL = f"http://{TRANSACTION_ROUTE}:8080/transaction/"

transaction_unavailable_response = JSONResponse(
    status_code=503,
    content={
        "error": "Transaction service temporarily unavailable. Check system logs for more information."
    },
)


async def create_transaction(
    session: aiohttp.ClientSession, csp: str, cost=0, result=None
) -> JSONResponse:
    """
    Log a transaction to the transaction logging microservice.
    Returns the transaction log information on success, otherwise a 503 response
    defined by transaction_unavailable_response.
    """
    payload = {
        "service_type": "PROOFING SERVICE",
        "provider": "idemia",
        "csp": csp,
        "cost": cost,
        "result": result,
    }

    try:
        async with session.post(TRANSACTION_URL, json=payload) as response:
            response.raise_for_status()
            body = await response.read()
            return JSONResponse(status_code=response.status, content=body)
    except aiohttp.ClientError as error:
        logging.error("Create transaction request raised exception: %s", error)
        return transaction_unavailable_response
