# mpesa_client.SecurityApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_v1_generate_get**](SecurityApi.md#oauth_v1_generate_get) | **GET** /oauth/v1/generate | Generate an OAuth Access Token

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
# Configure HTTP basic authorization: basicAuth
configuration = mpesa_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mpesa_client.SecurityApi(mpesa_client.ApiClient(configuration))
grant_type = 'grant_type_example' # str |  (optional)

try:
    # Generate an OAuth Access Token
    api_instance.oauth_v1_generate_get(grant_type=grant_type)
except ApiException as e:
    print("Exception when calling SecurityApi->oauth_v1_generate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

