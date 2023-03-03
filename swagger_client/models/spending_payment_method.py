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

class SpendingPaymentMethod(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ARUHITEL = "aruhitel"
    BANKCARD = "bankcard"
    BARION = "barion"
    BARTER = "barter"
    CASH = "cash"
    CASH_ON_DELIVERY = "cash_on_delivery"
    COUPON = "coupon"
    ELORE_UTALAS = "elore_utalas"
    EP_KARTYA = "ep_kartya"
    KOMPENZACIO = "kompenzacio"
    LEVONAS = "levonas"
    ONLINE_BANKCARD = "online_bankcard"
    OTHER = "other"
    PAYLIKE = "paylike"
    PAYONEER = "payoneer"
    PAYPAL = "paypal"
    PAYPAL_UTOLAG = "paypal_utolag"
    PAYU = "payu"
    PICK_PACK_PONT = "pick_pack_pont"
    POSTAI_CSEKK = "postai_csekk"
    POSTAUTALVANY = "postautalvany"
    SKRILL = "skrill"
    SZEP_CARD = "szep_card"
    TRANSFERWISE = "transferwise"
    UPWORK = "upwork"
    UTALVANY = "utalvany"
    VALTO = "valto"
    WIRE_TRANSFER = "wire_transfer"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """SpendingPaymentMethod - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(SpendingPaymentMethod, dict):
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
        if not isinstance(other, SpendingPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
