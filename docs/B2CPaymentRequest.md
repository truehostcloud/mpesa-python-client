# B2CPaymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_name** | **str** | This is the Timestamp of the transaction, normally in the format of YEAR+MONTH+DATE+HOUR+MINUTE+SECOND (YYYYMMDDHHMMSS). Each part should be at least two digits, apart from the year which takes four digits. | 
**transaction_type** | **str** | This is the transaction type to be used for the request. Only two types are allowed: CustomerPayBillOnline: This is a transaction where the customer is expected to pay a bill e.g. utility bill. CustomerBuyGoodsOnline: This is a transaction where the customer is expected to pay for goods e.g. a supermarket.  | [optional] 
**amount** | **int** | This is the Amount transacted normally a numeric value. Money that the customer pays to the Shortcode. Only whole numbers are supported. | 
**party_a** | **int** | The phone number sending money. The parameter expected is a Valid Safaricom Mobile Number that is M-PESA registered in the format 2547XXXXXXXX | 
**party_b** | **int** | The organization shortcode receiving the funds. The parameter expected is a 5 to 7 digit Paybill number. | 
**phone_number** | **int** | The Mobile Number to receive the STK Pin Prompt. This number can be the same as PartyA value above. | [optional] 
**call_back_url** | **str** | A CallBack URL is a valid secure URL that is used to receive notifications from M-Pesa API. It is the endpoint to which the results will be sent by M-Pesa API. | [optional] 
**account_reference** | **str** | This is an Alpha-Numeric parameter that is defined by your system as an Identifier of the transaction for the CustomerPayBillOnline transaction type. Along with the business name, this value is also displayed to the customer in the STK Pin Prompt message. Maximum of 12 characters. | [optional] 
**transaction_desc** | **str** | This is any additional information/comment that can be sent along with the request from your system. Maximum of 13 Characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

