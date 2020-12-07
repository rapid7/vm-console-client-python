# ScanEngine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address the scan engine is hosted. | 
**content_version** | **str** | The content version of the scan engine. | [optional] 
**engine_pools** | **list[int]** | A list of identifiers of engine pools this engine is included in. | [optional] 
**id** | **int** | The identifier of the scan engine. | 
**last_refreshed_date** | **str** | The date the engine was last refreshed. Date format is in ISO 8601. | [optional] 
**last_updated_date** | **str** | The date the engine was last updated. Date format is in ISO 8601. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**name** | **str** | The name of the scan engine. | 
**port** | **int** | The port used by the scan engine to communicate with the Security Console. | 
**product_version** | **str** | The product version of the scan engine. | [optional] 
**sites** | **list[int]** | A list of identifiers of each site the scan engine is assigned to. | [optional] 
**status** | **str** | The scan engine status. Can be one of the following values:  | Value                     | Description                                                                                |  | ------------------------- | ------------------------------------------------------------------------------------------ |  | &#x60;\&quot;active\&quot;&#x60;                | The scan engine is active.                                                                 |  | &#x60;\&quot;incompatible-version\&quot;&#x60;  | The product version of the remote scan engine is not compatible with the Security Console. |  | &#x60;\&quot;not-responding\&quot;&#x60;        | The scan engine is not responding to the Security Console.                                 |  | &#x60;\&quot;pending-authorization\&quot;&#x60; | The Security Console is not yet authorized to connect to the scan engine.                  |  | &#x60;\&quot;unknown\&quot;&#x60;               | The status of the scan engine is unknown.                                                  |   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


