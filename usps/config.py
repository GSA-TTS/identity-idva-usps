from pydantic import BaseSettings, parse_obj_as
from typing import Union, Optional, ClassVar
from typing_extensions import Literal


class DebugContext(BaseSettings):
    DEBUG: Literal["True"]
    TRANSACTION_ROUTE: ClassVar[str] = "localhost"


class ProdContext(BaseSettings):
    DEBUG: Optional[str] = "False"
    USPS_SERVICE_INFO: str
    USPS_TARGET_AUDIENCE: str
    TRANSACTION_ROUTE: str


settings = parse_obj_as(Union[DebugContext, ProdContext], {})
