# WebHeaderAuthentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | The base URL is the main address from which all paths in the target Web site begin. Includes the protocol. Example: http://acme.com. | [optional] 
**enabled** | **bool** | Flag indicating whether the HTTP header web authentication is enabled for the site&#39;s scans. | [optional] 
**headers** | **dict(str, str)** | A map of HTTP headers the scan engine will use when negotiating with the Web server for an \&quot;authenticated\&quot; page. Make sure that the session ID is valid between the time you save this ID for the site and when you start the scan. Note: This property is not returned in responses for security. | [optional] 
**id** | **int** | The identifier of the HTTP header web authentication. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**login_regular_expression** | **str** | The regular expression matches the message that the Web server returns if the login attempt fails. | [optional] 
**name** | **str** | The HTTP header web authentication name. | [optional] 
**service** | **str** | Value indicating whether this web authentication  configuration is for HTML form authentication or HTTP header authentication. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


