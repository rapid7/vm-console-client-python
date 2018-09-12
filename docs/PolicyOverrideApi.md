# rapid7vmconsole.PolicyOverrideApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_override**](PolicyOverrideApi.md#create_policy_override) | **POST** /api/3/policy_overrides | Policy Overrides
[**delete_policy_override**](PolicyOverrideApi.md#delete_policy_override) | **DELETE** /api/3/policy_overrides/{id} | Policy Override
[**get_asset_policy_overrides**](PolicyOverrideApi.md#get_asset_policy_overrides) | **GET** /api/3/assets/{id}/policy_overrides | Asset Policy Overrides
[**get_policy_override**](PolicyOverrideApi.md#get_policy_override) | **GET** /api/3/policy_overrides/{id} | Policy Override
[**get_policy_override_expiration**](PolicyOverrideApi.md#get_policy_override_expiration) | **GET** /api/3/policy_overrides/{id}/expires | Policy Override Expiration
[**get_policy_overrides**](PolicyOverrideApi.md#get_policy_overrides) | **GET** /api/3/policy_overrides | Policy Overrides
[**set_policy_override_expiration**](PolicyOverrideApi.md#set_policy_override_expiration) | **PUT** /api/3/policy_overrides/{id}/expires | Policy Override Expiration
[**set_policy_override_status**](PolicyOverrideApi.md#set_policy_override_status) | **POST** /api/3/policy_overrides/{id}/{status} | Policy Override Status


# **create_policy_override**
> CreatedReferencePolicyOverrideIDLink create_policy_override(param0=param0)

Policy Overrides

Submit a policy override. The policy override can be submitted or it can be submitted and approved in a single request.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
param0 = rapid7vmconsole.PolicyOverride() # PolicyOverride | The specification of a policy override. Allows users to override the compliance result of a policy rule. (optional)

try:
    # Policy Overrides
    api_response = api_instance.create_policy_override(param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->create_policy_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param0** | [**PolicyOverride**](PolicyOverride.md)| The specification of a policy override. Allows users to override the compliance result of a policy rule. | [optional] 

### Return type

[**CreatedReferencePolicyOverrideIDLink**](CreatedReferencePolicyOverrideIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_override**
> Links delete_policy_override(id)

Policy Override

Removes a policy override created for a policy rule.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
id = 789 # int | The identifier of the policy override.

try:
    # Policy Override
    api_response = api_instance.delete_policy_override(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->delete_policy_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the policy override. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_policy_overrides**
> ResourcesPolicyOverride get_asset_policy_overrides(id)

Asset Policy Overrides

Retrieves policy overrides defined on policy rules for the specified asset.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
id = 789 # int | The identifier of the asset.

try:
    # Asset Policy Overrides
    api_response = api_instance.get_asset_policy_overrides(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->get_asset_policy_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 

### Return type

[**ResourcesPolicyOverride**](ResourcesPolicyOverride.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_override**
> PolicyOverride get_policy_override(id)

Policy Override

Retrieve the specified policy override.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
id = 789 # int | The identifier of the policy override.

try:
    # Policy Override
    api_response = api_instance.get_policy_override(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->get_policy_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the policy override. | 

### Return type

[**PolicyOverride**](PolicyOverride.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_override_expiration**
> str get_policy_override_expiration(id)

Policy Override Expiration

Get the expiration date for a policy override.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
id = 789 # int | The identifier of the policy override.

try:
    # Policy Override Expiration
    api_response = api_instance.get_policy_override_expiration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->get_policy_override_expiration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the policy override. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_overrides**
> PageOfPolicyOverride get_policy_overrides(page=page, size=size, sort=sort)

Policy Overrides

Retrieves policy overrides defined on policy rules.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Overrides
    api_response = api_instance.get_policy_overrides(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->get_policy_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyOverride**](PageOfPolicyOverride.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_policy_override_expiration**
> Links set_policy_override_expiration(id, param1=param1)

Policy Override Expiration

Set the expiration date for a policy override. This must be a valid date in the future.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
id = 789 # int | The identifier of the policy override.
param1 = 'param1_example' # str | The date the policy override is set to expire. Date is represented in ISO 8601 format. (optional)

try:
    # Policy Override Expiration
    api_response = api_instance.set_policy_override_expiration(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->set_policy_override_expiration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the policy override. | 
 **param1** | **str**| The date the policy override is set to expire. Date is represented in ISO 8601 format. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_policy_override_status**
> set_policy_override_status(id, status, param2=param2)

Policy Override Status

Update the status of the specified policy override. The status can be one of the following: `\"recall\"`, `\"approve\"`, or `\"reject\"`.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.PolicyOverrideApi()
id = 789 # int | The identifier of the policy override.
status = 'status_example' # str | Policy Override Status
param2 = 'param2_example' # str | A comment describing the change of the policy override status. (optional)

try:
    # Policy Override Status
    api_instance.set_policy_override_status(id, status, param2=param2)
except ApiException as e:
    print("Exception when calling PolicyOverrideApi->set_policy_override_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the policy override. | 
 **status** | **str**| Policy Override Status | 
 **param2** | **str**| A comment describing the change of the policy override status. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

