# MatchedSolution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_information** | [**AdditionalInformation**](AdditionalInformation.md) | Additional information or resources that can assist in applying the remediation. | [optional] 
**applies_to** | **str** | The systems or software the solution applies to. | [optional] 
**confidence** | **str** | The confidence of the matching process for the solution. | [optional] 
**estimate** | **str** | The estimated duration to apply the solution, in ISO 8601 format. For example: &#x60;\&quot;PT5M\&quot;&#x60;. | [optional] 
**id** | **str** | The identifier of the solution. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**matches** | [**list[SolutionMatch]**](SolutionMatch.md) | The raw matches that were performed in order to select the best solution(s). | [optional] 
**steps** | [**Steps**](Steps.md) | The steps required to remediate the vulnerability. | [optional] 
**summary** | [**Summary**](Summary.md) | The summary of the solution. | [optional] 
**type** | **str** | The type of the solution. One of: &#x60;\&quot;Configuration\&quot;&#x60;, &#x60;\&quot;Rollup patch\&quot;&#x60;, &#x60;\&quot;Patch\&quot;&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


