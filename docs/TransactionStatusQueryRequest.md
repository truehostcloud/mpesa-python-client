# TransactionStatusQueryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **str** | The name of the initiator initiating the request. | [optional] 
**security_credential** | **str** | Encrypted credential of the user getting transaction status | [optional] 
**command_id** | **str** | Takes only the &#x27;TransactionStatusQuery&#x27; Command ID. | [optional] 
**transaction_id** | **str** | Unique identifier to identify a transaction on Mpesa | [optional] 
**party_a** | **int** | Organization/MSISDN receiving the transaction | [optional] 
**identifier_type** | **str** | Type of organization receiving the transaction | [optional] 
**result_url** | **str** | URL where the results will be sent by M-Pesa API | [optional] 
**queue_time_out_url** | **str** | URL where the results will be sent by M-Pesa API | [optional] 
**remarks** | **str** | Comments that are sent along with the transaction | [optional] 
**occasion** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

