# AssetPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_name** | **str** | The name of the policy&#39;s benchmark. | [optional] 
**benchmark_version** | **str** | The version number of the benchmark that includes the policy. | [optional] 
**category** | **str** | A grouping of similar benchmarks based on their source, purpose, or other criteria. Examples include FDCC, USGCB, and CIS. | [optional] 
**description** | **str** | The description of the policy. | [optional] 
**failed_assets_count** | **int** | The number of assets that are not compliant with the policy. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 
**failed_rules_count** | **int** | The number of rules in the policy that are not compliant with any scanned assets. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 
**id** | **str** | The textual representation of the policy identifier. | [optional] 
**is_custom** | **bool** | A flag indicating whether the policy is custom. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**not_applicable_assets_count** | **int** | The number of assets that were attempted to be scanned, but are not applicable to the policy. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 
**not_applicable_rules_count** | **int** | The number of rules in the policy that are not applicable with any scanned assets. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 
**passed_assets_count** | **int** | The number of assets that are compliant with the policy. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 
**passed_rules_count** | **int** | The number of rules in the policy that are compliant with all scanned assets. The assets considered in the calculation are based on the user&#39;s list of accessible assets. | [optional] 
**policy_name** | **str** | The name of the policy. | [optional] 
**rule_compliance** | **float** | The ratio of PASS results for the rules to the total number of rules in each policy. | [optional] 
**rule_compliance_delta** | **float** | The change in rule compliance between the last two scans of all assets. The list of scanned policies is based on the user&#39;s list of accessible assets. | [optional] 
**scope** | **str** | The textual representation of the policy scope. Policies that are automatically available have &#x60;\&quot;Built-in\&quot;&#x60; scope, whereas policies created by users have scope as &#x60;\&quot;Custom\&quot;&#x60;. | [optional] 
**status** | **str** | The overall compliance status of the policy. | [optional] 
**surrogate_id** | **int** | The identifier of the policy | [optional] 
**title** | **str** | The title of the policy as visible to the user. | [optional] 
**unscored_rules** | **int** | The number of rules defined in the policy with a role of \&quot;unscored\&quot;. These rules will not affect rule compliance scoring for the policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


