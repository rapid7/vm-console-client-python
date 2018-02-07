# swagger_client.PolicyApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_policy_children**](PolicyApi.md#get_asset_policy_children) | **GET** /api/3/assets/{assetId}/policies/{policyId}/children | Policy Rules or Groups Directly Under Policy For Asset
[**get_asset_policy_group_children**](PolicyApi.md#get_asset_policy_group_children) | **GET** /api/3/assets/{assetId}/policies/{policyId}/groups/{groupId}/children | Policy Rules or Groups Directly Under Policy Group For Asset
[**get_asset_policy_rules_summary**](PolicyApi.md#get_asset_policy_rules_summary) | **GET** /api/3/assets/{assetId}/policies/{policyId}/rules | Policy Rules For Asset
[**get_descendant_policy_rules**](PolicyApi.md#get_descendant_policy_rules) | **GET** /api/3/policies/{policyId}/groups/{groupId}/rules | Policy Rules Under Policy Group
[**get_disabled_policy_rules**](PolicyApi.md#get_disabled_policy_rules) | **GET** /api/3/policies/{policyId}/rules/disabled | Disabled Policy Rules
[**get_policies**](PolicyApi.md#get_policies) | **GET** /api/3/policies | Policies
[**get_policies_for_asset**](PolicyApi.md#get_policies_for_asset) | **GET** /api/3/assets/{assetId}/policies | Policies For Asset
[**get_policy**](PolicyApi.md#get_policy) | **GET** /api/3/policies/{policyId} | Policy
[**get_policy_asset_result**](PolicyApi.md#get_policy_asset_result) | **GET** /api/3/policies/{policyId}/assets/{assetId} | Policy Asset Result
[**get_policy_asset_results**](PolicyApi.md#get_policy_asset_results) | **GET** /api/3/policies/{policyId}/assets | Policy Asset Results
[**get_policy_children**](PolicyApi.md#get_policy_children) | **GET** /api/3/policies/{id}/children | Policy Rules or Groups Directly Under Policy
[**get_policy_group**](PolicyApi.md#get_policy_group) | **GET** /api/3/policies/{policyId}/groups/{groupId} | Policy Group
[**get_policy_group_asset_result**](PolicyApi.md#get_policy_group_asset_result) | **GET** /api/3/policies/{policyId}/groups/{groupId}/assets/{assetId} | Asset Compliance For Policy Rules Under Policy Group
[**get_policy_group_asset_results**](PolicyApi.md#get_policy_group_asset_results) | **GET** /api/3/policies/{policyId}/groups/{groupId}/assets | Assets Compliance For Policy Rules Under Policy Group
[**get_policy_group_children**](PolicyApi.md#get_policy_group_children) | **GET** /api/3/policies/{policyId}/groups/{groupId}/children | Policy Rules or Groups Directly Under Policy Group
[**get_policy_group_rules_with_asset_assessment**](PolicyApi.md#get_policy_group_rules_with_asset_assessment) | **GET** /api/3/assets/{assetId}/policies/{policyId}/groups/{groupId}/rules | Policy Rules Under Policy Group For Asset
[**get_policy_groups**](PolicyApi.md#get_policy_groups) | **GET** /api/3/policies/{policyId}/groups | Policy Groups
[**get_policy_rule**](PolicyApi.md#get_policy_rule) | **GET** /api/3/policies/{policyId}/rules/{ruleId} | Policy Rule
[**get_policy_rule_asset_result**](PolicyApi.md#get_policy_rule_asset_result) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/assets/{assetId} | Asset Compliance For Policy Rule
[**get_policy_rule_asset_result_proof**](PolicyApi.md#get_policy_rule_asset_result_proof) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/assets/{assetId}/proof | Policy Rule Proof For Asset
[**get_policy_rule_asset_results**](PolicyApi.md#get_policy_rule_asset_results) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/assets | Assets Compliance For Policy Rule
[**get_policy_rule_controls**](PolicyApi.md#get_policy_rule_controls) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/controls | Policy Rule Controls
[**get_policy_rule_rationale**](PolicyApi.md#get_policy_rule_rationale) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/rationale | Policy Rule Rationale
[**get_policy_rule_remediation**](PolicyApi.md#get_policy_rule_remediation) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/remediation | Policy Rule Remediation
[**get_policy_rules**](PolicyApi.md#get_policy_rules) | **GET** /api/3/policies/{policyId}/rules | Policy Rules
[**get_policy_summary**](PolicyApi.md#get_policy_summary) | **GET** /api/3/policy/summary | Policy Compliance Summaries


# **get_asset_policy_children**
> PageOfAssetPolicyItem get_asset_policy_children(asset_id, policy_id)

Policy Rules or Groups Directly Under Policy For Asset

Retrieves a paged resource of either policy rules, or groups, that are defined directly underneath the specified policy with rule compliance results for the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
asset_id = 789 # int | The identifier of the asset.
policy_id = 789 # int | The identifier of the policy

try:
    # Policy Rules or Groups Directly Under Policy For Asset
    api_response = api_instance.get_asset_policy_children(asset_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_asset_policy_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The identifier of the asset. | 
 **policy_id** | **int**| The identifier of the policy | 

### Return type

[**PageOfAssetPolicyItem**](PageOfAssetPolicyItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_policy_group_children**
> PageOfAssetPolicyItem get_asset_policy_group_children(asset_id, policy_id, group_id)

Policy Rules or Groups Directly Under Policy Group For Asset

Retrieves a paged resource of either policy rules, or groups, that are defined directly underneath the specified policy group with rule compliance results for the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
asset_id = 789 # int | The identifier of the asset.
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.

try:
    # Policy Rules or Groups Directly Under Policy Group For Asset
    api_response = api_instance.get_asset_policy_group_children(asset_id, policy_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_asset_policy_group_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The identifier of the asset. | 
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 

### Return type

[**PageOfAssetPolicyItem**](PageOfAssetPolicyItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_policy_rules_summary**
> PageOfPolicyRule get_asset_policy_rules_summary(asset_id, policy_id, page=page, size=size, sort=sort)

Policy Rules For Asset

Retrieves the list of policy rules with compliance results for the specified asset and policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
asset_id = 789 # int | The identifier of the asset.
policy_id = 789 # int | The identifier of the policy
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Rules For Asset
    api_response = api_instance.get_asset_policy_rules_summary(asset_id, policy_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_asset_policy_rules_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The identifier of the asset. | 
 **policy_id** | **int**| The identifier of the policy | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyRule**](PageOfPolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_descendant_policy_rules**
> PageOfPolicyRule get_descendant_policy_rules(policy_id, group_id, page=page, size=size, sort=sort)

Policy Rules Under Policy Group

Retrieves the list of policy rules defined directly, or indirectly, underneath the specified policy group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Rules Under Policy Group
    api_response = api_instance.get_descendant_policy_rules(policy_id, group_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_descendant_policy_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyRule**](PageOfPolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disabled_policy_rules**
> PageOfPolicyRule get_disabled_policy_rules(policy_id, page=page, size=size, sort=sort)

Disabled Policy Rules

Retrieves a paged resource of disabled policy rules for the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Disabled Policy Rules
    api_response = api_instance.get_disabled_policy_rules(policy_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_disabled_policy_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyRule**](PageOfPolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> PageOfPolicy get_policies(filter=filter, scanned_only=scanned_only, page=page, size=size, sort=sort)

Policies

Retrieves a paged resource of policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Filters the retrieved policies with those whose titles that match the parameter. (optional)
scanned_only = true # bool | Flag indicating the policies retrieved should only include those with Pass or Fail compliance results. The list of scanned policies is based on the user's list of accessible assets. (optional)
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policies
    api_response = api_instance.get_policies(filter=filter, scanned_only=scanned_only, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the retrieved policies with those whose titles that match the parameter. | [optional] 
 **scanned_only** | **bool**| Flag indicating the policies retrieved should only include those with Pass or Fail compliance results. The list of scanned policies is based on the user&#39;s list of accessible assets. | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicy**](PageOfPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies_for_asset**
> PageOfAssetPolicy get_policies_for_asset(asset_id, applicable_only=applicable_only, page=page, size=size, sort=sort)

Policies For Asset

Retrieves the list of policies with compliance results for the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
asset_id = 789 # int | The identifier of the asset.
applicable_only = true # bool | An optional boolean parameter indicating the policies retrieved should only include those with a policy compliance status of either a PASS of FAIL result. Default value is `false`, which will also include policies with a compliance status of NOT_APPLICABLE. (optional)
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policies For Asset
    api_response = api_instance.get_policies_for_asset(asset_id, applicable_only=applicable_only, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policies_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The identifier of the asset. | 
 **applicable_only** | **bool**| An optional boolean parameter indicating the policies retrieved should only include those with a policy compliance status of either a PASS of FAIL result. Default value is &#x60;false&#x60;, which will also include policies with a compliance status of NOT_APPLICABLE. | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfAssetPolicy**](PageOfAssetPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(policy_id)

Policy

Retrieves the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy

try:
    # Policy
    api_response = api_instance.get_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_asset_result**
> PolicyAsset get_policy_asset_result(policy_id, asset_id)

Policy Asset Result

Retrieves an asset resource with rule compliance results for the specified asset and policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
asset_id = 789 # int | The identifier of the asset.

try:
    # Policy Asset Result
    api_response = api_instance.get_policy_asset_result(policy_id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_asset_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

[**PolicyAsset**](PolicyAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_asset_results**
> PageOfPolicyAsset get_policy_asset_results(policy_id, applicable_only=applicable_only, page=page, size=size, sort=sort)

Policy Asset Results

Retrieves asset resources with rule compliance results for the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
applicable_only = true # bool | An optional boolean parameter indicating the assets retrieved should only include those with rule results of either PASS or FAIL. Default value is `false`, which will also include assets with a compliance status of NOT_APPLICABLE. (optional)
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Asset Results
    api_response = api_instance.get_policy_asset_results(policy_id, applicable_only=applicable_only, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_asset_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **applicable_only** | **bool**| An optional boolean parameter indicating the assets retrieved should only include those with rule results of either PASS or FAIL. Default value is &#x60;false&#x60;, which will also include assets with a compliance status of NOT_APPLICABLE. | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyAsset**](PageOfPolicyAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_children**
> PageOfPolicyItem get_policy_children(id)

Policy Rules or Groups Directly Under Policy

Retrieves a paged resource of either policy rules, or groups, that are defined directly underneath the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
id = 789 # int | The identifier of the policy

try:
    # Policy Rules or Groups Directly Under Policy
    api_response = api_instance.get_policy_children(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the policy | 

### Return type

[**PageOfPolicyItem**](PageOfPolicyItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_group**
> PolicyGroup get_policy_group(policy_id, group_id)

Policy Group

Retrieves the specified policy group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.

try:
    # Policy Group
    api_response = api_instance.get_policy_group(policy_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 

### Return type

[**PolicyGroup**](PolicyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_group_asset_result**
> PolicyAsset get_policy_group_asset_result(policy_id, group_id, asset_id)

Asset Compliance For Policy Rules Under Policy Group

Retrieves an asset resource with rule compliance status against all rules under the specified policy group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.
asset_id = 789 # int | The identifier of the asset.

try:
    # Asset Compliance For Policy Rules Under Policy Group
    api_response = api_instance.get_policy_group_asset_result(policy_id, group_id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_group_asset_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

[**PolicyAsset**](PolicyAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_group_asset_results**
> PageOfPolicyAsset get_policy_group_asset_results(policy_id, group_id, applicable_only=applicable_only, page=page, size=size, sort=sort)

Assets Compliance For Policy Rules Under Policy Group

Retrieves asset resources with rule compliance status against all rules under the specified policy group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.
applicable_only = true # bool | An optional boolean parameter indicating the assets retrieved should only include those with rule results of either PASS or FAIL. Default value is `false`, which will also include assets with a compliance status of NOT_APPLICABLE. (optional)
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Assets Compliance For Policy Rules Under Policy Group
    api_response = api_instance.get_policy_group_asset_results(policy_id, group_id, applicable_only=applicable_only, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_group_asset_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 
 **applicable_only** | **bool**| An optional boolean parameter indicating the assets retrieved should only include those with rule results of either PASS or FAIL. Default value is &#x60;false&#x60;, which will also include assets with a compliance status of NOT_APPLICABLE. | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyAsset**](PageOfPolicyAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_group_children**
> PageOfPolicyItem get_policy_group_children(policy_id, group_id)

Policy Rules or Groups Directly Under Policy Group

Retrieves a paged resource of either policy rules, or groups, that are defined directly underneath the specified policy group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.

try:
    # Policy Rules or Groups Directly Under Policy Group
    api_response = api_instance.get_policy_group_children(policy_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_group_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 

### Return type

[**PageOfPolicyItem**](PageOfPolicyItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_group_rules_with_asset_assessment**
> PageOfPolicyRule get_policy_group_rules_with_asset_assessment(asset_id, policy_id, group_id, page=page, size=size, sort=sort)

Policy Rules Under Policy Group For Asset

Retrieves the list of policy rules defined directly, or indirectly, underneath the specified policy group and the compliance results for the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
asset_id = 789 # int | The identifier of the asset.
policy_id = 789 # int | The identifier of the policy
group_id = 789 # int | The identifier of the policy group.
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Rules Under Policy Group For Asset
    api_response = api_instance.get_policy_group_rules_with_asset_assessment(asset_id, policy_id, group_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_group_rules_with_asset_assessment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The identifier of the asset. | 
 **policy_id** | **int**| The identifier of the policy | 
 **group_id** | **int**| The identifier of the policy group. | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyRule**](PageOfPolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_groups**
> PageOfPolicyGroup get_policy_groups(policy_id, page=page, size=size, sort=sort)

Policy Groups

Retrieves a paged resource of policy groups for the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Groups
    api_response = api_instance.get_policy_groups(policy_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyGroup**](PageOfPolicyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule**
> PolicyRule get_policy_rule(policy_id, rule_id)

Policy Rule

Retrieves the specified policy rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.

try:
    # Policy Rule
    api_response = api_instance.get_policy_rule(policy_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 

### Return type

[**PolicyRule**](PolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule_asset_result**
> PolicyAsset get_policy_rule_asset_result(policy_id, rule_id, asset_id)

Asset Compliance For Policy Rule

Retrieves an asset resource with rule compliance results for the specified policy policy rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.
asset_id = 789 # int | The identifier of the asset.

try:
    # Asset Compliance For Policy Rule
    api_response = api_instance.get_policy_rule_asset_result(policy_id, rule_id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule_asset_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

[**PolicyAsset**](PolicyAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule_asset_result_proof**
> str get_policy_rule_asset_result_proof(policy_id, rule_id, asset_id)

Policy Rule Proof For Asset

Retrieves the policy rule proof captured during evaluation against the specified asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.
asset_id = 789 # int | The identifier of the asset.

try:
    # Policy Rule Proof For Asset
    api_response = api_instance.get_policy_rule_asset_result_proof(policy_id, rule_id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule_asset_result_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule_asset_results**
> PageOfPolicyAsset get_policy_rule_asset_results(policy_id, rule_id, applicable_only=applicable_only, page=page, size=size, sort=sort)

Assets Compliance For Policy Rule

Retrieves asset resources with rule compliance results for the specified policy policy rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.
applicable_only = true # bool | An optional boolean parameter indicating the assets retrieved should only include those with rule results of either PASS or FAIL. Default value is `false`, which will also include assets with a compliance status of NOT_APPLICABLE. (optional)
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Assets Compliance For Policy Rule
    api_response = api_instance.get_policy_rule_asset_results(policy_id, rule_id, applicable_only=applicable_only, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule_asset_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 
 **applicable_only** | **bool**| An optional boolean parameter indicating the assets retrieved should only include those with rule results of either PASS or FAIL. Default value is &#x60;false&#x60;, which will also include assets with a compliance status of NOT_APPLICABLE. | [optional] 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyAsset**](PageOfPolicyAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule_controls**
> PageOfPolicyControl get_policy_rule_controls(policy_id, rule_id, page=page, size=size, sort=sort)

Policy Rule Controls

Retrieves all NIST SP 800-53 controls mappings for each CCE within the specified policy rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Rule Controls
    api_response = api_instance.get_policy_rule_controls(policy_id, rule_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyControl**](PageOfPolicyControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule_rationale**
> str get_policy_rule_rationale(policy_id, rule_id)

Policy Rule Rationale

Retrieves the policy rule rationale for the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.

try:
    # Policy Rule Rationale
    api_response = api_instance.get_policy_rule_rationale(policy_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule_rationale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule_remediation**
> str get_policy_rule_remediation(policy_id, rule_id)

Policy Rule Remediation

Retrieves the policy rule remediation for the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
rule_id = 789 # int | The identifier of the policy rule.

try:
    # Policy Rule Remediation
    api_response = api_instance.get_policy_rule_remediation(policy_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule_remediation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **rule_id** | **int**| The identifier of the policy rule. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rules**
> PageOfPolicyRule get_policy_rules(policy_id, page=page, size=size, sort=sort)

Policy Rules

Retrieves a paged resource of policy rules for the specified policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_id = 789 # int | The identifier of the policy
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Policy Rules
    api_response = api_instance.get_policy_rules(policy_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The identifier of the policy | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfPolicyRule**](PageOfPolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_summary**
> PolicySummaryResource get_policy_summary()

Policy Compliance Summaries

Retrieves a compliance summary of all policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()

try:
    # Policy Compliance Summaries
    api_response = api_instance.get_policy_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PolicySummaryResource**](PolicySummaryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

