# AssetGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | **int** | The number of assets that belong to the asset group. | [optional] 
**description** | **str** | The description of the asset group. | [optional] 
**id** | **int** | The identifier of the asset group. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**name** | **str** | The name of the asset group. | 
**risk_score** | **float** | The total risk score of all assets that belong to the asset group. | [optional] 
**search_criteria** | [**SearchCriteria**](SearchCriteria.md) | Search criteria used to determine dynamic membership, if &#x60;type&#x60; is &#x60;\&quot;dynamic\&quot;&#x60;.  | [optional] 
**type** | **str** | The type of the asset group. | 
**vulnerabilities** | [**Vulnerabilities**](Vulnerabilities.md) | Summary information for distinct vulnerabilities found on the assets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


