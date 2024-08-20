# B2CPaymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_name** | **str** | This is an API user created by the Business Administrator of the M-PESA Bulk disbursement account that is active and authorized to initiate B2C transactions via API. | [optional] 
**security_credential** | **str** | This is the value obtained after encrypting the API initiator password. The password on Sandbox has been provisioned on the simulator. However, on production the password is created when the user is being created on the M-PESA organization portal. | [optional] 
**command_id** | **str** | This is a unique command that specifies B2C transaction type. SalaryPayment: This supports sending money to both registered and unregistered M-Pesa customers. BusinessPayment: This is a normal business to customer payment, supports only M-PESA registered customers. PromotionPayment: This is a promotional payment to customers. The M-PESA notification message is a congratulatory message. Supports only M-PESA registered customers.  | [optional] 
**amount** | **int** | The amount of money being sent to the customer. | [optional] 
**party_a** | **int** | This is the B2C organization shortcode from which the money is sent from. | [optional] 
**party_b** | **str** | This is the customer mobile number to receive the amount. - The number should have the country code (254) without the plus sign. | [optional] 
**remarks** | **str** | Any additional information to be associated with the transaction. | [optional] 
**queue_time_out_url** | **str** | This is the URL to be specified in your request that will be used by API Proxy to send notification incase the payment request is timed out while awaiting processing in the queue. | [optional] 
**result_url** | **str** | This is the URL to be specified in your request that will be used by M-PESA to send notification upon processing of the payment request. | [optional] 
**occasion** | **str** | Any additional information to be associated with the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

