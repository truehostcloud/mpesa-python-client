# mpesa_client.DisbursementApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mpesa_b2c_v1_paymentrequest_post**](DisbursementApi.md#mpesa_b2c_v1_paymentrequest_post) | **POST** /mpesa/b2c/v1/paymentrequest | Make a B2C Payment Request

# **mpesa_b2c_v1_paymentrequest_post**
> B2CPaymentResponse mpesa_b2c_v1_paymentrequest_post(body)

Make a B2C Payment Request

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**B2CPaymentRequest**](B2CPaymentRequest.md)|  | 

### Return type

[**B2CPaymentResponse**](B2CPaymentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

