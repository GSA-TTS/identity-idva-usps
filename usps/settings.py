"""
Configuration for the USPS microservice settings.
Context is switched based on if the app is in debug mode.
"""
import os

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG set is set to True if env var is "True"
DEBUG = os.getenv("DEBUG", "False") == "True"

USPS_CLIENT_ID = os.getenv("USPS_CLIENT_ID")
USPS_CLIENT_SECRET = os.getenv("USPS_CLIENT_SECRET")
USPS_URL = os.getenv("USPS_URL")
