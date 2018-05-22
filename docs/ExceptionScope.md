# ExceptionScope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the scope type to which the exception applies. For example in a site scoped vulnerability exception this is the site id, in an asset group vulnerability exception this is the asset group id. | [optional] 
**key** | **str** | If the scope type is &#x60;\&quot;Instance\&quot;&#x60;, an optional key to discriminate the instance the exception applies to. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**port** | **int** | If the scope type is &#x60;\&quot;Instance\&quot;&#x60; and the vulnerability is detected on a service, the port on which the exception applies. | [optional] 
**type** | **str** | The type of the exception scope. One of: &#x60;\&quot;Global\&quot;&#x60;, &#x60;\&quot;Site\&quot;&#x60;, &#x60;\&quot;Asset\&quot;&#x60;, &#x60;\&quot;Asset Group\&quot;&#x60;, &#x60;\&quot;Instance\&quot;&#x60; | [optional] 
**vulnerability** | **str** | The identifier of the vulnerability to which the exception applies. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


