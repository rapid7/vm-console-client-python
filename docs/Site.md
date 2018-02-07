# Site

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | **int** | The number of assets that belong to the site. | [optional] 
**connection_type** | **str** | The type of discovery connection configured for the site. This property only applies to dynamic sites. | [optional] 
**description** | **str** | The site description. | [optional] 
**id** | **int** | The identifier of the site. | [optional] 
**importance** | **str** | The site importance. | [optional] 
**last_scan_time** | **str** | The date and time of the site&#39;s last scan. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**name** | **str** | The site name. | [optional] 
**risk_score** | **float** | The risk score (with criticality adjustments) of the site. | [optional] 
**scan_engine** | **int** | The identifier of the scan engine configured in the site. | [optional] 
**scan_template** | **str** | The identifier of the scan template configured in the site. | [optional] 
**type** | **str** | The type of the site. | [optional] 
**vulnerabilities** | [**Vulnerabilities**](Vulnerabilities.md) | Summary information for distinct vulnerabilities found on the assets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


