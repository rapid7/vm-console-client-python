# ScanSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_timeout** | **str** | The connection timeout when establishing connections to remote scan engines, in ISO 8601 format. For example: &#x60;\&quot;PT15S\&quot;&#x60;. | [optional] 
**incremental** | **bool** | Whether incremental scan results is enabled. | [optional] 
**maximum_threads** | **int** | The maximum number of scan threads to use in any scan. -1 means this is set by the scan template. | [optional] 
**read_timeout** | **str** | The read timeout when establishing connections to remote scan engines, in ISO 8601 format. For example: &#x60;\&quot;PT15M\&quot;&#x60;. | [optional] 
**status_idle_timeout** | **str** | The idle timeout when checking the status of running scans, in ISO 8601 format. For example: &#x60;\&quot;PT3M\&quot;&#x60;. | [optional] 
**status_threads** | **int** | The number of threads to use when checking the status of running scans. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


