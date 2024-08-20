# mpesa_client.DefaultApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mpesa_accountbalance_v1_query_post**](DefaultApi.md#mpesa_accountbalance_v1_query_post) | **POST** /mpesa/accountbalance/v1/query | Make an Account Balance query
[**mpesa_b2b_v1_paymentrequest_post**](DefaultApi.md#mpesa_b2b_v1_paymentrequest_post) | **POST** /mpesa/b2b/v1/paymentrequest | Make a B2B Payment Request
[**mpesa_b2c_v1_paymentrequest_post**](DefaultApi.md#mpesa_b2c_v1_paymentrequest_post) | **POST** /mpesa/b2c/v1/paymentrequest | Make a B2C Payment Request
[**mpesa_c2b_v1_registerurl_post**](DefaultApi.md#mpesa_c2b_v1_registerurl_post) | **POST** /mpesa/c2b/v1/registerurl | Register C2B Confirmation and Validation URLs
[**mpesa_c2b_v1_simulate_post**](DefaultApi.md#mpesa_c2b_v1_simulate_post) | **POST** /mpesa/c2b/v1/simulate | Simulate a C2B Payment
[**mpesa_reversal_v1_request_post**](DefaultApi.md#mpesa_reversal_v1_request_post) | **POST** /mpesa/reversal/v1/request | Reverse an M-Pesa Transaction
[**mpesa_stkpush_v1_processrequest_post**](DefaultApi.md#mpesa_stkpush_v1_processrequest_post) | **POST** /mpesa/stkpush/v1/processrequest | Initiate a Lipa na M-Pesa Online Payment
[**mpesa_stkpushquery_v1_query_post**](DefaultApi.md#mpesa_stkpushquery_v1_query_post) | **POST** /mpesa/stkpushquery/v1/query | Query the status of a Lipa na M-Pesa Online Payment
[**mpesa_transactionstatus_v1_query_post**](DefaultApi.md#mpesa_transactionstatus_v1_query_post) | **POST** /mpesa/transactionstatus/v1/query | Query the Transaction Status of an M-Pesa Transaction
[**oauth_v1_generate_get**](DefaultApi.md#oauth_v1_generate_get) | **GET** /oauth/v1/generate | Generate an OAuth Access Token

# **mpesa_accountbalance_v1_query_post**
> mpesa_accountbalance_v1_query_post(body=body, authorization=authorization, content_type=content_type)

Make an Account Balance query

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Make an Account Balance query
    api_instance.mpesa_accountbalance_v1_query_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_accountbalance_v1_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_b2b_v1_paymentrequest_post**
> mpesa_b2b_v1_paymentrequest_post(body=body, authorization=authorization, content_type=content_type)

Make a B2B Payment Request

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Make a B2B Payment Request
    api_instance.mpesa_b2b_v1_paymentrequest_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_b2b_v1_paymentrequest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_b2c_v1_paymentrequest_post**
> mpesa_b2c_v1_paymentrequest_post(body=body, authorization=authorization, content_type=content_type)

Make a B2C Payment Request

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Make a B2C Payment Request
    api_instance.mpesa_b2c_v1_paymentrequest_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_b2c_v1_paymentrequest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_c2b_v1_registerurl_post**
> mpesa_c2b_v1_registerurl_post(body=body, authorization=authorization, content_type=content_type)

Register C2B Confirmation and Validation URLs

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Register C2B Confirmation and Validation URLs
    api_instance.mpesa_c2b_v1_registerurl_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_c2b_v1_registerurl_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_c2b_v1_simulate_post**
> mpesa_c2b_v1_simulate_post(body=body, authorization=authorization, content_type=content_type)

Simulate a C2B Payment

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Simulate a C2B Payment
    api_instance.mpesa_c2b_v1_simulate_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_c2b_v1_simulate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_reversal_v1_request_post**
> mpesa_reversal_v1_request_post(body=body, authorization=authorization, content_type=content_type)

Reverse an M-Pesa Transaction

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Reverse an M-Pesa Transaction
    api_instance.mpesa_reversal_v1_request_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_reversal_v1_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_stkpush_v1_processrequest_post**
> mpesa_stkpush_v1_processrequest_post(body=body, authorization=authorization, content_type=content_type)

Initiate a Lipa na M-Pesa Online Payment

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Initiate a Lipa na M-Pesa Online Payment
    api_instance.mpesa_stkpush_v1_processrequest_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_stkpush_v1_processrequest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_stkpushquery_v1_query_post**
> mpesa_stkpushquery_v1_query_post(body=body, authorization=authorization, content_type=content_type)

Query the status of a Lipa na M-Pesa Online Payment

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Query the status of a Lipa na M-Pesa Online Payment
    api_instance.mpesa_stkpushquery_v1_query_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_stkpushquery_v1_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_transactionstatus_v1_query_post**
> mpesa_transactionstatus_v1_query_post(body=body, authorization=authorization, content_type=content_type)

Query the Transaction Status of an M-Pesa Transaction

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Query the Transaction Status of an M-Pesa Transaction
    api_instance.mpesa_transactionstatus_v1_query_post(body=body, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->mpesa_transactionstatus_v1_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_v1_generate_get**
> oauth_v1_generate_get(grant_type=grant_type)

Generate an OAuth Access Token

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpesa_client.DefaultApi()
grant_type = 'grant_type_example' # str |  (optional)

try:
    # Generate an OAuth Access Token
    api_instance.oauth_v1_generate_get(grant_type=grant_type)
except ApiException as e:
    print("Exception when calling DefaultApi->oauth_v1_generate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

