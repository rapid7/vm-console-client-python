# ReportConfigFiltersResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**ReportConfigCategoryFilters**](ReportConfigCategoryFilters.md) | Vulnerability categories to include or exclude. Only &#x60;included&#x60; or &#x60;excluded&#x60; may be specified, but not both. | [optional] 
**severity** | **str** | The vulnerability severities to include. Defaults to &#x60;all&#x60;. | [optional] 
**statuses** | **list[str]** | The vulnerability statuses to include. Defaults to [ &#x60;vulnerable&#x60;, &#x60;vulnerable-version&#x60;, &#x60;potentially-vulnerable&#x60; ]. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


