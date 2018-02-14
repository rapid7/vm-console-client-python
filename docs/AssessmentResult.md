# AssessmentResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | The identifier of the vulnerability check. | [optional] 
**exceptions** | **list[int]** | If the result is vulnerable with exceptions applied, the identifier(s) of the exceptions actively applied to the result. | [optional] 
**key** | **str** | An additional discriminating key used to uniquely identify between multiple instances of results on the same finding. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**port** | **int** | The port of the service the result was discovered on. | [optional] 
**proof** | **str** | The proof explaining why the result was found vulnerable. The proof may container embedded HTML formatting markup. | [optional] 
**protocol** | **str** | The protocol of the service the result was discovered on. | [optional] 
**since** | **str** | The date and time the result was first recorded, in the ISO8601 format. If the result changes status this value is the date and time of the status change. | [optional] 
**status** | **str** | The status of the vulnerability check result. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


