""" USPS Project URL definitions """
from django.urls import include, path

urlpatterns = [path("usps/", include("api.urls"))]
