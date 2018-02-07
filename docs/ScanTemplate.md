# ScanTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**ScanTemplateVulnerabilityChecks**](ScanTemplateVulnerabilityChecks.md) | Settings for which vulnerability checks to run during a scan. &lt;br/&gt;  The rules for inclusion of checks is as follows:  &lt;ul&gt;  &lt;li&gt;Enabled checks by category and by check type are included&lt;/li&gt;  &lt;li&gt;Disabled checks in by category and by check type are removed&lt;/li&gt;  &lt;li&gt;Enabled checks in by individual check are added (even if they are disabled in by category or check type)&lt;/li&gt;  &lt;li&gt;Disabled checks in by individual check are removed&lt;/li&gt;  &lt;li&gt;If unsafe is disabled, unsafe checks are removed&lt;/li&gt;  &lt;li&gt;If potential is disabled, potential checks are removed&lt;/li&gt;  &lt;ul&gt; | [optional] 
**database** | [**ScanTemplateDatabase**](ScanTemplateDatabase.md) | Settings for discovery databases. | [optional] 
**description** | **str** | A verbose description of the scan template.. | [optional] 
**discovery** | [**ScanTemplateDiscovery**](ScanTemplateDiscovery.md) | Discovery settings used during a scan. | [optional] 
**discovery_only** | **bool** | Whether only discovery is performed during a scan. | [optional] 
**enable_windows_services** | **bool** | Whether Windows services are enabled during a scan. Windows services will be temporarily reconfigured when this option is selected. Original settings will be restored after the scan completes, unless it is interrupted. | [optional] 
**enhanced_logging** | **bool** | Whether enhanced logging is gathered during scanning. Collection of enhanced logs may greatly increase the disk space used by a scan. | [optional] 
**id** | **str** | The identifier of the scan template | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**max_parallel_assets** | **int** | The maximum number of assets scanned simultaneously per scan engine during a scan. | [optional] 
**max_scan_processes** | **int** | The maximum number of scan processes simultaneously allowed against each asset during a scan. | [optional] 
**name** | **str** | A concise name for the scan template. | [optional] 
**policy** | [**Policy**](Policy.md) | Policy configuration settings used during a scan. | [optional] 
**policy_enabled** | **bool** | Whether policy assessment is performed during a scan. | [optional] 
**telnet** | [**Telnet**](Telnet.md) | Settings for interacting with the Telnet protocol. | [optional] 
**vulnerability_enabled** | **bool** | Whether vulnerability assessment is performed during a scan. | [optional] 
**web** | [**ScanTemplateWebSpider**](ScanTemplateWebSpider.md) | Web spider settings used during a scan. | [optional] 
**web_enabled** | **bool** | Whether web spidering and assessment are performed during a scan. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


