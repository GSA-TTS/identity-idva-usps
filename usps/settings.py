"""
Configuration for the USPS microservice settings.
Context is switched based on if the app is in debug mode.
"""
import os

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG set is set to True if env var is "True"
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Deployment-specific settings
USPS_SERVICE_INFO = os.environ.get("USPS_SERVICE_INFO", {})
USPS_TARGET_AUDIENCE = os.environ.get("USPS_TARGET_AUDIENCE", {})
