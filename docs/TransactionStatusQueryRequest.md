# TransactionStatusQueryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **str** | The name of the initiator initiating the request. | 
**security_credential** | **str** | Encrypted credential of the user getting transaction status | 
**command_id** | **str** | Takes only the &#x27;TransactionStatusQuery&#x27; Command ID. | 
**transaction_id** | **str** | Unique identifier to identify a transaction on Mpesa | 
**party_a** | **int** | Organization/MSISDN receiving the transaction | 
**identifier_type** | **str** | Type of organization receiving the transaction | 
**result_url** | **str** | URL where the results will be sent by M-Pesa API | 
**queue_time_out_url** | **str** | URL where the results will be sent by M-Pesa API | 
**remarks** | **str** | Comments that are sent along with the transaction | 
**occasion** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

