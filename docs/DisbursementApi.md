# mpesa_client.DisbursementApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mpesa_b2c_v1_paymentrequest_post**](DisbursementApi.md#mpesa_b2c_v1_paymentrequest_post) | **POST** /mpesa/b2c/v1/paymentrequest | Make a B2C Payment Request

# **mpesa_b2c_v1_paymentrequest_post**
> mpesa_b2c_v1_paymentrequest_post(body=body)

Make a B2C Payment Request

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.DisbursementApi(mpesa_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Make a B2C Payment Request
    api_instance.mpesa_b2c_v1_paymentrequest_post(body=body)
except ApiException as e:
    print("Exception when calling DisbursementApi->mpesa_b2c_v1_paymentrequest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

