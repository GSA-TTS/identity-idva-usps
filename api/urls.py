""" USPS API app url definitions """
from django.urls import path
from api import views
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from drf_yasg import openapi
from .serializers import (
    ConfidenceIndicatorRequestSerializer,
    ConfidenceIndicatorResponseSerializer,
)

decorated_confidence_indicator_view = swagger_auto_schema(
    method="post",
    request_body=ConfidenceIndicatorRequestSerializer,
    responses={
        status.HTTP_200_OK: ConfidenceIndicatorResponseSerializer,
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Missing Fields",
            examples={
                "application/json": {
                    "uid": "90c0a824-d5f6-4e18-8420-efd7464f436a",
                    "error": "Mandatory field(s) missing (first_name, last_name)",
                },
            },
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="Internal Server Error",
            examples={
                "application/json": {
                    "uid": "90c0a824-d5f6-4e18-8420-efd7464f436a",
                    "error": "Internal Server error",
                }
            },
        ),
    },
)(views.confidence_indicator)

urlpatterns = [
    path(
        "confidenceindicator",
        decorated_confidence_indicator_view,
        name="confidence_indicator",
    ),
]
