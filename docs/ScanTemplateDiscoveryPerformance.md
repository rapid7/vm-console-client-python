# ScanTemplateDiscoveryPerformance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_rate** | [**ScanTemplateDiscoveryPerformancePacketsRate**](ScanTemplateDiscoveryPerformancePacketsRate.md) | The number of packets to send per second during scanning. | [optional] 
**parallelism** | [**ScanTemplateDiscoveryPerformanceParallelism**](ScanTemplateDiscoveryPerformanceParallelism.md) | The number of discovery connection requests to be sent to target host simultaneously. These settings has no effect if values have been set for &#x60;scanDelay&#x60;. | [optional] 
**retry_limit** | **int** | The maximum number of attempts to contact target assets. If the limit is exceeded with no response, the given asset is not scanned. Defaults to &#x60;3&#x60;. | [optional] 
**scan_delay** | [**ScanTemplateDiscoveryPerformanceScanDelay**](ScanTemplateDiscoveryPerformanceScanDelay.md) | The duration to wait between sending packets to each target host during a scan. | [optional] 
**timeout** | [**ScanTemplateDiscoveryPerformanceTimeout**](ScanTemplateDiscoveryPerformanceTimeout.md) | The duration to wait between retry attempts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


