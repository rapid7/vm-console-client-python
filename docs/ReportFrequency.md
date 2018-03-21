# ReportFrequency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_runtimes** | **list[str]** | The next scheduled run-times for generation of the report when type is &#x60;schedule&#x60;. | [optional] 
**repeat** | [**ReportRepeat**](ReportRepeat.md) | How often the report generates when type is &#x60;schedule&#x60;. | [optional] 
**start** | **str** | When the report starts generating when type is &#x60;schedule&#x60;. | [optional] 
**type** | **str** | The frequency to generate the report. &#x60;schedule&#x60; generates the report every scheduled time interval, and requires the &#x60;repeat&#x60; and &#x60;start&#x60; properties to be specified. &#x60;scan&#x60; generates the report after any scan of any element in the scope of the report. &#x60;none&#x60; does not generate the report automatically. Defaults to &#x60;none&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


