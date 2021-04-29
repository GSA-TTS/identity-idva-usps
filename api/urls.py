""" USPS API app url definitions """
from django.urls import path
from api import views

urlpatterns = [
    path(
        "confidenceindicator", views.confidence_indicator, name="confidence_indicator"
    ),
]
