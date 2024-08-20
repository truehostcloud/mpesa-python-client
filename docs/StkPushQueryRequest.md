# StkPushQueryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_short_code** | **int** | This is the organization&#x27;s shortcode (Paybill or Buygoods - a 5 to 7-digit account number) used to identify an organization and receive the transaction. | 
**password** | **str** | This is the password used for encrypting the request sent. a base64 encoded string. (The base64 string is a combination of Shortcode+Passkey+Timestamp). | 
**timestamp** | **str** | This is the Timestamp of the transaction, normally in the format of YEAR+MONTH+DATE+HOUR+MINUTE+SECOND (YYYYMMDDHHMMSS). Each part should be at least two digits, apart from the year which takes four digits. | 
**checkout_request_id** | **str** | This is a global unique identifier of the processed checkout transaction request. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

