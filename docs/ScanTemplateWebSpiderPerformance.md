# ScanTemplateWebSpiderPerformance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_daemons_to_skip** | **list[str]** | The names of HTTP Daemons (HTTPd) to skip when spidering. For example, &#x60;\&quot;CUPS\&quot;&#x60;. | [optional] 
**maximum_directory_levels** | **int** | The directory depth limit for web spidering. Limiting directory depth can save significant time, especially with large sites. A value of &#x60;0&#x60; signifies unlimited directory traversal. Defaults to &#x60;6&#x60;. | [optional] 
**maximum_foreign_hosts** | **int** | The maximum number of unique host names that the spider may resolve. This function adds substantial time to the spidering process, especially with large Web sites, because of frequent cross-link checking involved. Defaults to &#x60;100&#x60;. | [optional] 
**maximum_link_depth** | **int** | The maximum depth of links to traverse when spidering. Defaults to &#x60;6&#x60;. | [optional] 
**maximum_pages** | **int** | The maximum the number of pages that are spidered. This is a time-saving measure for large sites. Defaults to &#x60;3000&#x60;. | [optional] 
**maximum_retries** | **int** | The maximum the number of times to retry a request after a failure. A value of &#x60;0&#x60; means no retry attempts are made. Defaults to &#x60;2&#x60;. | [optional] 
**maximum_time** | **str** | The maximum length of time to web spider. This limit prevents scans from taking longer than the allotted scan schedule. A value of &#x60;PT0S&#x60; means no limit is applied. The acceptable range is &#x60;PT1M&#x60; to &#x60;PT16666.6667H&#x60;. | [optional] 
**response_timeout** | **str** | The duration to wait for a response from a target web server. The value is specified as a ISO8601 duration and can range from &#x60;PT0S&#x60; (0ms) to &#x60;P1H&#x60; (1 hour). Defaults to &#x60;PT2M&#x60;. | [optional] 
**threads_per_server** | **int** | The number of threads to use per web server being spidered. Defaults to &#x60;3&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


