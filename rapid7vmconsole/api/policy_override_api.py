# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rapid7vmconsole.api_client import ApiClient


class PolicyOverrideApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_policy_override(self, **kwargs):  # noqa: E501
        """Policy Overrides  # noqa: E501

        Submit a policy override. The policy override can be submitted or it can be submitted and approved in a single request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_override(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PolicyOverride policy_override: The specification of a policy override. Allows users to override the compliance result of a policy rule.
        :return: CreatedReferencePolicyOverrideIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_policy_override_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_override_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_policy_override_with_http_info(self, **kwargs):  # noqa: E501
        """Policy Overrides  # noqa: E501

        Submit a policy override. The policy override can be submitted or it can be submitted and approved in a single request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_override_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PolicyOverride policy_override: The specification of a policy override. Allows users to override the compliance result of a policy rule.
        :return: CreatedReferencePolicyOverrideIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_override']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy_override" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policy_override' in params:
            body_params = params['policy_override']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatedReferencePolicyOverrideIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_policy_override(self, id, **kwargs):  # noqa: E501
        """Policy Override  # noqa: E501

        Removes a policy override created for a policy rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy_override(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_policy_override_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_policy_override_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_policy_override_with_http_info(self, id, **kwargs):  # noqa: E501
        """Policy Override  # noqa: E501

        Removes a policy override created for a policy rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy_override_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_policy_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_asset_policy_overrides(self, id, **kwargs):  # noqa: E501
        """Asset Policy Overrides  # noqa: E501

        Retrieves policy overrides defined on policy rules for the specified asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_policy_overrides(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the asset. (required)
        :return: ResourcesPolicyOverride
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_policy_overrides_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_policy_overrides_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_asset_policy_overrides_with_http_info(self, id, **kwargs):  # noqa: E501
        """Asset Policy Overrides  # noqa: E501

        Retrieves policy overrides defined on policy rules for the specified asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_policy_overrides_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the asset. (required)
        :return: ResourcesPolicyOverride
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset_policy_overrides" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_asset_policy_overrides`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/assets/{id}/policy_overrides', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesPolicyOverride',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy_override(self, id, **kwargs):  # noqa: E501
        """Policy Override  # noqa: E501

        Retrieve the specified policy override.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_override(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :return: PolicyOverride
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_override_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_override_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_policy_override_with_http_info(self, id, **kwargs):  # noqa: E501
        """Policy Override  # noqa: E501

        Retrieve the specified policy override.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_override_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :return: PolicyOverride
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_policy_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyOverride',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy_override_expiration(self, id, **kwargs):  # noqa: E501
        """Policy Override Expiration  # noqa: E501

        Get the expiration date for a policy override.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_override_expiration(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_override_expiration_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_override_expiration_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_policy_override_expiration_with_http_info(self, id, **kwargs):  # noqa: E501
        """Policy Override Expiration  # noqa: E501

        Get the expiration date for a policy override.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_override_expiration_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_override_expiration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_policy_override_expiration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides/{id}/expires', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy_overrides(self, **kwargs):  # noqa: E501
        """Policy Overrides  # noqa: E501

        Retrieves policy overrides defined on policy rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_overrides(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The index of the page (zero-based) to retrieve.
        :param int size: The number of records per page to retrieve.
        :param list[str] sort: The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters.
        :return: PageOfPolicyOverride
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_overrides_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_overrides_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_policy_overrides_with_http_info(self, **kwargs):  # noqa: E501
        """Policy Overrides  # noqa: E501

        Retrieves policy overrides defined on policy rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_overrides_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The index of the page (zero-based) to retrieve.
        :param int size: The number of records per page to retrieve.
        :param list[str] sort: The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters.
        :return: PageOfPolicyOverride
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_overrides" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfPolicyOverride',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_policy_override_expiration(self, id, **kwargs):  # noqa: E501
        """Policy Override Expiration  # noqa: E501

        Set the expiration date for a policy override. This must be a valid date in the future.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_policy_override_expiration(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :param str expiration: The date the policy override is set to expire. Date is represented in ISO 8601 format.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_policy_override_expiration_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_policy_override_expiration_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_policy_override_expiration_with_http_info(self, id, **kwargs):  # noqa: E501
        """Policy Override Expiration  # noqa: E501

        Set the expiration date for a policy override. This must be a valid date in the future.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_policy_override_expiration_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :param str expiration: The date the policy override is set to expire. Date is represented in ISO 8601 format.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'expiration']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_policy_override_expiration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_policy_override_expiration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'expiration' in params:
            body_params = params['expiration']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides/{id}/expires', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_policy_override_status(self, id, status, **kwargs):  # noqa: E501
        """Policy Override Status  # noqa: E501

        Update the status of the specified policy override. The status can be one of the following: `\"recall\"`, `\"approve\"`, or `\"reject\"`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_policy_override_status(id, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :param str status: Policy Override Status (required)
        :param str comment: A comment describing the change of the policy override status.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_policy_override_status_with_http_info(id, status, **kwargs)  # noqa: E501
        else:
            (data) = self.set_policy_override_status_with_http_info(id, status, **kwargs)  # noqa: E501
            return data

    def set_policy_override_status_with_http_info(self, id, status, **kwargs):  # noqa: E501
        """Policy Override Status  # noqa: E501

        Update the status of the specified policy override. The status can be one of the following: `\"recall\"`, `\"approve\"`, or `\"reject\"`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_policy_override_status_with_http_info(id, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the policy override. (required)
        :param str status: Policy Override Status (required)
        :param str comment: A comment describing the change of the policy override status.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'status', 'comment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_policy_override_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_policy_override_status`")  # noqa: E501
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `set_policy_override_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'status' in params:
            path_params['status'] = params['status']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'comment' in params:
            body_params = params['comment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/policy_overrides/{id}/{status}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
