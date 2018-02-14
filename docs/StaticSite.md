# StaticSite

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_asset_groups** | [**ExcludedAssetGroups**](ExcludedAssetGroups.md) | Assets associated with these asset groups will be excluded from the site&#39;s scan. | [optional] 
**excluded_targets** | [**ExcludedScanTargets**](ExcludedScanTargets.md) | Addresses to be excluded from the site&#39;s scan. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. | [optional] 
**included_asset_groups** | [**IncludedAssetGroups**](IncludedAssetGroups.md) | Assets associated with these asset groups will be included in the site&#39;s scan. | [optional] 
**included_targets** | [**IncludedScanTargets**](IncludedScanTargets.md) | Addresses to be included in the site&#39;s scan. At least one address must be specified in a static site. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


