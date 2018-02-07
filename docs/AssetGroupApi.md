# swagger_client.AssetGroupApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_group_tag**](AssetGroupApi.md#add_asset_group_tag) | **PUT** /api/3/asset_groups/{id}/tags/{tagId} | Asset Group Tag
[**add_asset_group_user**](AssetGroupApi.md#add_asset_group_user) | **PUT** /api/3/asset_groups/{id}/users/{userId} | Asset Group User
[**add_asset_to_asset_group**](AssetGroupApi.md#add_asset_to_asset_group) | **PUT** /api/3/asset_groups/{id}/assets/{assetId} | Asset Group Asset
[**create_asset_group**](AssetGroupApi.md#create_asset_group) | **POST** /api/3/asset_groups | Asset Groups
[**delete_asset_group**](AssetGroupApi.md#delete_asset_group) | **DELETE** /api/3/asset_groups/{id} | Asset Group
[**get_asset_group**](AssetGroupApi.md#get_asset_group) | **GET** /api/3/asset_groups/{id} | Asset Group
[**get_asset_group_assets**](AssetGroupApi.md#get_asset_group_assets) | **GET** /api/3/asset_groups/{id}/assets | Asset Group Assets
[**get_asset_group_search_criteria**](AssetGroupApi.md#get_asset_group_search_criteria) | **GET** /api/3/asset_groups/{id}/search_criteria | Asset Group Search Criteria
[**get_asset_group_tags**](AssetGroupApi.md#get_asset_group_tags) | **GET** /api/3/asset_groups/{id}/tags | Asset Group Tags
[**get_asset_group_users**](AssetGroupApi.md#get_asset_group_users) | **GET** /api/3/asset_groups/{id}/users | Asset Group Users
[**get_asset_groups**](AssetGroupApi.md#get_asset_groups) | **GET** /api/3/asset_groups | Asset Groups
[**remove_all_asset_group_tags**](AssetGroupApi.md#remove_all_asset_group_tags) | **DELETE** /api/3/asset_groups/{id}/tags | Asset Group Tags
[**remove_all_assets_from_asset_group**](AssetGroupApi.md#remove_all_assets_from_asset_group) | **DELETE** /api/3/asset_groups/{id}/assets | Asset Group Assets
[**remove_asset_from_asset_group**](AssetGroupApi.md#remove_asset_from_asset_group) | **DELETE** /api/3/asset_groups/{id}/assets/{assetId} | Asset Group Asset
[**remove_asset_group_tag**](AssetGroupApi.md#remove_asset_group_tag) | **DELETE** /api/3/asset_groups/{id}/tags/{tagId} | Asset Group Tag
[**remove_asset_group_user**](AssetGroupApi.md#remove_asset_group_user) | **DELETE** /api/3/asset_groups/{id}/users/{userId} | Asset Group User
[**set_asset_group_search_criteria**](AssetGroupApi.md#set_asset_group_search_criteria) | **PUT** /api/3/asset_groups/{id}/search_criteria | Asset Group Search Criteria
[**set_asset_group_tags**](AssetGroupApi.md#set_asset_group_tags) | **PUT** /api/3/asset_groups/{id}/tags | Asset Group Tags
[**set_asset_group_users**](AssetGroupApi.md#set_asset_group_users) | **PUT** /api/3/asset_groups/{id}/users | Asset Group Users
[**update_asset_group**](AssetGroupApi.md#update_asset_group) | **PUT** /api/3/asset_groups/{id} | Asset Group
[**update_asset_group_assets**](AssetGroupApi.md#update_asset_group_assets) | **PUT** /api/3/asset_groups/{id}/assets | Asset Group Assets


# **add_asset_group_tag**
> Links add_asset_group_tag(id, tag_id)

Asset Group Tag

Adds a tag to an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
tag_id = 56 # int | The identifier of the tag.

try:
    # Asset Group Tag
    api_response = api_instance.add_asset_group_tag(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->add_asset_group_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **tag_id** | **int**| The identifier of the tag. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asset_group_user**
> Links add_asset_group_user(id, user_id)

Asset Group User

Grants a user with sufficient privileges access to the asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
user_id = 56 # int | The identifier of the user.

try:
    # Asset Group User
    api_response = api_instance.add_asset_group_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->add_asset_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **user_id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asset_to_asset_group**
> Links add_asset_to_asset_group(id, asset_id)

Asset Group Asset

Adds an asset to a static asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
asset_id = 789 # int | The identifier of the asset.

try:
    # Asset Group Asset
    api_response = api_instance.add_asset_to_asset_group(id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->add_asset_to_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_group**
> CreatedReferenceAssetGroupIDLink create_asset_group(param0=param0)

Asset Groups

Creates a new asset group. The `searchCriteria` field can be passed no matter what the type of the asset group is. The asset group `type` changes when the assets are refreshed. Dynamic asset groups constantly refreshed their membership as assets are scanned whereas static asset groups do not change membership automatically.  See the <a href=\"#section/Responses/SearchCriteria\">Search Criteria</a> for more information on using dynamic criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
param0 = swagger_client.AssetGroup() # AssetGroup | The details of the asset group. (optional)

try:
    # Asset Groups
    api_response = api_instance.create_asset_group(param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->create_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param0** | [**AssetGroup**](AssetGroup.md)| The details of the asset group. | [optional] 

### Return type

[**CreatedReferenceAssetGroupIDLink**](CreatedReferenceAssetGroupIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_group**
> Links delete_asset_group(id)

Asset Group

Deletes the asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group
    api_response = api_instance.delete_asset_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->delete_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_group**
> AssetGroup get_asset_group(id)

Asset Group

Returns an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group
    api_response = api_instance.get_asset_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->get_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**AssetGroup**](AssetGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_group_assets**
> ReferencesWithAssetIDLink get_asset_group_assets(id)

Asset Group Assets

Returns hypermedia links for the assets that belong to an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Assets
    api_response = api_instance.get_asset_group_assets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->get_asset_group_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**ReferencesWithAssetIDLink**](ReferencesWithAssetIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_group_search_criteria**
> SearchCriteria get_asset_group_search_criteria(id)

Asset Group Search Criteria

Returns the search criteria of a dynamic asset group.For a reference of valid search criteria input see the <a href=\"#operation/getAssetsSearchUsingPOST\">Asset Search</a> resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Search Criteria
    api_response = api_instance.get_asset_group_search_criteria(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->get_asset_group_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**SearchCriteria**](SearchCriteria.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_group_tags**
> ReferencesWithTagIDLink get_asset_group_tags(id)

Asset Group Tags

Returns the tags assigned to an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Tags
    api_response = api_instance.get_asset_group_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->get_asset_group_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**ReferencesWithTagIDLink**](ReferencesWithTagIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_group_users**
> ReferencesWithUserIDLink get_asset_group_users(id)

Asset Group Users

Returns hypermedia links for the users with access to this asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Users
    api_response = api_instance.get_asset_group_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->get_asset_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**ReferencesWithUserIDLink**](ReferencesWithUserIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_groups**
> PageOfAssetGroup get_asset_groups(type=type, name=name, page=page, size=size, sort=sort)

Asset Groups

Returns all asset groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
type = 'type_example' # str | The type of asset group. (optional)
name = 'name_example' # str | A search pattern for the name of the asset group. Searches are case-insensitive contains. (optional)
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Asset Groups
    api_response = api_instance.get_asset_groups(type=type, name=name, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->get_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of asset group. | [optional] 
 **name** | **str**| A search pattern for the name of the asset group. Searches are case-insensitive contains. | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfAssetGroup**](PageOfAssetGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_asset_group_tags**
> Links remove_all_asset_group_tags(id)

Asset Group Tags

Removes all tag associations from the asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Tags
    api_response = api_instance.remove_all_asset_group_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->remove_all_asset_group_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_assets_from_asset_group**
> Links remove_all_assets_from_asset_group(id)

Asset Group Assets

Removes the assets from the given static asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.

try:
    # Asset Group Assets
    api_response = api_instance.remove_all_assets_from_asset_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->remove_all_assets_from_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_from_asset_group**
> Links remove_asset_from_asset_group(id, asset_id)

Asset Group Asset

Removes an asset from an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
asset_id = 789 # int | The identifier of the asset.

try:
    # Asset Group Asset
    api_response = api_instance.remove_asset_from_asset_group(id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->remove_asset_from_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_group_tag**
> Links remove_asset_group_tag(id, tag_id)

Asset Group Tag

Removes a tag from an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
tag_id = 56 # int | The identifier of the tag.

try:
    # Asset Group Tag
    api_response = api_instance.remove_asset_group_tag(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->remove_asset_group_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **tag_id** | **int**| The identifier of the tag. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_group_user**
> Links remove_asset_group_user(id, user_id)

Asset Group User

Removes a user's access from an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
user_id = 56 # int | The identifier of the user.

try:
    # Asset Group User
    api_response = api_instance.remove_asset_group_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->remove_asset_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **user_id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_group_search_criteria**
> Links set_asset_group_search_criteria(id, param1=param1)

Asset Group Search Criteria

Updates the search criteria of a dynamic asset group. For a reference of valid search criteria input see the <a href=\"#operation/getAssetsSearchUsingPOST\">Asset Search</a> resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
param1 = swagger_client.SearchCriteria() # SearchCriteria | The search criteria specification. (optional)

try:
    # Asset Group Search Criteria
    api_response = api_instance.set_asset_group_search_criteria(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->set_asset_group_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **param1** | [**SearchCriteria**](SearchCriteria.md)| The search criteria specification. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_group_tags**
> Links set_asset_group_tags(id, param1=param1)

Asset Group Tags

Updates the tags of an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
param1 = [swagger_client.list[int]()] # list[int] | The tags to associate to the asset group. (optional)

try:
    # Asset Group Tags
    api_response = api_instance.set_asset_group_tags(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->set_asset_group_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **param1** | **list[int]**| The tags to associate to the asset group. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_group_users**
> Links set_asset_group_users(id, param1=param1)

Asset Group Users

Grants users with sufficient privileges access to an asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
param1 = [swagger_client.list[int]()] # list[int] | The users to grant access to the asset group. (optional)

try:
    # Asset Group Users
    api_response = api_instance.set_asset_group_users(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->set_asset_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **param1** | **list[int]**| The users to grant access to the asset group. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_group**
> Links update_asset_group(id, param1=param1)

Asset Group

Updates the details of an asset group. See the search criteria endpoint (/search_criteria) for more information about building the search criteria and examples.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
param1 = swagger_client.AssetGroup() # AssetGroup | The details of the asset group. (optional)

try:
    # Asset Group
    api_response = api_instance.update_asset_group(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->update_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **param1** | [**AssetGroup**](AssetGroup.md)| The details of the asset group. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_group_assets**
> Links update_asset_group_assets(id, param1=param1)

Asset Group Assets

Updates all the assets that belong to a static asset group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetGroupApi()
id = 56 # int | The identifier of the asset group.
param1 = [swagger_client.list[int]()] # list[int] | The assets to place in the asset group.  (optional)

try:
    # Asset Group Assets
    api_response = api_instance.update_asset_group_assets(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetGroupApi->update_asset_group_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset group. | 
 **param1** | **list[int]**| The assets to place in the asset group.  | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

