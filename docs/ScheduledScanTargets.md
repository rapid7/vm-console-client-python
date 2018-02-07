# ScheduledScanTargets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_asset_groups** | [**ExcludedAssetGroups**](ExcludedAssetGroups.md) | Assets associated with these asset groups will be excluded from the site&#39;s scan. | [optional] 
**excluded_targets** | [**ExcludedScanTargets**](ExcludedScanTargets.md) | Addresses to be excluded from the site&#39;s scan. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. | [optional] 
**included_asset_groups** | [**IncludedAssetGroups**](IncludedAssetGroups.md) | Allows users to specify a subset of the site&#39;s included asset groups to be included in the scan. If the property is defined, then at least one valid already defined as an included asset group must be specified. | [optional] 
**included_targets** | [**IncludedScanTargets**](IncludedScanTargets.md) | Allows users to specify a subset of the site&#39;s scan targets to be included in the scan. If the property is defined, then at least one address must be specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


