""" USPS API unit tests """
import json
from http import HTTPStatus
from django.test import SimpleTestCase


class HelloWorldTest(SimpleTestCase):
    """ Hello world view tests """

    def test_hello_world(self):
        response = self.client.get("/usps/hello")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.getvalue()), {"message": "Hello, world!"})
