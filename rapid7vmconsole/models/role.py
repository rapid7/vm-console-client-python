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


class Role(object):
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
        'description': 'str',
        'id': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'privileges': 'privileges'
    }

    def __init__(self, description=None, id=None, links=None, name=None, privileges=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._links = None
        self._name = None
        self._privileges = None
        self.discriminator = None

        self.description = description
        self.id = id
        if links is not None:
            self.links = links
        self.name = name
        if privileges is not None:
            self.privileges = privileges

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501

        The description of the role.  # noqa: E501

        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.

        The description of the role.  # noqa: E501

        :param description: The description of this Role.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501

        The identifier of the role.  # noqa: E501

        :return: The id of this Role.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.

        The identifier of the role.  # noqa: E501

        :param id: The id of this Role.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def links(self):
        """Gets the links of this Role.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Role.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Role.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Role.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501

        The human readable name of the role.  # noqa: E501

        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.

        The human readable name of the role.  # noqa: E501

        :param name: The name of this Role.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def privileges(self):
        """Gets the privileges of this Role.  # noqa: E501

        The privileges granted to the role.  # noqa: E501

        :return: The privileges of this Role.  # noqa: E501
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this Role.

        The privileges granted to the role.  # noqa: E501

        :param privileges: The privileges of this Role.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["all-permissions", "create-reports", "configure-global-settings", "manage-sites", "manage-tags", "manage-static-asset-groups", "manage-dynamic-asset-groups", "manage-scan-templates", "manage-report-templates", "manage-scan-engines", "submit-vulnerability-exceptions", "approve-vulnerability-exceptions", "delete-vulnerability-exceptions", "manage-vuln-investigations", "view-vuln-investigations", "create-tickets", "close-tickets", "assign-ticket-assignee", "manage-site-access", "manage-asset-group-access", "manage-report-access", "use-restricted-report-sections", "manage-policies", "view-asset-group-asset-data", "manage-asset-group-assets", "view-site-asset-data", "specify-site-metadata", "purge-site-asset-data", "specify-scan-targets", "assign-scan-engine", "assign-scan-template", "manage-site-credentials", "manage-scan-alerts", "schedule-automatic-scans", "start-unscheduled-scans"]  # noqa: E501
        if not set(privileges).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `privileges` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(privileges) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._privileges = privileges

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
