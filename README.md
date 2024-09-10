# ARCHIVED 

This repository is not supported or maintained.
Clients for other languages can be generated from the Swagger specification. Note that generated clients are not officially supported or maintained by Rapid7.

# rapid7_vm_console

rapid7_vm_console - the __UNOFFICIAL__ (but useful) Python library for the Rapid7 InsightVM/Nexpose RESTful API

DISCLAIMER: the resulting Python library and the files found in this repository are meant for community use and are leveraged
by internal Rapid7 team(s). They are NOT officially supported artifacts and are not supported by Rapid7 Support. Best
effort is used to keep this repository and resulting Python library up to date and resolve reported issues/bugs.

If any issues are experienced, any user can leverage the Swagger file at `https://localhost:3780/api/html/json` of their
Console to create their own library or interact with the API as needed.  By auto-generating this repository and
artifacts, users can begin interacting with the Rapid7 InsightVM/Nexpose API with Python by simply importing `rapid7vmconsole`.

## Quick Setup

Download this repository and cd into its directory
```
$ git clone https://github.com/rapid7/vm-console-client-python.git
$ cd vm-console-client-python
```

Setup your environment and install dependencies.  We recommend using python [Virtualenv](https://virtualenv.pypa.io/en/stable/) but this is not required.
```
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

Run one of the sample clients.

```
$ mv samples/list_assets.py .
$ # At a minimum, edit username, password, and host within the config section of list_assets.py
$ python3 list_assets.py
> Asset ID: 637; Hostname: superman.batman.rapid7.com; IP Address: 192.168.1.1
Asset ID: 644; Hostname: switch-wars.rapid7.com; IP Address: 127.0.0.1
Asset ID: 649; Hostname: switch-boss.rapid7.com; IP Address: 127.0.0.2
```

## Auto-generating code
The code and resulting library of this repository have been auto generated using [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)
along with the most recent Rapid7 InsightVM/Nexpose Swagger file. After each new console release, the script found
at `setup_workspace/setup_workspace.sh` is run to check if any changes have been made to the API Swagger file. If changes
exist, the script automates the download of swagger-codegen-cli.jar, updates the version, and executes the jar generate
process. An example command for running codegen to generate Python source is below:
```
java -jar swagger-codegen-cli-2.3.0.jar generate \
         -i api-files/console-swagger-6.5.5.json \
         -l python \
         -o ./ \
         -c setup_workspace/config.json
```

Any issues or questions regarding Swagger Codegen should be directed to the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)
Github repository.

## Versioning and Releases
Currently any generated libraries are prerelease and are following X.Y.Z-{CONSOLE_VERSION} versioning. It will be decided
whether a two version system will be followed or a single version decoupled from the Console version. Feedback is greatly
appreciated.

Building the universal library:
```
python setup.py bdist_wheel --universal
```

Whenever a new version of the API is released, the most up to date and past releases will be found
[here](https://github.com/rapid7/vm-console-client-python/releases) along with generated tags. Once the maintainers feel
comfortable with the state of this repository, releases will also be pushed to PyPi.

# Auto-generated README Below
## Overview
This guide documents the InsightVM Application Programming Interface (API) Version 3. This API supports the Representation State Transfer (REST) design pattern. Unless noted otherwise this API accepts and produces the `application/json` media type. This API uses Hypermedia as the Engine of Application State (HATEOAS) and is hypermedia friendly. All API connections must be made to the security console using HTTPS.
## Versioning
Versioning is specified in the URL and the base path of this API is: `https://<host>:<port>/api/3/`.
## Specification
An <a target=\"_blank\" href=\"https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md\">OpenAPI v2</a> specification (also  known as Swagger 2) of this API is available. Tools such as <a target=\"_blank\" href=\"https://github.com/swagger-api/swagger-codegen\">swagger-codegen</a> can be used to generate an API client in the language of your choosing using this specification document.  <p class=\"openapi\">Download the specification: <a class=\"openapi-button\" target=\"_blank\" download=\"\" href=\"/api/3/json\"> Download </a></p>
## Authentication
Authorization to the API uses HTTP Basic Authorization  (see <a target=\"_blank\" href=\"https://www.ietf.org/rfc/rfc2617.txt\">RFC 2617</a> for more information). Requests must  supply authorization credentials in the `Authorization` header using a Base64 encoded hash of `\"username:password\"`.  <!-- ReDoc-Inject: <security-definitions> -->
### 2FA
This API supports two-factor authentication (2FA) by supplying an authentication token in addition to the Basic Authorization. The token is specified using the `Token` request header. To leverage two-factor authentication, this must be enabled on the console and be configured for the account accessing the API.
## Resources
### Naming
Resource names represent nouns and identify the entity being manipulated or accessed. All collection resources are  pluralized to indicate to the client they are interacting with a collection of multiple resources of the same type. Singular resource names are used when there exists only one resource available to interact with.  The following naming conventions are used by this API:  | Type                                          | Case                     | | --------------------------------------------- | ------------------------ | | Resource names                                | `lower_snake_case`       | | Header, body, and query parameters parameters | `camelCase`              | | JSON fields and property names                | `camelCase`              |
#### Collections
A collection resource is a parent resource for instance resources, but can itself be retrieved and operated on  independently. Collection resources use a pluralized resource name. The resource path for collection resources follow  the convention:  ``` /api/3/{resource_name} ```
#### Instances
n instance resource is a \"leaf\" level resource that may be retrieved, optionally nested within a collection resource. Instance resources are usually retrievable with opaque identifiers. The resource path for instance resources follows  the convention:  ``` /api/3/{resource_name}/{instance_id}... ```
## Verbs
The following HTTP operations are supported throughout this API. The general usage of the operation and both its failure and success status codes are outlined below.    | Verb      | Usage                                                                                 | Success     | Failure                                                        | | --------- | ------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | | `GET`     | Used to retrieve a resource by identifier, or a collection of resources by type.      | `200`       | `400`, `401`, `402`, `404`, `405`, `408`, `410`, `415`, `500`  | | `POST`    | Creates a resource with an application-specified identifier.                          | `201`       | `400`, `401`, `404`, `405`, `408`, `413`, `415`, `500`         | | `POST`    | Performs a request to queue an asynchronous job.                                      | `202`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `PUT`     | Creates a resource with a client-specified identifier.                                | `200`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `PUT`     | Performs a full update of a resource with a specified identifier.                     | `201`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `DELETE`  | Deletes a resource by identifier or an entire collection of resources.                | `204`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `OPTIONS` | Requests what operations are available on a resource.                                 | `200`       | `401`, `404`, `405`, `408`, `500`                              |
### Common Operations
#### OPTIONS
All resources respond to the `OPTIONS` request, which allows discoverability of available operations that are supported.  The `OPTIONS` response returns the acceptable HTTP operations on that resource within the `Allow` header. The response is always a `200 OK` status.
### Collection Resources
Collection resources can support the `GET`, `POST`, `PUT`, and `DELETE` operations.
#### GET
The `GET` operation invoked on a collection resource indicates a request to retrieve all, or some, of the entities  contained within the collection. This also includes the optional capability to filter or search resources during the request. The response from a collection listing is a paginated document. See  [hypermedia links](#section/Overview/Paging) for more information.
#### POST
The `POST` is a non-idempotent operation that allows for the creation of a new resource when the resource identifier  is not provided by the system during the creation operation (i.e. the Security Console generates the identifier). The content of the `POST` request is sent in the request body. The response to a successful `POST` request should be a  `201 CREATED` with a valid `Location` header field set to the URI that can be used to access to the newly  created resource.   The `POST` to a collection resource can also be used to interact with asynchronous resources. In this situation,  instead of a `201 CREATED` response, the `202 ACCEPTED` response indicates that processing of the request is not fully  complete but has been accepted for future processing. This request will respond similarly with a `Location` header with  link to the job-oriented asynchronous resource that was created and/or queued.
#### PUT
The `PUT` is an idempotent operation that either performs a create with user-supplied identity, or a full replace or update of a resource by a known identifier. The response to a `PUT` operation to create an entity is a `201 Created` with a valid `Location` header field set to the URI that can be used to access to the newly created resource.  `PUT` on a collection resource replaces all values in the collection. The typical response to a `PUT` operation that  updates an entity is hypermedia links, which may link to related resources caused by the side-effects of the changes  performed.
#### DELETE
The `DELETE` is an idempotent operation that physically deletes a resource, or removes an association between resources. The typical response to a `DELETE` operation is hypermedia links, which may link to related resources caused by the  side-effects of the changes performed.
### Instance Resources
Instance resources can support the `GET`, `PUT`, `POST`, `PATCH` and `DELETE` operations.
#### GET
Retrieves the details of a specific resource by its identifier. The details retrieved can be controlled through  property selection and property views. The content of the resource is returned within the body of the response in the  acceptable media type.
#### PUT
Allows for and idempotent \"full update\" (complete replacement) on a specific resource. If the resource does not exist,  it will be created; if it does exist, it is completely overwritten. Any omitted properties in the request are assumed to  be undefined/null. For \"partial updates\" use `POST` or `PATCH` instead.   The content of the `PUT` request is sent in the request body. The identifier of the resource is specified within the URL  (not the request body). The response to a successful `PUT` request is a `201 CREATED` to represent the created status,  with a valid `Location` header field set to the URI that can be used to access to the newly created (or fully replaced)  resource.
#### POST
Performs a non-idempotent creation of a new resource. The `POST` of an instance resource most commonly occurs with the  use of nested resources (e.g. searching on a parent collection resource). The response to a `POST` of an instance  resource is typically a `200 OK` if the resource is non-persistent, and a `201 CREATED` if there is a resource  created/persisted as a result of the operation. This varies by endpoint.
#### PATCH
The `PATCH` operation is used to perform a partial update of a resource. `PATCH` is a non-idempotent operation that enforces an atomic mutation of a resource. Only the properties specified in the request are to be overwritten on the  resource it is applied to. If a property is missing, it is assumed to not have changed.
#### DELETE
Permanently removes the individual resource from the system. If the resource is an association between resources, only  the association is removed, not the resources themselves. A successful deletion of the resource should return  `204 NO CONTENT` with no response body. This operation is not fully idempotent, as follow-up requests to delete a  non-existent resource should return a `404 NOT FOUND`.
## Requests
Unless otherwise indicated, the default request body media type is `application/json`.
### Headers
Commonly used request headers include:  | Header             | Example                                       | Purpose                                                                                        |                    | ------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------------- | | `Accept`           | `application/json`                            | Defines what acceptable content types are allowed by the client. For all types, use `*/*`.     | | `Accept-Encoding`  | `deflate, gzip`                               | Allows for the encoding to be specified (such as gzip).                                        | | `Accept-Language`  | `en-US`                                       | Indicates to the server the client's locale (defaults `en-US`).                                | | `Authorization `   | `Basic Base64(\"username:password\")`           | Basic authentication                                                                           | | `Token `           | `123456`                                      | Two-factor authentication token (if enabled)                                                   |
### Dates & Times
Dates and/or times are specified as strings in the ISO 8601 format(s). The following formats are supported as input:  | Value                       | Format                                                 | Notes                                                 | | --------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | | Date                        | YYYY-MM-DD                                             | Defaults to 12 am UTC (if used for a date & time      | | Date & time only            | YYYY-MM-DD'T'hh:mm:ss[.nnn]                            | Defaults to UTC                                       | | Date & time in UTC          | YYYY-MM-DD'T'hh:mm:ss[.nnn]Z                           |                                                       | | Date & time w/ offset       | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm             |                                                       | | Date & time w/ zone-offset  | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm[<zone-id>]  |                                                       |
### Timezones
Timezones are specified in the regional zone format, such as `\"America/Los_Angeles\"`, `\"Asia/Tokyo\"`, or `\"GMT\"`.
### Paging
Pagination is supported on certain collection resources using a combination of two query parameters, `page` and `size`.  As these are control parameters, they are prefixed with the underscore character. The page parameter dictates the  zero-based index of the page to retrieve, and the `size` indicates the size of the page.   For example, `/resources?page=2&size=10` will return page 3, with 10 records per page, giving results 21-30.  The maximum page size for a request is 500.
### Sorting
Sorting is supported on paginated resources with the `sort` query parameter(s). The sort query parameter(s) supports  identifying a single or multi-property sort with a single or multi-direction output. The format of the parameter is:  ``` sort=property[,ASC|DESC]... ```  Therefore, the request `/resources?sort=name,title,DESC` would return the results sorted by the name and title  descending, in that order. The sort directions are either ascending `ASC` or descending `DESC`. With single-order  sorting, all properties are sorted in the same direction. To sort the results with varying orders by property,  multiple sort parameters are passed.    For example, the request `/resources?sort=name,ASC&sort=title,DESC` would sort by name ascending and title  descending, in that order.
## Responses
The following response statuses may be returned by this API.     | Status | Meaning                  | Usage                                                                                                                                                                    | | ------ | ------------------------ |------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `200`  | OK                       | The operation performed without error according to the specification of the request, and no more specific 2xx code is suitable.                                          | | `201`  | Created                  | A create request has been fulfilled and a resource has been created. The resource is available as the URI specified in the response, including the `Location` header.    | | `202`  | Accepted                 | An asynchronous task has been accepted, but not guaranteed, to be processed in the future.                                                                               | | `400`  | Bad Request              | The request was invalid or cannot be otherwise served. The request is not likely to succeed in the future without modifications.                                         | | `401`  | Unauthorized             | The user is unauthorized to perform the operation requested, or does not maintain permissions to perform the operation on the resource specified.                        | | `403`  | Forbidden                | The resource exists to which the user has access, but the operating requested is not permitted.                                                                          | | `404`  | Not Found                | The resource specified could not be located, does not exist, or an unauthenticated client does not have permissions to a resource.                                       | | `405`  | Method Not Allowed       | The operations may not be performed on the specific resource. Allowed operations are returned and may be performed on the resource.                                      | | `408`  | Request Timeout          | The client has failed to complete a request in a timely manner and the request has been discarded.                                                                       | | `413`  | Request Entity Too Large | The request being provided is too large for the server to accept processing.                                                                                             | | `415`  | Unsupported Media Type   | The media type is not supported for the requested resource.                                                                                                              | | `500`  | Internal Server Error    | An internal and unexpected error has occurred on the server at no fault of the client.                                                                                   |
### Security
The response statuses 401, 403 and 404 need special consideration for security purposes. As necessary,  error statuses and messages may be obscured to strengthen security and prevent information exposure. The following is a  guideline for privileged resource response statuses:  | Use Case                                                           | Access             | Resource           | Permission   | Status       | | ------------------------------------------------------------------ | ------------------ |------------------- | ------------ | ------------ | | Unauthenticated access to an unauthenticated resource.             | Unauthenticated    | Unauthenticated    | Yes          | `20x`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Authenticated      | No           | `401`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Non-existent       | No           | `401`        | | Authenticated access to a unauthenticated resource.                | Authenticated      | Unauthenticated    | Yes          | `20x`        | | Authenticated access to an authenticated, unprivileged resource.   | Authenticated      | Authenticated      | No           | `404`        | | Authenticated access to an authenticated, privileged resource.     | Authenticated      | Authenticated      | Yes          | `20x`        | | Authenticated access to an authenticated, non-existent resource    | Authenticated      | Non-existent       | Yes          | `404`        |
### Headers
Commonly used response headers include:  | Header                     |  Example                          | Purpose                                                         | | -------------------------- | --------------------------------- | --------------------------------------------------------------- | | `Allow`                    | `OPTIONS, GET`                    | Defines the allowable HTTP operations on a resource.            | | `Cache-Control`            | `no-store, must-revalidate`       | Disables caching of resources (as they are all dynamic).        | | `Content-Encoding`         | `gzip`                            | The encoding of the response body (if any).                     | | `Location`                 |                                   | Refers to the URI of the resource created by a request.         | | `Transfer-Encoding`        | `chunked`                         | Specified the encoding used to transform response.              | | `Retry-After`              | 5000                              | Indicates the time to wait before retrying a request.           | | `X-Content-Type-Options`   | `nosniff`                         | Disables MIME type sniffing.                                    | | `X-XSS-Protection`         | `1; mode=block`                   | Enables XSS filter protection.                                  | | `X-Frame-Options`          | `SAMEORIGIN`                      | Prevents rendering in a frame from a different origin.          | | `X-UA-Compatible`          | `IE=edge,chrome=1`                | Specifies the browser mode to render in.                        |
### Format
When `application/json` is returned in the response body it is always pretty-printed (indented, human readable output).  Additionally, gzip compression/encoding is supported on all responses.
#### Dates & Times
Dates or times are returned as strings in the ISO 8601 'extended' format. When a date and time is returned (instant) the value is converted to UTC.  For example:  | Value           | Format                         | Example               | | --------------- | ------------------------------ | --------------------- | | Date            | `YYYY-MM-DD`                   | 2017-12-03            | | Date & Time     | `YYYY-MM-DD'T'hh:mm:ss[.nnn]Z` | 2017-12-03T10:15:30Z  |
#### Content
In some resources a Content data type is used. This allows for multiple formats of representation to be returned within resource, specifically `\"html\"` and `\"text\"`. The `\"text\"` property returns a flattened representation suitable for output in textual displays. The `\"html\"` property returns an HTML fragment suitable for display within an HTML  element. Note, the HTML returned is not a valid stand-alone HTML document.
#### Paging
The response to a paginated request follows the format:  ```json {    resources\": [        ...     ],    \"page\": {        \"number\" : ...,       \"size\" : ...,       \"totalResources\" : ...,       \"totalPages\" : ...    },    \"links\": [        \"first\" : {          \"href\" : \"...\"        },        \"prev\" : {          \"href\" : \"...\"        },        \"self\" : {          \"href\" : \"...\"        },        \"next\" : {          \"href\" : \"...\"        },        \"last\" : {          \"href\" : \"...\"        }     ] } ```  The `resources` property is an array of the resources being retrieved from the endpoint, each which should contain at  minimum a \"self\" relation hypermedia link. The `page` property outlines the details of the current page and total possible pages. The object for the page includes the following properties:  - number - The page number (zero-based) of the page returned. - size - The size of the pages, which is less than or equal to the maximum page size. - totalResources - The total amount of resources available across all pages. - totalPages - The total amount of pages.  The last property of the paged response is the `links` array, which contains all available hypermedia links. For  paginated responses, the \"self\", \"next\", \"previous\", \"first\", and \"last\" links are returned. The \"self\" link must always be returned and should contain a link to allow the client to replicate the original request against the  collection resource in an identical manner to that in which it was invoked.   The \"next\" and \"previous\" links are present if either or both there exists a previous or next page, respectively.  The \"next\" and \"previous\" links have hrefs that allow \"natural movement\" to the next page, that is all parameters  required to move the next page are provided in the link. The \"first\" and \"last\" links provide references to the first and last pages respectively.   Requests outside the boundaries of the pageable will result in a `404 NOT FOUND`. Paginated requests do not provide a  \"stateful cursor\" to the client, nor does it need to provide a read consistent view. Records in adjacent pages may  change while pagination is being traversed, and the total number of pages and resources may change between requests  within the same filtered/queries resource collection.
#### Property Views
The \"depth\" of the response of a resource can be configured using a \"view\". All endpoints supports two views that can  tune the extent of the information returned in the resource. The supported views are `summary` and `details` (the default).  View are specified using a query parameter, in this format:  ```bash /<resource>?view={viewName} ```
#### Error
Any error responses can provide a response body with a message to the client indicating more information (if applicable)  to aid debugging of the error. All 40x and 50x responses will return an error response in the body. The format of the  response is as follows:  ```json {    \"status\": <statusCode>,    \"message\": <message>,    \"links\" : [ {       \"rel\" : \"...\",       \"href\" : \"...\"     } ] }   ```   The `status` property is the same as the HTTP status returned in the response, to ease client parsing. The message  property is a localized message in the request client's locale (if applicable) that articulates the nature of the  error. The last property is the `links` property. This may contain additional  [hypermedia links](#section/Overview/Authentication) to troubleshoot.
#### Search Criteria
<a section=\"section/Responses/SearchCriteria\"></a>  Multiple resources make use of search criteria to match assets. Search criteria is an array of search filters. Each  search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The operator is a type and property-specific operating performed on the filtered property. The valid values for fields and operators are outlined in the table below.  Every filter also defines one or more values that are supplied to the operator. The valid values vary by operator and are outlined below.
##### Fields
The following table outlines the search criteria fields and the available operators:  | Field                             | Operators                                                                                                                      | | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | | `alternate-address-type`          | `in`                                                                                                                           | | `container-image`                 | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is like` ` not like`                              | | `container-status`                | `is` ` is not`                                                                                                                 | | `containers`                      | `are`                                                                                                                          | | `criticality-tag`                 | `is` ` is not` ` is greater than` ` is less than` ` is applied` ` is not applied`                                              | | `custom-tag`                      | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `cve`                             | `is` ` is not` ` contains` ` does not contain`                                                                                 | | `cvss-access-complexity`          | `is` ` is not`                                                                                                                 | | `cvss-authentication-required`    | `is` ` is not`                                                                                                                 | | `cvss-access-vector`              | `is` ` is not`                                                                                                                 | | `cvss-availability-impact`        | `is` ` is not`                                                                                                                 | | `cvss-confidentiality-impact`     | `is` ` is not`                                                                                                                 | | `cvss-integrity-impact`           | `is` ` is not`                                                                                                                 | | `cvss-v3-confidentiality-impact`  | `is` ` is not`                                                                                                                 | | `cvss-v3-integrity-impact`        | `is` ` is not`                                                                                                                 | | `cvss-v3-availability-impact`     | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-vector`           | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-complexity`       | `is` ` is not`                                                                                                                 | | `cvss-v3-user-interaction`        | `is` ` is not`                                                                                                                 | | `cvss-v3-privileges-required`     | `is` ` is not`                                                                                                                 | | `host-name`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is empty` ` is not empty` ` is like` ` not like`  | | `host-type`                       | `in` ` not in`                                                                                                                 | | `ip-address`                      | `is` ` is not` ` in range` ` not in range` ` is like` ` not like`                                                              | | `ip-address-type`                 | `in` ` not in`                                                                                                                 | | `last-scan-date`                  | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `location-tag`                    | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `mobile-device-last-sync-time`    | `is-within-the-last` ` is earlier than`                                                                                        | | `open-ports`                      | `is` ` is not` ` in range`                                                                                                     | | `operating-system`                | `contains` ` does not contain` ` is empty` ` is not empty`                                                                     | | `owner-tag`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `pci-compliance`                  | `is`                                                                                                                           | | `risk-score`                      | `is` ` is not` ` in range` ` greater than` ` less than`                                                                        | | `service-name`                    | `contains` ` does not contain`                                                                                                 | | `site-id`                         | `in` ` not in`                                                                                                                 | | `software`                        | `contains` ` does not contain`                                                                                                 | | `vAsset-cluster`                  | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-datacenter`               | `is` ` is not`                                                                                                                 | | `vAsset-host-name`                | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-power-state`              | `in` ` not in`                                                                                                                 | | `vAsset-resource-pool-path`       | `contains` ` does not contain`                                                                                                 | | `vulnerability-assessed`          | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `vulnerability-category`          | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain`                                                     | | `vulnerability-cvss-v3-score`     | `is` ` is not`                                                                                                                 | | `vulnerability-cvss-score`        | `is` ` is not` ` in range` ` is greater than` ` is less than`                                                                  | | `vulnerability-exposures`         | `includes` ` does not include`                                                                                                 | | `vulnerability-title`             | `contains` ` does not contain` ` is` ` is not` ` starts with` ` ends with`                                                     | | `vulnerability-validated-status`  | `are`                                                                                                                          |
##### Enumerated Properties
The following fields have enumerated values:  | Field                                     | Acceptable Values                                                                                             | | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- | | `alternate-address-type`                  | 0=IPv4, 1=IPv6                                                                                                | | `containers`                              | 0=present, 1=not present                                                                                      | | `container-status`                        | `created` `running` `paused` `restarting` `exited` `dead` `unknown`                                           | | `cvss-access-complexity`                  | <ul><li><code>L</code> = Low</li><li><code>M</code> = Medium</li><li><code>H</code> = High</li></ul>          | | `cvss-integrity-impact`                   | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-confidentiality-impact`             | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-availability-impact`                | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-access-vector`                      | <ul><li><code>L</code> = Local</li><li><code>A</code> = Adjacent</li><li><code>N</code> = Network</li></ul>   | | `cvss-authentication-required`            | <ul><li><code>N</code> = None</li><li><code>S</code> = Single</li><li><code>M</code> = Multiple</li></ul>     | | `cvss-v3-confidentiality-impact`     | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-integrity-impact`            | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-availability-impact`             | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `cvss-v3-attack-vector`                | <ul><li><code>N</code> = Network</li><li><code>A</code> = Adjacent</li><li><code>L</code> = Local</li><li><code>P</code> = Physical</li></ul>    | | `cvss-v3-attack-complexity`                      | <ul><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>   | | `cvss-v3-user-interaction`            | <ul><li><code>N</code> = None</li><li><code>R</code> = Required</li></ul>     | | `cvss-v3-privileges-required`         | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `host-type`                               | 0=Unknown, 1=Guest, 2=Hypervisor, 3=Physical, 4=Mobile                                                        | | `ip-address-type`                         | 0=IPv4, 1=IPv6                                                                                                | | `pci-compliance`                          | 0=fail, 1=pass                                                                                                | | `vulnerability-validated-status`          | 0=present, 1=not present                                                                                      |
##### Operator Properties
<a section=\"section/Responses/SearchCriteria/OperatorProperties\"></a>  The following table outlines which properties are required for each operator and the appropriate data type(s):  | Operator              | `value`               | `lower`               | `upper`               | | ----------------------|-----------------------|-----------------------|-----------------------| | `are`                 | `string`              |                       |                       | | `contains`            | `string`              |                       |                       | | `does-not-contain`    | `string`              |                       |                       | | `ends with`           | `string`              |                       |                       | | `in`                  | `Array[ string ]`     |                       |                       | | `in-range`            |                       | `numeric`             | `numeric`             | | `includes`            | `Array[ string ]`     |                       |                       | | `is`                  | `string`              |                       |                       | | `is-applied`          |                       |                       |                       | | `is-between`          |                       | `numeric`             | `numeric`             | | `is-earlier-than`     | `numeric`             |                       |                       | | `is-empty`            |                       |                       |                       | | `is-greater-than`     | `numeric`             |                       |                       | | `is-on-or-after`      | `string` (yyyy-MM-dd) |                       |                       | | `is-on-or-before`     | `string` (yyyy-MM-dd) |                       |                       | | `is-not`              | `string`              |                       |                       | | `is-not-applied`      |                       |                       |                       | | `is-not-empty`        |                       |                       |                       | | `is-within-the-last`  | `string`              |                       |                       | | `less-than`           | `string`              |                       |                       | | `like`                | `string`              |                       |                       | | `not-contains`        | `string`              |                       |                       | | `not-in`              | `Array[ string ]`     |                       |                       | | `not-in-range`        |                       | `numeric`             | `numeric`             | | `not-like`            | `string`              |                       |                       | | `starts-with`         | `string`              |                       |                       |
#### Discovery Connection Search Criteria
<a section=\"section/Responses/DiscoverySearchCriteria\"></a>  Dynamic sites make use of search criteria to match assets from a discovery connection. Search criteria is an array of search filters.    Each search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The list of supported fields vary depending on the type of discovery connection configured  for the dynamic site (e.g vSphere, ActiveSync, etc.). The operator is a type and property-specific operating  performed on the filtered property. The valid values for fields outlined in the tables below and are grouped by the  type of connection.    Every filter also defines one or more values that are supplied to the operator. See  <a href=\"#section/Responses/SearchCriteria/OperatorProperties\">Search Criteria Operator Properties</a> for more  information on the valid values for each operator.
##### Fields (ActiveSync)
This section documents search criteria information for ActiveSync discovery connections. The discovery connections  must be one of the following types: `\"activesync-ldap\"`, `\"activesync-office365\"`, or `\"activesync-powershell\"`.    The following table outlines the search criteria fields and the available operators for ActiveSync connections:  | Field                             | Operators                                                     | | --------------------------------- | ------------------------------------------------------------- | | `last-sync-time`                  | `is-within-the-last` ` is-earlier-than`                       | | `operating-system`                | `contains` ` does-not-contain`                                | | `user`                            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |
##### Fields (AWS)
This section documents search criteria information for AWS discovery connections. The discovery connections must be the type `\"aws\"`.    The following table outlines the search criteria fields and the available operators for AWS connections:  | Field                   | Operators                                                     | | ----------------------- | ------------------------------------------------------------- | | `availability-zone`     | `contains` ` does-not-contain`                                | | `guest-os-family`       | `contains` ` does-not-contain`                                | | `instance-id`           | `contains` ` does-not-contain`                                | | `instance-name`         | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `instance-state`        | `in` ` not-in`                                                | | `instance-type`         | `in` ` not-in`                                                | | `ip-address`            | `in-range` ` not-in-range` ` is` ` is-not`                    | | `region`                | `in` ` not-in`                                                | | `vpc-id`                | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |
##### Fields (DHCP)
This section documents search criteria information for DHCP discovery connections. The discovery connections must be the type `\"dhcp\"`.    The following table outlines the search criteria fields and the available operators for DHCP connections:  | Field           | Operators                                                     | | --------------- | ------------------------------------------------------------- | | `host-name`     | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `ip-address`    | `in-range` ` not-in-range` ` is` ` is-not`                    | | `mac-address`   | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |
##### Fields (Sonar)
This section documents search criteria information for Sonar discovery connections. The discovery connections must be the type `\"sonar\"`.    The following table outlines the search criteria fields and the available operators for Sonar connections:  | Field               | Operators            | | ------------------- | -------------------- | | `search-domain`     | `contains` ` is`     | | `ip-address`        | `in-range` ` is`     | | `sonar-scan-date`   | `is-within-the-last` |
##### Fields (vSphere)
This section documents search criteria information for vSphere discovery connections. The discovery connections must be the type `\"vsphere\"`.    The following table outlines the search criteria fields and the available operators for vSphere connections:  | Field                | Operators                                                                                  | | -------------------- | ------------------------------------------------------------------------------------------ | | `cluster`            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `data-center`        | `is` ` is-not`                                                                             | | `discovered-time`    | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `guest-os-family`    | `contains` ` does-not-contain`                                                             | | `host-name`          | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `ip-address`         | `in-range` ` not-in-range` ` is` ` is-not`                                                 | | `power-state`        | `in` ` not-in`                                                                             | | `resource-pool-path` | `contains` ` does-not-contain`                                                             | | `last-time-seen`     | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `vm`                 | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              |
##### Enumerated Properties (vSphere)
The following fields have enumerated values:  | Field         | Acceptable Values                    | | ------------- | ------------------------------------ | | `power-state` | `poweredOn` `poweredOff` `suspended` |
## HATEOAS
This API follows Hypermedia as the Engine of Application State (HATEOAS) principals and is therefore hypermedia friendly.  Hyperlinks are returned in the `links` property of any given resource and contain a fully-qualified hyperlink to the corresponding resource. The format of the hypermedia link adheres to both the <a target=\"_blank\" href=\"http://jsonapi.org\">{json:api} v1</a>  <a target=\"_blank\" href=\"http://jsonapi.org/format/#document-links\">\"Link Object\"</a> and  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html\">JSON Hyper-Schema</a>  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html#rfc.section.5.2\">\"Link Description Object\"</a> formats. For example:  ```json \"links\": [{   \"rel\": \"<relation>\",   \"href\": \"<href>\"   ... }] ```  Where appropriate link objects may also contain additional properties than the `rel` and `href` properties, such as `id`, `type`, etc.  See the [Root](#tag/Root) resources for the entry points into API discovery.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3
- Package version: 0.0.1-6.5.4
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/rapid7/vm-console-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/rapid7/vm-console-client-python.git`)

Then import the package:
```python
import rapid7vmconsole
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rapid7vmconsole
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import rapid7vmconsole
from rapid7vmconsole.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = rapid7vmconsole.AdministrationApi()
license = '/path/to/file.txt' # file | The contents of a license (.lic) file. (optional)
key = 'key_example' # str | A license activation key. (optional)

try:
    # License
    api_response = api_instance.activate_license(license=license, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->activate_license: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:3780*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdministrationApi* | [**activate_license**](docs/AdministrationApi.md#activate_license) | **POST** /api/3/administration/license | License
*AdministrationApi* | [**execute_command**](docs/AdministrationApi.md#execute_command) | **POST** /api/3/administration/commands | Console Commands
*AdministrationApi* | [**get_info**](docs/AdministrationApi.md#get_info) | **GET** /api/3/administration/info | Information
*AdministrationApi* | [**get_license**](docs/AdministrationApi.md#get_license) | **GET** /api/3/administration/license | License
*AdministrationApi* | [**get_properties**](docs/AdministrationApi.md#get_properties) | **GET** /api/3/administration/properties | Properties
*AdministrationApi* | [**get_settings**](docs/AdministrationApi.md#get_settings) | **GET** /api/3/administration/settings | Settings
*AssetApi* | [**add_asset_tag**](docs/AssetApi.md#add_asset_tag) | **PUT** /api/3/assets/{id}/tags/{tagId} | Asset Tag
*AssetApi* | [**create_asset**](docs/AssetApi.md#create_asset) | **POST** /api/3/sites/{id}/assets | Assets
*AssetApi* | [**delete_asset**](docs/AssetApi.md#delete_asset) | **DELETE** /api/3/assets/{id} | Asset
*AssetApi* | [**find_assets**](docs/AssetApi.md#find_assets) | **POST** /api/3/assets/search | Asset Search
*AssetApi* | [**get_asset**](docs/AssetApi.md#get_asset) | **GET** /api/3/assets/{id} | Asset
*AssetApi* | [**get_asset_databases**](docs/AssetApi.md#get_asset_databases) | **GET** /api/3/assets/{id}/databases | Asset Databases
*AssetApi* | [**get_asset_files**](docs/AssetApi.md#get_asset_files) | **GET** /api/3/assets/{id}/files | Asset Files
*AssetApi* | [**get_asset_service**](docs/AssetApi.md#get_asset_service) | **GET** /api/3/assets/{id}/services/{protocol}/{port} | Asset Service
*AssetApi* | [**get_asset_service_configurations**](docs/AssetApi.md#get_asset_service_configurations) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/configurations | Asset Service Configurations
*AssetApi* | [**get_asset_service_databases**](docs/AssetApi.md#get_asset_service_databases) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/databases | Asset Service Databases
*AssetApi* | [**get_asset_service_user_groups**](docs/AssetApi.md#get_asset_service_user_groups) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/user_groups | Asset Service User Groups
*AssetApi* | [**get_asset_service_users**](docs/AssetApi.md#get_asset_service_users) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/users | Asset Service Users
*AssetApi* | [**get_asset_service_web_application**](docs/AssetApi.md#get_asset_service_web_application) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/web_applications/{webApplicationId} | Asset Service Web Application
*AssetApi* | [**get_asset_service_web_applications**](docs/AssetApi.md#get_asset_service_web_applications) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/web_applications | Asset Service Web Applications
*AssetApi* | [**get_asset_services**](docs/AssetApi.md#get_asset_services) | **GET** /api/3/assets/{id}/services | Asset Services
*AssetApi* | [**get_asset_software**](docs/AssetApi.md#get_asset_software) | **GET** /api/3/assets/{id}/software | Asset Software
*AssetApi* | [**get_asset_tags**](docs/AssetApi.md#get_asset_tags) | **GET** /api/3/assets/{id}/tags | Asset Tags
*AssetApi* | [**get_asset_user_groups**](docs/AssetApi.md#get_asset_user_groups) | **GET** /api/3/assets/{id}/user_groups | Asset User Groups
*AssetApi* | [**get_asset_users**](docs/AssetApi.md#get_asset_users) | **GET** /api/3/assets/{id}/users | Asset Users
*AssetApi* | [**get_assets**](docs/AssetApi.md#get_assets) | **GET** /api/3/assets | Assets
*AssetApi* | [**get_operating_system**](docs/AssetApi.md#get_operating_system) | **GET** /api/3/operating_systems/{id} | Operating System
*AssetApi* | [**get_operating_systems**](docs/AssetApi.md#get_operating_systems) | **GET** /api/3/operating_systems | Operating Systems
*AssetApi* | [**get_software**](docs/AssetApi.md#get_software) | **GET** /api/3/software/{id} | Software
*AssetApi* | [**get_softwares**](docs/AssetApi.md#get_softwares) | **GET** /api/3/software | Software
*AssetApi* | [**remove_asset_tag**](docs/AssetApi.md#remove_asset_tag) | **DELETE** /api/3/assets/{id}/tags/{tagId} | Asset Tag
*AssetDiscoveryApi* | [**create_sonar_query**](docs/AssetDiscoveryApi.md#create_sonar_query) | **POST** /api/3/sonar_queries | Sonar Queries
*AssetDiscoveryApi* | [**delete_sonar_query**](docs/AssetDiscoveryApi.md#delete_sonar_query) | **DELETE** /api/3/sonar_queries/{id} | Sonar Query
*AssetDiscoveryApi* | [**get_discovery_connection**](docs/AssetDiscoveryApi.md#get_discovery_connection) | **GET** /api/3/discovery_connections/{id} | Discovery Connection
*AssetDiscoveryApi* | [**get_discovery_connections**](docs/AssetDiscoveryApi.md#get_discovery_connections) | **GET** /api/3/discovery_connections | Discovery Connections
*AssetDiscoveryApi* | [**get_sonar_queries**](docs/AssetDiscoveryApi.md#get_sonar_queries) | **GET** /api/3/sonar_queries | Sonar Queries
*AssetDiscoveryApi* | [**get_sonar_query**](docs/AssetDiscoveryApi.md#get_sonar_query) | **GET** /api/3/sonar_queries/{id} | Sonar Query
*AssetDiscoveryApi* | [**get_sonar_query_assets**](docs/AssetDiscoveryApi.md#get_sonar_query_assets) | **GET** /api/3/sonar_queries/{id}/assets | Sonar Query Assets
*AssetDiscoveryApi* | [**reconnect_discovery_connection**](docs/AssetDiscoveryApi.md#reconnect_discovery_connection) | **POST** /api/3/discovery_connections/{id}/connect | Discovery Connection Reconnect
*AssetDiscoveryApi* | [**sonar_query_search**](docs/AssetDiscoveryApi.md#sonar_query_search) | **POST** /api/3/sonar_queries/search | Sonar Query Search
*AssetDiscoveryApi* | [**update_sonar_query**](docs/AssetDiscoveryApi.md#update_sonar_query) | **PUT** /api/3/sonar_queries/{id} | Sonar Query
*AssetGroupApi* | [**add_asset_group_tag**](docs/AssetGroupApi.md#add_asset_group_tag) | **PUT** /api/3/asset_groups/{id}/tags/{tagId} | Asset Group Tag
*AssetGroupApi* | [**add_asset_group_user**](docs/AssetGroupApi.md#add_asset_group_user) | **PUT** /api/3/asset_groups/{id}/users/{userId} | Asset Group User
*AssetGroupApi* | [**add_asset_to_asset_group**](docs/AssetGroupApi.md#add_asset_to_asset_group) | **PUT** /api/3/asset_groups/{id}/assets/{assetId} | Asset Group Asset
*AssetGroupApi* | [**create_asset_group**](docs/AssetGroupApi.md#create_asset_group) | **POST** /api/3/asset_groups | Asset Groups
*AssetGroupApi* | [**delete_asset_group**](docs/AssetGroupApi.md#delete_asset_group) | **DELETE** /api/3/asset_groups/{id} | Asset Group
*AssetGroupApi* | [**get_asset_group**](docs/AssetGroupApi.md#get_asset_group) | **GET** /api/3/asset_groups/{id} | Asset Group
*AssetGroupApi* | [**get_asset_group_assets**](docs/AssetGroupApi.md#get_asset_group_assets) | **GET** /api/3/asset_groups/{id}/assets | Asset Group Assets
*AssetGroupApi* | [**get_asset_group_search_criteria**](docs/AssetGroupApi.md#get_asset_group_search_criteria) | **GET** /api/3/asset_groups/{id}/search_criteria | Asset Group Search Criteria
*AssetGroupApi* | [**get_asset_group_tags**](docs/AssetGroupApi.md#get_asset_group_tags) | **GET** /api/3/asset_groups/{id}/tags | Asset Group Tags
*AssetGroupApi* | [**get_asset_group_users**](docs/AssetGroupApi.md#get_asset_group_users) | **GET** /api/3/asset_groups/{id}/users | Asset Group Users
*AssetGroupApi* | [**get_asset_groups**](docs/AssetGroupApi.md#get_asset_groups) | **GET** /api/3/asset_groups | Asset Groups
*AssetGroupApi* | [**remove_all_asset_group_tags**](docs/AssetGroupApi.md#remove_all_asset_group_tags) | **DELETE** /api/3/asset_groups/{id}/tags | Asset Group Tags
*AssetGroupApi* | [**remove_all_assets_from_asset_group**](docs/AssetGroupApi.md#remove_all_assets_from_asset_group) | **DELETE** /api/3/asset_groups/{id}/assets | Asset Group Assets
*AssetGroupApi* | [**remove_asset_from_asset_group**](docs/AssetGroupApi.md#remove_asset_from_asset_group) | **DELETE** /api/3/asset_groups/{id}/assets/{assetId} | Asset Group Asset
*AssetGroupApi* | [**remove_asset_group_tag**](docs/AssetGroupApi.md#remove_asset_group_tag) | **DELETE** /api/3/asset_groups/{id}/tags/{tagId} | Asset Group Tag
*AssetGroupApi* | [**remove_asset_group_user**](docs/AssetGroupApi.md#remove_asset_group_user) | **DELETE** /api/3/asset_groups/{id}/users/{userId} | Asset Group User
*AssetGroupApi* | [**set_asset_group_search_criteria**](docs/AssetGroupApi.md#set_asset_group_search_criteria) | **PUT** /api/3/asset_groups/{id}/search_criteria | Asset Group Search Criteria
*AssetGroupApi* | [**set_asset_group_tags**](docs/AssetGroupApi.md#set_asset_group_tags) | **PUT** /api/3/asset_groups/{id}/tags | Asset Group Tags
*AssetGroupApi* | [**set_asset_group_users**](docs/AssetGroupApi.md#set_asset_group_users) | **PUT** /api/3/asset_groups/{id}/users | Asset Group Users
*AssetGroupApi* | [**update_asset_group**](docs/AssetGroupApi.md#update_asset_group) | **PUT** /api/3/asset_groups/{id} | Asset Group
*AssetGroupApi* | [**update_asset_group_assets**](docs/AssetGroupApi.md#update_asset_group_assets) | **PUT** /api/3/asset_groups/{id}/assets | Asset Group Assets
*CredentialApi* | [**create_shared_credential**](docs/CredentialApi.md#create_shared_credential) | **POST** /api/3/shared_credentials | Shared Credentials
*CredentialApi* | [**delete_all_shared_credentials**](docs/CredentialApi.md#delete_all_shared_credentials) | **DELETE** /api/3/shared_credentials | Shared Credentials
*CredentialApi* | [**delete_shared_credential**](docs/CredentialApi.md#delete_shared_credential) | **DELETE** /api/3/shared_credentials/{id} | Shared Credential
*CredentialApi* | [**get_shared_credential**](docs/CredentialApi.md#get_shared_credential) | **GET** /api/3/shared_credentials/{id} | Shared Credential
*CredentialApi* | [**get_shared_credentials**](docs/CredentialApi.md#get_shared_credentials) | **GET** /api/3/shared_credentials | Shared Credentials
*CredentialApi* | [**update_shared_credential**](docs/CredentialApi.md#update_shared_credential) | **PUT** /api/3/shared_credentials/{id} | Shared Credential
*PolicyApi* | [**get_asset_policy_children**](docs/PolicyApi.md#get_asset_policy_children) | **GET** /api/3/assets/{assetId}/policies/{policyId}/children | Policy Rules or Groups Directly Under Policy For Asset
*PolicyApi* | [**get_asset_policy_group_children**](docs/PolicyApi.md#get_asset_policy_group_children) | **GET** /api/3/assets/{assetId}/policies/{policyId}/groups/{groupId}/children | Policy Rules or Groups Directly Under Policy Group For Asset
*PolicyApi* | [**get_asset_policy_rules_summary**](docs/PolicyApi.md#get_asset_policy_rules_summary) | **GET** /api/3/assets/{assetId}/policies/{policyId}/rules | Policy Rules For Asset
*PolicyApi* | [**get_descendant_policy_rules**](docs/PolicyApi.md#get_descendant_policy_rules) | **GET** /api/3/policies/{policyId}/groups/{groupId}/rules | Policy Rules Under Policy Group
*PolicyApi* | [**get_disabled_policy_rules**](docs/PolicyApi.md#get_disabled_policy_rules) | **GET** /api/3/policies/{policyId}/rules/disabled | Disabled Policy Rules
*PolicyApi* | [**get_policies**](docs/PolicyApi.md#get_policies) | **GET** /api/3/policies | Policies
*PolicyApi* | [**get_policies_for_asset**](docs/PolicyApi.md#get_policies_for_asset) | **GET** /api/3/assets/{assetId}/policies | Policies For Asset
*PolicyApi* | [**get_policy**](docs/PolicyApi.md#get_policy) | **GET** /api/3/policies/{policyId} | Policy
*PolicyApi* | [**get_policy_asset_result**](docs/PolicyApi.md#get_policy_asset_result) | **GET** /api/3/policies/{policyId}/assets/{assetId} | Policy Asset Result
*PolicyApi* | [**get_policy_asset_results**](docs/PolicyApi.md#get_policy_asset_results) | **GET** /api/3/policies/{policyId}/assets | Policy Asset Results
*PolicyApi* | [**get_policy_children**](docs/PolicyApi.md#get_policy_children) | **GET** /api/3/policies/{id}/children | Policy Rules or Groups Directly Under Policy
*PolicyApi* | [**get_policy_group**](docs/PolicyApi.md#get_policy_group) | **GET** /api/3/policies/{policyId}/groups/{groupId} | Policy Group
*PolicyApi* | [**get_policy_group_asset_result**](docs/PolicyApi.md#get_policy_group_asset_result) | **GET** /api/3/policies/{policyId}/groups/{groupId}/assets/{assetId} | Asset Compliance For Policy Rules Under Policy Group
*PolicyApi* | [**get_policy_group_asset_results**](docs/PolicyApi.md#get_policy_group_asset_results) | **GET** /api/3/policies/{policyId}/groups/{groupId}/assets | Assets Compliance For Policy Rules Under Policy Group
*PolicyApi* | [**get_policy_group_children**](docs/PolicyApi.md#get_policy_group_children) | **GET** /api/3/policies/{policyId}/groups/{groupId}/children | Policy Rules or Groups Directly Under Policy Group
*PolicyApi* | [**get_policy_group_rules_with_asset_assessment**](docs/PolicyApi.md#get_policy_group_rules_with_asset_assessment) | **GET** /api/3/assets/{assetId}/policies/{policyId}/groups/{groupId}/rules | Policy Rules Under Policy Group For Asset
*PolicyApi* | [**get_policy_groups**](docs/PolicyApi.md#get_policy_groups) | **GET** /api/3/policies/{policyId}/groups | Policy Groups
*PolicyApi* | [**get_policy_rule**](docs/PolicyApi.md#get_policy_rule) | **GET** /api/3/policies/{policyId}/rules/{ruleId} | Policy Rule
*PolicyApi* | [**get_policy_rule_asset_result**](docs/PolicyApi.md#get_policy_rule_asset_result) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/assets/{assetId} | Asset Compliance For Policy Rule
*PolicyApi* | [**get_policy_rule_asset_result_proof**](docs/PolicyApi.md#get_policy_rule_asset_result_proof) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/assets/{assetId}/proof | Policy Rule Proof For Asset
*PolicyApi* | [**get_policy_rule_asset_results**](docs/PolicyApi.md#get_policy_rule_asset_results) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/assets | Assets Compliance For Policy Rule
*PolicyApi* | [**get_policy_rule_controls**](docs/PolicyApi.md#get_policy_rule_controls) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/controls | Policy Rule Controls
*PolicyApi* | [**get_policy_rule_rationale**](docs/PolicyApi.md#get_policy_rule_rationale) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/rationale | Policy Rule Rationale
*PolicyApi* | [**get_policy_rule_remediation**](docs/PolicyApi.md#get_policy_rule_remediation) | **GET** /api/3/policies/{policyId}/rules/{ruleId}/remediation | Policy Rule Remediation
*PolicyApi* | [**get_policy_rules**](docs/PolicyApi.md#get_policy_rules) | **GET** /api/3/policies/{policyId}/rules | Policy Rules
*PolicyApi* | [**get_policy_summary**](docs/PolicyApi.md#get_policy_summary) | **GET** /api/3/policy/summary | Policy Compliance Summaries
*PolicyOverrideApi* | [**create_policy_override**](docs/PolicyOverrideApi.md#create_policy_override) | **POST** /api/3/policy_overrides | Policy Overrides
*PolicyOverrideApi* | [**delete_policy_override**](docs/PolicyOverrideApi.md#delete_policy_override) | **DELETE** /api/3/policy_overrides/{id} | Policy Override
*PolicyOverrideApi* | [**get_asset_policy_overrides**](docs/PolicyOverrideApi.md#get_asset_policy_overrides) | **GET** /api/3/assets/{id}/policy_overrides | Asset Policy Overrides
*PolicyOverrideApi* | [**get_policy_override**](docs/PolicyOverrideApi.md#get_policy_override) | **GET** /api/3/policy_overrides/{id} | Policy Override
*PolicyOverrideApi* | [**get_policy_override_expiration**](docs/PolicyOverrideApi.md#get_policy_override_expiration) | **GET** /api/3/policy_overrides/{id}/expires | Policy Override Expiration
*PolicyOverrideApi* | [**get_policy_overrides**](docs/PolicyOverrideApi.md#get_policy_overrides) | **GET** /api/3/policy_overrides | Policy Overrides
*PolicyOverrideApi* | [**set_policy_override_expiration**](docs/PolicyOverrideApi.md#set_policy_override_expiration) | **PUT** /api/3/policy_overrides/{id}/expires | Policy Override Expiration
*PolicyOverrideApi* | [**set_policy_override_status**](docs/PolicyOverrideApi.md#set_policy_override_status) | **POST** /api/3/policy_overrides/{id}/{status} | Policy Override Status
*RemediationApi* | [**get_asset_vulnerability_solutions**](docs/RemediationApi.md#get_asset_vulnerability_solutions) | **GET** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/solution | Asset Vulnerability Solution
*ReportApi* | [**create_report**](docs/ReportApi.md#create_report) | **POST** /api/3/reports | Reports
*ReportApi* | [**delete_report**](docs/ReportApi.md#delete_report) | **DELETE** /api/3/reports/{id} | Report
*ReportApi* | [**delete_report_instance**](docs/ReportApi.md#delete_report_instance) | **DELETE** /api/3/reports/{id}/history/{instance} | Report History
*ReportApi* | [**download_report**](docs/ReportApi.md#download_report) | **GET** /api/3/reports/{id}/history/{instance}/output | Report Download
*ReportApi* | [**generate_report**](docs/ReportApi.md#generate_report) | **POST** /api/3/reports/{id}/generate | Report Generation
*ReportApi* | [**get_report**](docs/ReportApi.md#get_report) | **GET** /api/3/reports/{id} | Report
*ReportApi* | [**get_report_formats**](docs/ReportApi.md#get_report_formats) | **GET** /api/3/report_formats | Report Formats
*ReportApi* | [**get_report_instance**](docs/ReportApi.md#get_report_instance) | **GET** /api/3/reports/{id}/history/{instance} | Report History
*ReportApi* | [**get_report_instances**](docs/ReportApi.md#get_report_instances) | **GET** /api/3/reports/{id}/history | Report Histories
*ReportApi* | [**get_report_template**](docs/ReportApi.md#get_report_template) | **GET** /api/3/report_templates/{id} | Report Template
*ReportApi* | [**get_report_templates**](docs/ReportApi.md#get_report_templates) | **GET** /api/3/report_templates | Report Templates
*ReportApi* | [**get_reports**](docs/ReportApi.md#get_reports) | **GET** /api/3/reports | Reports
*ReportApi* | [**update_report**](docs/ReportApi.md#update_report) | **PUT** /api/3/reports/{id} | Report
*RootApi* | [**resources**](docs/RootApi.md#resources) | **GET** /api/3 | Resources
*ScanApi* | [**get_scan**](docs/ScanApi.md#get_scan) | **GET** /api/3/scans/{id} | Scan
*ScanApi* | [**get_scans**](docs/ScanApi.md#get_scans) | **GET** /api/3/scans | Scans
*ScanApi* | [**get_site_scans**](docs/ScanApi.md#get_site_scans) | **GET** /api/3/sites/{id}/scans | Site Scans
*ScanApi* | [**set_scan_status**](docs/ScanApi.md#set_scan_status) | **POST** /api/3/scans/{id}/{status} | Scan Status
*ScanApi* | [**start_scan**](docs/ScanApi.md#start_scan) | **POST** /api/3/sites/{id}/scans | Site Scans
*ScanEngineApi* | [**add_scan_engine_pool_scan_engine**](docs/ScanEngineApi.md#add_scan_engine_pool_scan_engine) | **PUT** /api/3/scan_engine_pools/{id}/engines/{engineId} | Engine Pool Engines
*ScanEngineApi* | [**create_scan_engine**](docs/ScanEngineApi.md#create_scan_engine) | **POST** /api/3/scan_engines | Scan Engines
*ScanEngineApi* | [**create_scan_engine_pool**](docs/ScanEngineApi.md#create_scan_engine_pool) | **POST** /api/3/scan_engine_pools | Engine Pools
*ScanEngineApi* | [**delete_scan_engine**](docs/ScanEngineApi.md#delete_scan_engine) | **DELETE** /api/3/scan_engines/{id} | Scan Engine
*ScanEngineApi* | [**get_assigned_engine_pools**](docs/ScanEngineApi.md#get_assigned_engine_pools) | **GET** /api/3/scan_engines/{id}/scan_engine_pools | Assigned Engine Pools
*ScanEngineApi* | [**get_engine_pool**](docs/ScanEngineApi.md#get_engine_pool) | **GET** /api/3/scan_engine_pools/{id} | Engine Pool
*ScanEngineApi* | [**get_scan_engine**](docs/ScanEngineApi.md#get_scan_engine) | **GET** /api/3/scan_engines/{id} | Scan Engine
*ScanEngineApi* | [**get_scan_engine_pool_scan_engines**](docs/ScanEngineApi.md#get_scan_engine_pool_scan_engines) | **GET** /api/3/scan_engine_pools/{id}/engines | Engine Pool Engines
*ScanEngineApi* | [**get_scan_engine_pool_sites**](docs/ScanEngineApi.md#get_scan_engine_pool_sites) | **GET** /api/3/scan_engine_pools/{id}/sites | Engine Pool Sites
*ScanEngineApi* | [**get_scan_engine_pools**](docs/ScanEngineApi.md#get_scan_engine_pools) | **GET** /api/3/scan_engine_pools | Engine Pools
*ScanEngineApi* | [**get_scan_engine_scans**](docs/ScanEngineApi.md#get_scan_engine_scans) | **GET** /api/3/scan_engines/{id}/scans | Scan Engine Scans
*ScanEngineApi* | [**get_scan_engine_sites**](docs/ScanEngineApi.md#get_scan_engine_sites) | **GET** /api/3/scan_engines/{id}/sites | Scan Engine Sites
*ScanEngineApi* | [**get_scan_engines**](docs/ScanEngineApi.md#get_scan_engines) | **GET** /api/3/scan_engines | Scan Engines
*ScanEngineApi* | [**remove_scan_engine_pool**](docs/ScanEngineApi.md#remove_scan_engine_pool) | **DELETE** /api/3/scan_engine_pools/{id} | Engine Pool
*ScanEngineApi* | [**remove_scan_engine_pool_scan_engine**](docs/ScanEngineApi.md#remove_scan_engine_pool_scan_engine) | **DELETE** /api/3/scan_engine_pools/{id}/engines/{engineId} | Engine Pool Engines
*ScanEngineApi* | [**set_scan_engine_pool_scan_engines**](docs/ScanEngineApi.md#set_scan_engine_pool_scan_engines) | **PUT** /api/3/scan_engine_pools/{id}/engines | Engine Pool Engines
*ScanEngineApi* | [**update_scan_engine**](docs/ScanEngineApi.md#update_scan_engine) | **PUT** /api/3/scan_engines/{id} | Scan Engine
*ScanEngineApi* | [**update_scan_engine_pool**](docs/ScanEngineApi.md#update_scan_engine_pool) | **PUT** /api/3/scan_engine_pools/{id} | Engine Pool
*ScanTemplateApi* | [**create_scan_template**](docs/ScanTemplateApi.md#create_scan_template) | **POST** /api/3/scan_templates | Scan Templates
*ScanTemplateApi* | [**delete_scan_template**](docs/ScanTemplateApi.md#delete_scan_template) | **DELETE** /api/3/scan_templates/{id} | Scan Template
*ScanTemplateApi* | [**get_scan_template**](docs/ScanTemplateApi.md#get_scan_template) | **GET** /api/3/scan_templates/{id} | Scan Template
*ScanTemplateApi* | [**get_scan_templates**](docs/ScanTemplateApi.md#get_scan_templates) | **GET** /api/3/scan_templates | Scan Templates
*ScanTemplateApi* | [**update_scan_template**](docs/ScanTemplateApi.md#update_scan_template) | **PUT** /api/3/scan_templates/{id} | Scan Template
*SiteApi* | [**add_site_tag**](docs/SiteApi.md#add_site_tag) | **PUT** /api/3/sites/{id}/tags/{tagId} | Site Tag
*SiteApi* | [**add_site_user**](docs/SiteApi.md#add_site_user) | **POST** /api/3/sites/{id}/users | Site Users Access
*SiteApi* | [**create_site**](docs/SiteApi.md#create_site) | **POST** /api/3/sites | Sites
*SiteApi* | [**create_site_credential**](docs/SiteApi.md#create_site_credential) | **POST** /api/3/sites/{id}/site_credentials | Site Scan Credentials
*SiteApi* | [**create_site_scan_schedule**](docs/SiteApi.md#create_site_scan_schedule) | **POST** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
*SiteApi* | [**create_site_smtp_alert**](docs/SiteApi.md#create_site_smtp_alert) | **POST** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
*SiteApi* | [**create_site_snmp_alert**](docs/SiteApi.md#create_site_snmp_alert) | **POST** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
*SiteApi* | [**create_site_syslog_alert**](docs/SiteApi.md#create_site_syslog_alert) | **POST** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
*SiteApi* | [**delete_all_site_alerts**](docs/SiteApi.md#delete_all_site_alerts) | **DELETE** /api/3/sites/{id}/alerts | Site Alerts
*SiteApi* | [**delete_all_site_credentials**](docs/SiteApi.md#delete_all_site_credentials) | **DELETE** /api/3/sites/{id}/site_credentials | Site Scan Credentials
*SiteApi* | [**delete_all_site_scan_schedules**](docs/SiteApi.md#delete_all_site_scan_schedules) | **DELETE** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
*SiteApi* | [**delete_all_site_smtp_alerts**](docs/SiteApi.md#delete_all_site_smtp_alerts) | **DELETE** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
*SiteApi* | [**delete_all_site_snmp_alerts**](docs/SiteApi.md#delete_all_site_snmp_alerts) | **DELETE** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
*SiteApi* | [**delete_all_site_syslog_alerts**](docs/SiteApi.md#delete_all_site_syslog_alerts) | **DELETE** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
*SiteApi* | [**delete_site**](docs/SiteApi.md#delete_site) | **DELETE** /api/3/sites/{id} | Site
*SiteApi* | [**delete_site_credential**](docs/SiteApi.md#delete_site_credential) | **DELETE** /api/3/sites/{id}/site_credentials/{credentialId} | Site Scan Credential
*SiteApi* | [**delete_site_scan_schedule**](docs/SiteApi.md#delete_site_scan_schedule) | **DELETE** /api/3/sites/{id}/scan_schedules/{scheduleId} | Site Scan Schedule
*SiteApi* | [**delete_site_smtp_alert**](docs/SiteApi.md#delete_site_smtp_alert) | **DELETE** /api/3/sites/{id}/alerts/smtp/{alertId} | Site SMTP Alert
*SiteApi* | [**delete_site_snmp_alert**](docs/SiteApi.md#delete_site_snmp_alert) | **DELETE** /api/3/sites/{id}/alerts/snmp/{alertId} | Site SNMP Alert
*SiteApi* | [**delete_site_syslog_alert**](docs/SiteApi.md#delete_site_syslog_alert) | **DELETE** /api/3/sites/{id}/alerts/syslog/{alertId} | Site Syslog Alert
*SiteApi* | [**enable_shared_credential_on_site**](docs/SiteApi.md#enable_shared_credential_on_site) | **PUT** /api/3/sites/{id}/shared_credentials/{credentialId}/enabled | Assigned Shared Credential Enablement
*SiteApi* | [**enable_site_credential**](docs/SiteApi.md#enable_site_credential) | **PUT** /api/3/sites/{id}/site_credentials/{credentialId}/enabled | Site Credential Enablement
*SiteApi* | [**get_excluded_asset_groups**](docs/SiteApi.md#get_excluded_asset_groups) | **GET** /api/3/sites/{id}/excluded_asset_groups | Site Excluded Asset Groups
*SiteApi* | [**get_excluded_targets**](docs/SiteApi.md#get_excluded_targets) | **GET** /api/3/sites/{id}/excluded_targets | Site Excluded Targets
*SiteApi* | [**get_included_asset_groups**](docs/SiteApi.md#get_included_asset_groups) | **GET** /api/3/sites/{id}/included_asset_groups | Site Included Asset Groups
*SiteApi* | [**get_included_targets**](docs/SiteApi.md#get_included_targets) | **GET** /api/3/sites/{id}/included_targets | Site Included Targets
*SiteApi* | [**get_site**](docs/SiteApi.md#get_site) | **GET** /api/3/sites/{id} | Site
*SiteApi* | [**get_site_alerts**](docs/SiteApi.md#get_site_alerts) | **GET** /api/3/sites/{id}/alerts | Site Alerts
*SiteApi* | [**get_site_assets**](docs/SiteApi.md#get_site_assets) | **GET** /api/3/sites/{id}/assets | Site Assets
*SiteApi* | [**get_site_credential**](docs/SiteApi.md#get_site_credential) | **GET** /api/3/sites/{id}/site_credentials/{credentialId} | Site Scan Credential
*SiteApi* | [**get_site_credentials**](docs/SiteApi.md#get_site_credentials) | **GET** /api/3/sites/{id}/site_credentials | Site Scan Credentials
*SiteApi* | [**get_site_discovery_connection**](docs/SiteApi.md#get_site_discovery_connection) | **GET** /api/3/sites/{id}/discovery_connection | Site Discovery Connection
*SiteApi* | [**get_site_discovery_search_criteria**](docs/SiteApi.md#get_site_discovery_search_criteria) | **GET** /api/3/sites/{id}/discovery_search_criteria | Site Discovery Search Criteria
*SiteApi* | [**get_site_organization**](docs/SiteApi.md#get_site_organization) | **GET** /api/3/sites/{id}/organization | Site Organization Information
*SiteApi* | [**get_site_scan_engine**](docs/SiteApi.md#get_site_scan_engine) | **GET** /api/3/sites/{id}/scan_engine | Site Scan Engine
*SiteApi* | [**get_site_scan_schedule**](docs/SiteApi.md#get_site_scan_schedule) | **GET** /api/3/sites/{id}/scan_schedules/{scheduleId} | Site Scan Schedule
*SiteApi* | [**get_site_scan_schedules**](docs/SiteApi.md#get_site_scan_schedules) | **GET** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
*SiteApi* | [**get_site_scan_template**](docs/SiteApi.md#get_site_scan_template) | **GET** /api/3/sites/{id}/scan_template | Site Scan Template
*SiteApi* | [**get_site_shared_credentials**](docs/SiteApi.md#get_site_shared_credentials) | **GET** /api/3/sites/{id}/shared_credentials | Assigned Shared Credentials
*SiteApi* | [**get_site_smtp_alert**](docs/SiteApi.md#get_site_smtp_alert) | **GET** /api/3/sites/{id}/alerts/smtp/{alertId} | Site SMTP Alert
*SiteApi* | [**get_site_smtp_alerts**](docs/SiteApi.md#get_site_smtp_alerts) | **GET** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
*SiteApi* | [**get_site_snmp_alert**](docs/SiteApi.md#get_site_snmp_alert) | **GET** /api/3/sites/{id}/alerts/snmp/{alertId} | Site SNMP Alert
*SiteApi* | [**get_site_snmp_alerts**](docs/SiteApi.md#get_site_snmp_alerts) | **GET** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
*SiteApi* | [**get_site_syslog_alert**](docs/SiteApi.md#get_site_syslog_alert) | **GET** /api/3/sites/{id}/alerts/syslog/{alertId} | Site Syslog Alert
*SiteApi* | [**get_site_syslog_alerts**](docs/SiteApi.md#get_site_syslog_alerts) | **GET** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
*SiteApi* | [**get_site_tags**](docs/SiteApi.md#get_site_tags) | **GET** /api/3/sites/{id}/tags | Site Tags
*SiteApi* | [**get_site_users**](docs/SiteApi.md#get_site_users) | **GET** /api/3/sites/{id}/users | Site Users Access
*SiteApi* | [**get_sites**](docs/SiteApi.md#get_sites) | **GET** /api/3/sites | Sites
*SiteApi* | [**get_web_auth_html_forms**](docs/SiteApi.md#get_web_auth_html_forms) | **GET** /api/3/sites/{id}/web_authentication/html_forms | Web Authentication HTML Forms
*SiteApi* | [**get_web_auth_http_headers**](docs/SiteApi.md#get_web_auth_http_headers) | **GET** /api/3/sites/{id}/web_authentication/http_headers | Web Authentication HTTP Headers
*SiteApi* | [**remove_all_excluded_asset_groups**](docs/SiteApi.md#remove_all_excluded_asset_groups) | **DELETE** /api/3/sites/{id}/excluded_asset_groups | Site Excluded Asset Groups
*SiteApi* | [**remove_all_included_asset_groups**](docs/SiteApi.md#remove_all_included_asset_groups) | **DELETE** /api/3/sites/{id}/included_asset_groups | Site Included Asset Groups
*SiteApi* | [**remove_asset_from_site**](docs/SiteApi.md#remove_asset_from_site) | **DELETE** /api/3/sites/{id}/assets/{assetId} | Site Asset
*SiteApi* | [**remove_excluded_asset_group**](docs/SiteApi.md#remove_excluded_asset_group) | **DELETE** /api/3/sites/{id}/excluded_asset_groups/{assetGroupId} | Site Excluded Asset Group
*SiteApi* | [**remove_included_asset_group**](docs/SiteApi.md#remove_included_asset_group) | **DELETE** /api/3/sites/{id}/included_asset_groups/{assetGroupId} | Site Included Asset Group
*SiteApi* | [**remove_site_assets**](docs/SiteApi.md#remove_site_assets) | **DELETE** /api/3/sites/{id}/assets | Site Assets
*SiteApi* | [**remove_site_tag**](docs/SiteApi.md#remove_site_tag) | **DELETE** /api/3/sites/{id}/tags/{tagId} | Site Tag
*SiteApi* | [**remove_site_user**](docs/SiteApi.md#remove_site_user) | **DELETE** /api/3/sites/{id}/users/{userId} | Site User Access
*SiteApi* | [**set_site_credentials**](docs/SiteApi.md#set_site_credentials) | **PUT** /api/3/sites/{id}/site_credentials | Site Scan Credentials
*SiteApi* | [**set_site_discovery_connection**](docs/SiteApi.md#set_site_discovery_connection) | **PUT** /api/3/sites/{id}/discovery_connection | Site Discovery Connection
*SiteApi* | [**set_site_discovery_search_criteria**](docs/SiteApi.md#set_site_discovery_search_criteria) | **PUT** /api/3/sites/{id}/discovery_search_criteria | Site Discovery Search Criteria
*SiteApi* | [**set_site_scan_engine**](docs/SiteApi.md#set_site_scan_engine) | **PUT** /api/3/sites/{id}/scan_engine | Site Scan Engine
*SiteApi* | [**set_site_scan_schedules**](docs/SiteApi.md#set_site_scan_schedules) | **PUT** /api/3/sites/{id}/scan_schedules | Site Scan Schedules
*SiteApi* | [**set_site_scan_template**](docs/SiteApi.md#set_site_scan_template) | **PUT** /api/3/sites/{id}/scan_template | Site Scan Template
*SiteApi* | [**set_site_smtp_alerts**](docs/SiteApi.md#set_site_smtp_alerts) | **PUT** /api/3/sites/{id}/alerts/smtp | Site SMTP Alerts
*SiteApi* | [**set_site_snmp_alerts**](docs/SiteApi.md#set_site_snmp_alerts) | **PUT** /api/3/sites/{id}/alerts/snmp | Site SNMP Alerts
*SiteApi* | [**set_site_syslog_alerts**](docs/SiteApi.md#set_site_syslog_alerts) | **PUT** /api/3/sites/{id}/alerts/syslog | Site Syslog Alerts
*SiteApi* | [**set_site_tags**](docs/SiteApi.md#set_site_tags) | **PUT** /api/3/sites/{id}/tags | Site Tags
*SiteApi* | [**set_site_users**](docs/SiteApi.md#set_site_users) | **PUT** /api/3/sites/{id}/users | Site Users Access
*SiteApi* | [**update_excluded_asset_groups**](docs/SiteApi.md#update_excluded_asset_groups) | **PUT** /api/3/sites/{id}/excluded_asset_groups | Site Excluded Asset Groups
*SiteApi* | [**update_excluded_targets**](docs/SiteApi.md#update_excluded_targets) | **PUT** /api/3/sites/{id}/excluded_targets | Site Excluded Targets
*SiteApi* | [**update_included_asset_groups**](docs/SiteApi.md#update_included_asset_groups) | **PUT** /api/3/sites/{id}/included_asset_groups | Site Included Asset Groups
*SiteApi* | [**update_included_targets**](docs/SiteApi.md#update_included_targets) | **PUT** /api/3/sites/{id}/included_targets | Site Included Targets
*SiteApi* | [**update_site**](docs/SiteApi.md#update_site) | **PUT** /api/3/sites/{id} | Site
*SiteApi* | [**update_site_credential**](docs/SiteApi.md#update_site_credential) | **PUT** /api/3/sites/{id}/site_credentials/{credentialId} | Site Scan Credential
*SiteApi* | [**update_site_organization**](docs/SiteApi.md#update_site_organization) | **PUT** /api/3/sites/{id}/organization | Site Organization Information
*SiteApi* | [**update_site_scan_schedule**](docs/SiteApi.md#update_site_scan_schedule) | **PUT** /api/3/sites/{id}/scan_schedules/{scheduleId} | Site Scan Schedule
*SiteApi* | [**update_site_smtp_alert**](docs/SiteApi.md#update_site_smtp_alert) | **PUT** /api/3/sites/{id}/alerts/smtp/{alertId} | Site SMTP Alert
*SiteApi* | [**update_site_snmp_alert**](docs/SiteApi.md#update_site_snmp_alert) | **PUT** /api/3/sites/{id}/alerts/snmp/{alertId} | Site SNMP Alert
*SiteApi* | [**update_site_syslog_alert**](docs/SiteApi.md#update_site_syslog_alert) | **PUT** /api/3/sites/{id}/alerts/syslog/{alertId} | Site Syslog Alert
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /api/3/tags | Tags
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /api/3/tags/{id} | Tag
*TagApi* | [**get_tag**](docs/TagApi.md#get_tag) | **GET** /api/3/tags/{id} | Tag
*TagApi* | [**get_tag_asset_groups**](docs/TagApi.md#get_tag_asset_groups) | **GET** /api/3/tags/{id}/asset_groups | Tag Asset Groups
*TagApi* | [**get_tag_search_criteria**](docs/TagApi.md#get_tag_search_criteria) | **GET** /api/3/tags/{id}/search_criteria | Tag Search Criteria
*TagApi* | [**get_tagged_assets**](docs/TagApi.md#get_tagged_assets) | **GET** /api/3/tags/{id}/assets | Tag Assets
*TagApi* | [**get_tagged_sites**](docs/TagApi.md#get_tagged_sites) | **GET** /api/3/tags/{id}/sites | Tag Sites
*TagApi* | [**get_tags**](docs/TagApi.md#get_tags) | **GET** /api/3/tags | Tags
*TagApi* | [**remove_tag_search_criteria**](docs/TagApi.md#remove_tag_search_criteria) | **DELETE** /api/3/tags/{id}/search_criteria | Tag Search Criteria
*TagApi* | [**remove_tagged_sites**](docs/TagApi.md#remove_tagged_sites) | **DELETE** /api/3/tags/{id}/sites | Tag Sites
*TagApi* | [**set_tagged_asset_groups**](docs/TagApi.md#set_tagged_asset_groups) | **PUT** /api/3/tags/{id}/asset_groups | Tag Asset Groups
*TagApi* | [**set_tagged_sites**](docs/TagApi.md#set_tagged_sites) | **PUT** /api/3/tags/{id}/sites | Tag Sites
*TagApi* | [**tag_asset**](docs/TagApi.md#tag_asset) | **PUT** /api/3/tags/{id}/assets/{assetId} | Tag Asset
*TagApi* | [**tag_asset_group**](docs/TagApi.md#tag_asset_group) | **PUT** /api/3/tags/{id}/asset_groups/{assetGroupId} | Tag Asset Group
*TagApi* | [**tag_site**](docs/TagApi.md#tag_site) | **PUT** /api/3/tags/{id}/sites/{siteId} | Tag Site
*TagApi* | [**untag_all_asset_groups**](docs/TagApi.md#untag_all_asset_groups) | **DELETE** /api/3/tags/{id}/asset_groups | Tag Asset Groups
*TagApi* | [**untag_asset**](docs/TagApi.md#untag_asset) | **DELETE** /api/3/tags/{id}/assets/{assetId} | Tag Asset
*TagApi* | [**untag_asset_group**](docs/TagApi.md#untag_asset_group) | **DELETE** /api/3/tags/{id}/asset_groups/{assetGroupId} | Tag Asset Group
*TagApi* | [**untag_site**](docs/TagApi.md#untag_site) | **DELETE** /api/3/tags/{id}/sites/{siteId} | Tag Site
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **PUT** /api/3/tags/{id} | Tag
*TagApi* | [**update_tag_search_criteria**](docs/TagApi.md#update_tag_search_criteria) | **PUT** /api/3/tags/{id}/search_criteria | Tag Search Criteria
*UserApi* | [**add_user_asset_group**](docs/UserApi.md#add_user_asset_group) | **PUT** /api/3/users/{id}/asset_groups/{assetGroupId} | Asset Group Access
*UserApi* | [**add_user_site**](docs/UserApi.md#add_user_site) | **PUT** /api/3/users/{id}/sites/{siteId} | Site Access
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /api/3/users | Users
*UserApi* | [**delete_role**](docs/UserApi.md#delete_role) | **DELETE** /api/3/roles/{id} | Role
*UserApi* | [**get_authentication_source**](docs/UserApi.md#get_authentication_source) | **GET** /api/3/authentication_sources/{id} | Authentication Source
*UserApi* | [**get_authentication_source_users**](docs/UserApi.md#get_authentication_source_users) | **GET** /api/3/authentication_sources/{id}/users | Authentication Source Users
*UserApi* | [**get_authentication_sources**](docs/UserApi.md#get_authentication_sources) | **GET** /api/3/authentication_sources | Authentication Sources
*UserApi* | [**get_privilege**](docs/UserApi.md#get_privilege) | **GET** /api/3/privileges/{id} | Privilege
*UserApi* | [**get_privileges**](docs/UserApi.md#get_privileges) | **GET** /api/3/privileges | Privileges
*UserApi* | [**get_role**](docs/UserApi.md#get_role) | **GET** /api/3/roles/{id} | Role
*UserApi* | [**get_role_users**](docs/UserApi.md#get_role_users) | **GET** /api/3/roles/{id}/users | Users With Role
*UserApi* | [**get_roles**](docs/UserApi.md#get_roles) | **GET** /api/3/roles | Roles
*UserApi* | [**get_two_factor_authentication_key**](docs/UserApi.md#get_two_factor_authentication_key) | **GET** /api/3/users/{id}/2FA | Two-Factor Authentication
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /api/3/users/{id} | User
*UserApi* | [**get_user_asset_groups**](docs/UserApi.md#get_user_asset_groups) | **GET** /api/3/users/{id}/asset_groups | Asset Groups Access
*UserApi* | [**get_user_privileges**](docs/UserApi.md#get_user_privileges) | **GET** /api/3/users/{id}/privileges | User Privileges
*UserApi* | [**get_user_sites**](docs/UserApi.md#get_user_sites) | **GET** /api/3/users/{id}/sites | Sites Access
*UserApi* | [**get_users**](docs/UserApi.md#get_users) | **GET** /api/3/users | Users
*UserApi* | [**get_users_with_privilege**](docs/UserApi.md#get_users_with_privilege) | **GET** /api/3/privileges/{id}/users | Users With Privilege
*UserApi* | [**regenerate_two_factor_authentication**](docs/UserApi.md#regenerate_two_factor_authentication) | **POST** /api/3/users/{id}/2FA | Two-Factor Authentication
*UserApi* | [**remove_all_user_asset_groups**](docs/UserApi.md#remove_all_user_asset_groups) | **DELETE** /api/3/users/{id}/asset_groups | Asset Groups Access
*UserApi* | [**remove_all_user_sites**](docs/UserApi.md#remove_all_user_sites) | **DELETE** /api/3/users/{id}/sites | Sites Access
*UserApi* | [**remove_user_asset_group**](docs/UserApi.md#remove_user_asset_group) | **DELETE** /api/3/users/{id}/asset_groups/{assetGroupId} | Asset Group Access
*UserApi* | [**remove_user_site**](docs/UserApi.md#remove_user_site) | **DELETE** /api/3/users/{id}/sites/{siteId} | Site Access
*UserApi* | [**reset_password**](docs/UserApi.md#reset_password) | **PUT** /api/3/users/{id}/password | Password Reset
*UserApi* | [**set_two_factor_authentication**](docs/UserApi.md#set_two_factor_authentication) | **PUT** /api/3/users/{id}/2FA | Two-Factor Authentication
*UserApi* | [**set_user_asset_groups**](docs/UserApi.md#set_user_asset_groups) | **PUT** /api/3/users/{id}/asset_groups | Asset Groups Access
*UserApi* | [**set_user_sites**](docs/UserApi.md#set_user_sites) | **PUT** /api/3/users/{id}/sites | Sites Access
*UserApi* | [**unlock_user**](docs/UserApi.md#unlock_user) | **DELETE** /api/3/users/{id}/lock | Unlock Account
*UserApi* | [**update_role**](docs/UserApi.md#update_role) | **PUT** /api/3/roles/{id} | Role
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /api/3/users/{id} | User
*VulnerabilityApi* | [**get_affected_assets**](docs/VulnerabilityApi.md#get_affected_assets) | **GET** /api/3/vulnerabilities/{id}/assets | Vulnerability Affected Assets
*VulnerabilityApi* | [**get_exploit**](docs/VulnerabilityApi.md#get_exploit) | **GET** /api/3/exploits/{id} | Exploit
*VulnerabilityApi* | [**get_exploit_vulnerabilities**](docs/VulnerabilityApi.md#get_exploit_vulnerabilities) | **GET** /api/3/exploits/{id}/vulnerabilities | Exploitable Vulnerabilities
*VulnerabilityApi* | [**get_exploits**](docs/VulnerabilityApi.md#get_exploits) | **GET** /api/3/exploits | Exploits
*VulnerabilityApi* | [**get_malware_kit**](docs/VulnerabilityApi.md#get_malware_kit) | **GET** /api/3/malware_kits/{id} | Malware Kit
*VulnerabilityApi* | [**get_malware_kit_vulnerabilities**](docs/VulnerabilityApi.md#get_malware_kit_vulnerabilities) | **GET** /api/3/malware_kits/{id}/vulnerabilities | Malware Kit Vulnerabilities
*VulnerabilityApi* | [**get_malware_kits**](docs/VulnerabilityApi.md#get_malware_kits) | **GET** /api/3/malware_kits | Malware Kits
*VulnerabilityApi* | [**get_prerequisite_solutions**](docs/VulnerabilityApi.md#get_prerequisite_solutions) | **GET** /api/3/solutions/{id}/prerequisites | Solution Prerequisites
*VulnerabilityApi* | [**get_solution**](docs/VulnerabilityApi.md#get_solution) | **GET** /api/3/solutions/{id} | Solution
*VulnerabilityApi* | [**get_solutions**](docs/VulnerabilityApi.md#get_solutions) | **GET** /api/3/solutions | Solutions
*VulnerabilityApi* | [**get_superseded_solutions**](docs/VulnerabilityApi.md#get_superseded_solutions) | **GET** /api/3/solutions/{id}/supersedes | Superseded Solutions
*VulnerabilityApi* | [**get_superseding_solutions**](docs/VulnerabilityApi.md#get_superseding_solutions) | **GET** /api/3/solutions/{id}/superseding | Superseding Solutions
*VulnerabilityApi* | [**get_vulnerabilities**](docs/VulnerabilityApi.md#get_vulnerabilities) | **GET** /api/3/vulnerabilities | Vulnerabilities
*VulnerabilityApi* | [**get_vulnerability**](docs/VulnerabilityApi.md#get_vulnerability) | **GET** /api/3/vulnerabilities/{id} | Vulnerability
*VulnerabilityApi* | [**get_vulnerability_categories**](docs/VulnerabilityApi.md#get_vulnerability_categories) | **GET** /api/3/vulnerability_categories | Categories
*VulnerabilityApi* | [**get_vulnerability_category**](docs/VulnerabilityApi.md#get_vulnerability_category) | **GET** /api/3/vulnerability_categories/{id} | Category
*VulnerabilityApi* | [**get_vulnerability_category_vulnerabilities**](docs/VulnerabilityApi.md#get_vulnerability_category_vulnerabilities) | **GET** /api/3/vulnerability_categories/{id}/vulnerabilities | Category Vulnerabilities
*VulnerabilityApi* | [**get_vulnerability_exploits**](docs/VulnerabilityApi.md#get_vulnerability_exploits) | **GET** /api/3/vulnerabilities/{id}/exploits | Vulnerability Exploits
*VulnerabilityApi* | [**get_vulnerability_malware_kits**](docs/VulnerabilityApi.md#get_vulnerability_malware_kits) | **GET** /api/3/vulnerabilities/{id}/malware_kits | Vulnerability Malware Kits
*VulnerabilityApi* | [**get_vulnerability_reference**](docs/VulnerabilityApi.md#get_vulnerability_reference) | **GET** /api/3/vulnerability_references/{id} | Reference
*VulnerabilityApi* | [**get_vulnerability_reference_vulnerabilities**](docs/VulnerabilityApi.md#get_vulnerability_reference_vulnerabilities) | **GET** /api/3/vulnerability_references/{id}/vulnerabilities | Reference Vulnerabilities
*VulnerabilityApi* | [**get_vulnerability_references**](docs/VulnerabilityApi.md#get_vulnerability_references) | **GET** /api/3/vulnerability_references | References
*VulnerabilityApi* | [**get_vulnerability_references1**](docs/VulnerabilityApi.md#get_vulnerability_references1) | **GET** /api/3/vulnerabilities/{id}/references | Vulnerability References
*VulnerabilityApi* | [**get_vulnerability_solutions**](docs/VulnerabilityApi.md#get_vulnerability_solutions) | **GET** /api/3/vulnerabilities/{id}/solutions | Vulnerability Solutions
*VulnerabilityCheckApi* | [**get_vulnerability_check_types**](docs/VulnerabilityCheckApi.md#get_vulnerability_check_types) | **GET** /api/3/vulnerability_checks_types | Check Types
*VulnerabilityCheckApi* | [**get_vulnerability_checks**](docs/VulnerabilityCheckApi.md#get_vulnerability_checks) | **GET** /api/3/vulnerability_checks | Checks
*VulnerabilityCheckApi* | [**get_vulnerability_checks_for_vulnerability**](docs/VulnerabilityCheckApi.md#get_vulnerability_checks_for_vulnerability) | **GET** /api/3/vulnerabilities/{id}/checks | Vulnerability Checks
*VulnerabilityCheckApi* | [**vulnerability_check**](docs/VulnerabilityCheckApi.md#vulnerability_check) | **GET** /api/3/vulnerability_checks/{id} | Check
*VulnerabilityExceptionApi* | [**create_vulnerability_exception**](docs/VulnerabilityExceptionApi.md#create_vulnerability_exception) | **POST** /api/3/vulnerability_exceptions | Exceptions
*VulnerabilityExceptionApi* | [**get_vulnerability_exception**](docs/VulnerabilityExceptionApi.md#get_vulnerability_exception) | **GET** /api/3/vulnerability_exceptions/{id} | Exception
*VulnerabilityExceptionApi* | [**get_vulnerability_exception_expiration**](docs/VulnerabilityExceptionApi.md#get_vulnerability_exception_expiration) | **GET** /api/3/vulnerability_exceptions/{id}/expires | Exception Expiration
*VulnerabilityExceptionApi* | [**get_vulnerability_exceptions**](docs/VulnerabilityExceptionApi.md#get_vulnerability_exceptions) | **GET** /api/3/vulnerability_exceptions | Exceptions
*VulnerabilityExceptionApi* | [**remove_vulnerability_exception**](docs/VulnerabilityExceptionApi.md#remove_vulnerability_exception) | **DELETE** /api/3/vulnerability_exceptions/{id} | Exception
*VulnerabilityExceptionApi* | [**update_vulnerability_exception_expiration**](docs/VulnerabilityExceptionApi.md#update_vulnerability_exception_expiration) | **PUT** /api/3/vulnerability_exceptions/{id}/expires | Exception Expiration
*VulnerabilityExceptionApi* | [**update_vulnerability_exception_status**](docs/VulnerabilityExceptionApi.md#update_vulnerability_exception_status) | **POST** /api/3/vulnerability_exceptions/{id}/{status} | Exception Status
*VulnerabilityResultApi* | [**create_vulnerability_validation**](docs/VulnerabilityResultApi.md#create_vulnerability_validation) | **POST** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/validations | Asset Vulnerability Validations
*VulnerabilityResultApi* | [**delete_vulnerability_validation**](docs/VulnerabilityResultApi.md#delete_vulnerability_validation) | **DELETE** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/validations/{validationId} | Asset Vulnerability Validation
*VulnerabilityResultApi* | [**get_asset_service_vulnerabilities**](docs/VulnerabilityResultApi.md#get_asset_service_vulnerabilities) | **GET** /api/3/assets/{id}/services/{protocol}/{port}/vulnerabilities | Asset Service Vulnerabilities
*VulnerabilityResultApi* | [**get_asset_vulnerabilities**](docs/VulnerabilityResultApi.md#get_asset_vulnerabilities) | **GET** /api/3/assets/{id}/vulnerabilities | Asset Vulnerabilities
*VulnerabilityResultApi* | [**get_asset_vulnerability**](docs/VulnerabilityResultApi.md#get_asset_vulnerability) | **GET** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId} | Asset Vulnerability
*VulnerabilityResultApi* | [**get_vulnerability_validation**](docs/VulnerabilityResultApi.md#get_vulnerability_validation) | **GET** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/validations/{validationId} | Asset Vulnerability Validation
*VulnerabilityResultApi* | [**get_vulnerability_validations**](docs/VulnerabilityResultApi.md#get_vulnerability_validations) | **GET** /api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/validations | Asset Vulnerability Validations


## Documentation For Models

 - [Account](docs/Account.md)
 - [AdditionalInformation](docs/AdditionalInformation.md)
 - [Address](docs/Address.md)
 - [AdhocScan](docs/AdhocScan.md)
 - [AdvisoryLink](docs/AdvisoryLink.md)
 - [Alert](docs/Alert.md)
 - [AssessmentResult](docs/AssessmentResult.md)
 - [Asset](docs/Asset.md)
 - [AssetCreate](docs/AssetCreate.md)
 - [AssetCreatedOrUpdatedReference](docs/AssetCreatedOrUpdatedReference.md)
 - [AssetGroup](docs/AssetGroup.md)
 - [AssetHistory](docs/AssetHistory.md)
 - [AssetPolicy](docs/AssetPolicy.md)
 - [AssetPolicyAssessment](docs/AssetPolicyAssessment.md)
 - [AssetPolicyItem](docs/AssetPolicyItem.md)
 - [AssetTag](docs/AssetTag.md)
 - [AssetVulnerabilities](docs/AssetVulnerabilities.md)
 - [AuthenticationSettings](docs/AuthenticationSettings.md)
 - [AuthenticationSource](docs/AuthenticationSource.md)
 - [AvailableReportFormat](docs/AvailableReportFormat.md)
 - [BackupsSize](docs/BackupsSize.md)
 - [BadRequestError](docs/BadRequestError.md)
 - [CPUInfo](docs/CPUInfo.md)
 - [Configuration](docs/Configuration.md)
 - [ConsoleCommandOutput](docs/ConsoleCommandOutput.md)
 - [ContentDescription](docs/ContentDescription.md)
 - [CreateAuthenticationSource](docs/CreateAuthenticationSource.md)
 - [CreatedOrUpdatedReference](docs/CreatedOrUpdatedReference.md)
 - [CreatedReference](docs/CreatedReference.md)
 - [CreatedReferenceAssetGroupIDLink](docs/CreatedReferenceAssetGroupIDLink.md)
 - [CreatedReferenceCredentialIDLink](docs/CreatedReferenceCredentialIDLink.md)
 - [CreatedReferenceDiscoveryQueryIDLink](docs/CreatedReferenceDiscoveryQueryIDLink.md)
 - [CreatedReferenceEngineIDLink](docs/CreatedReferenceEngineIDLink.md)
 - [CreatedReferencePolicyOverrideIDLink](docs/CreatedReferencePolicyOverrideIDLink.md)
 - [CreatedReferenceScanIDLink](docs/CreatedReferenceScanIDLink.md)
 - [CreatedReferenceScanTemplateIDLink](docs/CreatedReferenceScanTemplateIDLink.md)
 - [CreatedReferenceUserIDLink](docs/CreatedReferenceUserIDLink.md)
 - [CreatedReferenceVulnerabilityExceptionIDLink](docs/CreatedReferenceVulnerabilityExceptionIDLink.md)
 - [CreatedReferenceVulnerabilityValidationIDLink](docs/CreatedReferenceVulnerabilityValidationIDLink.md)
 - [CreatedReferenceintLink](docs/CreatedReferenceintLink.md)
 - [Criterion](docs/Criterion.md)
 - [Database](docs/Database.md)
 - [DatabaseConnectionSettings](docs/DatabaseConnectionSettings.md)
 - [DatabaseSettings](docs/DatabaseSettings.md)
 - [DatabaseSize](docs/DatabaseSize.md)
 - [DiscoveryAsset](docs/DiscoveryAsset.md)
 - [DiscoveryConnection](docs/DiscoveryConnection.md)
 - [DiscoverySearchCriteria](docs/DiscoverySearchCriteria.md)
 - [DiskFree](docs/DiskFree.md)
 - [DiskInfo](docs/DiskInfo.md)
 - [DiskTotal](docs/DiskTotal.md)
 - [DynamicSite](docs/DynamicSite.md)
 - [EnginePool](docs/EnginePool.md)
 - [EnvironmentProperties](docs/EnvironmentProperties.md)
 - [Error](docs/Error.md)
 - [ExceptionScope](docs/ExceptionScope.md)
 - [ExcludedAssetGroups](docs/ExcludedAssetGroups.md)
 - [ExcludedScanTargets](docs/ExcludedScanTargets.md)
 - [Exploit](docs/Exploit.md)
 - [ExploitSource](docs/ExploitSource.md)
 - [ExploitSourceLink](docs/ExploitSourceLink.md)
 - [Features](docs/Features.md)
 - [File](docs/File.md)
 - [Fingerprint](docs/Fingerprint.md)
 - [GlobalScan](docs/GlobalScan.md)
 - [GroupAccount](docs/GroupAccount.md)
 - [HostName](docs/HostName.md)
 - [IMetaData](docs/IMetaData.md)
 - [IncludedAssetGroups](docs/IncludedAssetGroups.md)
 - [IncludedScanTargets](docs/IncludedScanTargets.md)
 - [Info](docs/Info.md)
 - [InstallSize](docs/InstallSize.md)
 - [InstallationTotalSize](docs/InstallationTotalSize.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [JVMInfo](docs/JVMInfo.md)
 - [JsonNode](docs/JsonNode.md)
 - [License](docs/License.md)
 - [LicenseLimits](docs/LicenseLimits.md)
 - [LicensePolicyScanning](docs/LicensePolicyScanning.md)
 - [LicensePolicyScanningBenchmarks](docs/LicensePolicyScanningBenchmarks.md)
 - [LicenseReporting](docs/LicenseReporting.md)
 - [LicenseScanning](docs/LicenseScanning.md)
 - [Link](docs/Link.md)
 - [Links](docs/Links.md)
 - [LocalePreferences](docs/LocalePreferences.md)
 - [MalwareKit](docs/MalwareKit.md)
 - [MatchedSolution](docs/MatchedSolution.md)
 - [MemoryFree](docs/MemoryFree.md)
 - [MemoryInfo](docs/MemoryInfo.md)
 - [MemoryTotal](docs/MemoryTotal.md)
 - [MetadataContainer](docs/MetadataContainer.md)
 - [NotFoundError](docs/NotFoundError.md)
 - [OperatingSystem](docs/OperatingSystem.md)
 - [OperatingSystemCpe](docs/OperatingSystemCpe.md)
 - [PCI](docs/PCI.md)
 - [PageInfo](docs/PageInfo.md)
 - [PageOfAsset](docs/PageOfAsset.md)
 - [PageOfAssetGroup](docs/PageOfAssetGroup.md)
 - [PageOfAssetPolicy](docs/PageOfAssetPolicy.md)
 - [PageOfAssetPolicyItem](docs/PageOfAssetPolicyItem.md)
 - [PageOfDiscoveryConnection](docs/PageOfDiscoveryConnection.md)
 - [PageOfExploit](docs/PageOfExploit.md)
 - [PageOfGlobalScan](docs/PageOfGlobalScan.md)
 - [PageOfMalwareKit](docs/PageOfMalwareKit.md)
 - [PageOfOperatingSystem](docs/PageOfOperatingSystem.md)
 - [PageOfPolicy](docs/PageOfPolicy.md)
 - [PageOfPolicyAsset](docs/PageOfPolicyAsset.md)
 - [PageOfPolicyControl](docs/PageOfPolicyControl.md)
 - [PageOfPolicyGroup](docs/PageOfPolicyGroup.md)
 - [PageOfPolicyItem](docs/PageOfPolicyItem.md)
 - [PageOfPolicyOverride](docs/PageOfPolicyOverride.md)
 - [PageOfPolicyRule](docs/PageOfPolicyRule.md)
 - [PageOfReport](docs/PageOfReport.md)
 - [PageOfScan](docs/PageOfScan.md)
 - [PageOfSite](docs/PageOfSite.md)
 - [PageOfSoftware](docs/PageOfSoftware.md)
 - [PageOfTag](docs/PageOfTag.md)
 - [PageOfUser](docs/PageOfUser.md)
 - [PageOfVulnerability](docs/PageOfVulnerability.md)
 - [PageOfVulnerabilityCategory](docs/PageOfVulnerabilityCategory.md)
 - [PageOfVulnerabilityCheck](docs/PageOfVulnerabilityCheck.md)
 - [PageOfVulnerabilityException](docs/PageOfVulnerabilityException.md)
 - [PageOfVulnerabilityFinding](docs/PageOfVulnerabilityFinding.md)
 - [PageOfVulnerabilityReference](docs/PageOfVulnerabilityReference.md)
 - [Policy](docs/Policy.md)
 - [PolicyAsset](docs/PolicyAsset.md)
 - [PolicyBenchmark](docs/PolicyBenchmark.md)
 - [PolicyControl](docs/PolicyControl.md)
 - [PolicyGroup](docs/PolicyGroup.md)
 - [PolicyItem](docs/PolicyItem.md)
 - [PolicyMetadataResource](docs/PolicyMetadataResource.md)
 - [PolicyOverride](docs/PolicyOverride.md)
 - [PolicyOverrideReviewer](docs/PolicyOverrideReviewer.md)
 - [PolicyOverrideScope](docs/PolicyOverrideScope.md)
 - [PolicyOverrideSubmitter](docs/PolicyOverrideSubmitter.md)
 - [PolicyRule](docs/PolicyRule.md)
 - [PolicyRuleAssessmentResource](docs/PolicyRuleAssessmentResource.md)
 - [PolicySummaryResource](docs/PolicySummaryResource.md)
 - [Privileges](docs/Privileges.md)
 - [ReferenceWithAlertIDLink](docs/ReferenceWithAlertIDLink.md)
 - [ReferenceWithAssetIDLink](docs/ReferenceWithAssetIDLink.md)
 - [ReferenceWithEndpointIDLink](docs/ReferenceWithEndpointIDLink.md)
 - [ReferenceWithEngineIDLink](docs/ReferenceWithEngineIDLink.md)
 - [ReferenceWithReportIDLink](docs/ReferenceWithReportIDLink.md)
 - [ReferenceWithScanScheduleIDLink](docs/ReferenceWithScanScheduleIDLink.md)
 - [ReferenceWithSiteIDLink](docs/ReferenceWithSiteIDLink.md)
 - [ReferenceWithTagIDLink](docs/ReferenceWithTagIDLink.md)
 - [ReferenceWithUserIDLink](docs/ReferenceWithUserIDLink.md)
 - [ReferencesWithAssetGroupIDLink](docs/ReferencesWithAssetGroupIDLink.md)
 - [ReferencesWithAssetIDLink](docs/ReferencesWithAssetIDLink.md)
 - [ReferencesWithEngineIDLink](docs/ReferencesWithEngineIDLink.md)
 - [ReferencesWithReferenceWithEndpointIDLinkServiceLink](docs/ReferencesWithReferenceWithEndpointIDLinkServiceLink.md)
 - [ReferencesWithSiteIDLink](docs/ReferencesWithSiteIDLink.md)
 - [ReferencesWithSolutionNaturalIDLink](docs/ReferencesWithSolutionNaturalIDLink.md)
 - [ReferencesWithTagIDLink](docs/ReferencesWithTagIDLink.md)
 - [ReferencesWithUserIDLink](docs/ReferencesWithUserIDLink.md)
 - [ReferencesWithVulnerabilityCheckIDLink](docs/ReferencesWithVulnerabilityCheckIDLink.md)
 - [ReferencesWithVulnerabilityCheckTypeIDLink](docs/ReferencesWithVulnerabilityCheckTypeIDLink.md)
 - [ReferencesWithVulnerabilityNaturalIDLink](docs/ReferencesWithVulnerabilityNaturalIDLink.md)
 - [ReferencesWithWebApplicationIDLink](docs/ReferencesWithWebApplicationIDLink.md)
 - [RepeatResource](docs/RepeatResource.md)
 - [RepeatSchedule](docs/RepeatSchedule.md)
 - [Report](docs/Report.md)
 - [ReportConfigCategoryFilters](docs/ReportConfigCategoryFilters.md)
 - [ReportConfigDatabaseCredentialsResource](docs/ReportConfigDatabaseCredentialsResource.md)
 - [ReportConfigDatabaseResource](docs/ReportConfigDatabaseResource.md)
 - [ReportConfigFiltersResource](docs/ReportConfigFiltersResource.md)
 - [ReportConfigScopeResource](docs/ReportConfigScopeResource.md)
 - [ReportEmail](docs/ReportEmail.md)
 - [ReportEmailSmtp](docs/ReportEmailSmtp.md)
 - [ReportFilters](docs/ReportFilters.md)
 - [ReportFrequency](docs/ReportFrequency.md)
 - [ReportInstance](docs/ReportInstance.md)
 - [ReportScope](docs/ReportScope.md)
 - [ReportSize](docs/ReportSize.md)
 - [ReportStorage](docs/ReportStorage.md)
 - [ReportTemplate](docs/ReportTemplate.md)
 - [ResourcesAlert](docs/ResourcesAlert.md)
 - [ResourcesAssetGroup](docs/ResourcesAssetGroup.md)
 - [ResourcesAssetTag](docs/ResourcesAssetTag.md)
 - [ResourcesAuthenticationSource](docs/ResourcesAuthenticationSource.md)
 - [ResourcesAvailableReportFormat](docs/ResourcesAvailableReportFormat.md)
 - [ResourcesConfiguration](docs/ResourcesConfiguration.md)
 - [ResourcesDatabase](docs/ResourcesDatabase.md)
 - [ResourcesDiscoveryAsset](docs/ResourcesDiscoveryAsset.md)
 - [ResourcesEnginePool](docs/ResourcesEnginePool.md)
 - [ResourcesFile](docs/ResourcesFile.md)
 - [ResourcesGroupAccount](docs/ResourcesGroupAccount.md)
 - [ResourcesMatchedSolution](docs/ResourcesMatchedSolution.md)
 - [ResourcesPolicyOverride](docs/ResourcesPolicyOverride.md)
 - [ResourcesReportInstance](docs/ResourcesReportInstance.md)
 - [ResourcesReportTemplate](docs/ResourcesReportTemplate.md)
 - [ResourcesRole](docs/ResourcesRole.md)
 - [ResourcesScanEngine](docs/ResourcesScanEngine.md)
 - [ResourcesScanSchedule](docs/ResourcesScanSchedule.md)
 - [ResourcesScanTemplate](docs/ResourcesScanTemplate.md)
 - [ResourcesSharedCredential](docs/ResourcesSharedCredential.md)
 - [ResourcesSiteCredential](docs/ResourcesSiteCredential.md)
 - [ResourcesSiteSharedCredential](docs/ResourcesSiteSharedCredential.md)
 - [ResourcesSmtpAlert](docs/ResourcesSmtpAlert.md)
 - [ResourcesSnmpAlert](docs/ResourcesSnmpAlert.md)
 - [ResourcesSoftware](docs/ResourcesSoftware.md)
 - [ResourcesSolution](docs/ResourcesSolution.md)
 - [ResourcesSonarQuery](docs/ResourcesSonarQuery.md)
 - [ResourcesSyslogAlert](docs/ResourcesSyslogAlert.md)
 - [ResourcesTag](docs/ResourcesTag.md)
 - [ResourcesUser](docs/ResourcesUser.md)
 - [ResourcesUserAccount](docs/ResourcesUserAccount.md)
 - [ResourcesVulnerabilityValidationResource](docs/ResourcesVulnerabilityValidationResource.md)
 - [ResourcesWebFormAuthentication](docs/ResourcesWebFormAuthentication.md)
 - [ResourcesWebHeaderAuthentication](docs/ResourcesWebHeaderAuthentication.md)
 - [Review](docs/Review.md)
 - [RiskModifierSettings](docs/RiskModifierSettings.md)
 - [RiskSettings](docs/RiskSettings.md)
 - [Role](docs/Role.md)
 - [Scan](docs/Scan.md)
 - [ScanEngine](docs/ScanEngine.md)
 - [ScanEvents](docs/ScanEvents.md)
 - [ScanSchedule](docs/ScanSchedule.md)
 - [ScanScope](docs/ScanScope.md)
 - [ScanSettings](docs/ScanSettings.md)
 - [ScanSize](docs/ScanSize.md)
 - [ScanTargetsResource](docs/ScanTargetsResource.md)
 - [ScanTemplate](docs/ScanTemplate.md)
 - [ScanTemplateAssetDiscovery](docs/ScanTemplateAssetDiscovery.md)
 - [ScanTemplateDatabase](docs/ScanTemplateDatabase.md)
 - [ScanTemplateDiscovery](docs/ScanTemplateDiscovery.md)
 - [ScanTemplateDiscoveryPerformance](docs/ScanTemplateDiscoveryPerformance.md)
 - [ScanTemplateDiscoveryPerformancePacketsRate](docs/ScanTemplateDiscoveryPerformancePacketsRate.md)
 - [ScanTemplateDiscoveryPerformanceParallelism](docs/ScanTemplateDiscoveryPerformanceParallelism.md)
 - [ScanTemplateDiscoveryPerformanceScanDelay](docs/ScanTemplateDiscoveryPerformanceScanDelay.md)
 - [ScanTemplateDiscoveryPerformanceTimeout](docs/ScanTemplateDiscoveryPerformanceTimeout.md)
 - [ScanTemplateServiceDiscovery](docs/ScanTemplateServiceDiscovery.md)
 - [ScanTemplateServiceDiscoveryTcp](docs/ScanTemplateServiceDiscoveryTcp.md)
 - [ScanTemplateServiceDiscoveryUdp](docs/ScanTemplateServiceDiscoveryUdp.md)
 - [ScanTemplateVulnerabilityCheckCategories](docs/ScanTemplateVulnerabilityCheckCategories.md)
 - [ScanTemplateVulnerabilityCheckIndividual](docs/ScanTemplateVulnerabilityCheckIndividual.md)
 - [ScanTemplateVulnerabilityChecks](docs/ScanTemplateVulnerabilityChecks.md)
 - [ScanTemplateWebSpider](docs/ScanTemplateWebSpider.md)
 - [ScanTemplateWebSpiderPaths](docs/ScanTemplateWebSpiderPaths.md)
 - [ScanTemplateWebSpiderPatterns](docs/ScanTemplateWebSpiderPatterns.md)
 - [ScanTemplateWebSpiderPerformance](docs/ScanTemplateWebSpiderPerformance.md)
 - [ScheduledScanTargets](docs/ScheduledScanTargets.md)
 - [SearchCriteria](docs/SearchCriteria.md)
 - [Service](docs/Service.md)
 - [ServiceLink](docs/ServiceLink.md)
 - [ServiceUnavailableError](docs/ServiceUnavailableError.md)
 - [Settings](docs/Settings.md)
 - [SharedCredential](docs/SharedCredential.md)
 - [SharedCredentialAccount](docs/SharedCredentialAccount.md)
 - [Site](docs/Site.md)
 - [SiteCreateResource](docs/SiteCreateResource.md)
 - [SiteCredential](docs/SiteCredential.md)
 - [SiteDiscoveryConnection](docs/SiteDiscoveryConnection.md)
 - [SiteOrganization](docs/SiteOrganization.md)
 - [SiteSharedCredential](docs/SiteSharedCredential.md)
 - [SiteUpdateResource](docs/SiteUpdateResource.md)
 - [SmtpAlert](docs/SmtpAlert.md)
 - [SmtpSettings](docs/SmtpSettings.md)
 - [SnmpAlert](docs/SnmpAlert.md)
 - [Software](docs/Software.md)
 - [SoftwareCpe](docs/SoftwareCpe.md)
 - [Solution](docs/Solution.md)
 - [SolutionMatch](docs/SolutionMatch.md)
 - [SonarCriteria](docs/SonarCriteria.md)
 - [SonarCriterion](docs/SonarCriterion.md)
 - [SonarQuery](docs/SonarQuery.md)
 - [StaticSite](docs/StaticSite.md)
 - [Steps](docs/Steps.md)
 - [Submission](docs/Submission.md)
 - [Summary](docs/Summary.md)
 - [SwaggerDiscoverySearchCriteriaFilter](docs/SwaggerDiscoverySearchCriteriaFilter.md)
 - [SwaggerSearchCriteriaFilter](docs/SwaggerSearchCriteriaFilter.md)
 - [SyslogAlert](docs/SyslogAlert.md)
 - [Tag](docs/Tag.md)
 - [TagAssetSource](docs/TagAssetSource.md)
 - [TagLink](docs/TagLink.md)
 - [TaggedAssetReferences](docs/TaggedAssetReferences.md)
 - [Telnet](docs/Telnet.md)
 - [TokenResource](docs/TokenResource.md)
 - [UnauthorizedError](docs/UnauthorizedError.md)
 - [UniqueId](docs/UniqueId.md)
 - [UpdateId](docs/UpdateId.md)
 - [UpdateInfo](docs/UpdateInfo.md)
 - [UpdateSettings](docs/UpdateSettings.md)
 - [User](docs/User.md)
 - [UserAccount](docs/UserAccount.md)
 - [UserCreateRole](docs/UserCreateRole.md)
 - [UserRole](docs/UserRole.md)
 - [VersionInfo](docs/VersionInfo.md)
 - [Vulnerabilities](docs/Vulnerabilities.md)
 - [Vulnerability](docs/Vulnerability.md)
 - [VulnerabilityCategory](docs/VulnerabilityCategory.md)
 - [VulnerabilityCheck](docs/VulnerabilityCheck.md)
 - [VulnerabilityCheckType](docs/VulnerabilityCheckType.md)
 - [VulnerabilityCvss](docs/VulnerabilityCvss.md)
 - [VulnerabilityCvssV2](docs/VulnerabilityCvssV2.md)
 - [VulnerabilityCvssV3](docs/VulnerabilityCvssV3.md)
 - [VulnerabilityEvents](docs/VulnerabilityEvents.md)
 - [VulnerabilityException](docs/VulnerabilityException.md)
 - [VulnerabilityFinding](docs/VulnerabilityFinding.md)
 - [VulnerabilityReference](docs/VulnerabilityReference.md)
 - [VulnerabilityValidationResource](docs/VulnerabilityValidationResource.md)
 - [VulnerabilityValidationSource](docs/VulnerabilityValidationSource.md)
 - [WebApplication](docs/WebApplication.md)
 - [WebFormAuthentication](docs/WebFormAuthentication.md)
 - [WebHeaderAuthentication](docs/WebHeaderAuthentication.md)
 - [WebPage](docs/WebPage.md)
 - [WebSettings](docs/WebSettings.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication
