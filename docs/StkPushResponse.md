# StkPushResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_request_id** | **str** | This is a global unique Identifier for any submitted payment request. | [optional] 
**checkout_request_id** | **str** | This is a global unique identifier of the processed checkout transaction request. | [optional] 
**response_code** | **int** | This is a numeric status code that indicates the status of the request. 0 means the request was successful. | [optional] 
**response_description** | **str** | Response description is an acknowledgment message from the API that gives the status of the request submission usually maps to a specific ResponseCode value. It can be a \&quot;Success\&quot; submission message or an error description. | [optional] 
**customer_message** | **str** | This is a message that your system can display to the customer as an acknowledgment of the payment request submission. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

