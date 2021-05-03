""" USPS API unit tests """
from fastapi.testclient import TestClient
from usps.main import app

client = TestClient(app)


def test_read_main():
    """
    Stub unit test.
    """
    # response = client.get("/")
    # assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}
