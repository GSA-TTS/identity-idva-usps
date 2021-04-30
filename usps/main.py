import logging
import ssl
import base64
from usps import transaction_log
from http import HTTPStatus
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from aiohttp import ClientSession, ClientError
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from usps.config import settings
from google.oauth2 import service_account
from google.auth.transport.requests import Request

app = FastAPI()


class AddressVerificationInfo(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    suffix: Optional[str] = None
    delivery_address: str
    address_city_state_zip: str


class VerifiedResponse(BaseModel):
    uid: UUID
    confidence_indicator: str


class ErrorResponse(BaseModel):
    uid: UUID
    error: str


USPS_UUID = "5738f577-d283-49ec-9695-32b106c049d8"
USPS_URL = "https://cat-aii.usps.gov/"

if not settings.DEBUG:
    credentials = service_account.IDTokenCredentials.from_service_account_info(
        json.loads(base64.b64decode(settings.USPS_SERVICE_INFO)),
        target_audience=settings.USPS_TARGET_AUDIENCE,
    )
    credentials.refresh(Request())
    sslcontext = ssl.create_default_context(cafile="cat-aii-root.cer")


@app.post(
    "/confidence_indicator",
    response_model=VerifiedResponse,
    responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)
async def confidence_indicator(
    address_verification_info: AddressVerificationInfo,
    http_x_consumer_custom_id: str = Header(None),
):
    if settings.DEBUG:
        logging.debug("Skipping network requests while in debug mode")
        return JSONResponse({"uid": USPS_UUID, "confidence_indicator": "50.00"})

    if not credentials.valid:
        credentials.refresh(Request())
        logging.info("Refreshed credentials")

    headers = {
        "authorization": f"bearer {credentials.token}",
        "content-type": "application/json",
    }

    try:
        async with ClientSession(headers=headers) as session:
            log_response = await transaction_log.create_transaction(
                session, http_x_consumer_custom_id
            )
            if log_response.status_code != HTTPStatus.CREATED:
                return transaction_log.transaction_unavailable_response

            async with session.post(
                USPS_URL, data=address_verification_info.dict(), ssl=sslcontext
            ) as response:
                return JSONResponse(
                    status_code=response.status, content=await response.read()
                )
    except ClientError as error:
        logging.error("Aiohttp error: %s", error)
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={"error": "ClientError while validating address"},
        )
