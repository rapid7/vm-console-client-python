# PolicySummaryResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decreased_compliance** | **int** | The total number of policies whose overall compliance has decreased between the last two scans of all assets. The list of scanned policies is based on the user&#39;s list of accessible assets. | [optional] 
**increased_compliance** | **int** | The total number of policies whose overall compliance has increased between the last two scans of all assets. The list of scanned policies is based on the user&#39;s list of accessible assets. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**number_of_policies** | **int** | The total number of policies available in the Security Console. | [optional] 
**overall_compliance** | **float** | The ratio of compliant rules to the total number of rules across all policies. | [optional] 
**scanned_policies** | **int** | The total number of policies that were evaluated against assets and have applicable results. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


