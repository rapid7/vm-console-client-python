# rapid7vmconsole.UserApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_asset_group**](UserApi.md#add_user_asset_group) | **PUT** /api/3/users/{id}/asset_groups/{assetGroupId} | Asset Group Access
[**add_user_site**](UserApi.md#add_user_site) | **PUT** /api/3/users/{id}/sites/{siteId} | Site Access
[**create_user**](UserApi.md#create_user) | **POST** /api/3/users | Users
[**delete_role**](UserApi.md#delete_role) | **DELETE** /api/3/roles/{id} | Role
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/3/users/{id} | User
[**get_authentication_source**](UserApi.md#get_authentication_source) | **GET** /api/3/authentication_sources/{id} | Authentication Source
[**get_authentication_source_users**](UserApi.md#get_authentication_source_users) | **GET** /api/3/authentication_sources/{id}/users | Authentication Source Users
[**get_authentication_sources**](UserApi.md#get_authentication_sources) | **GET** /api/3/authentication_sources | Authentication Sources
[**get_privilege**](UserApi.md#get_privilege) | **GET** /api/3/privileges/{id} | Privilege
[**get_privileges**](UserApi.md#get_privileges) | **GET** /api/3/privileges | Privileges
[**get_role**](UserApi.md#get_role) | **GET** /api/3/roles/{id} | Role
[**get_role_users**](UserApi.md#get_role_users) | **GET** /api/3/roles/{id}/users | Users With Role
[**get_roles**](UserApi.md#get_roles) | **GET** /api/3/roles | Roles
[**get_two_factor_authentication_key**](UserApi.md#get_two_factor_authentication_key) | **GET** /api/3/users/{id}/2FA | Two-Factor Authentication
[**get_user**](UserApi.md#get_user) | **GET** /api/3/users/{id} | User
[**get_user_asset_groups**](UserApi.md#get_user_asset_groups) | **GET** /api/3/users/{id}/asset_groups | Asset Groups Access
[**get_user_privileges**](UserApi.md#get_user_privileges) | **GET** /api/3/users/{id}/privileges | User Privileges
[**get_user_sites**](UserApi.md#get_user_sites) | **GET** /api/3/users/{id}/sites | Sites Access
[**get_users**](UserApi.md#get_users) | **GET** /api/3/users | Users
[**get_users_with_privilege**](UserApi.md#get_users_with_privilege) | **GET** /api/3/privileges/{id}/users | Users With Privilege
[**regenerate_two_factor_authentication**](UserApi.md#regenerate_two_factor_authentication) | **POST** /api/3/users/{id}/2FA | Two-Factor Authentication
[**remove_all_user_asset_groups**](UserApi.md#remove_all_user_asset_groups) | **DELETE** /api/3/users/{id}/asset_groups | Asset Groups Access
[**remove_all_user_sites**](UserApi.md#remove_all_user_sites) | **DELETE** /api/3/users/{id}/sites | Sites Access
[**remove_user_asset_group**](UserApi.md#remove_user_asset_group) | **DELETE** /api/3/users/{id}/asset_groups/{assetGroupId} | Asset Group Access
[**remove_user_site**](UserApi.md#remove_user_site) | **DELETE** /api/3/users/{id}/sites/{siteId} | Site Access
[**reset_password**](UserApi.md#reset_password) | **PUT** /api/3/users/{id}/password | Password Reset
[**set_two_factor_authentication**](UserApi.md#set_two_factor_authentication) | **PUT** /api/3/users/{id}/2FA | Two-Factor Authentication
[**set_user_asset_groups**](UserApi.md#set_user_asset_groups) | **PUT** /api/3/users/{id}/asset_groups | Asset Groups Access
[**set_user_sites**](UserApi.md#set_user_sites) | **PUT** /api/3/users/{id}/sites | Sites Access
[**unlock_user**](UserApi.md#unlock_user) | **DELETE** /api/3/users/{id}/lock | Unlock Account
[**update_role**](UserApi.md#update_role) | **PUT** /api/3/roles/{id} | Role
[**update_user**](UserApi.md#update_user) | **PUT** /api/3/users/{id} | User


# **add_user_asset_group**
> Links add_user_asset_group(id, asset_group_id)

Asset Group Access

Grants the user access to the asset group. Individual asset group access cannot be granted to users with the `allAssetGroups` permission. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
asset_group_id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Access
    api_response = api_instance.add_user_asset_group(id, asset_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **asset_group_id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_site**
> Links add_user_site(id, site_id)

Site Access

Grants the user access to the site. Individual site access cannot be granted to users with the `allSites` permission. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
site_id = 56 # int | The identifier of the site.

try:
    # Site Access
    api_response = api_instance.add_user_site(id, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **site_id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> CreatedReferenceUserIDLink create_user(user=user)

Users

Creates a new user. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
user = rapid7vmconsole.UserEdit() # UserEdit | The details of the user. (optional)

try:
    # Users
    api_response = api_instance.create_user(user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserEdit**](UserEdit.md)| The details of the user. | [optional] 

### Return type

[**CreatedReferenceUserIDLink**](CreatedReferenceUserIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> Links delete_role(id)

Role

Removes a role with the specified identifier. The role must not be built-in and cannot be currently assigned to any users.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 'id_example' # str | The identifier of the role.

try:
    # Role
    api_response = api_instance.delete_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the role. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Links delete_user(id)

User

Deletes a user account.<span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # User
    api_response = api_instance.delete_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_source**
> AuthenticationSource get_authentication_source(id)

Authentication Source

Returns the details for an authentication source.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the authentication source.

try:
    # Authentication Source
    api_response = api_instance.get_authentication_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_authentication_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the authentication source. | 

### Return type

[**AuthenticationSource**](AuthenticationSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_source_users**
> ReferencesWithUserIDLink get_authentication_source_users(id)

Authentication Source Users

Returns hypermedia links for the user accounts that use the authentication source to authenticate.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the authentication source.

try:
    # Authentication Source Users
    api_response = api_instance.get_authentication_source_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_authentication_source_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the authentication source. | 

### Return type

[**ReferencesWithUserIDLink**](ReferencesWithUserIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_sources**
> ResourcesAuthenticationSource get_authentication_sources()

Authentication Sources

Returns all available sources of authentication for users.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()

try:
    # Authentication Sources
    api_response = api_instance.get_authentication_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_authentication_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourcesAuthenticationSource**](ResourcesAuthenticationSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privilege**
> Links get_privilege(id)

Privilege

Returns the details for a privilege.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 'id_example' # str | The identifier of the privilege.

try:
    # Privilege
    api_response = api_instance.get_privilege(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the privilege. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privileges**
> Privileges get_privileges()

Privileges

Returns all privileges that may be granted to a role.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()

try:
    # Privileges
    api_response = api_instance.get_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Privileges**](Privileges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(id)

Role

Retrieves the details of a role.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 'id_example' # str | The identifier of the role.

try:
    # Role
    api_response = api_instance.get_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the role. | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_users**
> ReferencesWithUserIDLink get_role_users(id)

Users With Role

Returns hypermedia links for the the users currently assigned a role.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 'id_example' # str | The identifier of the role.

try:
    # Users With Role
    api_response = api_instance.get_role_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_role_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the role. | 

### Return type

[**ReferencesWithUserIDLink**](ReferencesWithUserIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> ResourcesRole get_roles()

Roles

Returns all roles for which users may be assigned.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()

try:
    # Roles
    api_response = api_instance.get_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourcesRole**](ResourcesRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_two_factor_authentication_key**
> TokenResource get_two_factor_authentication_key(id)

Two-Factor Authentication

Retrieves the current authentication token seed (key) for the user, if configured.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Two-Factor Authentication
    api_response = api_instance.get_two_factor_authentication_key(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_two_factor_authentication_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**TokenResource**](TokenResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id)

User

Returns the details for a user.<span class=\"authorization\">Global Administrator, Current User</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # User
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_asset_groups**
> ReferencesWithAssetGroupIDLink get_user_asset_groups(id)

Asset Groups Access

Returns the asset groups to which the user has access.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Asset Groups Access
    api_response = api_instance.get_user_asset_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**ReferencesWithAssetGroupIDLink**](ReferencesWithAssetGroupIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_privileges**
> Privileges get_user_privileges(id)

User Privileges

Returns the privileges granted to the user by their role. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # User Privileges
    api_response = api_instance.get_user_privileges(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**Privileges**](Privileges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_sites**
> ReferencesWithSiteIDLink get_user_sites(id)

Sites Access

Returns the sites to which the user has access.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Sites Access
    api_response = api_instance.get_user_sites(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**ReferencesWithSiteIDLink**](ReferencesWithSiteIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> PageOfUser get_users(page=page, size=size, sort=sort)

Users

Returns all defined users. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Users
    api_response = api_instance.get_users(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfUser**](PageOfUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_with_privilege**
> ReferencesWithUserIDLink get_users_with_privilege(id)

Users With Privilege

Returns hypermedia links for all users granted the specified privilege by their role.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 'id_example' # str | The identifier of the privilege.

try:
    # Users With Privilege
    api_response = api_instance.get_users_with_privilege(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_users_with_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the privilege. | 

### Return type

[**ReferencesWithUserIDLink**](ReferencesWithUserIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_two_factor_authentication**
> TokenResource regenerate_two_factor_authentication(id)

Two-Factor Authentication

Regenerates a new authentication token seed (key) and updates it for the user. This key may be then be used in the appropriate 2FA authenticator.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Two-Factor Authentication
    api_response = api_instance.regenerate_two_factor_authentication(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->regenerate_two_factor_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**TokenResource**](TokenResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_user_asset_groups**
> Links remove_all_user_asset_groups(id)

Asset Groups Access

Revokes access to all asset groups from the user.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Asset Groups Access
    api_response = api_instance.remove_all_user_asset_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_all_user_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_user_sites**
> Links remove_all_user_sites(id)

Sites Access

Revokes access to all sites from the user.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Sites Access
    api_response = api_instance.remove_all_user_sites(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_all_user_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_asset_group**
> Links remove_user_asset_group(id, asset_group_id)

Asset Group Access

Grants the user access to the asset group. Individual asset group access cannot be granted to users with the `allAssetGroups` permission. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
asset_group_id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Access
    api_response = api_instance.remove_user_asset_group(id, asset_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **asset_group_id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_site**
> Links remove_user_site(id, site_id)

Site Access

Grants the user access to the site. Individual site access cannot be granted to users with the `allSites` permission. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
site_id = 56 # int | The identifier of the site.

try:
    # Site Access
    api_response = api_instance.remove_user_site(id, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **site_id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> Links reset_password(id, password=password)

Password Reset

Changes the password for the user. Users may only change their own password.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
password = 'password_example' # str | The new password to set. (optional)

try:
    # Password Reset
    api_response = api_instance.reset_password(id, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **password** | **str**| The new password to set. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_two_factor_authentication**
> Links set_two_factor_authentication(id, token=token)

Two-Factor Authentication

Sets the authentication token seed (key) for the user. This key may be then be used in the appropriate 2FA authenticator.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
token = 'token_example' # str | The authentication token seed (key) to use for the user. (optional)

try:
    # Two-Factor Authentication
    api_response = api_instance.set_two_factor_authentication(id, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_two_factor_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **token** | **str**| The authentication token seed (key) to use for the user. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_asset_groups**
> Links set_user_asset_groups(id, asset_group_ids=asset_group_ids)

Asset Groups Access

Updates the asset groups to which the user has access. Individual asset group access cannot be granted to users with the `allAssetGroups` permission. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
asset_group_ids = [rapid7vmconsole.list[int]()] # list[int] | The identifiers of the asset groups to grant the user access to. Ignored if user has access to `allAssetGroups`. (optional)

try:
    # Asset Groups Access
    api_response = api_instance.set_user_asset_groups(id, asset_group_ids=asset_group_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_user_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **asset_group_ids** | **list[int]**| The identifiers of the asset groups to grant the user access to. Ignored if user has access to &#x60;allAssetGroups&#x60;. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_sites**
> Links set_user_sites(id, site_ids=site_ids)

Sites Access

Updates the sites to which the user has access. Individual site access cannot be granted to users with the `allSites` permission. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
site_ids = [rapid7vmconsole.list[int]()] # list[int] | The identifiers of the sites to grant the user access to. Ignored if the user has access to `allSites`. (optional)

try:
    # Sites Access
    api_response = api_instance.set_user_sites(id, site_ids=site_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_user_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **site_ids** | **list[int]**| The identifiers of the sites to grant the user access to. Ignored if the user has access to &#x60;allSites&#x60;. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> Links unlock_user(id)

Unlock Account

Unlocks a locked user account that has too many failed authentication attempts. Disabled accounts may not be unlocked.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.

try:
    # Unlock Account
    api_response = api_instance.unlock_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->unlock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Links update_role(id, role=role)

Role

Updates the details of a role.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 'id_example' # str | The identifier of the role.
role = rapid7vmconsole.Role() # Role | The details of the role. (optional)

try:
    # Role
    api_response = api_instance.update_role(id, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the role. | 
 **role** | [**Role**](Role.md)| The details of the role. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> Links update_user(id, user=user)

User

Updates the details of a user. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.UserApi()
id = 56 # int | The identifier of the user.
user = rapid7vmconsole.UserEdit() # UserEdit | The details of the user. (optional)

try:
    # User
    api_response = api_instance.update_user(id, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the user. | 
 **user** | [**UserEdit**](UserEdit.md)| The details of the user. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

