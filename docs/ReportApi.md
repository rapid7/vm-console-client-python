# swagger_client.ReportApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportApi.md#create_report) | **POST** /api/3/reports | Reports
[**delete_report**](ReportApi.md#delete_report) | **DELETE** /api/3/reports/{id} | Report
[**delete_report_instance**](ReportApi.md#delete_report_instance) | **DELETE** /api/3/reports/{id}/history/{instance} | Report History
[**download_report**](ReportApi.md#download_report) | **GET** /api/3/reports/{id}/history/{instance}/output | Report Download
[**generate_report**](ReportApi.md#generate_report) | **POST** /api/3/reports/{id}/generate | Report Generation
[**get_report**](ReportApi.md#get_report) | **GET** /api/3/reports/{id} | Report
[**get_report_formats**](ReportApi.md#get_report_formats) | **GET** /api/3/report_formats | Report Formats
[**get_report_instance**](ReportApi.md#get_report_instance) | **GET** /api/3/reports/{id}/history/{instance} | Report History
[**get_report_instances**](ReportApi.md#get_report_instances) | **GET** /api/3/reports/{id}/history | Report Histories
[**get_report_template**](ReportApi.md#get_report_template) | **GET** /api/3/report_templates/{id} | Report Template
[**get_report_templates**](ReportApi.md#get_report_templates) | **GET** /api/3/report_templates | Report Templates
[**get_reports**](ReportApi.md#get_reports) | **GET** /api/3/reports | Reports
[**update_report**](ReportApi.md#update_report) | **PUT** /api/3/reports/{id} | Report


# **create_report**
> CreatedReferenceintLink create_report(param0=param0)

Reports

Configures a new report for generation. Report types are controlled through either or both a format and template. Non-templatized (`export`) report formats do not require a template and have their output format preset. Templatized (`document` and `file`) report formats support a report template that governs the content of the output and the output format can be chosen from a list of supported formats.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
param0 = swagger_client.Report() # Report | The specification of a report configuration. (optional)

try:
    # Reports
    api_response = api_instance.create_report(param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param0** | [**Report**](Report.md)| The specification of a report configuration. | [optional] 

### Return type

[**CreatedReferenceintLink**](CreatedReferenceintLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report**
> Links delete_report(id)

Report

Deletes the configuration of a report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.

try:
    # Report
    api_response = api_instance.delete_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->delete_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_instance**
> Links delete_report_instance(id, instance)

Report History

Returns the details for a generation of the report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.
instance = 'instance_example' # str | The identifier of the report instance.

try:
    # Report History
    api_response = api_instance.delete_report_instance(id, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->delete_report_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 
 **instance** | **str**| The identifier of the report instance. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_report**
> str download_report(id, instance)

Report Download

Returns the contents of a generated report. The report content is usually returned in a GZip compressed format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.
instance = 'instance_example' # str | The identifier of the report instance.

try:
    # Report Download
    api_response = api_instance.download_report(id, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->download_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 
 **instance** | **str**| The identifier of the report instance. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_report**
> ReferenceWithReportIDLink generate_report(id)

Report Generation

Generates a configured report and returns the instance identifier of the report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.

try:
    # Report Generation
    api_response = api_instance.generate_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 

### Return type

[**ReferenceWithReportIDLink**](ReferenceWithReportIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> Report get_report(id)

Report

Returns the configuration details of a report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.

try:
    # Report
    api_response = api_instance.get_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_formats**
> ResourcesAvailableReportFormat get_report_formats()

Report Formats

Returns all available report formats. A report format indicates an output file format specification (e.g. PDF, XML, etc). Some printable formats may be templated, and others may not. The supported templates for each formated are provided.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()

try:
    # Report Formats
    api_response = api_instance.get_report_formats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_formats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourcesAvailableReportFormat**](ResourcesAvailableReportFormat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_instance**
> ReportInstance get_report_instance(id, instance)

Report History

Returns the details for a generation of the report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.
instance = 'instance_example' # str | The identifier of the report instance.

try:
    # Report History
    api_response = api_instance.get_report_instance(id, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 
 **instance** | **str**| The identifier of the report instance. | 

### Return type

[**ReportInstance**](ReportInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_instances**
> ResourcesReportInstance get_report_instances(id)

Report Histories

Returns all historical details for generation of the report over time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.

try:
    # Report Histories
    api_response = api_instance.get_report_instances(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 

### Return type

[**ResourcesReportInstance**](ResourcesReportInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_template**
> ReportTemplate get_report_template(id)

Report Template

Returns the details of a report template. Report templates govern the contents generated within a report. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 'id_example' # str | The identifier of the report template;

try:
    # Report Template
    api_response = api_instance.get_report_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the report template; | 

### Return type

[**ReportTemplate**](ReportTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_templates**
> ResourcesReportTemplate get_report_templates()

Report Templates

Returns all available report templates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()

try:
    # Report Templates
    api_response = api_instance.get_report_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourcesReportTemplate**](ResourcesReportTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> PageOfReport get_reports(page=page, size=size, sort=sort)

Reports

Returns all defined report configurations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Reports
    api_response = api_instance.get_reports(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfReport**](PageOfReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> Links update_report(id, param1=param1)

Report

Updates the configuration details of a report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
id = 56 # int | The identifier of the report.
param1 = swagger_client.Report() # Report | The specification of a report configuration. (optional)

try:
    # Report
    api_response = api_instance.update_report(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->update_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the report. | 
 **param1** | [**Report**](Report.md)| The specification of a report configuration. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

