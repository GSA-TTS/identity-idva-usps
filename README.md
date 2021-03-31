![Tests](https://github.com/18F/identity-give-usps/workflows/Unit-Tests/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/7a72205acec6d179707c/maintainability)](https://codeclimate.com/github/18F/identity-give-usps/maintainability)
![Black](https://github.com/18F/identity-give-usps/workflows/Black/badge.svg)
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

# GIVE USPS Address Validation Microservice
The USPS microservice is a Python Django application that uses the Django Rest
Framework to expose an API for address validation functions to GIVE.

## Why this project
The GIVE USPS microservice aims to provide address validation capabilites to
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

### Required environment variables
The Django settings.py file for this project requires setting an environment
variable: `SECRET_KEY`

Running the following in your shell should print a secret key that can be used.
```shell
python
import secrets
secrets.token_urlsafe()
exit()

```

Set the environment variable using *the entire output* (including quotes) from
the printed secret
```shell
# BASH-like shells
export SECRET_KEY=<your-secret-here>
```
```powershell
# PowerShell
$Env:SECRET_KEY=<your-secret-here>
```
Note: during development, it may also be helpful to add the `DEBUG` environment
variable and setting it to the string `True`

### Running the application
After completing [development setup](#development-setup) and
[environment variable setup](#required-environment-variables) you can run the
application locally with:
```shell
python manage.py collectstatic
python manage.py test --debug-mode
gunicorn -b 127.0.0.1:8080 usps.wsgi
```

### Deploying to Cloud.gov during development
All deployments require having the correct Cloud.gov credentials in place. If
you haven't already, visit [Cloud.gov](https://cloud.gov) and set up your
account and CLI.

*manifest.yml* file contains the deployment configuration for cloud.gov, and expects
a vars.yaml file that includes runtime variables referenced. For info, see
[cloud foundry manifest files reference](https://docs.cloudfoundry.org/devguide/deploy-apps/manifest-attributes.html)

Running the following `cf` command will deploy the application to cloud.gov
`cf push --vars-file vars.yaml --var SECRET_KEY=$SECRET_KEY`.

### API Endpoints

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