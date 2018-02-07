# swagger_client.AssetApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_tag**](AssetApi.md#add_asset_tag) | **PUT** /api/3/assets/{id}/tags/{tagId} | Asset Tag
[**create_asset**](AssetApi.md#create_asset) | **POST** /api/3/sites/{id}/assets | Assets
[**delete_asset**](AssetApi.md#delete_asset) | **DELETE** /api/3/assets/{id} | Asset
[**find_assets**](AssetApi.md#find_assets) | **POST** /api/3/assets/search | Asset Search
[**get_asset**](AssetApi.md#get_asset) | **GET** /api/3/assets/{id} | Asset
[**get_asset_databases**](AssetApi.md#get_asset_databases) | **GET** /api/3/assets/{id}/databases | Asset Databases
[**get_asset_files**](AssetApi.md#get_asset_files) | **GET** /api/3/assets/{id}/files | Asset Files
[**get_asset_service**](AssetApi.md#get_asset_service) | **GET** /api/3/assets/{id}/services/{protocol}/{port} | Asset Service
[**get_asset_service_configurations**](AssetApi.md#get_asset_service_configurations) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/configurations | Asset Service Configurations
[**get_asset_service_databases**](AssetApi.md#get_asset_service_databases) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/databases | Asset Service Databases
[**get_asset_service_user_groups**](AssetApi.md#get_asset_service_user_groups) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/user_groups | Asset Service User Groups
[**get_asset_service_users**](AssetApi.md#get_asset_service_users) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/users | Asset Service Users
[**get_asset_service_web_application**](AssetApi.md#get_asset_service_web_application) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/web_applications/{webApplicationId} | Asset Service Web Application
[**get_asset_service_web_applications**](AssetApi.md#get_asset_service_web_applications) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/web_applications | Asset Service Web Applications
[**get_asset_services**](AssetApi.md#get_asset_services) | **GET** /api/3/assets/{id}/services | Asset Services
[**get_asset_software**](AssetApi.md#get_asset_software) | **GET** /api/3/assets/{id}/software | Asset Software
[**get_asset_tags**](AssetApi.md#get_asset_tags) | **GET** /api/3/assets/{id}/tags | Asset Tags
[**get_asset_user_groups**](AssetApi.md#get_asset_user_groups) | **GET** /api/3/assets/{id}/user_groups | Asset User Groups
[**get_asset_users**](AssetApi.md#get_asset_users) | **GET** /api/3/assets/{id}/users | Asset Users
[**get_assets**](AssetApi.md#get_assets) | **GET** /api/3/assets | Assets
[**get_operating_system**](AssetApi.md#get_operating_system) | **GET** /api/3/operating_systems/{id} | Operating System
[**get_operating_systems**](AssetApi.md#get_operating_systems) | **GET** /api/3/operating_systems | Operating Systems
[**get_software**](AssetApi.md#get_software) | **GET** /api/3/software/{id} | Software
[**get_softwares**](AssetApi.md#get_softwares) | **GET** /api/3/software | Software
[**remove_asset_tag**](AssetApi.md#remove_asset_tag) | **DELETE** /api/3/assets/{id}/tags/{tagId} | Asset Tag


# **add_asset_tag**
> Links add_asset_tag(id, tag_id)

Asset Tag

Assigns the specified tag to the asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
tag_id = 56 # int | The identifier of the tag.

try:
    # Asset Tag
    api_response = api_instance.add_asset_tag(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->add_asset_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **tag_id** | **int**| The identifier of the tag. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset**
> CreatedReference create_asset(id, param1=param1)

Assets

Creates or updates an asset with the specified details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 56 # int | The identifier of the site.
param1 = swagger_client.AssetCreate() # AssetCreate | The details of the asset being added or updated.  The operating system can be specified in one of three ways, with the order of precedence: `\"osFingerprint\"`, `\"os\"`, `\"cpe\"` (optional)

try:
    # Assets
    api_response = api_instance.create_asset(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->create_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param1** | [**AssetCreate**](AssetCreate.md)| The details of the asset being added or updated.  The operating system can be specified in one of three ways, with the order of precedence: &#x60;\&quot;osFingerprint\&quot;&#x60;, &#x60;\&quot;os\&quot;&#x60;, &#x60;\&quot;cpe\&quot;&#x60; | [optional] 

### Return type

[**CreatedReference**](CreatedReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> Links delete_asset(id)

Asset

Deletes the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset
    api_response = api_instance.delete_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->delete_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_assets**
> PageOfAsset find_assets(param1, page=page, size=size, sort=sort)

Asset Search

Returns all assets for which you have access that match the given search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
param1 = swagger_client.SearchCriteria() # SearchCriteria | param1
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Asset Search
    api_response = api_instance.find_assets(param1, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->find_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param1** | [**SearchCriteria**](SearchCriteria.md)| param1 | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfAsset**](PageOfAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> Asset get_asset(id)

Asset

Returns the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset
    api_response = api_instance.get_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_databases**
> ResourcesDatabase get_asset_databases(id)

Asset Databases

Returns the databases enumerated on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Databases
    api_response = api_instance.get_asset_databases(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesDatabase**](ResourcesDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_files**
> ResourcesFile get_asset_files(id)

Asset Files

Returns the files discovered on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Files
    api_response = api_instance.get_asset_files(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesFile**](ResourcesFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service**
> Service get_asset_service(id, protocol, port)

Asset Service

Returns the service running a port and protocol on the asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.

try:
    # Asset Service
    api_response = api_instance.get_asset_service(id, protocol, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_configurations**
> ResourcesConfiguration get_asset_service_configurations(id, protocol, port)

Asset Service Configurations

Returns the configuration (properties) of a port and protocol on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.

try:
    # Asset Service Configurations
    api_response = api_instance.get_asset_service_configurations(id, protocol, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 

### Return type

[**ResourcesConfiguration**](ResourcesConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_databases**
> ResourcesDatabase get_asset_service_databases(id, protocol, port)

Asset Service Databases

Returns the databases running on a port and protocol on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.

try:
    # Asset Service Databases
    api_response = api_instance.get_asset_service_databases(id, protocol, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 

### Return type

[**ResourcesDatabase**](ResourcesDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_user_groups**
> ResourcesGroupAccount get_asset_service_user_groups(id, protocol, port)

Asset Service User Groups

Returns the user groups enumerated on a port and protocol on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.

try:
    # Asset Service User Groups
    api_response = api_instance.get_asset_service_user_groups(id, protocol, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 

### Return type

[**ResourcesGroupAccount**](ResourcesGroupAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_users**
> ResourcesUserAccount get_asset_service_users(id, protocol, port)

Asset Service Users

Returns the users enumerated on a port and protocol on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.

try:
    # Asset Service Users
    api_response = api_instance.get_asset_service_users(id, protocol, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 

### Return type

[**ResourcesUserAccount**](ResourcesUserAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_web_application**
> WebApplication get_asset_service_web_application(id, protocol, port, web_application_id)

Asset Service Web Application

Returns a web application running on a port and protocol on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.
web_application_id = 789 # int | The identifier of the web application.

try:
    # Asset Service Web Application
    api_response = api_instance.get_asset_service_web_application(id, protocol, port, web_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service_web_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 
 **web_application_id** | **int**| The identifier of the web application. | 

### Return type

[**WebApplication**](WebApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_web_applications**
> ReferencesWithWebApplicationIDLink get_asset_service_web_applications(id, protocol, port)

Asset Service Web Applications

Returns the web applications running on a port and protocol on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
protocol = 'protocol_example' # str | The protocol of the service.
port = 56 # int | The port of the service.

try:
    # Asset Service Web Applications
    api_response = api_instance.get_asset_service_web_applications(id, protocol, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_service_web_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **protocol** | **str**| The protocol of the service. | 
 **port** | **int**| The port of the service. | 

### Return type

[**ReferencesWithWebApplicationIDLink**](ReferencesWithWebApplicationIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_services**
> ReferencesWithReferenceWithEndpointIDLinkServiceLink get_asset_services(id)

Asset Services

Returns the services discovered on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Services
    api_response = api_instance.get_asset_services(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ReferencesWithReferenceWithEndpointIDLinkServiceLink**](ReferencesWithReferenceWithEndpointIDLinkServiceLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_software**
> ResourcesSoftware get_asset_software(id)

Asset Software

Returns the software on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Software
    api_response = api_instance.get_asset_software(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_software: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesSoftware**](ResourcesSoftware.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_tags**
> ResourcesAssetTag get_asset_tags(id)

Asset Tags

Returns tags assigned to an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Tags
    api_response = api_instance.get_asset_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesAssetTag**](ResourcesAssetTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_user_groups**
> ResourcesGroupAccount get_asset_user_groups(id)

Asset User Groups

Returns user groups enumerated on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset User Groups
    api_response = api_instance.get_asset_user_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesGroupAccount**](ResourcesGroupAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_users**
> ResourcesUserAccount get_asset_users(id)

Asset Users

Returns users enumerated on an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Users
    api_response = api_instance.get_asset_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesUserAccount**](ResourcesUserAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> PageOfAsset get_assets(page=page, size=size, sort=sort)

Assets

Returns all assets for which you have access.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Assets
    api_response = api_instance.get_assets(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfAsset**](PageOfAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operating_system**
> OperatingSystem get_operating_system(id)

Operating System

Returns the details for an operating system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the operating system.

try:
    # Operating System
    api_response = api_instance.get_operating_system(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_operating_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the operating system. | 

### Return type

[**OperatingSystem**](OperatingSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operating_systems**
> PageOfOperatingSystem get_operating_systems(page=page, size=size, sort=sort)

Operating Systems

Returns all operating systems discovered across all assets. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Operating Systems
    api_response = api_instance.get_operating_systems(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_operating_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfOperatingSystem**](PageOfOperatingSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software**
> Software get_software(id)

Software

Returns the details for software.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the software.

try:
    # Software
    api_response = api_instance.get_software(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_software: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the software. | 

### Return type

[**Software**](Software.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_softwares**
> PageOfSoftware get_softwares(page=page, size=size, sort=sort)

Software

Returns all software enumerated on any asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Software
    api_response = api_instance.get_softwares(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_softwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfSoftware**](PageOfSoftware.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_tag**
> Links remove_asset_tag(id, tag_id)

Asset Tag

Removes the specified tag from the asset's tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
id = 789 # int | The identifier of the asset.
tag_id = 56 # int | The identifier of the tag.

try:
    # Asset Tag
    api_response = api_instance.remove_asset_tag(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->remove_asset_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **tag_id** | **int**| The identifier of the tag. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

