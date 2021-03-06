# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ScanTemplateDiscovery(object):
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
        'asset': 'ScanTemplateAssetDiscovery',
        'performance': 'ScanTemplateDiscoveryPerformance',
        'service': 'ScanTemplateServiceDiscovery'
    }

    attribute_map = {
        'asset': 'asset',
        'performance': 'performance',
        'service': 'service'
    }

    def __init__(self, asset=None, performance=None, service=None):  # noqa: E501
        """ScanTemplateDiscovery - a model defined in Swagger"""  # noqa: E501

        self._asset = None
        self._performance = None
        self._service = None
        self.discriminator = None

        if asset is not None:
            self.asset = asset
        if performance is not None:
            self.performance = performance
        if service is not None:
            self.service = service

    @property
    def asset(self):
        """Gets the asset of this ScanTemplateDiscovery.  # noqa: E501

        Asset discovery settings used during a scan.  # noqa: E501

        :return: The asset of this ScanTemplateDiscovery.  # noqa: E501
        :rtype: ScanTemplateAssetDiscovery
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this ScanTemplateDiscovery.

        Asset discovery settings used during a scan.  # noqa: E501

        :param asset: The asset of this ScanTemplateDiscovery.  # noqa: E501
        :type: ScanTemplateAssetDiscovery
        """

        self._asset = asset

    @property
    def performance(self):
        """Gets the performance of this ScanTemplateDiscovery.  # noqa: E501

        Discovery performance settings used during a scan.  # noqa: E501

        :return: The performance of this ScanTemplateDiscovery.  # noqa: E501
        :rtype: ScanTemplateDiscoveryPerformance
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this ScanTemplateDiscovery.

        Discovery performance settings used during a scan.  # noqa: E501

        :param performance: The performance of this ScanTemplateDiscovery.  # noqa: E501
        :type: ScanTemplateDiscoveryPerformance
        """

        self._performance = performance

    @property
    def service(self):
        """Gets the service of this ScanTemplateDiscovery.  # noqa: E501

        Service discovery settings used during a scan.  # noqa: E501

        :return: The service of this ScanTemplateDiscovery.  # noqa: E501
        :rtype: ScanTemplateServiceDiscovery
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ScanTemplateDiscovery.

        Service discovery settings used during a scan.  # noqa: E501

        :param service: The service of this ScanTemplateDiscovery.  # noqa: E501
        :type: ScanTemplateServiceDiscovery
        """

        self._service = service

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
        if issubclass(ScanTemplateDiscovery, dict):
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
        if not isinstance(other, ScanTemplateDiscovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
