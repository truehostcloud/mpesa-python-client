# mpesa-client
M-Pesa API client for Daraja

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/truehostcloud/mpesa-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/truehostcloud/mpesa-python-client.git`)

Then import the package:
```python
import mpesa_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mpesa_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = mpesa_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mpesa_client.DisbursementApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.B2CPaymentRequest() # B2CPaymentRequest | 

try:
    # Make a B2C Payment Request
    api_response = api_instance.mpesa_b2c_v1_paymentrequest_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementApi->mpesa_b2c_v1_paymentrequest_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox.safaricom.co.ke*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DisbursementApi* | [**mpesa_b2c_v1_paymentrequest_post**](docs/DisbursementApi.md#mpesa_b2c_v1_paymentrequest_post) | **POST** /mpesa/b2c/v1/paymentrequest | Make a B2C Payment Request
*ExperienceApi* | [**mpesa_accountbalance_v1_query_post**](docs/ExperienceApi.md#mpesa_accountbalance_v1_query_post) | **POST** /mpesa/accountbalance/v1/query | Make an Account Balance query
*ExperienceApi* | [**mpesa_reversal_v1_request_post**](docs/ExperienceApi.md#mpesa_reversal_v1_request_post) | **POST** /mpesa/reversal/v1/request | Reverse an M-Pesa Transaction
*ExperienceApi* | [**mpesa_stkpushquery_v1_query_post**](docs/ExperienceApi.md#mpesa_stkpushquery_v1_query_post) | **POST** /mpesa/stkpushquery/v1/query | Query the status of a Lipa na M-Pesa Online Payment
*ExperienceApi* | [**mpesa_transactionstatus_v1_query_post**](docs/ExperienceApi.md#mpesa_transactionstatus_v1_query_post) | **POST** /mpesa/transactionstatus/v1/query | Query the Transaction Status of an M-Pesa Transaction
*PaymentsApi* | [**mpesa_b2b_v1_paymentrequest_post**](docs/PaymentsApi.md#mpesa_b2b_v1_paymentrequest_post) | **POST** /mpesa/b2b/v1/paymentrequest | Make a B2B Payment Request
*PaymentsApi* | [**mpesa_c2b_v1_simulate_post**](docs/PaymentsApi.md#mpesa_c2b_v1_simulate_post) | **POST** /mpesa/c2b/v1/simulate | Simulate a C2B Payment
*PaymentsApi* | [**mpesa_c2b_v2_registerurl_post**](docs/PaymentsApi.md#mpesa_c2b_v2_registerurl_post) | **POST** /mpesa/c2b/v2/registerurl | Register C2B Confirmation and Validation URLs
*PaymentsApi* | [**mpesa_stkpush_v1_processrequest_post**](docs/PaymentsApi.md#mpesa_stkpush_v1_processrequest_post) | **POST** /mpesa/stkpush/v1/processrequest | Initiate a Lipa na M-Pesa Online Payment
*SecurityApi* | [**oauth_v1_generate_get**](docs/SecurityApi.md#oauth_v1_generate_get) | **GET** /oauth/v1/generate | Generate an OAuth Access Token

## Documentation For Models

 - [AccountBalanceQueryRequest](docs/AccountBalanceQueryRequest.md)
 - [AccountBalanceQueryResponse](docs/AccountBalanceQueryResponse.md)
 - [B2BPaymentRequest](docs/B2BPaymentRequest.md)
 - [B2BPaymentResponse](docs/B2BPaymentResponse.md)
 - [B2CPaymentRequest](docs/B2CPaymentRequest.md)
 - [B2CPaymentResponse](docs/B2CPaymentResponse.md)
 - [C2BPaymentSimulationRequest](docs/C2BPaymentSimulationRequest.md)
 - [C2BPaymentSimulationResponse](docs/C2BPaymentSimulationResponse.md)
 - [C2BURLRegistrationRequest](docs/C2BURLRegistrationRequest.md)
 - [C2BURLRegistrationResponse](docs/C2BURLRegistrationResponse.md)
 - [OAuthAccessTokenResponse](docs/OAuthAccessTokenResponse.md)
 - [StkPushQueryRequest](docs/StkPushQueryRequest.md)
 - [StkPushQueryResponse](docs/StkPushQueryResponse.md)
 - [StkPushRequest](docs/StkPushRequest.md)
 - [StkPushResponse](docs/StkPushResponse.md)
 - [TransactionReversalRequest](docs/TransactionReversalRequest.md)
 - [TransactionReversalResponse](docs/TransactionReversalResponse.md)
 - [TransactionStatusQueryRequest](docs/TransactionStatusQueryRequest.md)
 - [TransactionStatusQueryResponse](docs/TransactionStatusQueryResponse.md)

## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication

## bearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


