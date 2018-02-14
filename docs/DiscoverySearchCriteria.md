# DiscoverySearchCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The type of discovery connection configured for the site. This property only applies to dynamic sites. | [optional] 
**filters** | [**list[SwaggerDiscoverySearchCriteriaFilter]**](SwaggerDiscoverySearchCriteriaFilter.md) | Filters used to match assets from a discovery connection. See &lt;a href&#x3D;\&quot;#section/Responses/DiscoverySearchCriteria\&quot;&gt;Discovery Connection Search Criteria&lt;/a&gt; for more information on the structure and format. | [optional] 
**match** | **str** | Operator to determine how to match filters. &#x60;all&#x60; requires that all filters match for an asset to be included. &#x60;any&#x60; requires only one filter to match for an asset to be included. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


