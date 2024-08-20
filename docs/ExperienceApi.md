# mpesa_client.ExperienceApi

All URIs are relative to *https://sandbox.safaricom.co.ke*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mpesa_accountbalance_v1_query_post**](ExperienceApi.md#mpesa_accountbalance_v1_query_post) | **POST** /mpesa/accountbalance/v1/query | Make an Account Balance query
[**mpesa_reversal_v1_request_post**](ExperienceApi.md#mpesa_reversal_v1_request_post) | **POST** /mpesa/reversal/v1/request | Reverse an M-Pesa Transaction
[**mpesa_stkpushquery_v1_query_post**](ExperienceApi.md#mpesa_stkpushquery_v1_query_post) | **POST** /mpesa/stkpushquery/v1/query | Query the status of a Lipa na M-Pesa Online Payment
[**mpesa_transactionstatus_v1_query_post**](ExperienceApi.md#mpesa_transactionstatus_v1_query_post) | **POST** /mpesa/transactionstatus/v1/query | Query the Transaction Status of an M-Pesa Transaction

# **mpesa_accountbalance_v1_query_post**
> AccountBalanceQueryResponse mpesa_accountbalance_v1_query_post(body=body)

Make an Account Balance query

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.ExperienceApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.AccountBalanceQueryRequest() # AccountBalanceQueryRequest |  (optional)

try:
    # Make an Account Balance query
    api_response = api_instance.mpesa_accountbalance_v1_query_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperienceApi->mpesa_accountbalance_v1_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountBalanceQueryRequest**](AccountBalanceQueryRequest.md)|  | [optional] 

### Return type

[**AccountBalanceQueryResponse**](AccountBalanceQueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_reversal_v1_request_post**
> TransactionReversalResponse mpesa_reversal_v1_request_post(body=body)

Reverse an M-Pesa Transaction

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.ExperienceApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.TransactionReversalRequest() # TransactionReversalRequest |  (optional)

try:
    # Reverse an M-Pesa Transaction
    api_response = api_instance.mpesa_reversal_v1_request_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperienceApi->mpesa_reversal_v1_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionReversalRequest**](TransactionReversalRequest.md)|  | [optional] 

### Return type

[**TransactionReversalResponse**](TransactionReversalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_stkpushquery_v1_query_post**
> StkPushQueryResponse mpesa_stkpushquery_v1_query_post(body=body)

Query the status of a Lipa na M-Pesa Online Payment

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.ExperienceApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.StkPushQueryRequest() # StkPushQueryRequest |  (optional)

try:
    # Query the status of a Lipa na M-Pesa Online Payment
    api_response = api_instance.mpesa_stkpushquery_v1_query_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperienceApi->mpesa_stkpushquery_v1_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StkPushQueryRequest**](StkPushQueryRequest.md)|  | [optional] 

### Return type

[**StkPushQueryResponse**](StkPushQueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mpesa_transactionstatus_v1_query_post**
> TransactionStatusQueryResponse mpesa_transactionstatus_v1_query_post(body=body)

Query the Transaction Status of an M-Pesa Transaction

### Example
```python
from __future__ import print_function
import time
import mpesa_client
from mpesa_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mpesa_client.ExperienceApi(mpesa_client.ApiClient(configuration))
body = mpesa_client.TransactionStatusQueryRequest() # TransactionStatusQueryRequest |  (optional)

try:
    # Query the Transaction Status of an M-Pesa Transaction
    api_response = api_instance.mpesa_transactionstatus_v1_query_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperienceApi->mpesa_transactionstatus_v1_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionStatusQueryRequest**](TransactionStatusQueryRequest.md)|  | [optional] 

### Return type

[**TransactionStatusQueryResponse**](TransactionStatusQueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

