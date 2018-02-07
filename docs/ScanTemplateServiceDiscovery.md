# ScanTemplateServiceDiscovery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name_file** | **str** | An optional file that lists each port and the service that commonly resides on it. If scans cannot identify actual services on ports, service names will be derived from this file in scan results. Defaults to empty. | [optional] 
**tcp** | [**ScanTemplateServiceDiscoveryTcp**](ScanTemplateServiceDiscoveryTcp.md) | TCP service discovery settings. | [optional] 
**udp** | [**ScanTemplateServiceDiscoveryUdp**](ScanTemplateServiceDiscoveryUdp.md) | UDP service discovery settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


