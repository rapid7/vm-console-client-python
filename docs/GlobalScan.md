# GlobalScan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | **int** | The number of assets found in the scan. | [optional] 
**duration** | **str** | The duration of the scan in ISO8601 format. | [optional] 
**end_time** | **str** | The end time of the scan in ISO8601 format. | [optional] 
**engine_id** | **int** | The identifier of the scan engine. | [optional] 
**engine_name** | **str** | The name of the scan engine. | [optional] 
**id** | **int** | The identifier of the scan. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**message** | **str** | The reason for the scan status. | [optional] 
**scan_name** | **str** | The user-driven scan name for the scan. | [optional] 
**scan_type** | **str** | The scan type (automated, manual, scheduled).  | [optional] 
**site_id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**start_time** | **str** | The start time of the scan in ISO8601 format. | [optional] 
**started_by** | **str** | The name of the user that started the scan. | [optional] 
**status** | **str** | The scan status. | [optional] 
**vulnerabilities** | [**Vulnerabilities**](Vulnerabilities.md) | The vulnerability synopsis of the scan. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


