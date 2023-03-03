# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.  # noqa: E501

    OpenAPI spec version: 3.0.14
    Contact: hello@billingo.hu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OnlineSzamlaStatus(object):
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
        'transaction_id': 'str',
        'status': 'str',
        'messages': 'list[OnlineSzamlaStatusMessage]'
    }

    attribute_map = {
        'transaction_id': 'transaction_id',
        'status': 'status',
        'messages': 'messages'
    }

    def __init__(self, transaction_id=None, status=None, messages=None):  # noqa: E501
        """OnlineSzamlaStatus - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._status = None
        self._messages = None
        self.discriminator = None
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if status is not None:
            self.status = status
        if messages is not None:
            self.messages = messages

    @property
    def transaction_id(self):
        """Gets the transaction_id of this OnlineSzamlaStatus.  # noqa: E501


        :return: The transaction_id of this OnlineSzamlaStatus.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this OnlineSzamlaStatus.


        :param transaction_id: The transaction_id of this OnlineSzamlaStatus.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def status(self):
        """Gets the status of this OnlineSzamlaStatus.  # noqa: E501


        :return: The status of this OnlineSzamlaStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OnlineSzamlaStatus.


        :param status: The status of this OnlineSzamlaStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def messages(self):
        """Gets the messages of this OnlineSzamlaStatus.  # noqa: E501


        :return: The messages of this OnlineSzamlaStatus.  # noqa: E501
        :rtype: list[OnlineSzamlaStatusMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this OnlineSzamlaStatus.


        :param messages: The messages of this OnlineSzamlaStatus.  # noqa: E501
        :type: list[OnlineSzamlaStatusMessage]
        """

        self._messages = messages

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
        if issubclass(OnlineSzamlaStatus, dict):
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
        if not isinstance(other, OnlineSzamlaStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other