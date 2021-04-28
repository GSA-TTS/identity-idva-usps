""" Serializers for Generating Swagger Documentation """
from rest_framework import serializers


class ConfidenceIndicatorRequestSerializer(serializers.Serializer):
    """ Serializer for Confidence Indicator Requests """

    uid = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    suffix = serializers.CharField(required=False)
    delivery_address = serializers.CharField()
    address_city_state_zip = serializers.CharField()


class ConfidenceIndicatorResponseSerializer(serializers.Serializer):
    """ Serializer for Confidence Indicator Responses """

    uid = serializers.UUIDField()
    indicator = serializers.CharField()
