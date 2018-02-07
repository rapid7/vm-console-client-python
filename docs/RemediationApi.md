# swagger_client.RemediationApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_vulnerability_solutions**](RemediationApi.md#get_asset_vulnerability_solutions) | **GET** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/solution | Asset Vulnerability Solution


# **get_asset_vulnerability_solutions**
> ResourcesMatchedSolution get_asset_vulnerability_solutions(id, vulnerability_id)

Asset Vulnerability Solution

Returns the highest-superceding rollup solutions for a vulnerability on an asset. The solution(s) selected will be the most recent and cost-effective means by which the vulnerability can be remediated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemediationApi()
id = 789 # int | The identifier of the asset.
vulnerability_id = 'vulnerability_id_example' # str | The identifier of the vulnerability.

try:
    # Asset Vulnerability Solution
    api_response = api_instance.get_asset_vulnerability_solutions(id, vulnerability_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemediationApi->get_asset_vulnerability_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the asset. | 
 **vulnerability_id** | **str**| The identifier of the vulnerability. | 

### Return type

[**ResourcesMatchedSolution**](ResourcesMatchedSolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

