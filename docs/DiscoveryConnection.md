# DiscoveryConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The AWS credential access key identifier (only used for the AWS connection). | [optional] 
**address** | **str** | The address used to connect to the discovery connection source. | [optional] 
**arn** | **str** | The AWS credential ARN (only used for the AWS connection). | [optional] 
**aws_session_name** | **str** | The AWS credential session name (only used for the AWS connection). | [optional] 
**connection_type** | **str** | The type of the discovery connection. | [optional] 
**event_source** | **str** | The event source type to use. | [optional] 
**exchange_server_hostname** | **str** | The hostname of the exchange server to connect to. | [optional] 
**exchange_user** | **str** | The username used to connect to the exchange server. | [optional] 
**folder_path** | **str** | The folder path to pull logs from. | [optional] 
**id** | **int** | The identifier of the discovery connection. | [optional] 
**ldap_server** | **str** | The LDAP server to connect to. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**name** | **str** | The discovery connection name. | [optional] 
**port** | **int** | The port used to connect to the discovery connection source. | [optional] 
**protocol** | **str** | The protocol used to connect to the discovery connection source. | [optional] 
**region** | **str** | The AWS region (only used for the AWS connection). | [optional] 
**scan_engine_is_inside_aws** | **bool** | Flag denoting whether the scan engine is in AWS, this is used for AWS discovery connections for scanning purposes (only used for the AWS connection). | [optional] 
**secret_access_key** | **str** | The AWS credential secret access key (only used for the AWS connection). | [optional] 
**status** | **str** | The status of the discovery connection. | [optional] 
**username** | **str** | The username used to authenticate to the discovery connection source. | [optional] 
**win_rm_server** | **str** | The WinRM server to connect to.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


