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

class CreateDocumentExport(object):
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
        'query_type': 'DocumentExportQueryType',
        'start_date': 'date',
        'end_date': 'date',
        'document_block_id': 'int',
        'export_type': 'DocumentExportType',
        'number_start_year': 'int',
        'number_start_sequence': 'int',
        'number_end_year': 'int',
        'number_end_sequence': 'int',
        'payment_method': 'PaymentMethod',
        'sort_by': 'DocumentExportSortBy',
        'other_options': 'DocumentExportOtherOptions',
        'filter_extra': 'DocumentExportFilterExtra'
    }

    attribute_map = {
        'query_type': 'query_type',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'document_block_id': 'document_block_id',
        'export_type': 'export_type',
        'number_start_year': 'number_start_year',
        'number_start_sequence': 'number_start_sequence',
        'number_end_year': 'number_end_year',
        'number_end_sequence': 'number_end_sequence',
        'payment_method': 'payment_method',
        'sort_by': 'sort_by',
        'other_options': 'other_options',
        'filter_extra': 'filter_extra'
    }

    def __init__(self, query_type=None, start_date=None, end_date=None, document_block_id=None, export_type=None, number_start_year=None, number_start_sequence=None, number_end_year=None, number_end_sequence=None, payment_method=None, sort_by=None, other_options=None, filter_extra=None):  # noqa: E501
        """CreateDocumentExport - a model defined in Swagger"""  # noqa: E501
        self._query_type = None
        self._start_date = None
        self._end_date = None
        self._document_block_id = None
        self._export_type = None
        self._number_start_year = None
        self._number_start_sequence = None
        self._number_end_year = None
        self._number_end_sequence = None
        self._payment_method = None
        self._sort_by = None
        self._other_options = None
        self._filter_extra = None
        self.discriminator = None
        self.query_type = query_type
        self.start_date = start_date
        self.end_date = end_date
        if document_block_id is not None:
            self.document_block_id = document_block_id
        self.export_type = export_type
        if number_start_year is not None:
            self.number_start_year = number_start_year
        if number_start_sequence is not None:
            self.number_start_sequence = number_start_sequence
        if number_end_year is not None:
            self.number_end_year = number_end_year
        if number_end_sequence is not None:
            self.number_end_sequence = number_end_sequence
        if payment_method is not None:
            self.payment_method = payment_method
        if sort_by is not None:
            self.sort_by = sort_by
        if other_options is not None:
            self.other_options = other_options
        if filter_extra is not None:
            self.filter_extra = filter_extra

    @property
    def query_type(self):
        """Gets the query_type of this CreateDocumentExport.  # noqa: E501


        :return: The query_type of this CreateDocumentExport.  # noqa: E501
        :rtype: DocumentExportQueryType
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this CreateDocumentExport.


        :param query_type: The query_type of this CreateDocumentExport.  # noqa: E501
        :type: DocumentExportQueryType
        """
        if query_type is None:
            raise ValueError("Invalid value for `query_type`, must not be `None`")  # noqa: E501

        self._query_type = query_type

    @property
    def start_date(self):
        """Gets the start_date of this CreateDocumentExport.  # noqa: E501


        :return: The start_date of this CreateDocumentExport.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreateDocumentExport.


        :param start_date: The start_date of this CreateDocumentExport.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreateDocumentExport.  # noqa: E501


        :return: The end_date of this CreateDocumentExport.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreateDocumentExport.


        :param end_date: The end_date of this CreateDocumentExport.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def document_block_id(self):
        """Gets the document_block_id of this CreateDocumentExport.  # noqa: E501


        :return: The document_block_id of this CreateDocumentExport.  # noqa: E501
        :rtype: int
        """
        return self._document_block_id

    @document_block_id.setter
    def document_block_id(self, document_block_id):
        """Sets the document_block_id of this CreateDocumentExport.


        :param document_block_id: The document_block_id of this CreateDocumentExport.  # noqa: E501
        :type: int
        """

        self._document_block_id = document_block_id

    @property
    def export_type(self):
        """Gets the export_type of this CreateDocumentExport.  # noqa: E501


        :return: The export_type of this CreateDocumentExport.  # noqa: E501
        :rtype: DocumentExportType
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """Sets the export_type of this CreateDocumentExport.


        :param export_type: The export_type of this CreateDocumentExport.  # noqa: E501
        :type: DocumentExportType
        """
        if export_type is None:
            raise ValueError("Invalid value for `export_type`, must not be `None`")  # noqa: E501

        self._export_type = export_type

    @property
    def number_start_year(self):
        """Gets the number_start_year of this CreateDocumentExport.  # noqa: E501


        :return: The number_start_year of this CreateDocumentExport.  # noqa: E501
        :rtype: int
        """
        return self._number_start_year

    @number_start_year.setter
    def number_start_year(self, number_start_year):
        """Sets the number_start_year of this CreateDocumentExport.


        :param number_start_year: The number_start_year of this CreateDocumentExport.  # noqa: E501
        :type: int
        """

        self._number_start_year = number_start_year

    @property
    def number_start_sequence(self):
        """Gets the number_start_sequence of this CreateDocumentExport.  # noqa: E501


        :return: The number_start_sequence of this CreateDocumentExport.  # noqa: E501
        :rtype: int
        """
        return self._number_start_sequence

    @number_start_sequence.setter
    def number_start_sequence(self, number_start_sequence):
        """Sets the number_start_sequence of this CreateDocumentExport.


        :param number_start_sequence: The number_start_sequence of this CreateDocumentExport.  # noqa: E501
        :type: int
        """

        self._number_start_sequence = number_start_sequence

    @property
    def number_end_year(self):
        """Gets the number_end_year of this CreateDocumentExport.  # noqa: E501


        :return: The number_end_year of this CreateDocumentExport.  # noqa: E501
        :rtype: int
        """
        return self._number_end_year

    @number_end_year.setter
    def number_end_year(self, number_end_year):
        """Sets the number_end_year of this CreateDocumentExport.


        :param number_end_year: The number_end_year of this CreateDocumentExport.  # noqa: E501
        :type: int
        """

        self._number_end_year = number_end_year

    @property
    def number_end_sequence(self):
        """Gets the number_end_sequence of this CreateDocumentExport.  # noqa: E501


        :return: The number_end_sequence of this CreateDocumentExport.  # noqa: E501
        :rtype: int
        """
        return self._number_end_sequence

    @number_end_sequence.setter
    def number_end_sequence(self, number_end_sequence):
        """Sets the number_end_sequence of this CreateDocumentExport.


        :param number_end_sequence: The number_end_sequence of this CreateDocumentExport.  # noqa: E501
        :type: int
        """

        self._number_end_sequence = number_end_sequence

    @property
    def payment_method(self):
        """Gets the payment_method of this CreateDocumentExport.  # noqa: E501


        :return: The payment_method of this CreateDocumentExport.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this CreateDocumentExport.


        :param payment_method: The payment_method of this CreateDocumentExport.  # noqa: E501
        :type: PaymentMethod
        """

        self._payment_method = payment_method

    @property
    def sort_by(self):
        """Gets the sort_by of this CreateDocumentExport.  # noqa: E501


        :return: The sort_by of this CreateDocumentExport.  # noqa: E501
        :rtype: DocumentExportSortBy
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this CreateDocumentExport.


        :param sort_by: The sort_by of this CreateDocumentExport.  # noqa: E501
        :type: DocumentExportSortBy
        """

        self._sort_by = sort_by

    @property
    def other_options(self):
        """Gets the other_options of this CreateDocumentExport.  # noqa: E501


        :return: The other_options of this CreateDocumentExport.  # noqa: E501
        :rtype: DocumentExportOtherOptions
        """
        return self._other_options

    @other_options.setter
    def other_options(self, other_options):
        """Sets the other_options of this CreateDocumentExport.


        :param other_options: The other_options of this CreateDocumentExport.  # noqa: E501
        :type: DocumentExportOtherOptions
        """

        self._other_options = other_options

    @property
    def filter_extra(self):
        """Gets the filter_extra of this CreateDocumentExport.  # noqa: E501


        :return: The filter_extra of this CreateDocumentExport.  # noqa: E501
        :rtype: DocumentExportFilterExtra
        """
        return self._filter_extra

    @filter_extra.setter
    def filter_extra(self, filter_extra):
        """Sets the filter_extra of this CreateDocumentExport.


        :param filter_extra: The filter_extra of this CreateDocumentExport.  # noqa: E501
        :type: DocumentExportFilterExtra
        """

        self._filter_extra = filter_extra

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
        if issubclass(CreateDocumentExport, dict):
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
        if not isinstance(other, CreateDocumentExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
