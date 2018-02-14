# ScanTemplateServiceDiscoveryTcp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_ports** | **list[object]** | Additional TCP ports to scan. Individual ports can be specified as numbers or a string, but port ranges must be strings (e.g. &#x60;\&quot;7892-7898\&quot;&#x60;). Defaults to empty. | [optional] 
**excluded_ports** | **list[object]** | TCP ports to exclude from scanning. Individual ports can be specified as numbers or a string, but port ranges must be strings (e.g. &#x60;\&quot;7892-7898\&quot;&#x60;). Defaults to empty. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**method** | **str** | The method of TCP discovery. Defaults to &#x60;SYN&#x60;. | [optional] 
**ports** | **str** | The TCP ports to scan. Defaults to &#x60;well-known&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


