# coding: utf-8

"""
    Safaricom APIs

    M-Pesa API client for Daraja  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StkPushRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'business_short_code': 'int',
        'password': 'str',
        'timestamp': 'str',
        'transaction_type': 'str',
        'amount': 'int',
        'party_a': 'int',
        'party_b': 'int',
        'phone_number': 'int',
        'call_back_url': 'str',
        'account_reference': 'str',
        'transaction_desc': 'str'
    }

    attribute_map = {
        'business_short_code': 'BusinessShortCode',
        'password': 'Password',
        'timestamp': 'Timestamp',
        'transaction_type': 'TransactionType',
        'amount': 'Amount',
        'party_a': 'PartyA',
        'party_b': 'PartyB',
        'phone_number': 'PhoneNumber',
        'call_back_url': 'CallBackURL',
        'account_reference': 'AccountReference',
        'transaction_desc': 'TransactionDesc'
    }

    def __init__(self, business_short_code=None, password=None, timestamp=None, transaction_type=None, amount=None, party_a=None, party_b=None, phone_number=None, call_back_url=None, account_reference=None, transaction_desc=None):  # noqa: E501
        """StkPushRequest - a model defined in Swagger"""  # noqa: E501
        self._business_short_code = None
        self._password = None
        self._timestamp = None
        self._transaction_type = None
        self._amount = None
        self._party_a = None
        self._party_b = None
        self._phone_number = None
        self._call_back_url = None
        self._account_reference = None
        self._transaction_desc = None
        self.discriminator = None
        self.business_short_code = business_short_code
        self.password = password
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.amount = amount
        self.party_a = party_a
        self.party_b = party_b
        self.phone_number = phone_number
        self.call_back_url = call_back_url
        self.account_reference = account_reference
        self.transaction_desc = transaction_desc

    @property
    def business_short_code(self):
        """Gets the business_short_code of this StkPushRequest.  # noqa: E501

        This is the organization's shortcode (Paybill or Buygoods - a 5 to 7-digit account number) used to identify an organization and receive the transaction.  # noqa: E501

        :return: The business_short_code of this StkPushRequest.  # noqa: E501
        :rtype: int
        """
        return self._business_short_code

    @business_short_code.setter
    def business_short_code(self, business_short_code):
        """Sets the business_short_code of this StkPushRequest.

        This is the organization's shortcode (Paybill or Buygoods - a 5 to 7-digit account number) used to identify an organization and receive the transaction.  # noqa: E501

        :param business_short_code: The business_short_code of this StkPushRequest.  # noqa: E501
        :type: int
        """
        if business_short_code is None:
            raise ValueError("Invalid value for `business_short_code`, must not be `None`")  # noqa: E501

        self._business_short_code = business_short_code

    @property
    def password(self):
        """Gets the password of this StkPushRequest.  # noqa: E501

        This is the password used for encrypting the request sent. a base64 encoded string. (The base64 string is a combination of Shortcode+Passkey+Timestamp).  # noqa: E501

        :return: The password of this StkPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this StkPushRequest.

        This is the password used for encrypting the request sent. a base64 encoded string. (The base64 string is a combination of Shortcode+Passkey+Timestamp).  # noqa: E501

        :param password: The password of this StkPushRequest.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def timestamp(self):
        """Gets the timestamp of this StkPushRequest.  # noqa: E501

        This is the Timestamp of the transaction, normally in the format of YEAR+MONTH+DATE+HOUR+MINUTE+SECOND (YYYYMMDDHHMMSS). Each part should be at least two digits, apart from the year which takes four digits.  # noqa: E501

        :return: The timestamp of this StkPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this StkPushRequest.

        This is the Timestamp of the transaction, normally in the format of YEAR+MONTH+DATE+HOUR+MINUTE+SECOND (YYYYMMDDHHMMSS). Each part should be at least two digits, apart from the year which takes four digits.  # noqa: E501

        :param timestamp: The timestamp of this StkPushRequest.  # noqa: E501
        :type: str
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def transaction_type(self):
        """Gets the transaction_type of this StkPushRequest.  # noqa: E501

        This is the transaction type to be used for the request. Only two types are allowed: CustomerPayBillOnline: This is a transaction where the customer is expected to pay a bill e.g. utility bill. CustomerBuyGoodsOnline: This is a transaction where the customer is expected to pay for goods e.g. a supermarket.   # noqa: E501

        :return: The transaction_type of this StkPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this StkPushRequest.

        This is the transaction type to be used for the request. Only two types are allowed: CustomerPayBillOnline: This is a transaction where the customer is expected to pay a bill e.g. utility bill. CustomerBuyGoodsOnline: This is a transaction where the customer is expected to pay for goods e.g. a supermarket.   # noqa: E501

        :param transaction_type: The transaction_type of this StkPushRequest.  # noqa: E501
        :type: str
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CustomerPayBillOnline", "CustomerBuyGoodsOnline"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

    @property
    def amount(self):
        """Gets the amount of this StkPushRequest.  # noqa: E501

        This is the Amount transacted normally a numeric value. Money that the customer pays to the Shortcode. Only whole numbers are supported.  # noqa: E501

        :return: The amount of this StkPushRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this StkPushRequest.

        This is the Amount transacted normally a numeric value. Money that the customer pays to the Shortcode. Only whole numbers are supported.  # noqa: E501

        :param amount: The amount of this StkPushRequest.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def party_a(self):
        """Gets the party_a of this StkPushRequest.  # noqa: E501

        The phone number sending money. The parameter expected is a Valid Safaricom Mobile Number that is M-PESA registered in the format 2547XXXXXXXX  # noqa: E501

        :return: The party_a of this StkPushRequest.  # noqa: E501
        :rtype: int
        """
        return self._party_a

    @party_a.setter
    def party_a(self, party_a):
        """Sets the party_a of this StkPushRequest.

        The phone number sending money. The parameter expected is a Valid Safaricom Mobile Number that is M-PESA registered in the format 2547XXXXXXXX  # noqa: E501

        :param party_a: The party_a of this StkPushRequest.  # noqa: E501
        :type: int
        """
        if party_a is None:
            raise ValueError("Invalid value for `party_a`, must not be `None`")  # noqa: E501

        self._party_a = party_a

    @property
    def party_b(self):
        """Gets the party_b of this StkPushRequest.  # noqa: E501

        The organization shortcode receiving the funds. The parameter expected is a 5 to 7 digit Paybill number.  # noqa: E501

        :return: The party_b of this StkPushRequest.  # noqa: E501
        :rtype: int
        """
        return self._party_b

    @party_b.setter
    def party_b(self, party_b):
        """Sets the party_b of this StkPushRequest.

        The organization shortcode receiving the funds. The parameter expected is a 5 to 7 digit Paybill number.  # noqa: E501

        :param party_b: The party_b of this StkPushRequest.  # noqa: E501
        :type: int
        """
        if party_b is None:
            raise ValueError("Invalid value for `party_b`, must not be `None`")  # noqa: E501

        self._party_b = party_b

    @property
    def phone_number(self):
        """Gets the phone_number of this StkPushRequest.  # noqa: E501

        The Mobile Number to receive the STK Pin Prompt. This number can be the same as PartyA value above.  # noqa: E501

        :return: The phone_number of this StkPushRequest.  # noqa: E501
        :rtype: int
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this StkPushRequest.

        The Mobile Number to receive the STK Pin Prompt. This number can be the same as PartyA value above.  # noqa: E501

        :param phone_number: The phone_number of this StkPushRequest.  # noqa: E501
        :type: int
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def call_back_url(self):
        """Gets the call_back_url of this StkPushRequest.  # noqa: E501

        A CallBack URL is a valid secure URL that is used to receive notifications from M-Pesa API. It is the endpoint to which the results will be sent by M-Pesa API.  # noqa: E501

        :return: The call_back_url of this StkPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._call_back_url

    @call_back_url.setter
    def call_back_url(self, call_back_url):
        """Sets the call_back_url of this StkPushRequest.

        A CallBack URL is a valid secure URL that is used to receive notifications from M-Pesa API. It is the endpoint to which the results will be sent by M-Pesa API.  # noqa: E501

        :param call_back_url: The call_back_url of this StkPushRequest.  # noqa: E501
        :type: str
        """
        if call_back_url is None:
            raise ValueError("Invalid value for `call_back_url`, must not be `None`")  # noqa: E501

        self._call_back_url = call_back_url

    @property
    def account_reference(self):
        """Gets the account_reference of this StkPushRequest.  # noqa: E501

        This is an Alpha-Numeric parameter that is defined by your system as an Identifier of the transaction for the CustomerPayBillOnline transaction type. Along with the business name, this value is also displayed to the customer in the STK Pin Prompt message. Maximum of 12 characters.  # noqa: E501

        :return: The account_reference of this StkPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_reference

    @account_reference.setter
    def account_reference(self, account_reference):
        """Sets the account_reference of this StkPushRequest.

        This is an Alpha-Numeric parameter that is defined by your system as an Identifier of the transaction for the CustomerPayBillOnline transaction type. Along with the business name, this value is also displayed to the customer in the STK Pin Prompt message. Maximum of 12 characters.  # noqa: E501

        :param account_reference: The account_reference of this StkPushRequest.  # noqa: E501
        :type: str
        """
        if account_reference is None:
            raise ValueError("Invalid value for `account_reference`, must not be `None`")  # noqa: E501

        self._account_reference = account_reference

    @property
    def transaction_desc(self):
        """Gets the transaction_desc of this StkPushRequest.  # noqa: E501

        This is any additional information/comment that can be sent along with the request from your system. Maximum of 13 Characters.  # noqa: E501

        :return: The transaction_desc of this StkPushRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_desc

    @transaction_desc.setter
    def transaction_desc(self, transaction_desc):
        """Sets the transaction_desc of this StkPushRequest.

        This is any additional information/comment that can be sent along with the request from your system. Maximum of 13 Characters.  # noqa: E501

        :param transaction_desc: The transaction_desc of this StkPushRequest.  # noqa: E501
        :type: str
        """
        if transaction_desc is None:
            raise ValueError("Invalid value for `transaction_desc`, must not be `None`")  # noqa: E501

        self._transaction_desc = transaction_desc

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StkPushRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StkPushRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
