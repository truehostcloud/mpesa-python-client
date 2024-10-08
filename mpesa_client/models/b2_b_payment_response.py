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

class B2BPaymentResponse(object):
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
        'originator_conversation_id': 'str',
        'conversation_id': 'str',
        'response_code': 'str',
        'response_description': 'str'
    }

    attribute_map = {
        'originator_conversation_id': 'OriginatorConversationID',
        'conversation_id': 'ConversationID',
        'response_code': 'ResponseCode',
        'response_description': 'ResponseDescription'
    }

    def __init__(self, originator_conversation_id=None, conversation_id=None, response_code=None, response_description=None):  # noqa: E501
        """B2BPaymentResponse - a model defined in Swagger"""  # noqa: E501
        self._originator_conversation_id = None
        self._conversation_id = None
        self._response_code = None
        self._response_description = None
        self.discriminator = None
        if originator_conversation_id is not None:
            self.originator_conversation_id = originator_conversation_id
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if response_code is not None:
            self.response_code = response_code
        if response_description is not None:
            self.response_description = response_description

    @property
    def originator_conversation_id(self):
        """Gets the originator_conversation_id of this B2BPaymentResponse.  # noqa: E501

        Unique request identifier assigned by Daraja upon successful request submission.  # noqa: E501

        :return: The originator_conversation_id of this B2BPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._originator_conversation_id

    @originator_conversation_id.setter
    def originator_conversation_id(self, originator_conversation_id):
        """Sets the originator_conversation_id of this B2BPaymentResponse.

        Unique request identifier assigned by Daraja upon successful request submission.  # noqa: E501

        :param originator_conversation_id: The originator_conversation_id of this B2BPaymentResponse.  # noqa: E501
        :type: str
        """

        self._originator_conversation_id = originator_conversation_id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this B2BPaymentResponse.  # noqa: E501

        Unique request identifier assigned by M-Pesa upon successful request submission.  # noqa: E501

        :return: The conversation_id of this B2BPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this B2BPaymentResponse.

        Unique request identifier assigned by M-Pesa upon successful request submission.  # noqa: E501

        :param conversation_id: The conversation_id of this B2BPaymentResponse.  # noqa: E501
        :type: str
        """

        self._conversation_id = conversation_id

    @property
    def response_code(self):
        """Gets the response_code of this B2BPaymentResponse.  # noqa: E501

        The numeric status code indicates the status of transaction processing. 0 means success and any other code means an error occurred or the transaction failed.  # noqa: E501

        :return: The response_code of this B2BPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this B2BPaymentResponse.

        The numeric status code indicates the status of transaction processing. 0 means success and any other code means an error occurred or the transaction failed.  # noqa: E501

        :param response_code: The response_code of this B2BPaymentResponse.  # noqa: E501
        :type: str
        """

        self._response_code = response_code

    @property
    def response_description(self):
        """Gets the response_description of this B2BPaymentResponse.  # noqa: E501

        Response description message  # noqa: E501

        :return: The response_description of this B2BPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_description

    @response_description.setter
    def response_description(self, response_description):
        """Sets the response_description of this B2BPaymentResponse.

        Response description message  # noqa: E501

        :param response_description: The response_description of this B2BPaymentResponse.  # noqa: E501
        :type: str
        """

        self._response_description = response_description

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
        if issubclass(B2BPaymentResponse, dict):
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
        if not isinstance(other, B2BPaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
