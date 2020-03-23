# Agent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[Address]**](Address.md) | All addresses discovered on the asset. | [optional] 
**agent_id** | **str** | The identifier of the agent. | [optional] 
**assessed_for_policies** | **bool** | Whether the asset has been assessed for policies at least once. | [optional] 
**assessed_for_vulnerabilities** | **bool** | Whether the asset has been assessed for vulnerabilities at least once. | [optional] 
**configurations** | [**list[Configuration]**](Configuration.md) | Configuration key-values pairs enumerated on the asset. | [optional] 
**databases** | [**list[Database]**](Database.md) | The databases enumerated on the asset. | [optional] 
**files** | [**list[File]**](File.md) | The files discovered with searching on the asset. | [optional] 
**history** | [**list[AssetHistory]**](AssetHistory.md) | The history of changes to the asset over time. | [optional] 
**host_name** | **str** | The primary host name (local or FQDN) of the asset. | [optional] 
**host_names** | [**list[HostName]**](HostName.md) | All host names or aliases discovered on the asset. | [optional] 
**id** | **int** | The identifier of the asset. | [optional] 
**ids** | [**list[UniqueId]**](UniqueId.md) | Unique identifiers found on the asset, such as hardware or operating system identifiers. | [optional] 
**ip** | **str** | The primary IPv4 or IPv6 address of the asset. | [optional] 
**last_assessed_for_vulnerabilities** | **str** | The time the last vulnerability assessment occured. | 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**mac** | **str** | The primary Media Access Control (MAC) address of the asset. The format is six groups of two hexadecimal digits separated by colons. | [optional] 
**os** | **str** | The full description of the operating system of the asset. | [optional] 
**os_fingerprint** | [**OperatingSystem**](OperatingSystem.md) | The details of the operating system of the asset. | [optional] 
**raw_risk_score** | **float** | The base risk score of the asset. | [optional] 
**risk_score** | **float** | The risk score (with criticality adjustments) of the asset. | [optional] 
**services** | [**list[Service]**](Service.md) | The services discovered on the asset. | [optional] 
**software** | [**list[Software]**](Software.md) | The software discovered on the asset. | [optional] 
**type** | **str** | The type of asset. | [optional] 
**user_groups** | [**list[GroupAccount]**](GroupAccount.md) | The group accounts enumerated on the asset. | [optional] 
**users** | [**list[UserAccount]**](UserAccount.md) | The user accounts enumerated on the asset. | [optional] 
**vulnerabilities** | [**AssetVulnerabilities**](AssetVulnerabilities.md) | Summary information for vulnerabilities on the asset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


