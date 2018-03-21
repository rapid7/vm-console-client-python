# RiskTrendResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_assets** | [**RiskTrendAllAssetsResource**](RiskTrendAllAssetsResource.md) | Trend settings for a trend across all assets in the scope of the report. | [optional] 
**asset_group_membership** | **str** | Whether all asset groups in the history of deployment or those as of the report generation time are to be included. | [optional] 
**asset_groups** | **str** | Whether to include a trend for the 5 highest-risk asset groups in the scope of the report (either the average or total risk). Only allowed if asset groups are specified in the report scope. | [optional] 
**assets** | **bool** | Whether to include a trend for the 5 highest-risk assets in the scope of the report. | [optional] 
**_from** | **str** | The start date of the risk trend, which can either be a duration or a specific date and time. | [optional] 
**sites** | **str** | Whether to include a trend for the 5 highest-risk sites in the scope of the report (either the average or total risk). Only allowed if sites are specified in the report scope. | [optional] 
**tag_membership** | **str** | Whether all assets tagged in the history of deployment or those tagged as of the report generation time are to be included. | [optional] 
**tags** | **str** | Whether to include a trend for the 5 highest-risk tags for assets in the scope of the report (either the average or total risk). Only allowed if tags are specified in the report scope. | [optional] 
**to** | **str** | The end date of the risk trend (empty if &#x60;from&#x60; is a duration). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


