![Tests](https://github.com/18F/identity-give-usps/workflows/Unit-Tests/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/7a72205acec6d179707c/maintainability)](https://codeclimate.com/github/18F/identity-give-usps/maintainability)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

# GIVE USPS Address Validation Microservice
The USPS microservice is a Python [FastAPI](https://fastapi.tiangolo.com/)
application that exposes an API for address verification functions to GIVE
via the USPS AII API.

## Why this project
The GIVE USPS microservice aims to provide address verification capabilites to
the GIVE API via its upstream USPS integration. The USPS microservice has
the following goals:
* Expose the USPS address verification endpoints to GIVE users

## CI/CD Workflows with GitHub Actions
The most up-to-date information about the CI/CD flows for this repo can be found in the
[GitHub workflows directory](https://github.com/18F/identity-give-usps/tree/main/.github/workflows)

## Building Locally

### Pre-requisites
Make sure you have the following installed if you intend to build the project locally.
- [Python 3](https://www.python.org/) (Check [runtime.txt](runtime.txt) for exact version)
- [CloudFoundry CLI](https://docs.cloudfoundry.org/cf-cli/)

### Development Setup
To set up your environment, run the following commands (or the equivalent
commands if not using a bash-like terminal):
```shell
# Clone the project
git clone https://github.com/18F/identity-give-usps
cd identity-give-usps

# Set up Python virtual environment
python3.9 -m venv .venv
source venv/bin/activate
# .venv\Scripts\Activate.ps1 on Windows

# Install dependencies and pre-commit hooks
python -m pip install -r requirements-dev.txt
pre-commit install
```

### Running the application
After completing [development setup](#development-setup) application locally with:
```shell
python -m pytest # Unit tests should be passing
uvicorn usps.main:app
```

### Viewing API Endpoints and documentation
Documentation can be viewed locally by running the application and visiting
http://127.0.0.1:8000/docs

### Deploying to Cloud.gov during development
All deployments require having the correct Cloud.gov credentials in place. If
you haven't already, visit [Cloud.gov](https://cloud.gov) and set up your
account and CLI.

*manifest.yml* file contains the deployment configuration for cloud.gov, and expects
a vars.yaml file that includes runtime variables referenced. For info, see
[cloud foundry manifest files reference](https://docs.cloudfoundry.org/devguide/deploy-apps/manifest-attributes.html)

Running the following `cf` command will deploy the application to cloud.gov
```shell
cf push --vars-file vars.yaml \
  --var ROUTE=<application-route> \
  --var TRANSACTION_ROUTE=<transaction-logging-service-route> \
  --var USPS_SERVICE_INFO=<usps-service-info> \
  --var USPS_TARGET_AUDIENCE=<usps-target-audience> \
```

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in
[CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright
and related rights in the work worldwide are waived through the
[CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication.
By submitting a pull request, you are agreeing to comply with this waiver of
copyright interest.
