# B2BPaymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **str** | The M-Pesa API operator username. This user needs Org Business Pay Bill API initiator role on M-Pesa | 
**security_credential** | **str** | Encrypted credential of the user getting transaction status | 
**command_id** | **str** | This is a unique command that specifies B2B transaction type. BusinessPayBill: This supports sending money to both registered and unregistered M-Pesa customers. BusinessPayToBulk: This is a normal business to customer payment, supports only M-PESA registered customers.  | 
**sender_identifier_type** | **int** | The type of shortcode from which money is deducted. For this API, only \&quot;4\&quot; is allowed. | 
**receiver_identifier_type** | **int** | The type of shortcode to which money is sent. For this API, only \&quot;4\&quot; is allowed. | 
**amount** | **int** | The transaction amount. | 
**party_a** | **int** | Your shortcode. The shortcode from which money will be deducted. | 
**party_b** | **int** | The shortcode to which money will be moved | 
**account_reference** | **str** | The account number to be associated with the payment. Up to 13 characters. | 
**remarks** | **str** | Comments that are sent along with the transaction | 
**queue_time_out_url** | **str** | A URL that will be used to notify your system in case the request times out before processing. | 
**result_url** | **str** | A URL that will be used to send transaction results after processing. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

