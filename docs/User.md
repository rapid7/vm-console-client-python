# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**AuthenticationSource**](AuthenticationSource.md) | The authentication source used to authenticate the user. | [optional] 
**email** | **str** | The email address of the user. | [optional] 
**enabled** | **bool** | Whether the user account is enabled. | [optional] 
**id** | **int** | The identifier of the user. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**locale** | [**LocalePreferences**](LocalePreferences.md) | The locale and language preferences for the user. | [optional] 
**locked** | **bool** | Whether the user account is locked (exceeded maximum password retry attempts). | [optional] 
**login** | **str** | The login name of the user. | 
**name** | **str** | The full name of the user. | 
**role** | [**UserRole**](UserRole.md) | The privileges and role the user is assigned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


