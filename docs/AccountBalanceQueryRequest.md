# AccountBalanceQueryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **str** | This is the credential/username used to authenticate the transaction request | 
**security_credential** | **str** | Base64 encoded string of the M-PESA short code and password, which is encrypted using M-PESA public key and validates the transaction on M-PESA Core system. It indicates the Encrypted credential of the initiator getting the account balance. Its value must match the inputted value of the parameter IdentifierType. | 
**command_id** | **str** | A unique command is passed to the M-PESA system. | 
**party_a** | **int** | The shortcode of the organization querying for the account balance. | 
**identifier_type** | **int** | Type of organization querying for the account balance. | 
**remarks** | **str** | Comments that are sent along with the transaction. | 
**queue_time_out_url** | **str** | URL where the results will be sent by M-Pesa API. | 
**result_url** | **str** | URL where the results will be sent by M-Pesa API. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

