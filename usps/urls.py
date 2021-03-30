from django.urls import path
from usps import views

urlpatterns = [
    path("hello", views.hello_world, name="hello"),
]
