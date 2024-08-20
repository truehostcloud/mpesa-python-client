# TransactionReversalRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **str** | The name of the initiator initiating the request. | [optional] 
**security_credential** | **str** | Encrypted credential of the user getting transaction status | [optional] 
**command_id** | **str** | Takes only the &#x27;TransactionReversal&#x27; Command ID. | [optional] 
**transaction_id** | **str** | Unique identifier to identify a transaction on Mpesa | [optional] 
**amount** | **int** | The amount of money being sent to the customer. | [optional] 
**receiver_party** | **int** | The organization that receives the transaction. | [optional] 
**receiver_identifier_type** | **str** | Type of organization receiving the transaction | [optional] 
**result_url** | **str** | URL where the results will be sent by M-Pesa API | [optional] 
**queue_time_out_url** | **str** | URL where the results will be sent by M-Pesa API | [optional] 
**remarks** | **str** | Comments that are sent along with the transaction | [optional] 
**occasion** | **str** | Any additional information to be associated with the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

