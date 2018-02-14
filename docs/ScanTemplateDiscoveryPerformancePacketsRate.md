# ScanTemplateDiscoveryPerformancePacketsRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defeat_rate_limit** | **bool** | Whether defeat rate limit (defeat-rst-ratelimit) is enforced on the minimum packet setting, which can improve scan speed. If it is disabled, the minimum packet rate setting may be ignored when a target limits its rate of RST (reset) responses to a port scan. This can increase scan accuracy by preventing the scan from missing ports. Defaults to &#x60;true&#x60;. | [optional] 
**maximum** | **int** | The minimum number of packets to send each second during discovery attempts. Defaults to &#x60;0&#x60;. | [optional] 
**minimum** | **int** | The minimum number of packets to send each second during discovery attempts. Defaults to &#x60;0&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


