# TransactionStatusQueryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_conversation_id** | **str** | The unique request ID for tracking a transaction | [optional] 
**conversation_id** | **str** | The unique request ID returned my M-PESA for each request made | [optional] 
**response_code** | **int** | he numeric status code indicates the status transaction processing. 0 means success and any other code means an error occurred or the transaction failed. Success submission message or an error description | [optional] 
**response_description** | **str** | Response description message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

