# mpesa_client.PaymentsApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mpesa_b2b_v1_paymentrequest_post**](PaymentsApi.md#mpesa_b2b_v1_paymentrequest_post) | **POST** /mpesa/b2b/v1/paymentrequest | Make a B2B Payment Request
[**mpesa_c2b_v1_registerurl_post**](PaymentsApi.md#mpesa_c2b_v1_registerurl_post) | **POST** /mpesa/c2b/v1/registerurl | Register C2B Confirmation and Validation URLs
[**mpesa_c2b_v1_simulate_post**](PaymentsApi.md#mpesa_c2b_v1_simulate_post) | **POST** /mpesa/c2b/v1/simulate | Simulate a C2B Payment
[**mpesa_stkpush_v1_processrequest_post**](PaymentsApi.md#mpesa_stkpush_v1_processrequest_post) | **POST** /mpesa/stkpush/v1/processrequest | Initiate a Lipa na M-Pesa Online Payment

# **mpesa_b2b_v1_paymentrequest_post**
> mpesa_b2b_v1_paymentrequest_post(body=body)

Make a B2B Payment Request

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Make a B2B Payment Request
    api_instance.mpesa_b2b_v1_paymentrequest_post(body=body)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_b2b_v1_paymentrequest_post: %s\n" % e)
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

# **mpesa_c2b_v1_registerurl_post**
> mpesa_c2b_v1_registerurl_post(body=body)

Register C2B Confirmation and Validation URLs

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Register C2B Confirmation and Validation URLs
    api_instance.mpesa_c2b_v1_registerurl_post(body=body)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_c2b_v1_registerurl_post: %s\n" % e)
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

# **mpesa_c2b_v1_simulate_post**
> mpesa_c2b_v1_simulate_post(body=body)

Simulate a C2B Payment

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Simulate a C2B Payment
    api_instance.mpesa_c2b_v1_simulate_post(body=body)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_c2b_v1_simulate_post: %s\n" % e)
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

# **mpesa_stkpush_v1_processrequest_post**
> mpesa_stkpush_v1_processrequest_post(body=body)

Initiate a Lipa na M-Pesa Online Payment

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Initiate a Lipa na M-Pesa Online Payment
    api_instance.mpesa_stkpush_v1_processrequest_post(body=body)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_stkpush_v1_processrequest_post: %s\n" % e)
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

