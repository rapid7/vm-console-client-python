# WebFormAuthentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | The base URL is the main address from which all paths in the target Web site begin. Includes the protocol. Example: http://acme.com. | [optional] 
**enabled** | **bool** | Flag indicating whether the HTML form web authentication is enabled for the site&#39;s scans. | [optional] 
**id** | **int** | The identifier of the HTML form web authentication. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**login_regular_expression** | **str** | The regular expression matches the message that the Web server returns if the login attempt fails. | [optional] 
**login_url** | **str** | The login page URL contains form for logging on. Include the base URL. Example: http://acme.com/login. | [optional] 
**name** | **str** | The HTML form web authentication name. | [optional] 
**service** | **str** | Value indicating whether this web authentication  configuration is for HTML form authentication or HTTP header authentication. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


