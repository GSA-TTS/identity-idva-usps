""" USPS API app url definitions """
from django.urls import path
from api import views

urlpatterns = [
    path("hello", views.hello_world, name="hello"),
]
