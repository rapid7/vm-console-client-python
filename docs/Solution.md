# Solution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_information** | [**AdditionalInformation**](AdditionalInformation.md) | Additional information or resources that can assist in applying the remediation. | [optional] 
**applies_to** | **str** | The systems or software the solution applies to. | [optional] 
**estimate** | **str** | The estimated duration to apply the solution, in ISO 8601 format. For example: &#x60;\&quot;PT5M\&quot;&#x60;. | [optional] 
**id** | **str** | The identifier of the solution. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**steps** | [**Steps**](Steps.md) | The steps required to remediate the vulnerability. | [optional] 
**summary** | [**Summary**](Summary.md) | The summary of the solution. | [optional] 
**type** | **str** | The type of the solution. One of: &#x60;\&quot;Configuration\&quot;&#x60;, &#x60;\&quot;Rollup patch\&quot;&#x60;, &#x60;\&quot;Patch\&quot;&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


