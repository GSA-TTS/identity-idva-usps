""" Views for USPS API """
from django.http import JsonResponse


async def hello_world(_request):
    """ Hello world view """
    return JsonResponse({"message": "Hello, world!"})
