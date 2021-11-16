"""
USPS Microservice FastAPI Web App.
"""

import json
import logging
import time
import requests
from typing import Optional
from uuid import UUID
from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from aiohttp import ClientSession, ClientError
from pydantic import BaseModel
from starlette_prometheus import metrics, PrometheusMiddleware
from usps import settings

from requests.auth import HTTPBasicAuth

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)

logging.getLogger().setLevel(logging.INFO)

app.token = ""
app.expires = 0


class AddressVerificationInfo(BaseModel):
    """
    Request model for the USPS AII /confidence_indicator API.
    """

    uid: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    suffix: Optional[str] = None
    delivery_address: str
    address_city_state_zip: str


class VerifiedResponse(BaseModel):
    """
    Response model for valid (2XX) responses from the USPS API.
    """

    uid: UUID
    confidence_indicator: str


class ErrorResponse(BaseModel):
    """
    Response model for failed (non-2XX) responses from the USPS API.
    """

    uid: UUID
    error: str


def get_token():
    client_id = settings.USPS_CLIENT_ID
    client_secret = settings.USPS_CLIENT_SECRET
    access_token_url = f"{settings.USPS_URL}/accesstoken?grant_type=client_credentials"
    auth_response = requests.post(
        access_token_url, auth=HTTPBasicAuth(client_id, client_secret), verify=True
    )
    if auth_response.status_code == HTTPStatus.OK:
        app.expires = (
            int(auth_response.json["issued_at"]) // 1000
            + int(auth_response.json["expires_in"])
            - 60
        )
        app.token = auth_response.json["access_token"]
    else:
        logging.error(
            f"Failed to refresh token: {auth_response.status_code} {auth_response.text}"
        )


@app.post(
    "/confidence_indicator",
    response_model=VerifiedResponse,
    responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)
async def confidence_indicator(address_verification_info: AddressVerificationInfo):
    """
    Confidence Indicator function that proxies requests to the USPS API.
    """

    if settings.DEBUG:
        logging.debug("Skipping network requests while in debug mode")
        return JSONResponse(
            {
                "uid": "5738f577-d283-49ec-9695-32b106c049d8",
                "confidence_indicator": "50.00",
            }
        )

    if round(time.time()) > app.expires:
        logging.info("Refreshing credentials")
        get_token()

    headers = {"authorization": f"Bearer {app.token}"}

    try:
        async with ClientSession(headers=headers) as session:
            async with session.post(
                f"{settings.USPS_URL}/confidenceindicator",
                json=address_verification_info.dict(),
            ) as response:
                return JSONResponse(
                    status_code=response.status, content=await response.json()
                )
    except ClientError as error:
        logging.error("Aiohttp error: %s", error)
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "error": "A server error occurred while makeing address validation request"
            },
        )
