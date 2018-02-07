# SmtpAlert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating the alert is enabled. | 
**enabled_scan_events** | [**ScanEvents**](ScanEvents.md) | Allows the user to specify which scan events generate an alert. Default values will be chosen if property is not specified as apart of the request. The default values are documented in the properties of &#x60;enabledScanEvents&#x60;. | [optional] 
**enabled_vulnerability_events** | [**VulnerabilityEvents**](VulnerabilityEvents.md) | Allows the user to specify which vulnerability result events generate an alert. Default values will be chosen if property is not specified as apart of the request. The default values are documented in the properties of &#x60;enabledVulnerabilityEvents&#x60;. | [optional] 
**id** | **int** | The identifier of the alert. | [optional] 
**limit_alert_text** | **bool** | Reports basic information in the alert, if enabled. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**maximum_alerts** | **int** | The maximum number of alerts that will be issued. To disable maximum alerts, omit the property in the request or specify the property with a value of &#x60;null&#x60;. | [optional] 
**name** | **str** | The name of the alert. | 
**notification** | **str** | The type of alert. | 
**recipients** | **list[str]** | The recipient list. At least one recipient must be specified. Each recipient must be a valid e-mail address. | 
**relay_server** | **str** | The SMTP server/relay to send messages through. | 
**sender_email_address** | **str** | The sender e-mail address that will appear in the from field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


