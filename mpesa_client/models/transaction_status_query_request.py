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

class TransactionStatusQueryRequest(object):
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
        'initiator': 'str',
        'security_credential': 'str',
        'command_id': 'str',
        'transaction_id': 'str',
        'party_a': 'int',
        'identifier_type': 'str',
        'result_url': 'str',
        'queue_time_out_url': 'str',
        'remarks': 'str',
        'occasion': 'str'
    }

    attribute_map = {
        'initiator': 'Initiator',
        'security_credential': 'SecurityCredential',
        'command_id': 'CommandID',
        'transaction_id': 'TransactionID',
        'party_a': 'PartyA',
        'identifier_type': 'IdentifierType',
        'result_url': 'ResultURL',
        'queue_time_out_url': 'QueueTimeOutURL',
        'remarks': 'Remarks',
        'occasion': 'Occasion'
    }

    def __init__(self, initiator=None, security_credential=None, command_id=None, transaction_id=None, party_a=None, identifier_type=None, result_url=None, queue_time_out_url=None, remarks=None, occasion=None):  # noqa: E501
        """TransactionStatusQueryRequest - a model defined in Swagger"""  # noqa: E501
        self._initiator = None
        self._security_credential = None
        self._command_id = None
        self._transaction_id = None
        self._party_a = None
        self._identifier_type = None
        self._result_url = None
        self._queue_time_out_url = None
        self._remarks = None
        self._occasion = None
        self.discriminator = None
        self.initiator = initiator
        self.security_credential = security_credential
        self.command_id = command_id
        self.transaction_id = transaction_id
        self.party_a = party_a
        self.identifier_type = identifier_type
        self.result_url = result_url
        self.queue_time_out_url = queue_time_out_url
        self.remarks = remarks
        if occasion is not None:
            self.occasion = occasion

    @property
    def initiator(self):
        """Gets the initiator of this TransactionStatusQueryRequest.  # noqa: E501

        The name of the initiator initiating the request.  # noqa: E501

        :return: The initiator of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this TransactionStatusQueryRequest.

        The name of the initiator initiating the request.  # noqa: E501

        :param initiator: The initiator of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if initiator is None:
            raise ValueError("Invalid value for `initiator`, must not be `None`")  # noqa: E501

        self._initiator = initiator

    @property
    def security_credential(self):
        """Gets the security_credential of this TransactionStatusQueryRequest.  # noqa: E501

        Encrypted credential of the user getting transaction status  # noqa: E501

        :return: The security_credential of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_credential

    @security_credential.setter
    def security_credential(self, security_credential):
        """Sets the security_credential of this TransactionStatusQueryRequest.

        Encrypted credential of the user getting transaction status  # noqa: E501

        :param security_credential: The security_credential of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if security_credential is None:
            raise ValueError("Invalid value for `security_credential`, must not be `None`")  # noqa: E501

        self._security_credential = security_credential

    @property
    def command_id(self):
        """Gets the command_id of this TransactionStatusQueryRequest.  # noqa: E501

        Takes only the 'TransactionStatusQuery' Command ID.  # noqa: E501

        :return: The command_id of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this TransactionStatusQueryRequest.

        Takes only the 'TransactionStatusQuery' Command ID.  # noqa: E501

        :param command_id: The command_id of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if command_id is None:
            raise ValueError("Invalid value for `command_id`, must not be `None`")  # noqa: E501
        allowed_values = ["TransactionStatusQuery"]  # noqa: E501
        if command_id not in allowed_values:
            raise ValueError(
                "Invalid value for `command_id` ({0}), must be one of {1}"  # noqa: E501
                .format(command_id, allowed_values)
            )

        self._command_id = command_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionStatusQueryRequest.  # noqa: E501

        Unique identifier to identify a transaction on Mpesa  # noqa: E501

        :return: The transaction_id of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionStatusQueryRequest.

        Unique identifier to identify a transaction on Mpesa  # noqa: E501

        :param transaction_id: The transaction_id of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def party_a(self):
        """Gets the party_a of this TransactionStatusQueryRequest.  # noqa: E501

        Organization/MSISDN receiving the transaction  # noqa: E501

        :return: The party_a of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: int
        """
        return self._party_a

    @party_a.setter
    def party_a(self, party_a):
        """Sets the party_a of this TransactionStatusQueryRequest.

        Organization/MSISDN receiving the transaction  # noqa: E501

        :param party_a: The party_a of this TransactionStatusQueryRequest.  # noqa: E501
        :type: int
        """
        if party_a is None:
            raise ValueError("Invalid value for `party_a`, must not be `None`")  # noqa: E501

        self._party_a = party_a

    @property
    def identifier_type(self):
        """Gets the identifier_type of this TransactionStatusQueryRequest.  # noqa: E501

        Type of organization receiving the transaction  # noqa: E501

        :return: The identifier_type of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this TransactionStatusQueryRequest.

        Type of organization receiving the transaction  # noqa: E501

        :param identifier_type: The identifier_type of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if identifier_type is None:
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501

        self._identifier_type = identifier_type

    @property
    def result_url(self):
        """Gets the result_url of this TransactionStatusQueryRequest.  # noqa: E501

        URL where the results will be sent by M-Pesa API  # noqa: E501

        :return: The result_url of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url):
        """Sets the result_url of this TransactionStatusQueryRequest.

        URL where the results will be sent by M-Pesa API  # noqa: E501

        :param result_url: The result_url of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if result_url is None:
            raise ValueError("Invalid value for `result_url`, must not be `None`")  # noqa: E501

        self._result_url = result_url

    @property
    def queue_time_out_url(self):
        """Gets the queue_time_out_url of this TransactionStatusQueryRequest.  # noqa: E501

        URL where the results will be sent by M-Pesa API  # noqa: E501

        :return: The queue_time_out_url of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._queue_time_out_url

    @queue_time_out_url.setter
    def queue_time_out_url(self, queue_time_out_url):
        """Sets the queue_time_out_url of this TransactionStatusQueryRequest.

        URL where the results will be sent by M-Pesa API  # noqa: E501

        :param queue_time_out_url: The queue_time_out_url of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if queue_time_out_url is None:
            raise ValueError("Invalid value for `queue_time_out_url`, must not be `None`")  # noqa: E501

        self._queue_time_out_url = queue_time_out_url

    @property
    def remarks(self):
        """Gets the remarks of this TransactionStatusQueryRequest.  # noqa: E501

        Comments that are sent along with the transaction  # noqa: E501

        :return: The remarks of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this TransactionStatusQueryRequest.

        Comments that are sent along with the transaction  # noqa: E501

        :param remarks: The remarks of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """
        if remarks is None:
            raise ValueError("Invalid value for `remarks`, must not be `None`")  # noqa: E501

        self._remarks = remarks

    @property
    def occasion(self):
        """Gets the occasion of this TransactionStatusQueryRequest.  # noqa: E501


        :return: The occasion of this TransactionStatusQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._occasion

    @occasion.setter
    def occasion(self, occasion):
        """Sets the occasion of this TransactionStatusQueryRequest.


        :param occasion: The occasion of this TransactionStatusQueryRequest.  # noqa: E501
        :type: str
        """

        self._occasion = occasion

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
        if issubclass(TransactionStatusQueryRequest, dict):
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
        if not isinstance(other, TransactionStatusQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
