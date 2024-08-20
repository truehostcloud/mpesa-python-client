# mpesa_client.PaymentsApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mpesa_b2b_v1_paymentrequest_post**](PaymentsApi.md#mpesa_b2b_v1_paymentrequest_post) | **POST** /mpesa/b2b/v1/paymentrequest | Make a B2B Payment Request
[**mpesa_c2b_v1_registerurl_post**](PaymentsApi.md#mpesa_c2b_v1_registerurl_post) | **POST** /mpesa/c2b/v1/registerurl | Register C2B Confirmation and Validation URLs
[**mpesa_c2b_v1_simulate_post**](PaymentsApi.md#mpesa_c2b_v1_simulate_post) | **POST** /mpesa/c2b/v1/simulate | Simulate a C2B Payment
[**mpesa_stkpush_v1_processrequest_post**](PaymentsApi.md#mpesa_stkpush_v1_processrequest_post) | **POST** /mpesa/stkpush/v1/processrequest | Initiate a Lipa na M-Pesa Online Payment

# **mpesa_b2b_v1_paymentrequest_post**
> B2BPaymentResponse mpesa_b2b_v1_paymentrequest_post(body)

Make a B2B Payment Request

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
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.B2BPaymentRequest() # B2BPaymentRequest | 

try:
    # Make a B2B Payment Request
    api_response = api_instance.mpesa_b2b_v1_paymentrequest_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_b2b_v1_paymentrequest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**B2BPaymentRequest**](B2BPaymentRequest.md)|  | 

### Return type

[**B2BPaymentResponse**](B2BPaymentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_c2b_v1_registerurl_post**
> C2BURLRegistrationResponse mpesa_c2b_v1_registerurl_post(body)

Register C2B Confirmation and Validation URLs

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
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.C2BURLRegistrationRequest() # C2BURLRegistrationRequest | 

try:
    # Register C2B Confirmation and Validation URLs
    api_response = api_instance.mpesa_c2b_v1_registerurl_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_c2b_v1_registerurl_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**C2BURLRegistrationRequest**](C2BURLRegistrationRequest.md)|  | 

### Return type

[**C2BURLRegistrationResponse**](C2BURLRegistrationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_c2b_v1_simulate_post**
> C2BPaymentSimulationResponse mpesa_c2b_v1_simulate_post(body)

Simulate a C2B Payment

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
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.C2BPaymentSimulationRequest() # C2BPaymentSimulationRequest | 

try:
    # Simulate a C2B Payment
    api_response = api_instance.mpesa_c2b_v1_simulate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_c2b_v1_simulate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**C2BPaymentSimulationRequest**](C2BPaymentSimulationRequest.md)|  | 

### Return type

[**C2BPaymentSimulationResponse**](C2BPaymentSimulationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_stkpush_v1_processrequest_post**
> StkPushResponse mpesa_stkpush_v1_processrequest_post(body)

Initiate a Lipa na M-Pesa Online Payment

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
api_instance = mpesa_client.PaymentsApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.StkPushRequest() # StkPushRequest | 

try:
    # Initiate a Lipa na M-Pesa Online Payment
    api_response = api_instance.mpesa_stkpush_v1_processrequest_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->mpesa_stkpush_v1_processrequest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StkPushRequest**](StkPushRequest.md)|  | 

### Return type

[**StkPushResponse**](StkPushResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

