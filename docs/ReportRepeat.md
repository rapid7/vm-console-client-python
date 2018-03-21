# ReportRepeat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **str** | The day of the week the scheduled task should repeat. This property only applies to schedules with a &#x60;every&#x60; value of &#x60;\&quot;day-of-month\&quot;&#x60;. | [optional] 
**every** | **str** | The frequency schedule repeats. Each value represents a different unit of time and is used in conjunction with the property &#x60;interval&#x60;. For example, a schedule can repeat hourly, daily, monthly, etc. The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | hour | Specifies the schedule repeats in hourly increments. |  | day | Specifies the schedule repeats in daily increments. |  | week | Specifies the schedule repeats in weekly increments. |  | date-of-month | Specifies the schedule repeats nth day of the &#x60;interval&#x60; month. Requires the property &#x60;dateOfMonth&#x60; to be specified. For example, if &#x60;dateOfMonth&#x60; is &#x60;17&#x60; and the &#x60;interval&#x60; is &#x60;2&#x60;, then the schedule will repeat every 2 months on the 17th day of the month. |  | day-of-month | Specifies the schedule repeats on a monthly interval but instead of a specific date being specified, the day of the week and week of the month are specified. Requires the properties &#x60;dayOfWeek&#x60; and &#x60;weekOfMonth&#x60; to be specified. For example, if &#x60;dayOfWeek&#x60; is &#x60;\&quot;friday\&quot;&#x60;, &#x60;weekOfMonth&#x60; is &#x60;3&#x60;, and the &#x60;interval&#x60; is &#x60;4&#x60;, then the schedule will repeat every 4 months on the 3rd Friday of the month. |   | 
**interval** | **int** | The interval time the schedule should repeat. The is depends on the value set in &#x60;every&#x60;. For example, if the value in property &#x60;every&#x60; is set to &#x60;\&quot;day\&quot;&#x60; and &#x60;interval&#x60; is set to &#x60;2&#x60;, then the schedule will repeat every 2 days. | 
**week_of_month** | **int** | The week of the month the scheduled task should repeat. For This property only applies to schedules with a &#x60;every&#x60; value of &#x60;\&quot;day-of-month\&quot;&#x60;. Each week of the month is counted in 7-day increments. For example, week 1 consists of days 1-7 of the month while week 2 consists of days 8-14 of the month and so forth. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


