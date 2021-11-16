""" USPS API unit tests """
from fastapi.testclient import TestClient
from usps.main import app

client = TestClient(app)


def usps_microservice_request(request):
    """Helper function that makes parameterized requests to the USPS Microservice."""
    return client.post("/confidence_indicator", json=request)


def test_successful_response():
    """Test successful 200 response from USPS Microservice"""
    request = {
        "uid": "5738f577-d283-49ec-9695-32b106c049d8",
        "first_name": "James",
        "last_name": "Smith",
        "delivery_address": "123 Test Road",
        "address_city_state_zip": "Test Test 12345",
    }
    response = usps_microservice_request(request)
    assert response.status_code == 200


def test_failed_response_missing_first_name():
    """Test fail 422 response from USPS Microservice with missing first_name"""

    request = {
        "uid": "5738f577-d283-49ec-9695-32b106c049d8",
        "last_name": "Smith",
        "delivery_address": "123 Test Road",
        "address_city_state_zip": "Test Test 12345",
    }
    response = usps_microservice_request(request)
    assert response.status_code == 422


def test_failed_response_missing_last_name():
    """Test fail 422 response from USPS Microservice with missing last_name"""

    request = {
        "uid": "5738f577-d283-49ec-9695-32b106c049d8",
        "first_name": "James",
        "delivery_address": "123 Test Road",
        "address_city_state_zip": "Test Test 12345",
    }
    response = usps_microservice_request(request)
    assert response.status_code == 422


def test_failed_response_missing_delivery_address():
    """Test fail 422 response from USPS Microservice with missing delivery_address"""

    request = {
        "uid": "5738f577-d283-49ec-9695-32b106c049d8",
        "first_name": "James",
        "last_name": "Smith",
        "address_city_state_zip": "Test Test 12345",
    }
    response = usps_microservice_request(request)
    assert response.status_code == 422


def test_failed_response_missing_address_city_state_zip():
    """Test fail 422 response from USPS Microservice with missing address_city_state_zip"""

    request = {
        "uid": "5738f577-d283-49ec-9695-32b106c049d8",
        "first_name": "James",
        "last_name": "Smith",
        "delivery_address": "123 Test Road",
    }
    response = usps_microservice_request(request)
    assert response.status_code == 422
