# rapid7vmconsole.SiteApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_site_tag**](SiteApi.md#add_site_tag) | **PUT** /api/3/sites/{id}/tags/{tagId} | Site Tag
[**add_site_user**](SiteApi.md#add_site_user) | **POST** /api/3/sites/{id}/users | Site Users Access
[**create_site**](SiteApi.md#create_site) | **POST** /api/3/sites | Sites
[**create_site_credential**](SiteApi.md#create_site_credential) | **POST** /api/3/sites/{id}/site_credentials | Site Scan Credentials
[**create_site_scan_schedule**](SiteApi.md#create_site_scan_schedule) | **POST** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
[**create_site_smtp_alert**](SiteApi.md#create_site_smtp_alert) | **POST** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
[**create_site_snmp_alert**](SiteApi.md#create_site_snmp_alert) | **POST** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
[**create_site_syslog_alert**](SiteApi.md#create_site_syslog_alert) | **POST** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
[**delete_all_site_alerts**](SiteApi.md#delete_all_site_alerts) | **DELETE** /api/3/sites/{id}/alerts | Site Alerts
[**delete_all_site_credentials**](SiteApi.md#delete_all_site_credentials) | **DELETE** /api/3/sites/{id}/site_credentials | Site Scan Credentials
[**delete_all_site_scan_schedules**](SiteApi.md#delete_all_site_scan_schedules) | **DELETE** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
[**delete_all_site_smtp_alerts**](SiteApi.md#delete_all_site_smtp_alerts) | **DELETE** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
[**delete_all_site_snmp_alerts**](SiteApi.md#delete_all_site_snmp_alerts) | **DELETE** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
[**delete_all_site_syslog_alerts**](SiteApi.md#delete_all_site_syslog_alerts) | **DELETE** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
[**delete_site**](SiteApi.md#delete_site) | **DELETE** /api/3/sites/{id} | Site
[**delete_site_credential**](SiteApi.md#delete_site_credential) | **DELETE** /api/3/sites/{id}/site_credentials/{credentialId} | Site Scan Credential
[**delete_site_scan_schedule**](SiteApi.md#delete_site_scan_schedule) | **DELETE** /api/3/sites/{id}/scan_schedules/{scheduleId} | Site Scan Schedule
[**delete_site_smtp_alert**](SiteApi.md#delete_site_smtp_alert) | **DELETE** /api/3/sites/{id}/alerts/smtp/{alertId} | Site SMTP Alert
[**delete_site_snmp_alert**](SiteApi.md#delete_site_snmp_alert) | **DELETE** /api/3/sites/{id}/alerts/snmp/{alertId} | Site SNMP Alert
[**delete_site_syslog_alert**](SiteApi.md#delete_site_syslog_alert) | **DELETE** /api/3/sites/{id}/alerts/syslog/{alertId} | Site Syslog Alert
[**enable_shared_credential_on_site**](SiteApi.md#enable_shared_credential_on_site) | **PUT** /api/3/sites/{id}/shared_credentials/{credentialId}/enabled | Assigned Shared Credential Enablement
[**enable_site_credential**](SiteApi.md#enable_site_credential) | **PUT** /api/3/sites/{id}/site_credentials/{credentialId}/enabled | Site Credential Enablement
[**get_excluded_asset_groups**](SiteApi.md#get_excluded_asset_groups) | **GET** /api/3/sites/{id}/excluded_asset_groups | Site Excluded Asset Groups
[**get_excluded_targets**](SiteApi.md#get_excluded_targets) | **GET** /api/3/sites/{id}/excluded_targets | Site Excluded Targets
[**get_included_asset_groups**](SiteApi.md#get_included_asset_groups) | **GET** /api/3/sites/{id}/included_asset_groups | Site Included Asset Groups
[**get_included_targets**](SiteApi.md#get_included_targets) | **GET** /api/3/sites/{id}/included_targets | Site Included Targets
[**get_site**](SiteApi.md#get_site) | **GET** /api/3/sites/{id} | Site
[**get_site_alerts**](SiteApi.md#get_site_alerts) | **GET** /api/3/sites/{id}/alerts | Site Alerts
[**get_site_assets**](SiteApi.md#get_site_assets) | **GET** /api/3/sites/{id}/assets | Site Assets
[**get_site_credential**](SiteApi.md#get_site_credential) | **GET** /api/3/sites/{id}/site_credentials/{credentialId} | Site Scan Credential
[**get_site_credentials**](SiteApi.md#get_site_credentials) | **GET** /api/3/sites/{id}/site_credentials | Site Scan Credentials
[**get_site_discovery_connection**](SiteApi.md#get_site_discovery_connection) | **GET** /api/3/sites/{id}/discovery_connection | Site Discovery Connection
[**get_site_discovery_search_criteria**](SiteApi.md#get_site_discovery_search_criteria) | **GET** /api/3/sites/{id}/discovery_search_criteria | Site Discovery Search Criteria
[**get_site_organization**](SiteApi.md#get_site_organization) | **GET** /api/3/sites/{id}/organization | Site Organization Information
[**get_site_scan_engine**](SiteApi.md#get_site_scan_engine) | **GET** /api/3/sites/{id}/scan_engine | Site Scan Engine
[**get_site_scan_schedule**](SiteApi.md#get_site_scan_schedule) | **GET** /api/3/sites/{id}/scan_schedules/{scheduleId} | Site Scan Schedule
[**get_site_scan_schedules**](SiteApi.md#get_site_scan_schedules) | **GET** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
[**get_site_scan_template**](SiteApi.md#get_site_scan_template) | **GET** /api/3/sites/{id}/scan_template | Site Scan Template
[**get_site_shared_credentials**](SiteApi.md#get_site_shared_credentials) | **GET** /api/3/sites/{id}/shared_credentials | Assigned Shared Credentials
[**get_site_smtp_alert**](SiteApi.md#get_site_smtp_alert) | **GET** /api/3/sites/{id}/alerts/smtp/{alertId} | Site SMTP Alert
[**get_site_smtp_alerts**](SiteApi.md#get_site_smtp_alerts) | **GET** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
[**get_site_snmp_alert**](SiteApi.md#get_site_snmp_alert) | **GET** /api/3/sites/{id}/alerts/snmp/{alertId} | Site SNMP Alert
[**get_site_snmp_alerts**](SiteApi.md#get_site_snmp_alerts) | **GET** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
[**get_site_syslog_alert**](SiteApi.md#get_site_syslog_alert) | **GET** /api/3/sites/{id}/alerts/syslog/{alertId} | Site Syslog Alert
[**get_site_syslog_alerts**](SiteApi.md#get_site_syslog_alerts) | **GET** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
[**get_site_tags**](SiteApi.md#get_site_tags) | **GET** /api/3/sites/{id}/tags | Site Tags
[**get_site_users**](SiteApi.md#get_site_users) | **GET** /api/3/sites/{id}/users | Site Users Access
[**get_sites**](SiteApi.md#get_sites) | **GET** /api/3/sites | Sites
[**get_web_auth_html_forms**](SiteApi.md#get_web_auth_html_forms) | **GET** /api/3/sites/{id}/web_authentication/html_forms | Web Authentication HTML Forms
[**get_web_auth_http_headers**](SiteApi.md#get_web_auth_http_headers) | **GET** /api/3/sites/{id}/web_authentication/http_headers | Web Authentication HTTP Headers
[**remove_all_excluded_asset_groups**](SiteApi.md#remove_all_excluded_asset_groups) | **DELETE** /api/3/sites/{id}/excluded_asset_groups | Site Excluded Asset Groups
[**remove_all_included_asset_groups**](SiteApi.md#remove_all_included_asset_groups) | **DELETE** /api/3/sites/{id}/included_asset_groups | Site Included Asset Groups
[**remove_asset_from_site**](SiteApi.md#remove_asset_from_site) | **DELETE** /api/3/sites/{id}/assets/{assetId} | Site Asset
[**remove_excluded_asset_group**](SiteApi.md#remove_excluded_asset_group) | **DELETE** /api/3/sites/{id}/excluded_asset_groups/{assetGroupId} | Site Excluded Asset Group
[**remove_included_asset_group**](SiteApi.md#remove_included_asset_group) | **DELETE** /api/3/sites/{id}/included_asset_groups/{assetGroupId} | Site Included Asset Group
[**remove_site_assets**](SiteApi.md#remove_site_assets) | **DELETE** /api/3/sites/{id}/assets | Site Assets
[**remove_site_tag**](SiteApi.md#remove_site_tag) | **DELETE** /api/3/sites/{id}/tags/{tagId} | Site Tag
[**remove_site_user**](SiteApi.md#remove_site_user) | **DELETE** /api/3/sites/{id}/users/{userId} | Site User Access
[**set_site_credentials**](SiteApi.md#set_site_credentials) | **PUT** /api/3/sites/{id}/site_credentials | Site Scan Credentials
[**set_site_discovery_connection**](SiteApi.md#set_site_discovery_connection) | **PUT** /api/3/sites/{id}/discovery_connection | Site Discovery Connection
[**set_site_discovery_search_criteria**](SiteApi.md#set_site_discovery_search_criteria) | **PUT** /api/3/sites/{id}/discovery_search_criteria | Site Discovery Search Criteria
[**set_site_scan_engine**](SiteApi.md#set_site_scan_engine) | **PUT** /api/3/sites/{id}/scan_engine | Site Scan Engine
[**set_site_scan_schedules**](SiteApi.md#set_site_scan_schedules) | **PUT** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
[**set_site_scan_template**](SiteApi.md#set_site_scan_template) | **PUT** /api/3/sites/{id}/scan_template | Site Scan Template
[**set_site_smtp_alerts**](SiteApi.md#set_site_smtp_alerts) | **PUT** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
[**set_site_snmp_alerts**](SiteApi.md#set_site_snmp_alerts) | **PUT** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
[**set_site_syslog_alerts**](SiteApi.md#set_site_syslog_alerts) | **PUT** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
[**set_site_tags**](SiteApi.md#set_site_tags) | **PUT** /api/3/sites/{id}/tags | Site Tags
[**set_site_users**](SiteApi.md#set_site_users) | **PUT** /api/3/sites/{id}/users | Site Users Access
[**update_excluded_asset_groups**](SiteApi.md#update_excluded_asset_groups) | **PUT** /api/3/sites/{id}/excluded_asset_groups | Site Excluded Asset Groups
[**update_excluded_targets**](SiteApi.md#update_excluded_targets) | **PUT** /api/3/sites/{id}/excluded_targets | Site Excluded Targets
[**update_included_asset_groups**](SiteApi.md#update_included_asset_groups) | **PUT** /api/3/sites/{id}/included_asset_groups | Site Included Asset Groups
[**update_included_targets**](SiteApi.md#update_included_targets) | **PUT** /api/3/sites/{id}/included_targets | Site Included Targets
[**update_site**](SiteApi.md#update_site) | **PUT** /api/3/sites/{id} | Site
[**update_site_credential**](SiteApi.md#update_site_credential) | **PUT** /api/3/sites/{id}/site_credentials/{credentialId} | Site Scan Credential
[**update_site_organization**](SiteApi.md#update_site_organization) | **PUT** /api/3/sites/{id}/organization | Site Organization Information
[**update_site_scan_schedule**](SiteApi.md#update_site_scan_schedule) | **PUT** /api/3/sites/{id}/scan_schedules/{scheduleId} | Site Scan Schedule
[**update_site_smtp_alert**](SiteApi.md#update_site_smtp_alert) | **PUT** /api/3/sites/{id}/alerts/smtp/{alertId} | Site SMTP Alert
[**update_site_snmp_alert**](SiteApi.md#update_site_snmp_alert) | **PUT** /api/3/sites/{id}/alerts/snmp/{alertId} | Site SNMP Alert
[**update_site_syslog_alert**](SiteApi.md#update_site_syslog_alert) | **PUT** /api/3/sites/{id}/alerts/syslog/{alertId} | Site Syslog Alert


# **add_site_tag**
> Links add_site_tag(id, tag_id)

Site Tag

Adds a tag to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
tag_id = 56 # int | The identifier of the tag.

try:
    # Site Tag
    api_response = api_instance.add_site_tag(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->add_site_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **tag_id** | **int**| The identifier of the tag. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_site_user**
> ReferenceWithUserIDLink add_site_user(id, param0=param0)

Site Users Access

Grants a non-administrator user access to the specified site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = 56 # int | The identifier of the user. (optional)

try:
    # Site Users Access
    api_response = api_instance.add_site_user(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->add_site_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **int**| The identifier of the user. | [optional] 

### Return type

[**ReferenceWithUserIDLink**](ReferenceWithUserIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site**
> ReferenceWithSiteIDLink create_site(param0=param0)

Sites

Creates a new site with the specified configuration.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
param0 = rapid7vmconsole.SiteCreateResource() # SiteCreateResource | Resource for creating a site configuration. (optional)

try:
    # Sites
    api_response = api_instance.create_site(param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->create_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param0** | [**SiteCreateResource**](SiteCreateResource.md)| Resource for creating a site configuration. | [optional] 

### Return type

[**ReferenceWithSiteIDLink**](ReferenceWithSiteIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_credential**
> CreatedReferenceCredentialIDLink create_site_credential(id, param1=param1)

Site Scan Credentials

Creates a new site credential.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param1 = rapid7vmconsole.SiteCredential() # SiteCredential | The specification of a site credential. (optional)

try:
    # Site Scan Credentials
    api_response = api_instance.create_site_credential(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->create_site_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param1** | [**SiteCredential**](SiteCredential.md)| The specification of a site credential. | [optional] 

### Return type

[**CreatedReferenceCredentialIDLink**](CreatedReferenceCredentialIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_scan_schedule**
> ReferenceWithScanScheduleIDLink create_site_scan_schedule(id, param0=param0)

Site Scan Schedules

Creates a new scan schedule for the specified site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = rapid7vmconsole.ScanSchedule() # ScanSchedule | Resource for a scan schedule. (optional)

try:
    # Site Scan Schedules
    api_response = api_instance.create_site_scan_schedule(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->create_site_scan_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**ScanSchedule**](ScanSchedule.md)| Resource for a scan schedule. | [optional] 

### Return type

[**ReferenceWithScanScheduleIDLink**](ReferenceWithScanScheduleIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_smtp_alert**
> ReferenceWithAlertIDLink create_site_smtp_alert(id, param0=param0)

Site SMTP Alerts

Creates a new SMTP alert for the specified site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = rapid7vmconsole.SmtpAlert() # SmtpAlert | Resource for creating a new SMTP alert. (optional)

try:
    # Site SMTP Alerts
    api_response = api_instance.create_site_smtp_alert(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->create_site_smtp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**SmtpAlert**](SmtpAlert.md)| Resource for creating a new SMTP alert. | [optional] 

### Return type

[**ReferenceWithAlertIDLink**](ReferenceWithAlertIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_snmp_alert**
> ReferenceWithAlertIDLink create_site_snmp_alert(id, param0=param0)

Site SNMP Alerts

Creates a new SNMP alert for the specified site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = rapid7vmconsole.SnmpAlert() # SnmpAlert | Resource for creating a new SNMP alert. (optional)

try:
    # Site SNMP Alerts
    api_response = api_instance.create_site_snmp_alert(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->create_site_snmp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**SnmpAlert**](SnmpAlert.md)| Resource for creating a new SNMP alert. | [optional] 

### Return type

[**ReferenceWithAlertIDLink**](ReferenceWithAlertIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_syslog_alert**
> ReferenceWithAlertIDLink create_site_syslog_alert(id, param0=param0)

Site Syslog Alerts

Creates a new Syslog alert for the specified site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = rapid7vmconsole.SyslogAlert() # SyslogAlert | Resource for creating a new Syslog alert. (optional)

try:
    # Site Syslog Alerts
    api_response = api_instance.create_site_syslog_alert(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->create_site_syslog_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**SyslogAlert**](SyslogAlert.md)| Resource for creating a new Syslog alert. | [optional] 

### Return type

[**ReferenceWithAlertIDLink**](ReferenceWithAlertIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_site_alerts**
> Links delete_all_site_alerts(id)

Site Alerts

Deletes all alerts from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Alerts
    api_response = api_instance.delete_all_site_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_all_site_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_site_credentials**
> Links delete_all_site_credentials(id)

Site Scan Credentials

Deletes all site credentials from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Scan Credentials
    api_response = api_instance.delete_all_site_credentials(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_all_site_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_site_scan_schedules**
> Links delete_all_site_scan_schedules(id)

Site Scan Schedules

Deletes all scan schedules from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Scan Schedules
    api_response = api_instance.delete_all_site_scan_schedules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_all_site_scan_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_site_smtp_alerts**
> Links delete_all_site_smtp_alerts(id)

Site SMTP Alerts

Deletes all SMTP alerts from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site SMTP Alerts
    api_response = api_instance.delete_all_site_smtp_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_all_site_smtp_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_site_snmp_alerts**
> Links delete_all_site_snmp_alerts(id)

Site SNMP Alerts

Deletes all SNMP alerts from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site SNMP Alerts
    api_response = api_instance.delete_all_site_snmp_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_all_site_snmp_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_site_syslog_alerts**
> Links delete_all_site_syslog_alerts(id)

Site Syslog Alerts

Deletes all Syslog alerts from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Syslog Alerts
    api_response = api_instance.delete_all_site_syslog_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_all_site_syslog_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site**
> Links delete_site(id)

Site

site.delete.description

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site
    api_response = api_instance.delete_site(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_credential**
> Links delete_site_credential(id, credential_id)

Site Scan Credential

Deletes the specified site credential.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
credential_id = 56 # int | The identifier of the site credential.

try:
    # Site Scan Credential
    api_response = api_instance.delete_site_credential(id, credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **credential_id** | **int**| The identifier of the site credential. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_scan_schedule**
> Links delete_site_scan_schedule(id, schedule_id)

Site Scan Schedule

Deletes the specified scan schedule from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
schedule_id = 56 # int | The identifier of the scan schedule.

try:
    # Site Scan Schedule
    api_response = api_instance.delete_site_scan_schedule(id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_scan_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **schedule_id** | **int**| The identifier of the scan schedule. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_smtp_alert**
> Links delete_site_smtp_alert(id, alert_id)

Site SMTP Alert

Deletes the specified SMTP alert from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.

try:
    # Site SMTP Alert
    api_response = api_instance.delete_site_smtp_alert(id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_smtp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_snmp_alert**
> Links delete_site_snmp_alert(id, alert_id)

Site SNMP Alert

Deletes the specified SNMP alert from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.

try:
    # Site SNMP Alert
    api_response = api_instance.delete_site_snmp_alert(id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_snmp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_syslog_alert**
> Links delete_site_syslog_alert(id, alert_id)

Site Syslog Alert

Deletes the specified Syslog alert from the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.

try:
    # Site Syslog Alert
    api_response = api_instance.delete_site_syslog_alert(id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_syslog_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_shared_credential_on_site**
> Links enable_shared_credential_on_site(id, credential_id, param0=param0)

Assigned Shared Credential Enablement

Enable or disable the shared credential for the site's scans.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
credential_id = 56 # int | The identifier of the shared credential.
param0 = true # bool | Flag indicating whether the shared credential is enabled for the site's scans. (optional)

try:
    # Assigned Shared Credential Enablement
    api_response = api_instance.enable_shared_credential_on_site(id, credential_id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->enable_shared_credential_on_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **credential_id** | **int**| The identifier of the shared credential. | 
 **param0** | **bool**| Flag indicating whether the shared credential is enabled for the site&#39;s scans. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_site_credential**
> Links enable_site_credential(id, credential_id, param0=param0)

Site Credential Enablement

Enable or disable the site credential for scans.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
credential_id = 56 # int | The identifier of the site credential.
param0 = true # bool | Flag indicating whether the credential is enabled for use during the scan. (optional)

try:
    # Site Credential Enablement
    api_response = api_instance.enable_site_credential(id, credential_id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->enable_site_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **credential_id** | **int**| The identifier of the site credential. | 
 **param0** | **bool**| Flag indicating whether the credential is enabled for use during the scan. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excluded_asset_groups**
> ResourcesAssetGroup get_excluded_asset_groups(id)

Site Excluded Asset Groups

Retrieves the excluded asset groups in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Excluded Asset Groups
    api_response = api_instance.get_excluded_asset_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_excluded_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesAssetGroup**](ResourcesAssetGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excluded_targets**
> ScanTargetsResource get_excluded_targets(id)

Site Excluded Targets

Retrieves the excluded targets in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Excluded Targets
    api_response = api_instance.get_excluded_targets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_excluded_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ScanTargetsResource**](ScanTargetsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_included_asset_groups**
> ResourcesAssetGroup get_included_asset_groups(id)

Site Included Asset Groups

Retrieves the included asset groups in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Included Asset Groups
    api_response = api_instance.get_included_asset_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_included_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesAssetGroup**](ResourcesAssetGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_included_targets**
> ScanTargetsResource get_included_targets(id)

Site Included Targets

Retrieves the included targets in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Included Targets
    api_response = api_instance.get_included_targets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_included_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ScanTargetsResource**](ScanTargetsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site**
> Site get_site(id)

Site

Retrieves the site with the specified identifier.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site
    api_response = api_instance.get_site(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_alerts**
> ResourcesAlert get_site_alerts(id)

Site Alerts

Retrieve all alerts defined in the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Alerts
    api_response = api_instance.get_site_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesAlert**](ResourcesAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_assets**
> PageOfAsset get_site_assets(id, page=page, size=size, sort=sort)

Site Assets

Retrieves a paged resource of assets linked with the specified site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Site Assets
    api_response = api_instance.get_site_assets(id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfAsset**](PageOfAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_credential**
> SiteCredential get_site_credential(id, credential_id)

Site Scan Credential

Retrieves the specified site credential.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
credential_id = 56 # int | The identifier of the site credential.

try:
    # Site Scan Credential
    api_response = api_instance.get_site_credential(id, credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **credential_id** | **int**| The identifier of the site credential. | 

### Return type

[**SiteCredential**](SiteCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_credentials**
> ResourcesSiteCredential get_site_credentials(id)

Site Scan Credentials

Retrieves all defined site credential resources.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Scan Credentials
    api_response = api_instance.get_site_credentials(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesSiteCredential**](ResourcesSiteCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_discovery_connection**
> SiteDiscoveryConnection get_site_discovery_connection(id)

Site Discovery Connection

Retrieves the discovery connection assigned to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Discovery Connection
    api_response = api_instance.get_site_discovery_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_discovery_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**SiteDiscoveryConnection**](SiteDiscoveryConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_discovery_search_criteria**
> DiscoverySearchCriteria get_site_discovery_search_criteria(id)

Site Discovery Search Criteria

Retrieve the search criteria of the dynamic site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Discovery Search Criteria
    api_response = api_instance.get_site_discovery_search_criteria(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_discovery_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**DiscoverySearchCriteria**](DiscoverySearchCriteria.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_organization**
> SiteOrganization get_site_organization(id)

Site Organization Information

Retrieves the site organization information.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Organization Information
    api_response = api_instance.get_site_organization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**SiteOrganization**](SiteOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_scan_engine**
> ScanEngine get_site_scan_engine(id)

Site Scan Engine

Retrieves the resource of the scan engine assigned to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Scan Engine
    api_response = api_instance.get_site_scan_engine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_scan_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ScanEngine**](ScanEngine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_scan_schedule**
> ScanSchedule get_site_scan_schedule(id, schedule_id)

Site Scan Schedule

Retrieves the specified scan schedule.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
schedule_id = 56 # int | The identifier of the scan schedule.

try:
    # Site Scan Schedule
    api_response = api_instance.get_site_scan_schedule(id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_scan_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **schedule_id** | **int**| The identifier of the scan schedule. | 

### Return type

[**ScanSchedule**](ScanSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_scan_schedules**
> ResourcesScanSchedule get_site_scan_schedules(id)

Site Scan Schedules

Returns all scan schedules for the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Scan Schedules
    api_response = api_instance.get_site_scan_schedules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_scan_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesScanSchedule**](ResourcesScanSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_scan_template**
> ScanTemplate get_site_scan_template(id)

Site Scan Template

Retrieves the resource of the scan template assigned to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Scan Template
    api_response = api_instance.get_site_scan_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_scan_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ScanTemplate**](ScanTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_shared_credentials**
> ResourcesSiteSharedCredential get_site_shared_credentials(id)

Assigned Shared Credentials

Retrieve all of the shared credentials assigned to the site. These shared credentials can be enabled/disabled for the site's scan.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Assigned Shared Credentials
    api_response = api_instance.get_site_shared_credentials(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_shared_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesSiteSharedCredential**](ResourcesSiteSharedCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_smtp_alert**
> SmtpAlert get_site_smtp_alert(id, alert_id)

Site SMTP Alert

Retrieves the specified SMTP alert.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.

try:
    # Site SMTP Alert
    api_response = api_instance.get_site_smtp_alert(id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_smtp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 

### Return type

[**SmtpAlert**](SmtpAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_smtp_alerts**
> ResourcesSmtpAlert get_site_smtp_alerts(id)

Site SMTP Alerts

Retrieves all SMTP alerts defined in the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site SMTP Alerts
    api_response = api_instance.get_site_smtp_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_smtp_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesSmtpAlert**](ResourcesSmtpAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_snmp_alert**
> SnmpAlert get_site_snmp_alert(id, alert_id)

Site SNMP Alert

Retrieves the specified SNMP alert.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.

try:
    # Site SNMP Alert
    api_response = api_instance.get_site_snmp_alert(id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_snmp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 

### Return type

[**SnmpAlert**](SnmpAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_snmp_alerts**
> ResourcesSnmpAlert get_site_snmp_alerts(id)

Site SNMP Alerts

Retrieves all SNMP alerts defined in the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site SNMP Alerts
    api_response = api_instance.get_site_snmp_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_snmp_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesSnmpAlert**](ResourcesSnmpAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_syslog_alert**
> SyslogAlert get_site_syslog_alert(id, alert_id)

Site Syslog Alert

Retrieves the specified Syslog alert.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.

try:
    # Site Syslog Alert
    api_response = api_instance.get_site_syslog_alert(id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_syslog_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 

### Return type

[**SyslogAlert**](SyslogAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_syslog_alerts**
> ResourcesSyslogAlert get_site_syslog_alerts(id)

Site Syslog Alerts

Retrieves all Syslog alerts defined in the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Syslog Alerts
    api_response = api_instance.get_site_syslog_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_syslog_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesSyslogAlert**](ResourcesSyslogAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_tags**
> ResourcesTag get_site_tags(id)

Site Tags

Retrieves the list of tags added to the sites.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Tags
    api_response = api_instance.get_site_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesTag**](ResourcesTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_users**
> ResourcesUser get_site_users(id)

Site Users Access

Retrieve the list of non-administrator users that have access to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Users Access
    api_response = api_instance.get_site_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesUser**](ResourcesUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites**
> PageOfSite get_sites(page=page, size=size, sort=sort)

Sites

Retrieves a paged resource of accessible sites.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
page = 0 # int | The index of the page (zero-based) to retrieve. (optional) (default to 0)
size = 10 # int | The number of records per page to retrieve. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. (optional)

try:
    # Sites
    api_response = api_instance.get_sites(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The index of the page (zero-based) to retrieve. | [optional] [default to 0]
 **size** | **int**| The number of records per page to retrieve. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The criteria to sort the records by, in the format: &#x60;property[,ASC|DESC]&#x60;. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters. | [optional] 

### Return type

[**PageOfSite**](PageOfSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_auth_html_forms**
> ResourcesWebFormAuthentication get_web_auth_html_forms(id)

Web Authentication HTML Forms

Retrieves all HTML form authentications configured in the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Web Authentication HTML Forms
    api_response = api_instance.get_web_auth_html_forms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_web_auth_html_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesWebFormAuthentication**](ResourcesWebFormAuthentication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_auth_http_headers**
> ResourcesWebHeaderAuthentication get_web_auth_http_headers(id)

Web Authentication HTTP Headers

Retrieves all HTTP header authentications configured in the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Web Authentication HTTP Headers
    api_response = api_instance.get_web_auth_http_headers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_web_auth_http_headers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**ResourcesWebHeaderAuthentication**](ResourcesWebHeaderAuthentication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_excluded_asset_groups**
> Links remove_all_excluded_asset_groups(id)

Site Excluded Asset Groups

Removes all excluded asset groups from the specified static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Excluded Asset Groups
    api_response = api_instance.remove_all_excluded_asset_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_all_excluded_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_included_asset_groups**
> Links remove_all_included_asset_groups(id)

Site Included Asset Groups

Removes all included asset groups from the specified static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Included Asset Groups
    api_response = api_instance.remove_all_included_asset_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_all_included_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_from_site**
> Links remove_asset_from_site(id, asset_id)

Site Asset

Removes an asset from a site. The asset will only be deleted if it belongs to no other sites.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
asset_id = 789 # int | The identifier of the asset.

try:
    # Site Asset
    api_response = api_instance.remove_asset_from_site(id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_asset_from_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **asset_id** | **int**| The identifier of the asset. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_excluded_asset_group**
> Links remove_excluded_asset_group(id, asset_group_id)

Site Excluded Asset Group

Removes the specified asset group from the excluded asset groups configured in the static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
asset_group_id = 56 # int | The identifier of the asset group.

try:
    # Site Excluded Asset Group
    api_response = api_instance.remove_excluded_asset_group(id, asset_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_excluded_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **asset_group_id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_included_asset_group**
> Links remove_included_asset_group(id, asset_group_id)

Site Included Asset Group

Removes the specified asset group from the included asset groups configured in the static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
asset_group_id = 56 # int | The identifier of the asset group.

try:
    # Site Included Asset Group
    api_response = api_instance.remove_included_asset_group(id, asset_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_included_asset_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **asset_group_id** | **int**| The identifier of the asset group. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_site_assets**
> Links remove_site_assets(id)

Site Assets

Removes all assets from the specified site. Assets will be deleted entirely from the Security Console if either Asset Linking is disabled or if Asset Linking is enabled and the asset only existed in this site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.

try:
    # Site Assets
    api_response = api_instance.remove_site_assets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_site_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_site_tag**
> Links remove_site_tag(id, tag_id)

Site Tag

Removes the specified tag from the site's tags.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
tag_id = 56 # int | The identifier of the tag.

try:
    # Site Tag
    api_response = api_instance.remove_site_tag(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_site_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **tag_id** | **int**| The identifier of the tag. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_site_user**
> Links remove_site_user(id, user_id)

Site User Access

Removes the specified user from the site's access list.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
user_id = 56 # int | The identifier of the user.

try:
    # Site User Access
    api_response = api_instance.remove_site_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->remove_site_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **user_id** | **int**| The identifier of the user. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_credentials**
> Links set_site_credentials(id, param1=param1)

Site Scan Credentials

Updates multiple site credentials.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param1 = [rapid7vmconsole.SiteCredential()] # list[SiteCredential] | A list of site credentials resources. (optional)

try:
    # Site Scan Credentials
    api_response = api_instance.set_site_credentials(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param1** | [**list[SiteCredential]**](SiteCredential.md)| A list of site credentials resources. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_discovery_connection**
> Links set_site_discovery_connection(id, param0=param0)

Site Discovery Connection

Updates the discovery connection assigned to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = 789 # int | The identifier of the discovery connection. (optional)

try:
    # Site Discovery Connection
    api_response = api_instance.set_site_discovery_connection(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_discovery_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **int**| The identifier of the discovery connection. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_discovery_search_criteria**
> Links set_site_discovery_search_criteria(id, param1)

Site Discovery Search Criteria

Update the search criteria of the dynamic site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param1 = rapid7vmconsole.DiscoverySearchCriteria() # DiscoverySearchCriteria | param1

try:
    # Site Discovery Search Criteria
    api_response = api_instance.set_site_discovery_search_criteria(id, param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_discovery_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param1** | [**DiscoverySearchCriteria**](DiscoverySearchCriteria.md)| param1 | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_scan_engine**
> Links set_site_scan_engine(id, param0=param0)

Site Scan Engine

Updates the assigned scan engine to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = 56 # int | The identifier of the scan engine. (optional)

try:
    # Site Scan Engine
    api_response = api_instance.set_site_scan_engine(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_scan_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **int**| The identifier of the scan engine. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_scan_schedules**
> Links set_site_scan_schedules(id, param0=param0)

Site Scan Schedules

Updates all scan schedules for the specified site in a single request using the array of resources defined in the request body.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.ScanSchedule()] # list[ScanSchedule] | Array of resources for updating all scan schedules defined in the site. Scan schedules defined in the site that are omitted from this request will be deleted from the site. (optional)

try:
    # Site Scan Schedules
    api_response = api_instance.set_site_scan_schedules(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_scan_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**list[ScanSchedule]**](ScanSchedule.md)| Array of resources for updating all scan schedules defined in the site. Scan schedules defined in the site that are omitted from this request will be deleted from the site. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_scan_template**
> Links set_site_scan_template(id, param0=param0)

Site Scan Template

Updates the assigned scan template to the site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = 'param0_example' # str | The identifier of the scan template. (optional)

try:
    # Site Scan Template
    api_response = api_instance.set_site_scan_template(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_scan_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **str**| The identifier of the scan template. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_smtp_alerts**
> Links set_site_smtp_alerts(id, param0=param0)

Site SMTP Alerts

Updates all SMTP alerts for the specified site in a single request using the array of resources defined in the request body.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.SmtpAlert()] # list[SmtpAlert] | Array of resources for updating all SMTP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site. (optional)

try:
    # Site SMTP Alerts
    api_response = api_instance.set_site_smtp_alerts(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_smtp_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**list[SmtpAlert]**](SmtpAlert.md)| Array of resources for updating all SMTP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_snmp_alerts**
> Links set_site_snmp_alerts(id, param0=param0)

Site SNMP Alerts

Updates all SNMP alerts for the specified site in a single request using the array of resources defined in the request body.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.SnmpAlert()] # list[SnmpAlert] | Array of resources for updating all SNMP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site. (optional)

try:
    # Site SNMP Alerts
    api_response = api_instance.set_site_snmp_alerts(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_snmp_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**list[SnmpAlert]**](SnmpAlert.md)| Array of resources for updating all SNMP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_syslog_alerts**
> Links set_site_syslog_alerts(id, param0=param0)

Site Syslog Alerts

Updates all Syslog alerts for the specified site in a single request using the array of resources defined in the request body.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.SyslogAlert()] # list[SyslogAlert] | Array of resources for updating all Syslog alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site. (optional)

try:
    # Site Syslog Alerts
    api_response = api_instance.set_site_syslog_alerts(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_syslog_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**list[SyslogAlert]**](SyslogAlert.md)| Array of resources for updating all Syslog alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_tags**
> Links set_site_tags(id, param1=param1)

Site Tags

Updates the site's list of tags.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param1 = [rapid7vmconsole.list[int]()] # list[int] | A list of tag identifiers to replace the site's tags. (optional)

try:
    # Site Tags
    api_response = api_instance.set_site_tags(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param1** | **list[int]**| A list of tag identifiers to replace the site&#39;s tags. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_users**
> Links set_site_users(id, param0=param0)

Site Users Access

Updates the site's access list.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.list[int]()] # list[int] | A list of user identifiers to replace the site's access list. (optional)

try:
    # Site Users Access
    api_response = api_instance.set_site_users(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->set_site_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **list[int]**| A list of user identifiers to replace the site&#39;s access list. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_excluded_asset_groups**
> Links update_excluded_asset_groups(id, param0=param0)

Site Excluded Asset Groups

Updates the excluded asset groups in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.list[int]()] # list[int] | Array of asset group identifiers. (optional)

try:
    # Site Excluded Asset Groups
    api_response = api_instance.update_excluded_asset_groups(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_excluded_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **list[int]**| Array of asset group identifiers. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_excluded_targets**
> Links update_excluded_targets(id, param0=param0)

Site Excluded Targets

Updates the excluded targets in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.list[str]()] # list[str] | List of addresses to be the site's new excluded scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. (optional)

try:
    # Site Excluded Targets
    api_response = api_instance.update_excluded_targets(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_excluded_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **list[str]**| List of addresses to be the site&#39;s new excluded scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_included_asset_groups**
> Links update_included_asset_groups(id, param0=param0)

Site Included Asset Groups

Updates the included asset groups in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.list[int]()] # list[int] | Array of asset group identifiers. (optional)

try:
    # Site Included Asset Groups
    api_response = api_instance.update_included_asset_groups(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_included_asset_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **list[int]**| Array of asset group identifiers. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_included_targets**
> Links update_included_targets(id, param0=param0)

Site Included Targets

Updates the included targets in a static site.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = [rapid7vmconsole.list[str]()] # list[str] | List of addresses to be the site's new included scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. (optional)

try:
    # Site Included Targets
    api_response = api_instance.update_included_targets(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_included_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | **list[str]**| List of addresses to be the site&#39;s new included scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site**
> Links update_site(id, param0=param0)

Site

Updates the configuration of the site with the specified identifier.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = rapid7vmconsole.SiteUpdateResource() # SiteUpdateResource | Resource for updating a site configuration. (optional)

try:
    # Site
    api_response = api_instance.update_site(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**SiteUpdateResource**](SiteUpdateResource.md)| Resource for updating a site configuration. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_credential**
> Links update_site_credential(id, credential_id, param2=param2)

Site Scan Credential

Updates the specified site credential.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
credential_id = 56 # int | The identifier of the site credential.
param2 = rapid7vmconsole.SiteCredential() # SiteCredential | The specification of the site credential to update. (optional)

try:
    # Site Scan Credential
    api_response = api_instance.update_site_credential(id, credential_id, param2=param2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **credential_id** | **int**| The identifier of the site credential. | 
 **param2** | [**SiteCredential**](SiteCredential.md)| The specification of the site credential to update. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_organization**
> Links update_site_organization(id, param0=param0)

Site Organization Information

Updates the site organization information.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
param0 = rapid7vmconsole.SiteOrganization() # SiteOrganization | Resource for updating the specified site's organization information. (optional)

try:
    # Site Organization Information
    api_response = api_instance.update_site_organization(id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **param0** | [**SiteOrganization**](SiteOrganization.md)| Resource for updating the specified site&#39;s organization information. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_scan_schedule**
> Links update_site_scan_schedule(id, schedule_id, param0=param0)

Site Scan Schedule

Updates the specified scan schedule.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
schedule_id = 56 # int | The identifier of the scan schedule.
param0 = rapid7vmconsole.ScanSchedule() # ScanSchedule | Resource for updating the specified scan schedule. (optional)

try:
    # Site Scan Schedule
    api_response = api_instance.update_site_scan_schedule(id, schedule_id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_scan_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **schedule_id** | **int**| The identifier of the scan schedule. | 
 **param0** | [**ScanSchedule**](ScanSchedule.md)| Resource for updating the specified scan schedule. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_smtp_alert**
> Links update_site_smtp_alert(id, alert_id, param0=param0)

Site SMTP Alert

Updates the specified SMTP alert.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.
param0 = rapid7vmconsole.SmtpAlert() # SmtpAlert | Resource for updating the specified SMTP alert. (optional)

try:
    # Site SMTP Alert
    api_response = api_instance.update_site_smtp_alert(id, alert_id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_smtp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 
 **param0** | [**SmtpAlert**](SmtpAlert.md)| Resource for updating the specified SMTP alert. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_snmp_alert**
> Links update_site_snmp_alert(id, alert_id, param0=param0)

Site SNMP Alert

Updates the specified SNMP alert.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.
param0 = rapid7vmconsole.SnmpAlert() # SnmpAlert | Resource for updating the specified SNMP alert. (optional)

try:
    # Site SNMP Alert
    api_response = api_instance.update_site_snmp_alert(id, alert_id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_snmp_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 
 **param0** | [**SnmpAlert**](SnmpAlert.md)| Resource for updating the specified SNMP alert. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_syslog_alert**
> Links update_site_syslog_alert(id, alert_id, param0=param0)

Site Syslog Alert

Updates the specified Syslog alert.

### Example
```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rapid7vmconsole.SiteApi()
id = 56 # int | The identifier of the site.
alert_id = 56 # int | The identifier of the alert.
param0 = rapid7vmconsole.SyslogAlert() # SyslogAlert | Resource for updating the specified Syslog alert. (optional)

try:
    # Site Syslog Alert
    api_response = api_instance.update_site_syslog_alert(id, alert_id, param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_syslog_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the site. | 
 **alert_id** | **int**| The identifier of the alert. | 
 **param0** | [**SyslogAlert**](SyslogAlert.md)| Resource for updating the specified Syslog alert. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

