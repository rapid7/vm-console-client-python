# AssetCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[Address]**](Address.md) | All addresses discovered on the asset. | [optional] 
**assessed_for_policies** | **bool** | Whether the asset has been assessed for policies at least once. | [optional] 
**assessed_for_vulnerabilities** | **bool** | Whether the asset has been assessed for vulnerabilities at least once. | [optional] 
**configurations** | [**list[Configuration]**](Configuration.md) | Configuration key-values pairs enumerated on the asset. | [optional] 
**cpe** | **str** | The Common Platform Enumeration (CPE) of the operating system. This is the tertiary means of specifying the operating system fingerprint. Use &#x60;\&quot;osFingerprint\&quot;&#x60; or &#x60;\&quot;os\&quot;&#x60; as a more accurate means of defining the operating system. | [optional] 
**databases** | [**list[Database]**](Database.md) | The databases enumerated on the asset. | [optional] 
**_date** | **str** | The date the data was collected on the asset. | 
**description** | **str** | The description of the source or collection of information on the asset. This description will appear in the history of the asset for future auditing purposes. | [optional] 
**files** | [**list[File]**](File.md) | The files discovered with searching on the asset. | [optional] 
**history** | [**list[AssetHistory]**](AssetHistory.md) | The history of changes to the asset over time. | [optional] 
**host_name** | [**HostName**](HostName.md) | The primary host name (local or FQDN) of the asset. | [optional] 
**host_names** | [**list[HostName]**](HostName.md) | Additional host names for the asset. | [optional] 
**id** | **int** | The identifier of the asset. | [optional] 
**ids** | [**list[UniqueId]**](UniqueId.md) | Unique identifiers found on the asset, such as hardware or operating system identifiers. | [optional] 
**ip** | **str** | The primary IPv4 or IPv6 address of the asset. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**mac** | **str** | The primary Media Access Control (MAC) address of the asset. The format is six groups of two hexadecimal digits separated by colons. | [optional] 
**os** | **str** | Free-form textual description of the operating system of the asset, typically from a fingerprinting source. This input will be parsed to produce a full fingerprint. This is the secondary means of specifying the operating system. Use &#x60;osFingerprint&#x60; for a more accurate definition. | [optional] 
**os_fingerprint** | [**OperatingSystem**](OperatingSystem.md) | The details of the operating system of the asset. At least one of &#x60;vendor&#x60;, &#x60;family&#x60;, or &#x60;product&#x60; must be supplied. This is the preferred means of defining the operating system. | [optional] 
**raw_risk_score** | **float** | The base risk score of the asset. | [optional] 
**risk_score** | **float** | The risk score (with criticality adjustments) of the asset. | [optional] 
**services** | [**list[Service]**](Service.md) | The services discovered on the asset. | [optional] 
**software** | [**list[Software]**](Software.md) | The software discovered on the asset. | [optional] 
**type** | **str** | The type of asset. | [optional] 
**user_groups** | [**list[GroupAccount]**](GroupAccount.md) | The group accounts enumerated on the asset. | [optional] 
**users** | [**list[UserAccount]**](UserAccount.md) | The user accounts enumerated on the asset. | [optional] 
**vulnerabilities** | [**AssetVulnerabilities**](AssetVulnerabilities.md) | Summary information for vulnerabilities on the asset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


