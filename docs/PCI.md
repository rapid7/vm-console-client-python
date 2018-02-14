# PCI

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_cvss_score** | **int** | The CVSS score of the vulnerability, adjusted for PCI rules and exceptions, on a scale of 0-10. | [optional] 
**adjusted_severity_score** | **int** | The severity score of the vulnerability, adjusted for PCI rules and exceptions, on a scale of 0-10. | [optional] 
**fail** | **bool** | Whether if present on a host this vulnerability would cause a PCI failure. &#x60;true&#x60; if \&quot;status\&quot; is &#x60;\&quot;Fail\&quot;&#x60;, &#x60;false&#x60; otherwise. | [optional] 
**special_notes** | **str** | Any special notes or remarks about the vulnerability that pertain to PCI compliance. | [optional] 
**status** | **str** | The PCI compliance status of the vulnerability. One of: &#x60;\&quot;Pass\&quot;&#x60;, &#x60;\&quot;Fail\&quot;&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


