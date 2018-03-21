# rapid7vmconsole.AssetDiscoveryApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sonar_query**](AssetDiscoveryApi.md#create_sonar_query) | **POST** /api/3/sonar_queries | Sonar Queries
[**delete_sonar_query**](AssetDiscoveryApi.md#delete_sonar_query) | **DELETE** /api/3/sonar_queries/{id} | Sonar Query
[**get_discovery_connection**](AssetDiscoveryApi.md#get_discovery_connection) | **GET** /api/3/discovery_connections/{id} | Discovery Connection
[**get_discovery_connections**](AssetDiscoveryApi.md#get_discovery_connections) | **GET** /api/3/discovery_connections | Discovery Connections
[**get_sonar_queries**](AssetDiscoveryApi.md#get_sonar_queries) | **GET** /api/3/sonar_queries | Sonar Queries
[**get_sonar_query**](AssetDiscoveryApi.md#get_sonar_query) | **GET** /api/3/sonar_queries/{id} | Sonar Query
[**get_sonar_query_assets**](AssetDiscoveryApi.md#get_sonar_query_assets) | **GET** /api/3/sonar_queries/{id}/assets | Sonar Query Assets
[**reconnect_discovery_connection**](AssetDiscoveryApi.md#reconnect_discovery_connection) | **POST** /api/3/discovery_connections/{id}/connect | Discovery Connection Reconnect
[**sonar_query_search**](AssetDiscoveryApi.md#sonar_query_search) | **POST** /api/3/sonar_queries/search | Sonar Query Search
[**update_sonar_query**](AssetDiscoveryApi.md#update_sonar_query) | **PUT** /api/3/sonar_queries/{id} | Sonar Query


# **create_sonar_query**
> CreatedReferenceDiscoveryQueryIDLink create_sonar_query(query=query)

Sonar Queries

Creates a sonar query.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
query = rapid7vmconsole.SonarQuery() # SonarQuery | The criteria for a Sonar query. (optional)

try:
    # Sonar Queries
    api_response = api_instance.create_sonar_query(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->create_sonar_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**SonarQuery**](SonarQuery.md)| The criteria for a Sonar query. | [optional] 

### Return type

[**CreatedReferenceDiscoveryQueryIDLink**](CreatedReferenceDiscoveryQueryIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonar_query**
> Links delete_sonar_query(id)

Sonar Query

Removes a sonar query.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
id = 789 # int | The identifier of the Sonar query.

try:
    # Sonar Query
    api_response = api_instance.delete_sonar_query(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->delete_sonar_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the Sonar query. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery_connection**
> DiscoveryConnection get_discovery_connection(id)

Discovery Connection

Returns a discovery connection.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
id = 789 # int | The identifier of the discovery connection.

try:
    # Discovery Connection
    api_response = api_instance.get_discovery_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->get_discovery_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the discovery connection. | 

### Return type

[**DiscoveryConnection**](DiscoveryConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery_connections**
> PageOfDiscoveryConnection get_discovery_connections(page=page, size=size, sort=sort)

Discovery Connections

Returns all discovery connections.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Discovery Connections
    api_response = api_instance.get_discovery_connections(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->get_discovery_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfDiscoveryConnection**](PageOfDiscoveryConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonar_queries**
> ResourcesSonarQuery get_sonar_queries()

Sonar Queries

Returns all sonar queries.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()

try:
    # Sonar Queries
    api_response = api_instance.get_sonar_queries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->get_sonar_queries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourcesSonarQuery**](ResourcesSonarQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonar_query**
> SonarQuery get_sonar_query(id)

Sonar Query

Returns a sonar query.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
id = 789 # int | The identifier of the Sonar query.

try:
    # Sonar Query
    api_response = api_instance.get_sonar_query(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->get_sonar_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the Sonar query. | 

### Return type

[**SonarQuery**](SonarQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonar_query_assets**
> ResourcesDiscoveryAsset get_sonar_query_assets(id)

Sonar Query Assets

Returns the assets that are discovered by a Sonar query.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
id = 789 # int | The identifier of the Sonar query.

try:
    # Sonar Query Assets
    api_response = api_instance.get_sonar_query_assets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->get_sonar_query_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the Sonar query. | 

### Return type

[**ResourcesDiscoveryAsset**](ResourcesDiscoveryAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconnect_discovery_connection**
> reconnect_discovery_connection(id)

Discovery Connection Reconnect

Attempts to reconnect the discovery connection.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
id = 789 # int | The identifier of the discovery connection.

try:
    # Discovery Connection Reconnect
    api_instance.reconnect_discovery_connection(id)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->reconnect_discovery_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the discovery connection. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sonar_query_search**
> list[DiscoveryAsset] sonar_query_search(query=query)

Sonar Query Search

Executes a Sonar query to discover assets with the given search criteria.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
query = rapid7vmconsole.SonarCriteria() # SonarCriteria | The criteria for a Sonar query. (optional)

try:
    # Sonar Query Search
    api_response = api_instance.sonar_query_search(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->sonar_query_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**SonarCriteria**](SonarCriteria.md)| The criteria for a Sonar query. | [optional] 

### Return type

[**list[DiscoveryAsset]**](DiscoveryAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sonar_query**
> Links update_sonar_query(id, query=query)

Sonar Query

Updates a sonar query.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.AssetDiscoveryApi()
id = 789 # int | The identifier of the Sonar query.
query = rapid7vmconsole.SonarQuery() # SonarQuery | The criteria for a Sonar query. (optional)

try:
    # Sonar Query
    api_response = api_instance.update_sonar_query(id, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDiscoveryApi->update_sonar_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the Sonar query. | 
 **query** | [**SonarQuery**](SonarQuery.md)| The criteria for a Sonar query. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

