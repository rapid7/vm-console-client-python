# coding: utf-8

"""
    InsightVM API

    # Overview   This guide documents the InsightVM Application Programming Interface (API) Version 3. This API supports the Representation State Transfer (REST) design pattern. Unless noted otherwise this API accepts and produces the `application/json` media type. This API uses Hypermedia as the Engine of Application State (HATEOAS) and is hypermedia friendly. All API connections must be made to the security console using HTTPS.  ## Versioning  Versioning is specified in the URL and the base path of this API is: `https://<host>:<port>/api/3/`.  ## Specification  An <a target=\"_blank\" href=\"https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md\">OpenAPI v2</a> specification (also  known as Swagger 2) of this API is available. Tools such as <a target=\"_blank\" href=\"https://github.com/swagger-api/swagger-codegen\">swagger-codegen</a> can be used to generate an API client in the language of your choosing using this specification document.  <p class=\"openapi\">Download the specification: <a class=\"openapi-button\" target=\"_blank\" download=\"\" href=\"/api/3/json\"> Download </a></p>  ## Authentication  Authorization to the API uses HTTP Basic Authorization  (see <a target=\"_blank\" href=\"https://www.ietf.org/rfc/rfc2617.txt\">RFC 2617</a> for more information). Requests must  supply authorization credentials in the `Authorization` header using a Base64 encoded hash of `\"username:password\"`.  <!-- ReDoc-Inject: <security-definitions> -->  ### 2FA  This API supports two-factor authentication (2FA) by supplying an authentication token in addition to the Basic Authorization. The token is specified using the `Token` request header. To leverage two-factor authentication, this must be enabled on the console and be configured for the account accessing the API.  ## Resources  ### Naming  Resource names represent nouns and identify the entity being manipulated or accessed. All collection resources are  pluralized to indicate to the client they are interacting with a collection of multiple resources of the same type. Singular resource names are used when there exists only one resource available to interact with.  The following naming conventions are used by this API:  | Type                                          | Case                     | | --------------------------------------------- | ------------------------ | | Resource names                                | `lower_snake_case`       | | Header, body, and query parameters parameters | `camelCase`              | | JSON fields and property names                | `camelCase`              |  #### Collections  A collection resource is a parent resource for instance resources, but can itself be retrieved and operated on  independently. Collection resources use a pluralized resource name. The resource path for collection resources follow  the convention:  ``` /api/3/{resource_name} ```  #### Instances  An instance resource is a \"leaf\" level resource that may be retrieved, optionally nested within a collection resource. Instance resources are usually retrievable with opaque identifiers. The resource path for instance resources follows  the convention:  ``` /api/3/{resource_name}/{instance_id}... ```  ## Verbs  The following HTTP operations are supported throughout this API. The general usage of the operation and both its failure and success status codes are outlined below.    | Verb      | Usage                                                                                 | Success     | Failure                                                        | | --------- | ------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | | `GET`     | Used to retrieve a resource by identifier, or a collection of resources by type.      | `200`       | `400`, `401`, `402`, `404`, `405`, `408`, `410`, `415`, `500`  | | `POST`    | Creates a resource with an application-specified identifier.                          | `201`       | `400`, `401`, `404`, `405`, `408`, `413`, `415`, `500`         | | `POST`    | Performs a request to queue an asynchronous job.                                      | `202`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `PUT`     | Creates a resource with a client-specified identifier.                                | `200`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `PUT`     | Performs a full update of a resource with a specified identifier.                     | `201`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `DELETE`  | Deletes a resource by identifier or an entire collection of resources.                | `204`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `OPTIONS` | Requests what operations are available on a resource.                                 | `200`       | `401`, `404`, `405`, `408`, `500`                              |  ### Common Operations  #### OPTIONS  All resources respond to the `OPTIONS` request, which allows discoverability of available operations that are supported.  The `OPTIONS` response returns the acceptable HTTP operations on that resource within the `Allow` header. The response is always a `200 OK` status.  ### Collection Resources  Collection resources can support the `GET`, `POST`, `PUT`, and `DELETE` operations.  #### GET  The `GET` operation invoked on a collection resource indicates a request to retrieve all, or some, of the entities  contained within the collection. This also includes the optional capability to filter or search resources during the request. The response from a collection listing is a paginated document. See  [hypermedia links](#section/Overview/Paging) for more information.  #### POST  The `POST` is a non-idempotent operation that allows for the creation of a new resource when the resource identifier  is not provided by the system during the creation operation (i.e. the Security Console generates the identifier). The content of the `POST` request is sent in the request body. The response to a successful `POST` request should be a  `201 CREATED` with a valid `Location` header field set to the URI that can be used to access to the newly  created resource.   The `POST` to a collection resource can also be used to interact with asynchronous resources. In this situation,  instead of a `201 CREATED` response, the `202 ACCEPTED` response indicates that processing of the request is not fully  complete but has been accepted for future processing. This request will respond similarly with a `Location` header with  link to the job-oriented asynchronous resource that was created and/or queued.  #### PUT  The `PUT` is an idempotent operation that either performs a create with user-supplied identity, or a full replace or update of a resource by a known identifier. The response to a `PUT` operation to create an entity is a `201 Created` with a valid `Location` header field set to the URI that can be used to access to the newly created resource.  `PUT` on a collection resource replaces all values in the collection. The typical response to a `PUT` operation that  updates an entity is hypermedia links, which may link to related resources caused by the side-effects of the changes  performed.  #### DELETE  The `DELETE` is an idempotent operation that physically deletes a resource, or removes an association between resources. The typical response to a `DELETE` operation is hypermedia links, which may link to related resources caused by the  side-effects of the changes performed.  ### Instance Resources  Instance resources can support the `GET`, `PUT`, `POST`, `PATCH` and `DELETE` operations.  #### GET  Retrieves the details of a specific resource by its identifier. The details retrieved can be controlled through  property selection and property views. The content of the resource is returned within the body of the response in the  acceptable media type.   #### PUT  Allows for and idempotent \"full update\" (complete replacement) on a specific resource. If the resource does not exist,  it will be created; if it does exist, it is completely overwritten. Any omitted properties in the request are assumed to  be undefined/null. For \"partial updates\" use `POST` or `PATCH` instead.   The content of the `PUT` request is sent in the request body. The identifier of the resource is specified within the URL  (not the request body). The response to a successful `PUT` request is a `201 CREATED` to represent the created status,  with a valid `Location` header field set to the URI that can be used to access to the newly created (or fully replaced)  resource.   #### POST  Performs a non-idempotent creation of a new resource. The `POST` of an instance resource most commonly occurs with the  use of nested resources (e.g. searching on a parent collection resource). The response to a `POST` of an instance  resource is typically a `200 OK` if the resource is non-persistent, and a `201 CREATED` if there is a resource  created/persisted as a result of the operation. This varies by endpoint.  #### PATCH  The `PATCH` operation is used to perform a partial update of a resource. `PATCH` is a non-idempotent operation that enforces an atomic mutation of a resource. Only the properties specified in the request are to be overwritten on the  resource it is applied to. If a property is missing, it is assumed to not have changed.  #### DELETE  Permanently removes the individual resource from the system. If the resource is an association between resources, only  the association is removed, not the resources themselves. A successful deletion of the resource should return  `204 NO CONTENT` with no response body. This operation is not fully idempotent, as follow-up requests to delete a  non-existent resource should return a `404 NOT FOUND`.  ## Requests  Unless otherwise indicated, the default request body media type is `application/json`.  ### Headers  Commonly used request headers include:  | Header             | Example                                       | Purpose                                                                                        |                    | ------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------------- | | `Accept`           | `application/json`                            | Defines what acceptable content types are allowed by the client. For all types, use `*/*`.     | | `Accept-Encoding`  | `deflate, gzip`                               | Allows for the encoding to be specified (such as gzip).                                        | | `Accept-Language`  | `en-US`                                       | Indicates to the server the client's locale (defaults `en-US`).                                | | `Authorization `   | `Basic Base64(\"username:password\")`           | Basic authentication                                                                           | | `Token `           | `123456`                                      | Two-factor authentication token (if enabled)                                                   |  ### Dates & Times  Dates and/or times are specified as strings in the ISO 8601 format(s). The following formats are supported as input:  | Value                       | Format                                                 | Notes                                                 | | --------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | | Date                        | YYYY-MM-DD                                             | Defaults to 12 am UTC (if used for a date & time      | | Date & time only            | YYYY-MM-DD'T'hh:mm:ss[.nnn]                            | Defaults to UTC                                       | | Date & time in UTC          | YYYY-MM-DD'T'hh:mm:ss[.nnn]Z                           |                                                       | | Date & time w/ offset       | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm             |                                                       | | Date & time w/ zone-offset  | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm[<zone-id>]  |                                                       |   ### Timezones  Timezones are specified in the regional zone format, such as `\"America/Los_Angeles\"`, `\"Asia/Tokyo\"`, or `\"GMT\"`.   ### Paging  Pagination is supported on certain collection resources using a combination of two query parameters, `page` and `size`.  As these are control parameters, they are prefixed with the underscore character. The page parameter dictates the  zero-based index of the page to retrieve, and the `size` indicates the size of the page.   For example, `/resources?page=2&size=10` will return page 3, with 10 records per page, giving results 21-30.  The maximum page size for a request is 500.  ### Sorting  Sorting is supported on paginated resources with the `sort` query parameter(s). The sort query parameter(s) supports  identifying a single or multi-property sort with a single or multi-direction output. The format of the parameter is:  ``` sort=property[,ASC|DESC]... ```  Therefore, the request `/resources?sort=name,title,DESC` would return the results sorted by the name and title  descending, in that order. The sort directions are either ascending `ASC` or descending `DESC`. With single-order  sorting, all properties are sorted in the same direction. To sort the results with varying orders by property,  multiple sort parameters are passed.    For example, the request `/resources?sort=name,ASC&sort=title,DESC` would sort by name ascending and title  descending, in that order.  ## Responses  The following response statuses may be returned by this API.     | Status | Meaning                  | Usage                                                                                                                                                                    | | ------ | ------------------------ |------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `200`  | OK                       | The operation performed without error according to the specification of the request, and no more specific 2xx code is suitable.                                          | | `201`  | Created                  | A create request has been fulfilled and a resource has been created. The resource is available as the URI specified in the response, including the `Location` header.    | | `202`  | Accepted                 | An asynchronous task has been accepted, but not guaranteed, to be processed in the future.                                                                               | | `400`  | Bad Request              | The request was invalid or cannot be otherwise served. The request is not likely to succeed in the future without modifications.                                         | | `401`  | Unauthorized             | The user is unauthorized to perform the operation requested, or does not maintain permissions to perform the operation on the resource specified.                        | | `403`  | Forbidden                | The resource exists to which the user has access, but the operating requested is not permitted.                                                                          | | `404`  | Not Found                | The resource specified could not be located, does not exist, or an unauthenticated client does not have permissions to a resource.                                       | | `405`  | Method Not Allowed       | The operations may not be performed on the specific resource. Allowed operations are returned and may be performed on the resource.                                      | | `408`  | Request Timeout          | The client has failed to complete a request in a timely manner and the request has been discarded.                                                                       | | `413`  | Request Entity Too Large | The request being provided is too large for the server to accept processing.                                                                                             | | `415`  | Unsupported Media Type   | The media type is not supported for the requested resource.                                                                                                              | | `500`  | Internal Server Error    | An internal and unexpected error has occurred on the server at no fault of the client.                                                                                   |  ### Security  The response statuses 401, 403 and 404 need special consideration for security purposes. As necessary,  error statuses and messages may be obscured to strengthen security and prevent information exposure. The following is a  guideline for privileged resource response statuses:  | Use Case                                                           | Access             | Resource           | Permission   | Status       | | ------------------------------------------------------------------ | ------------------ |------------------- | ------------ | ------------ | | Unauthenticated access to an unauthenticated resource.             | Unauthenticated    | Unauthenticated    | Yes          | `20x`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Authenticated      | No           | `401`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Non-existent       | No           | `401`        | | Authenticated access to a unauthenticated resource.                | Authenticated      | Unauthenticated    | Yes          | `20x`        | | Authenticated access to an authenticated, unprivileged resource.   | Authenticated      | Authenticated      | No           | `404`        | | Authenticated access to an authenticated, privileged resource.     | Authenticated      | Authenticated      | Yes          | `20x`        | | Authenticated access to an authenticated, non-existent resource    | Authenticated      | Non-existent       | Yes          | `404`        |  ### Headers  Commonly used response headers include:  | Header                     |  Example                          | Purpose                                                         | | -------------------------- | --------------------------------- | --------------------------------------------------------------- | | `Allow`                    | `OPTIONS, GET`                    | Defines the allowable HTTP operations on a resource.            | | `Cache-Control`            | `no-store, must-revalidate`       | Disables caching of resources (as they are all dynamic).        | | `Content-Encoding`         | `gzip`                            | The encoding of the response body (if any).                     | | `Location`                 |                                   | Refers to the URI of the resource created by a request.         | | `Transfer-Encoding`        | `chunked`                         | Specified the encoding used to transform response.              | | `Retry-After`              | 5000                              | Indicates the time to wait before retrying a request.           | | `X-Content-Type-Options`   | `nosniff`                         | Disables MIME type sniffing.                                    | | `X-XSS-Protection`         | `1; mode=block`                   | Enables XSS filter protection.                                  | | `X-Frame-Options`          | `SAMEORIGIN`                      | Prevents rendering in a frame from a different origin.          | | `X-UA-Compatible`          | `IE=edge,chrome=1`                | Specifies the browser mode to render in.                        |  ### Format  When `application/json` is returned in the response body it is always pretty-printed (indented, human readable output).  Additionally, gzip compression/encoding is supported on all responses.   #### Dates & Times  Dates or times are returned as strings in the ISO 8601 'extended' format. When a date and time is returned (instant) the value is converted to UTC.  For example:  | Value           | Format                         | Example               | | --------------- | ------------------------------ | --------------------- | | Date            | `YYYY-MM-DD`                   | 2017-12-03            | | Date & Time     | `YYYY-MM-DD'T'hh:mm:ss[.nnn]Z` | 2017-12-03T10:15:30Z  |  #### Content  In some resources a Content data type is used. This allows for multiple formats of representation to be returned within resource, specifically `\"html\"` and `\"text\"`. The `\"text\"` property returns a flattened representation suitable for output in textual displays. The `\"html\"` property returns an HTML fragment suitable for display within an HTML  element. Note, the HTML returned is not a valid stand-alone HTML document.  #### Paging  The response to a paginated request follows the format:  ```json {    resources\": [        ...     ],    \"page\": {        \"number\" : ...,       \"size\" : ...,       \"totalResources\" : ...,       \"totalPages\" : ...    },    \"links\": [        \"first\" : {          \"href\" : \"...\"        },        \"prev\" : {          \"href\" : \"...\"        },        \"self\" : {          \"href\" : \"...\"        },        \"next\" : {          \"href\" : \"...\"        },        \"last\" : {          \"href\" : \"...\"        }     ] } ```  The `resources` property is an array of the resources being retrieved from the endpoint, each which should contain at  minimum a \"self\" relation hypermedia link. The `page` property outlines the details of the current page and total possible pages. The object for the page includes the following properties:  - number - The page number (zero-based) of the page returned. - size - The size of the pages, which is less than or equal to the maximum page size. - totalResources - The total amount of resources available across all pages. - totalPages - The total amount of pages.  The last property of the paged response is the `links` array, which contains all available hypermedia links. For  paginated responses, the \"self\", \"next\", \"previous\", \"first\", and \"last\" links are returned. The \"self\" link must always be returned and should contain a link to allow the client to replicate the original request against the  collection resource in an identical manner to that in which it was invoked.   The \"next\" and \"previous\" links are present if either or both there exists a previous or next page, respectively.  The \"next\" and \"previous\" links have hrefs that allow \"natural movement\" to the next page, that is all parameters  required to move the next page are provided in the link. The \"first\" and \"last\" links provide references to the first and last pages respectively.   Requests outside the boundaries of the pageable will result in a `404 NOT FOUND`. Paginated requests do not provide a  \"stateful cursor\" to the client, nor does it need to provide a read consistent view. Records in adjacent pages may  change while pagination is being traversed, and the total number of pages and resources may change between requests  within the same filtered/queries resource collection.  #### Property Views  The \"depth\" of the response of a resource can be configured using a \"view\". All endpoints supports two views that can  tune the extent of the information returned in the resource. The supported views are `summary` and `details` (the default).  View are specified using a query parameter, in this format:  ```bash /<resource>?view={viewName} ```  #### Error  Any error responses can provide a response body with a message to the client indicating more information (if applicable)  to aid debugging of the error. All 40x and 50x responses will return an error response in the body. The format of the  response is as follows:  ```json {    \"status\": <statusCode>,    \"message\": <message>,    \"links\" : [ {       \"rel\" : \"...\",       \"href\" : \"...\"     } ] }   ```   The `status` property is the same as the HTTP status returned in the response, to ease client parsing. The message  property is a localized message in the request client's locale (if applicable) that articulates the nature of the  error. The last property is the `links` property. This may contain additional  [hypermedia links](#section/Overview/Authentication) to troubleshoot.  #### Search Criteria <a section=\"section/Responses/SearchCriteria\"></a>  Multiple resources make use of search criteria to match assets. Search criteria is an array of search filters. Each  search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The operator is a type and property-specific operating performed on the filtered property. The valid values for fields and operators are outlined in the table below.  Every filter also defines one or more values that are supplied to the operator. The valid values vary by operator and are outlined below.  ##### Fields  The following table outlines the search criteria fields and the available operators:  | Field                             | Operators                                                                                                                      | | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | | `alternate-address-type`          | `in`                                                                                                                           | | `container-image`                 | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is like` ` not like`                              | | `container-status`                | `is` ` is not`                                                                                                                 | | `containers`                      | `are`                                                                                                                          | | `criticality-tag`                 | `is` ` is not` ` is greater than` ` is less than` ` is applied` ` is not applied`                                              | | `custom-tag`                      | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `cve`                             | `is` ` is not` ` contains` ` does not contain`                                                                                 | | `cvss-access-complexity`          | `is` ` is not`                                                                                                                 | | `cvss-authentication-required`    | `is` ` is not`                                                                                                                 | | `cvss-access-vector`              | `is` ` is not`                                                                                                                 | | `cvss-availability-impact`        | `is` ` is not`                                                                                                                 | | `cvss-confidentiality-impact`     | `is` ` is not`                                                                                                                 | | `cvss-integrity-impact`           | `is` ` is not`                                                                                                                 | | `cvss-v3-confidentiality-impact`  | `is` ` is not`                                                                                                                 | | `cvss-v3-integrity-impact`        | `is` ` is not`                                                                                                                 | | `cvss-v3-availability-impact`     | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-vector`           | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-complexity`       | `is` ` is not`                                                                                                                 | | `cvss-v3-user-interaction`        | `is` ` is not`                                                                                                                 | | `cvss-v3-privileges-required`     | `is` ` is not`                                                                                                                 | | `host-name`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is empty` ` is not empty` ` is like` ` not like`  | | `host-type`                       | `in` ` not in`                                                                                                                 | | `ip-address`                      | `is` ` is not` ` in range` ` not in range` ` is like` ` not like`                                                              | | `ip-address-type`                 | `in` ` not in`                                                                                                                 | | `last-scan-date`                  | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `location-tag`                    | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `mobile-device-last-sync-time`    | `is-within-the-last` ` is earlier than`                                                                                        | | `open-ports`                      | `is` ` is not` ` in range`                                                                                                     | | `operating-system`                | `contains` ` does not contain` ` is empty` ` is not empty`                                                                     | | `owner-tag`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `pci-compliance`                  | `is`                                                                                                                           | | `risk-score`                      | `is` ` is not` ` in range` ` greater than` ` less than`                                                                        | | `service-name`                    | `contains` ` does not contain`                                                                                                 | | `site-id`                         | `in` ` not in`                                                                                                                 | | `software`                        | `contains` ` does not contain`                                                                                                 | | `vAsset-cluster`                  | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-datacenter`               | `is` ` is not`                                                                                                                 | | `vAsset-host-name`                | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-power-state`              | `in` ` not in`                                                                                                                 | | `vAsset-resource-pool-path`       | `contains` ` does not contain`                                                                                                 | | `vulnerability-assessed`          | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `vulnerability-category`          | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain`                                                     | | `vulnerability-cvss-v3-score`     | `is` ` is not`                                                                                                                 | | `vulnerability-cvss-score`        | `is` ` is not` ` in range` ` is greater than` ` is less than`                                                                  | | `vulnerability-exposures`         | `includes` ` does not include`                                                                                                 | | `vulnerability-title`             | `contains` ` does not contain` ` is` ` is not` ` starts with` ` ends with`                                                     | | `vulnerability-validated-status`  | `are`                                                                                                                          |  ##### Enumerated Properties  The following fields have enumerated values:  | Field                                     | Acceptable Values                                                                                             | | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- | | `alternate-address-type`                  | 0=IPv4, 1=IPv6                                                                                                | | `containers`                              | 0=present, 1=not present                                                                                      | | `container-status`                        | `created` `running` `paused` `restarting` `exited` `dead` `unknown`                                           | | `cvss-access-complexity`                  | <ul><li><code>L</code> = Low</li><li><code>M</code> = Medium</li><li><code>H</code> = High</li></ul>          | | `cvss-integrity-impact`                   | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-confidentiality-impact`             | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-availability-impact`                | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-access-vector`                      | <ul><li><code>L</code> = Local</li><li><code>A</code> = Adjacent</li><li><code>N</code> = Network</li></ul>   | | `cvss-authentication-required`            | <ul><li><code>N</code> = None</li><li><code>S</code> = Single</li><li><code>M</code> = Multiple</li></ul>     | | `cvss-v3-confidentiality-impact`     | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-integrity-impact`            | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-availability-impact`             | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `cvss-v3-attack-vector`                | <ul><li><code>N</code> = Network</li><li><code>A</code> = Adjacent</li><li><code>L</code> = Local</li><li><code>P</code> = Physical</li></ul>    | | `cvss-v3-attack-complexity`                      | <ul><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>   | | `cvss-v3-user-interaction`            | <ul><li><code>N</code> = None</li><li><code>R</code> = Required</li></ul>     | | `cvss-v3-privileges-required`         | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `host-type`                               | 0=Unknown, 1=Guest, 2=Hypervisor, 3=Physical, 4=Mobile                                                        | | `ip-address-type`                         | 0=IPv4, 1=IPv6                                                                                                | | `pci-compliance`                          | 0=fail, 1=pass                                                                                                | | `vulnerability-validated-status`          | 0=present, 1=not present                                                                                      |  ##### Operator Properties <a section=\"section/Responses/SearchCriteria/OperatorProperties\"></a>  The following table outlines which properties are required for each operator and the appropriate data type(s):  | Operator              | `value`               | `lower`               | `upper`               | | ----------------------|-----------------------|-----------------------|-----------------------| | `are`                 | `string`              |                       |                       | | `contains`            | `string`              |                       |                       | | `does-not-contain`    | `string`              |                       |                       | | `ends with`           | `string`              |                       |                       | | `in`                  | `Array[ string ]`     |                       |                       | | `in-range`            |                       | `numeric`             | `numeric`             | | `includes`            | `Array[ string ]`     |                       |                       | | `is`                  | `string`              |                       |                       | | `is-applied`          |                       |                       |                       | | `is-between`          |                       | `numeric`             | `numeric`             | | `is-earlier-than`     | `numeric`             |                       |                       | | `is-empty`            |                       |                       |                       | | `is-greater-than`     | `numeric`             |                       |                       | | `is-on-or-after`      | `string` (yyyy-MM-dd) |                       |                       | | `is-on-or-before`     | `string` (yyyy-MM-dd) |                       |                       | | `is-not`              | `string`              |                       |                       | | `is-not-applied`      |                       |                       |                       | | `is-not-empty`        |                       |                       |                       | | `is-within-the-last`  | `string`              |                       |                       | | `less-than`           | `string`              |                       |                       | | `like`                | `string`              |                       |                       | | `not-contains`        | `string`              |                       |                       | | `not-in`              | `Array[ string ]`     |                       |                       | | `not-in-range`        |                       | `numeric`             | `numeric`             | | `not-like`            | `string`              |                       |                       | | `starts-with`         | `string`              |                       |                       |  #### Discovery Connection Search Criteria <a section=\"section/Responses/DiscoverySearchCriteria\"></a>  Dynamic sites make use of search criteria to match assets from a discovery connection. Search criteria is an array of search filters.    Each search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The list of supported fields vary depending on the type of discovery connection configured  for the dynamic site (e.g vSphere, ActiveSync, etc.). The operator is a type and property-specific operating  performed on the filtered property. The valid values for fields outlined in the tables below and are grouped by the  type of connection.    Every filter also defines one or more values that are supplied to the operator. See  <a href=\"#section/Responses/SearchCriteria/OperatorProperties\">Search Criteria Operator Properties</a> for more  information on the valid values for each operator.    ##### Fields (ActiveSync)  This section documents search criteria information for ActiveSync discovery connections. The discovery connections  must be one of the following types: `\"activesync-ldap\"`, `\"activesync-office365\"`, or `\"activesync-powershell\"`.    The following table outlines the search criteria fields and the available operators for ActiveSync connections:  | Field                             | Operators                                                     | | --------------------------------- | ------------------------------------------------------------- | | `last-sync-time`                  | `is-within-the-last` ` is-earlier-than`                       | | `operating-system`                | `contains` ` does-not-contain`                                | | `user`                            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (AWS)  This section documents search criteria information for AWS discovery connections. The discovery connections must be the type `\"aws\"`.    The following table outlines the search criteria fields and the available operators for AWS connections:  | Field                   | Operators                                                     | | ----------------------- | ------------------------------------------------------------- | | `availability-zone`     | `contains` ` does-not-contain`                                | | `guest-os-family`       | `contains` ` does-not-contain`                                | | `instance-id`           | `contains` ` does-not-contain`                                | | `instance-name`         | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `instance-state`        | `in` ` not-in`                                                | | `instance-type`         | `in` ` not-in`                                                | | `ip-address`            | `in-range` ` not-in-range` ` is` ` is-not`                    | | `region`                | `in` ` not-in`                                                | | `vpc-id`                | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (DHCP)  This section documents search criteria information for DHCP discovery connections. The discovery connections must be the type `\"dhcp\"`.    The following table outlines the search criteria fields and the available operators for DHCP connections:  | Field           | Operators                                                     | | --------------- | ------------------------------------------------------------- | | `host-name`     | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `ip-address`    | `in-range` ` not-in-range` ` is` ` is-not`                    | | `mac-address`   | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (Sonar)  This section documents search criteria information for Sonar discovery connections. The discovery connections must be the type `\"sonar\"`.    The following table outlines the search criteria fields and the available operators for Sonar connections:  | Field               | Operators            | | ------------------- | -------------------- | | `search-domain`     | `contains` ` is`     | | `ip-address`        | `in-range` ` is`     | | `sonar-scan-date`   | `is-within-the-last` |  ##### Fields (vSphere)  This section documents search criteria information for vSphere discovery connections. The discovery connections must be the type `\"vsphere\"`.    The following table outlines the search criteria fields and the available operators for vSphere connections:  | Field                | Operators                                                                                  | | -------------------- | ------------------------------------------------------------------------------------------ | | `cluster`            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `data-center`        | `is` ` is-not`                                                                             | | `discovered-time`    | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `guest-os-family`    | `contains` ` does-not-contain`                                                             | | `host-name`          | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `ip-address`         | `in-range` ` not-in-range` ` is` ` is-not`                                                 | | `power-state`        | `in` ` not-in`                                                                             | | `resource-pool-path` | `contains` ` does-not-contain`                                                             | | `last-time-seen`     | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `vm`                 | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              |  ##### Enumerated Properties (vSphere)  The following fields have enumerated values:  | Field         | Acceptable Values                    | | ------------- | ------------------------------------ | | `power-state` | `poweredOn` `poweredOff` `suspended` |  ## HATEOAS  This API follows Hypermedia as the Engine of Application State (HATEOAS) principals and is therefore hypermedia friendly.  Hyperlinks are returned in the `links` property of any given resource and contain a fully-qualified hyperlink to the corresponding resource. The format of the hypermedia link adheres to both the <a target=\"_blank\" href=\"http://jsonapi.org\">{json:api} v1</a>  <a target=\"_blank\" href=\"http://jsonapi.org/format/#document-links\">\"Link Object\"</a> and  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html\">JSON Hyper-Schema</a>  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html#rfc.section.5.2\">\"Link Description Object\"</a> formats. For example:  ```json \"links\": [{   \"rel\": \"<relation>\",   \"href\": \"<href>\"   ... }] ```  Where appropriate link objects may also contain additional properties than the `rel` and `href` properties, such as `id`, `type`, etc.  See the [Root](#tag/Root) resources for the entry points into API discovery.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JsonNode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'array': 'bool',
        'big_decimal': 'bool',
        'big_integer': 'bool',
        'binary': 'bool',
        'boolean': 'bool',
        'container_node': 'bool',
        'double': 'bool',
        'float': 'bool',
        'floating_point_number': 'bool',
        'int': 'bool',
        'integral_number': 'bool',
        'long': 'bool',
        'missing_node': 'bool',
        'node_type': 'str',
        'null': 'bool',
        'number': 'bool',
        'object': 'bool',
        'pojo': 'bool',
        'short': 'bool',
        'textual': 'bool',
        'value_node': 'bool'
    }

    attribute_map = {
        'array': 'array',
        'big_decimal': 'bigDecimal',
        'big_integer': 'bigInteger',
        'binary': 'binary',
        'boolean': 'boolean',
        'container_node': 'containerNode',
        'double': 'double',
        'float': 'float',
        'floating_point_number': 'floatingPointNumber',
        'int': 'int',
        'integral_number': 'integralNumber',
        'long': 'long',
        'missing_node': 'missingNode',
        'node_type': 'nodeType',
        'null': 'null',
        'number': 'number',
        'object': 'object',
        'pojo': 'pojo',
        'short': 'short',
        'textual': 'textual',
        'value_node': 'valueNode'
    }

    def __init__(self, array=None, big_decimal=None, big_integer=None, binary=None, boolean=None, container_node=None, double=None, float=None, floating_point_number=None, int=None, integral_number=None, long=None, missing_node=None, node_type=None, null=None, number=None, object=None, pojo=None, short=None, textual=None, value_node=None):  # noqa: E501
        """JsonNode - a model defined in Swagger"""  # noqa: E501

        self._array = None
        self._big_decimal = None
        self._big_integer = None
        self._binary = None
        self._boolean = None
        self._container_node = None
        self._double = None
        self._float = None
        self._floating_point_number = None
        self._int = None
        self._integral_number = None
        self._long = None
        self._missing_node = None
        self._node_type = None
        self._null = None
        self._number = None
        self._object = None
        self._pojo = None
        self._short = None
        self._textual = None
        self._value_node = None
        self.discriminator = None

        if array is not None:
            self.array = array
        if big_decimal is not None:
            self.big_decimal = big_decimal
        if big_integer is not None:
            self.big_integer = big_integer
        if binary is not None:
            self.binary = binary
        if boolean is not None:
            self.boolean = boolean
        if container_node is not None:
            self.container_node = container_node
        if double is not None:
            self.double = double
        if float is not None:
            self.float = float
        if floating_point_number is not None:
            self.floating_point_number = floating_point_number
        if int is not None:
            self.int = int
        if integral_number is not None:
            self.integral_number = integral_number
        if long is not None:
            self.long = long
        if missing_node is not None:
            self.missing_node = missing_node
        if node_type is not None:
            self.node_type = node_type
        if null is not None:
            self.null = null
        if number is not None:
            self.number = number
        if object is not None:
            self.object = object
        if pojo is not None:
            self.pojo = pojo
        if short is not None:
            self.short = short
        if textual is not None:
            self.textual = textual
        if value_node is not None:
            self.value_node = value_node

    @property
    def array(self):
        """Gets the array of this JsonNode.  # noqa: E501


        :return: The array of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._array

    @array.setter
    def array(self, array):
        """Sets the array of this JsonNode.


        :param array: The array of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._array = array

    @property
    def big_decimal(self):
        """Gets the big_decimal of this JsonNode.  # noqa: E501


        :return: The big_decimal of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._big_decimal

    @big_decimal.setter
    def big_decimal(self, big_decimal):
        """Sets the big_decimal of this JsonNode.


        :param big_decimal: The big_decimal of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._big_decimal = big_decimal

    @property
    def big_integer(self):
        """Gets the big_integer of this JsonNode.  # noqa: E501


        :return: The big_integer of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._big_integer

    @big_integer.setter
    def big_integer(self, big_integer):
        """Sets the big_integer of this JsonNode.


        :param big_integer: The big_integer of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._big_integer = big_integer

    @property
    def binary(self):
        """Gets the binary of this JsonNode.  # noqa: E501


        :return: The binary of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """Sets the binary of this JsonNode.


        :param binary: The binary of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._binary = binary

    @property
    def boolean(self):
        """Gets the boolean of this JsonNode.  # noqa: E501


        :return: The boolean of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        """Sets the boolean of this JsonNode.


        :param boolean: The boolean of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._boolean = boolean

    @property
    def container_node(self):
        """Gets the container_node of this JsonNode.  # noqa: E501


        :return: The container_node of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._container_node

    @container_node.setter
    def container_node(self, container_node):
        """Sets the container_node of this JsonNode.


        :param container_node: The container_node of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._container_node = container_node

    @property
    def double(self):
        """Gets the double of this JsonNode.  # noqa: E501


        :return: The double of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this JsonNode.


        :param double: The double of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._double = double

    @property
    def float(self):
        """Gets the float of this JsonNode.  # noqa: E501


        :return: The float of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._float

    @float.setter
    def float(self, float):
        """Sets the float of this JsonNode.


        :param float: The float of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._float = float

    @property
    def floating_point_number(self):
        """Gets the floating_point_number of this JsonNode.  # noqa: E501


        :return: The floating_point_number of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._floating_point_number

    @floating_point_number.setter
    def floating_point_number(self, floating_point_number):
        """Sets the floating_point_number of this JsonNode.


        :param floating_point_number: The floating_point_number of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._floating_point_number = floating_point_number

    @property
    def int(self):
        """Gets the int of this JsonNode.  # noqa: E501


        :return: The int of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._int

    @int.setter
    def int(self, int):
        """Sets the int of this JsonNode.


        :param int: The int of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._int = int

    @property
    def integral_number(self):
        """Gets the integral_number of this JsonNode.  # noqa: E501


        :return: The integral_number of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._integral_number

    @integral_number.setter
    def integral_number(self, integral_number):
        """Sets the integral_number of this JsonNode.


        :param integral_number: The integral_number of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._integral_number = integral_number

    @property
    def long(self):
        """Gets the long of this JsonNode.  # noqa: E501


        :return: The long of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this JsonNode.


        :param long: The long of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._long = long

    @property
    def missing_node(self):
        """Gets the missing_node of this JsonNode.  # noqa: E501


        :return: The missing_node of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._missing_node

    @missing_node.setter
    def missing_node(self, missing_node):
        """Sets the missing_node of this JsonNode.


        :param missing_node: The missing_node of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._missing_node = missing_node

    @property
    def node_type(self):
        """Gets the node_type of this JsonNode.  # noqa: E501


        :return: The node_type of this JsonNode.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this JsonNode.


        :param node_type: The node_type of this JsonNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["ARRAY", "BINARY", "BOOLEAN", "MISSING", "NULL", "NUMBER", "OBJECT", "POJO", "STRING"]  # noqa: E501
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def null(self):
        """Gets the null of this JsonNode.  # noqa: E501


        :return: The null of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._null

    @null.setter
    def null(self, null):
        """Sets the null of this JsonNode.


        :param null: The null of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._null = null

    @property
    def number(self):
        """Gets the number of this JsonNode.  # noqa: E501


        :return: The number of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this JsonNode.


        :param number: The number of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._number = number

    @property
    def object(self):
        """Gets the object of this JsonNode.  # noqa: E501


        :return: The object of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this JsonNode.


        :param object: The object of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._object = object

    @property
    def pojo(self):
        """Gets the pojo of this JsonNode.  # noqa: E501


        :return: The pojo of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._pojo

    @pojo.setter
    def pojo(self, pojo):
        """Sets the pojo of this JsonNode.


        :param pojo: The pojo of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._pojo = pojo

    @property
    def short(self):
        """Gets the short of this JsonNode.  # noqa: E501


        :return: The short of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this JsonNode.


        :param short: The short of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._short = short

    @property
    def textual(self):
        """Gets the textual of this JsonNode.  # noqa: E501


        :return: The textual of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._textual

    @textual.setter
    def textual(self, textual):
        """Sets the textual of this JsonNode.


        :param textual: The textual of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._textual = textual

    @property
    def value_node(self):
        """Gets the value_node of this JsonNode.  # noqa: E501


        :return: The value_node of this JsonNode.  # noqa: E501
        :rtype: bool
        """
        return self._value_node

    @value_node.setter
    def value_node(self, value_node):
        """Sets the value_node of this JsonNode.


        :param value_node: The value_node of this JsonNode.  # noqa: E501
        :type: bool
        """

        self._value_node = value_node

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JsonNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
