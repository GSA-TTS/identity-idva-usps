"""
Configuration for USPS Microservice environmental variables.
Context is switched based on if the app is in debug mode.
"""
from typing import Union, Optional, ClassVar
from pydantic import BaseSettings, parse_obj_as
from typing_extensions import Literal


class DebugContext(BaseSettings):
    """
    Environmental variables for debug mode.
    These are used when DEBUG is set to True.
    """

    DEBUG: Literal[True]
    TRANSACTION_ROUTE: ClassVar[str] = "localhost"


class ProdContext(BaseSettings):
    """
    Environmental variables for production mode.
    These are used when DEBUG is not set to True.
    """

    DEBUG: Optional[bool] = False
    USPS_SERVICE_INFO: str
    USPS_TARGET_AUDIENCE: str
    TRANSACTION_ROUTE: str


settings = parse_obj_as(Union[DebugContext, ProdContext], {})
