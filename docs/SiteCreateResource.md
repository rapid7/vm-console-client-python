# SiteCreateResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The site&#39;s description. | [optional] 
**engine_id** | **int** | The identifier of a scan engine. Default scan engine is selected when not specified. | [optional] 
**importance** | **str** | The site importance. Defaults to &#x60;\&quot;normal\&quot;&#x60; if not specified. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**name** | **str** | The site name. Name must be unique. | 
**scan** | [**ScanScope**](ScanScope.md) | Defines the scope of scan targets for the site, which can be addresses, or asset groups, for static sites and a discovery configuration for dynamic sites. Only one property must be set by the user when saving a site. | [optional] 
**scan_template_id** | **str** | The identifier of a scan template. Default scan template is selected when not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


