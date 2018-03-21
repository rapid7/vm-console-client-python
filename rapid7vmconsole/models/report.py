# coding: utf-8

"""
    InsightVM API

    # Overview   This guide documents the InsightVM Application Programming Interface (API) Version 3. This API supports the Representation State Transfer (REST) design pattern. Unless noted otherwise this API accepts and produces the `application/json` media type. This API uses Hypermedia as the Engine of Application State (HATEOAS) and is hypermedia friendly. All API connections must be made to the security console using HTTPS.  ## Versioning  Versioning is specified in the URL and the base path of this API is: `https://<host>:<port>/api/3/`.  ## Specification  An <a target=\"_blank\" href=\"https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md\">OpenAPI v2</a> specification (also  known as Swagger 2) of this API is available. Tools such as <a target=\"_blank\" href=\"https://github.com/swagger-api/swagger-codegen\">swagger-codegen</a> can be used to generate an API client in the language of your choosing using this specification document.  <p class=\"openapi\">Download the specification: <a class=\"openapi-button\" target=\"_blank\" download=\"\" href=\"/api/3/json\"> Download </a></p>  ## Authentication  Authorization to the API uses HTTP Basic Authorization  (see <a target=\"_blank\" href=\"https://www.ietf.org/rfc/rfc2617.txt\">RFC 2617</a> for more information). Requests must  supply authorization credentials in the `Authorization` header using a Base64 encoded hash of `\"username:password\"`.  <!-- ReDoc-Inject: <security-definitions> -->  ### 2FA  This API supports two-factor authentication (2FA) by supplying an authentication token in addition to the Basic Authorization. The token is specified using the `Token` request header. To leverage two-factor authentication, this must be enabled on the console and be configured for the account accessing the API.  ## Resources  ### Naming  Resource names represent nouns and identify the entity being manipulated or accessed. All collection resources are  pluralized to indicate to the client they are interacting with a collection of multiple resources of the same type. Singular resource names are used when there exists only one resource available to interact with.  The following naming conventions are used by this API:  | Type                                          | Case                     | | --------------------------------------------- | ------------------------ | | Resource names                                | `lower_snake_case`       | | Header, body, and query parameters parameters | `camelCase`              | | JSON fields and property names                | `camelCase`              |  #### Collections  A collection resource is a parent resource for instance resources, but can itself be retrieved and operated on  independently. Collection resources use a pluralized resource name. The resource path for collection resources follow  the convention:  ``` /api/3/{resource_name} ```  #### Instances  An instance resource is a \"leaf\" level resource that may be retrieved, optionally nested within a collection resource. Instance resources are usually retrievable with opaque identifiers. The resource path for instance resources follows  the convention:  ``` /api/3/{resource_name}/{instance_id}... ```  ## Verbs  The following HTTP operations are supported throughout this API. The general usage of the operation and both its failure and success status codes are outlined below.    | Verb      | Usage                                                                                 | Success     | Failure                                                        | | --------- | ------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | | `GET`     | Used to retrieve a resource by identifier, or a collection of resources by type.      | `200`       | `400`, `401`, `402`, `404`, `405`, `408`, `410`, `415`, `500`  | | `POST`    | Creates a resource with an application-specified identifier.                          | `201`       | `400`, `401`, `404`, `405`, `408`, `413`, `415`, `500`         | | `POST`    | Performs a request to queue an asynchronous job.                                      | `202`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `PUT`     | Creates a resource with a client-specified identifier.                                | `200`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `PUT`     | Performs a full update of a resource with a specified identifier.                     | `201`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `DELETE`  | Deletes a resource by identifier or an entire collection of resources.                | `204`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `OPTIONS` | Requests what operations are available on a resource.                                 | `200`       | `401`, `404`, `405`, `408`, `500`                              |  ### Common Operations  #### OPTIONS  All resources respond to the `OPTIONS` request, which allows discoverability of available operations that are supported.  The `OPTIONS` response returns the acceptable HTTP operations on that resource within the `Allow` header. The response is always a `200 OK` status.  ### Collection Resources  Collection resources can support the `GET`, `POST`, `PUT`, and `DELETE` operations.  #### GET  The `GET` operation invoked on a collection resource indicates a request to retrieve all, or some, of the entities  contained within the collection. This also includes the optional capability to filter or search resources during the request. The response from a collection listing is a paginated document. See  [hypermedia links](#section/Overview/Paging) for more information.  #### POST  The `POST` is a non-idempotent operation that allows for the creation of a new resource when the resource identifier  is not provided by the system during the creation operation (i.e. the Security Console generates the identifier). The content of the `POST` request is sent in the request body. The response to a successful `POST` request should be a  `201 CREATED` with a valid `Location` header field set to the URI that can be used to access to the newly  created resource.   The `POST` to a collection resource can also be used to interact with asynchronous resources. In this situation,  instead of a `201 CREATED` response, the `202 ACCEPTED` response indicates that processing of the request is not fully  complete but has been accepted for future processing. This request will respond similarly with a `Location` header with  link to the job-oriented asynchronous resource that was created and/or queued.  #### PUT  The `PUT` is an idempotent operation that either performs a create with user-supplied identity, or a full replace or update of a resource by a known identifier. The response to a `PUT` operation to create an entity is a `201 Created` with a valid `Location` header field set to the URI that can be used to access to the newly created resource.  `PUT` on a collection resource replaces all values in the collection. The typical response to a `PUT` operation that  updates an entity is hypermedia links, which may link to related resources caused by the side-effects of the changes  performed.  #### DELETE  The `DELETE` is an idempotent operation that physically deletes a resource, or removes an association between resources. The typical response to a `DELETE` operation is hypermedia links, which may link to related resources caused by the  side-effects of the changes performed.  ### Instance Resources  Instance resources can support the `GET`, `PUT`, `POST`, `PATCH` and `DELETE` operations.  #### GET  Retrieves the details of a specific resource by its identifier. The details retrieved can be controlled through  property selection and property views. The content of the resource is returned within the body of the response in the  acceptable media type.   #### PUT  Allows for and idempotent \"full update\" (complete replacement) on a specific resource. If the resource does not exist,  it will be created; if it does exist, it is completely overwritten. Any omitted properties in the request are assumed to  be undefined/null. For \"partial updates\" use `POST` or `PATCH` instead.   The content of the `PUT` request is sent in the request body. The identifier of the resource is specified within the URL  (not the request body). The response to a successful `PUT` request is a `201 CREATED` to represent the created status,  with a valid `Location` header field set to the URI that can be used to access to the newly created (or fully replaced)  resource.   #### POST  Performs a non-idempotent creation of a new resource. The `POST` of an instance resource most commonly occurs with the  use of nested resources (e.g. searching on a parent collection resource). The response to a `POST` of an instance  resource is typically a `200 OK` if the resource is non-persistent, and a `201 CREATED` if there is a resource  created/persisted as a result of the operation. This varies by endpoint.  #### PATCH  The `PATCH` operation is used to perform a partial update of a resource. `PATCH` is a non-idempotent operation that enforces an atomic mutation of a resource. Only the properties specified in the request are to be overwritten on the  resource it is applied to. If a property is missing, it is assumed to not have changed.  #### DELETE  Permanently removes the individual resource from the system. If the resource is an association between resources, only  the association is removed, not the resources themselves. A successful deletion of the resource should return  `204 NO CONTENT` with no response body. This operation is not fully idempotent, as follow-up requests to delete a  non-existent resource should return a `404 NOT FOUND`.  ## Requests  Unless otherwise indicated, the default request body media type is `application/json`.  ### Headers  Commonly used request headers include:  | Header             | Example                                       | Purpose                                                                                        |                    | ------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------------- | | `Accept`           | `application/json`                            | Defines what acceptable content types are allowed by the client. For all types, use `*/*`.     | | `Accept-Encoding`  | `deflate, gzip`                               | Allows for the encoding to be specified (such as gzip).                                        | | `Accept-Language`  | `en-US`                                       | Indicates to the server the client's locale (defaults `en-US`).                                | | `Authorization `   | `Basic Base64(\"username:password\")`           | Basic authentication                                                                           | | `Token `           | `123456`                                      | Two-factor authentication token (if enabled)                                                   |  ### Dates & Times  Dates and/or times are specified as strings in the ISO 8601 format(s). The following formats are supported as input:  | Value                       | Format                                                 | Notes                                                 | | --------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | | Date                        | YYYY-MM-DD                                             | Defaults to 12 am UTC (if used for a date & time      | | Date & time only            | YYYY-MM-DD'T'hh:mm:ss[.nnn]                            | Defaults to UTC                                       | | Date & time in UTC          | YYYY-MM-DD'T'hh:mm:ss[.nnn]Z                           |                                                       | | Date & time w/ offset       | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm             |                                                       | | Date & time w/ zone-offset  | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm[<zone-id>]  |                                                       |   ### Timezones  Timezones are specified in the regional zone format, such as `\"America/Los_Angeles\"`, `\"Asia/Tokyo\"`, or `\"GMT\"`.   ### Paging  Pagination is supported on certain collection resources using a combination of two query parameters, `page` and `size`.  As these are control parameters, they are prefixed with the underscore character. The page parameter dictates the  zero-based index of the page to retrieve, and the `size` indicates the size of the page.   For example, `/resources?page=2&size=10` will return page 3, with 10 records per page, giving results 21-30.  The maximum page size for a request is 500.  ### Sorting  Sorting is supported on paginated resources with the `sort` query parameter(s). The sort query parameter(s) supports  identifying a single or multi-property sort with a single or multi-direction output. The format of the parameter is:  ``` sort=property[,ASC|DESC]... ```  Therefore, the request `/resources?sort=name,title,DESC` would return the results sorted by the name and title  descending, in that order. The sort directions are either ascending `ASC` or descending `DESC`. With single-order  sorting, all properties are sorted in the same direction. To sort the results with varying orders by property,  multiple sort parameters are passed.    For example, the request `/resources?sort=name,ASC&sort=title,DESC` would sort by name ascending and title  descending, in that order.  ## Responses  The following response statuses may be returned by this API.     | Status | Meaning                  | Usage                                                                                                                                                                    | | ------ | ------------------------ |------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `200`  | OK                       | The operation performed without error according to the specification of the request, and no more specific 2xx code is suitable.                                          | | `201`  | Created                  | A create request has been fulfilled and a resource has been created. The resource is available as the URI specified in the response, including the `Location` header.    | | `202`  | Accepted                 | An asynchronous task has been accepted, but not guaranteed, to be processed in the future.                                                                               | | `400`  | Bad Request              | The request was invalid or cannot be otherwise served. The request is not likely to succeed in the future without modifications.                                         | | `401`  | Unauthorized             | The user is unauthorized to perform the operation requested, or does not maintain permissions to perform the operation on the resource specified.                        | | `403`  | Forbidden                | The resource exists to which the user has access, but the operating requested is not permitted.                                                                          | | `404`  | Not Found                | The resource specified could not be located, does not exist, or an unauthenticated client does not have permissions to a resource.                                       | | `405`  | Method Not Allowed       | The operations may not be performed on the specific resource. Allowed operations are returned and may be performed on the resource.                                      | | `408`  | Request Timeout          | The client has failed to complete a request in a timely manner and the request has been discarded.                                                                       | | `413`  | Request Entity Too Large | The request being provided is too large for the server to accept processing.                                                                                             | | `415`  | Unsupported Media Type   | The media type is not supported for the requested resource.                                                                                                              | | `500`  | Internal Server Error    | An internal and unexpected error has occurred on the server at no fault of the client.                                                                                   |  ### Security  The response statuses 401, 403 and 404 need special consideration for security purposes. As necessary,  error statuses and messages may be obscured to strengthen security and prevent information exposure. The following is a  guideline for privileged resource response statuses:  | Use Case                                                           | Access             | Resource           | Permission   | Status       | | ------------------------------------------------------------------ | ------------------ |------------------- | ------------ | ------------ | | Unauthenticated access to an unauthenticated resource.             | Unauthenticated    | Unauthenticated    | Yes          | `20x`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Authenticated      | No           | `401`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Non-existent       | No           | `401`        | | Authenticated access to a unauthenticated resource.                | Authenticated      | Unauthenticated    | Yes          | `20x`        | | Authenticated access to an authenticated, unprivileged resource.   | Authenticated      | Authenticated      | No           | `404`        | | Authenticated access to an authenticated, privileged resource.     | Authenticated      | Authenticated      | Yes          | `20x`        | | Authenticated access to an authenticated, non-existent resource    | Authenticated      | Non-existent       | Yes          | `404`        |  ### Headers  Commonly used response headers include:  | Header                     |  Example                          | Purpose                                                         | | -------------------------- | --------------------------------- | --------------------------------------------------------------- | | `Allow`                    | `OPTIONS, GET`                    | Defines the allowable HTTP operations on a resource.            | | `Cache-Control`            | `no-store, must-revalidate`       | Disables caching of resources (as they are all dynamic).        | | `Content-Encoding`         | `gzip`                            | The encoding of the response body (if any).                     | | `Location`                 |                                   | Refers to the URI of the resource created by a request.         | | `Transfer-Encoding`        | `chunked`                         | Specified the encoding used to transform response.              | | `Retry-After`              | 5000                              | Indicates the time to wait before retrying a request.           | | `X-Content-Type-Options`   | `nosniff`                         | Disables MIME type sniffing.                                    | | `X-XSS-Protection`         | `1; mode=block`                   | Enables XSS filter protection.                                  | | `X-Frame-Options`          | `SAMEORIGIN`                      | Prevents rendering in a frame from a different origin.          | | `X-UA-Compatible`          | `IE=edge,chrome=1`                | Specifies the browser mode to render in.                        |  ### Format  When `application/json` is returned in the response body it is always pretty-printed (indented, human readable output).  Additionally, gzip compression/encoding is supported on all responses.   #### Dates & Times  Dates or times are returned as strings in the ISO 8601 'extended' format. When a date and time is returned (instant) the value is converted to UTC.  For example:  | Value           | Format                         | Example               | | --------------- | ------------------------------ | --------------------- | | Date            | `YYYY-MM-DD`                   | 2017-12-03            | | Date & Time     | `YYYY-MM-DD'T'hh:mm:ss[.nnn]Z` | 2017-12-03T10:15:30Z  |  #### Content  In some resources a Content data type is used. This allows for multiple formats of representation to be returned within resource, specifically `\"html\"` and `\"text\"`. The `\"text\"` property returns a flattened representation suitable for output in textual displays. The `\"html\"` property returns an HTML fragment suitable for display within an HTML  element. Note, the HTML returned is not a valid stand-alone HTML document.  #### Paging  The response to a paginated request follows the format:  ```json {    resources\": [        ...     ],    \"page\": {        \"number\" : ...,       \"size\" : ...,       \"totalResources\" : ...,       \"totalPages\" : ...    },    \"links\": [        \"first\" : {          \"href\" : \"...\"        },        \"prev\" : {          \"href\" : \"...\"        },        \"self\" : {          \"href\" : \"...\"        },        \"next\" : {          \"href\" : \"...\"        },        \"last\" : {          \"href\" : \"...\"        }     ] } ```  The `resources` property is an array of the resources being retrieved from the endpoint, each which should contain at  minimum a \"self\" relation hypermedia link. The `page` property outlines the details of the current page and total possible pages. The object for the page includes the following properties:  - number - The page number (zero-based) of the page returned. - size - The size of the pages, which is less than or equal to the maximum page size. - totalResources - The total amount of resources available across all pages. - totalPages - The total amount of pages.  The last property of the paged response is the `links` array, which contains all available hypermedia links. For  paginated responses, the \"self\", \"next\", \"previous\", \"first\", and \"last\" links are returned. The \"self\" link must always be returned and should contain a link to allow the client to replicate the original request against the  collection resource in an identical manner to that in which it was invoked.   The \"next\" and \"previous\" links are present if either or both there exists a previous or next page, respectively.  The \"next\" and \"previous\" links have hrefs that allow \"natural movement\" to the next page, that is all parameters  required to move the next page are provided in the link. The \"first\" and \"last\" links provide references to the first and last pages respectively.   Requests outside the boundaries of the pageable will result in a `404 NOT FOUND`. Paginated requests do not provide a  \"stateful cursor\" to the client, nor does it need to provide a read consistent view. Records in adjacent pages may  change while pagination is being traversed, and the total number of pages and resources may change between requests  within the same filtered/queries resource collection.  #### Property Views  The \"depth\" of the response of a resource can be configured using a \"view\". All endpoints supports two views that can  tune the extent of the information returned in the resource. The supported views are `summary` and `details` (the default).  View are specified using a query parameter, in this format:  ```bash /<resource>?view={viewName} ```  #### Error  Any error responses can provide a response body with a message to the client indicating more information (if applicable)  to aid debugging of the error. All 40x and 50x responses will return an error response in the body. The format of the  response is as follows:  ```json {    \"status\": <statusCode>,    \"message\": <message>,    \"links\" : [ {       \"rel\" : \"...\",       \"href\" : \"...\"     } ] }   ```   The `status` property is the same as the HTTP status returned in the response, to ease client parsing. The message  property is a localized message in the request client's locale (if applicable) that articulates the nature of the  error. The last property is the `links` property. This may contain additional  [hypermedia links](#section/Overview/Authentication) to troubleshoot.  #### Search Criteria <a section=\"section/Responses/SearchCriteria\"></a>  Multiple resources make use of search criteria to match assets. Search criteria is an array of search filters. Each  search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The operator is a type and property-specific operating performed on the filtered property. The valid values for fields and operators are outlined in the table below.  Every filter also defines one or more values that are supplied to the operator. The valid values vary by operator and are outlined below.  ##### Fields  The following table outlines the search criteria fields and the available operators:  | Field                             | Operators                                                                                                                      | | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | | `alternate-address-type`          | `in`                                                                                                                           | | `container-image`                 | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is like` ` not like`                              | | `container-status`                | `is` ` is not`                                                                                                                 | | `containers`                      | `are`                                                                                                                          | | `criticality-tag`                 | `is` ` is not` ` is greater than` ` is less than` ` is applied` ` is not applied`                                              | | `custom-tag`                      | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `cve`                             | `is` ` is not` ` contains` ` does not contain`                                                                                 | | `cvss-access-complexity`          | `is` ` is not`                                                                                                                 | | `cvss-authentication-required`    | `is` ` is not`                                                                                                                 | | `cvss-access-vector`              | `is` ` is not`                                                                                                                 | | `cvss-availability-impact`        | `is` ` is not`                                                                                                                 | | `cvss-confidentiality-impact`     | `is` ` is not`                                                                                                                 | | `cvss-integrity-impact`           | `is` ` is not`                                                                                                                 | | `cvss-v3-confidentiality-impact`  | `is` ` is not`                                                                                                                 | | `cvss-v3-integrity-impact`        | `is` ` is not`                                                                                                                 | | `cvss-v3-availability-impact`     | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-vector`           | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-complexity`       | `is` ` is not`                                                                                                                 | | `cvss-v3-user-interaction`        | `is` ` is not`                                                                                                                 | | `cvss-v3-privileges-required`     | `is` ` is not`                                                                                                                 | | `host-name`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is empty` ` is not empty` ` is like` ` not like`  | | `host-type`                       | `in` ` not in`                                                                                                                 | | `ip-address`                      | `is` ` is not` ` in range` ` not in range` ` is like` ` not like`                                                              | | `ip-address-type`                 | `in` ` not in`                                                                                                                 | | `last-scan-date`                  | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `location-tag`                    | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `mobile-device-last-sync-time`    | `is-within-the-last` ` is earlier than`                                                                                        | | `open-ports`                      | `is` ` is not` ` in range`                                                                                                     | | `operating-system`                | `contains` ` does not contain` ` is empty` ` is not empty`                                                                     | | `owner-tag`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `pci-compliance`                  | `is`                                                                                                                           | | `risk-score`                      | `is` ` is not` ` in range` ` greater than` ` less than`                                                                        | | `service-name`                    | `contains` ` does not contain`                                                                                                 | | `site-id`                         | `in` ` not in`                                                                                                                 | | `software`                        | `contains` ` does not contain`                                                                                                 | | `vAsset-cluster`                  | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-datacenter`               | `is` ` is not`                                                                                                                 | | `vAsset-host-name`                | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-power-state`              | `in` ` not in`                                                                                                                 | | `vAsset-resource-pool-path`       | `contains` ` does not contain`                                                                                                 | | `vulnerability-assessed`          | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `vulnerability-category`          | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain`                                                     | | `vulnerability-cvss-v3-score`     | `is` ` is not`                                                                                                                 | | `vulnerability-cvss-score`        | `is` ` is not` ` in range` ` is greater than` ` is less than`                                                                  | | `vulnerability-exposures`         | `includes` ` does not include`                                                                                                 | | `vulnerability-title`             | `contains` ` does not contain` ` is` ` is not` ` starts with` ` ends with`                                                     | | `vulnerability-validated-status`  | `are`                                                                                                                          |  ##### Enumerated Properties  The following fields have enumerated values:  | Field                                     | Acceptable Values                                                                                             | | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- | | `alternate-address-type`                  | 0=IPv4, 1=IPv6                                                                                                | | `containers`                              | 0=present, 1=not present                                                                                      | | `container-status`                        | `created` `running` `paused` `restarting` `exited` `dead` `unknown`                                           | | `cvss-access-complexity`                  | <ul><li><code>L</code> = Low</li><li><code>M</code> = Medium</li><li><code>H</code> = High</li></ul>          | | `cvss-integrity-impact`                   | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-confidentiality-impact`             | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-availability-impact`                | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-access-vector`                      | <ul><li><code>L</code> = Local</li><li><code>A</code> = Adjacent</li><li><code>N</code> = Network</li></ul>   | | `cvss-authentication-required`            | <ul><li><code>N</code> = None</li><li><code>S</code> = Single</li><li><code>M</code> = Multiple</li></ul>     | | `cvss-v3-confidentiality-impact`     | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-integrity-impact`            | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-availability-impact`             | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `cvss-v3-attack-vector`                | <ul><li><code>N</code> = Network</li><li><code>A</code> = Adjacent</li><li><code>L</code> = Local</li><li><code>P</code> = Physical</li></ul>    | | `cvss-v3-attack-complexity`                      | <ul><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>   | | `cvss-v3-user-interaction`            | <ul><li><code>N</code> = None</li><li><code>R</code> = Required</li></ul>     | | `cvss-v3-privileges-required`         | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `host-type`                               | 0=Unknown, 1=Guest, 2=Hypervisor, 3=Physical, 4=Mobile                                                        | | `ip-address-type`                         | 0=IPv4, 1=IPv6                                                                                                | | `pci-compliance`                          | 0=fail, 1=pass                                                                                                | | `vulnerability-validated-status`          | 0=present, 1=not present                                                                                      |  ##### Operator Properties <a section=\"section/Responses/SearchCriteria/OperatorProperties\"></a>  The following table outlines which properties are required for each operator and the appropriate data type(s):  | Operator              | `value`               | `lower`               | `upper`               | | ----------------------|-----------------------|-----------------------|-----------------------| | `are`                 | `string`              |                       |                       | | `contains`            | `string`              |                       |                       | | `does-not-contain`    | `string`              |                       |                       | | `ends with`           | `string`              |                       |                       | | `in`                  | `Array[ string ]`     |                       |                       | | `in-range`            |                       | `numeric`             | `numeric`             | | `includes`            | `Array[ string ]`     |                       |                       | | `is`                  | `string`              |                       |                       | | `is-applied`          |                       |                       |                       | | `is-between`          |                       | `numeric`             | `numeric`             | | `is-earlier-than`     | `numeric`             |                       |                       | | `is-empty`            |                       |                       |                       | | `is-greater-than`     | `numeric`             |                       |                       | | `is-on-or-after`      | `string` (yyyy-MM-dd) |                       |                       | | `is-on-or-before`     | `string` (yyyy-MM-dd) |                       |                       | | `is-not`              | `string`              |                       |                       | | `is-not-applied`      |                       |                       |                       | | `is-not-empty`        |                       |                       |                       | | `is-within-the-last`  | `numeric`              |                       |                       | | `less-than`           | `string`              |                       |                       | | `like`                | `string`              |                       |                       | | `not-contains`        | `string`              |                       |                       | | `not-in`              | `Array[ string ]`     |                       |                       | | `not-in-range`        |                       | `numeric`             | `numeric`             | | `not-like`            | `string`              |                       |                       | | `starts-with`         | `string`              |                       |                       |  #### Discovery Connection Search Criteria <a section=\"section/Responses/DiscoverySearchCriteria\"></a>  Dynamic sites make use of search criteria to match assets from a discovery connection. Search criteria is an array of search filters.    Each search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The list of supported fields vary depending on the type of discovery connection configured  for the dynamic site (e.g vSphere, ActiveSync, etc.). The operator is a type and property-specific operating  performed on the filtered property. The valid values for fields outlined in the tables below and are grouped by the  type of connection.    Every filter also defines one or more values that are supplied to the operator. See  <a href=\"#section/Responses/SearchCriteria/OperatorProperties\">Search Criteria Operator Properties</a> for more  information on the valid values for each operator.    ##### Fields (ActiveSync)  This section documents search criteria information for ActiveSync discovery connections. The discovery connections  must be one of the following types: `\"activesync-ldap\"`, `\"activesync-office365\"`, or `\"activesync-powershell\"`.    The following table outlines the search criteria fields and the available operators for ActiveSync connections:  | Field                             | Operators                                                     | | --------------------------------- | ------------------------------------------------------------- | | `last-sync-time`                  | `is-within-the-last` ` is-earlier-than`                       | | `operating-system`                | `contains` ` does-not-contain`                                | | `user`                            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (AWS)  This section documents search criteria information for AWS discovery connections. The discovery connections must be the type `\"aws\"`.    The following table outlines the search criteria fields and the available operators for AWS connections:  | Field                   | Operators                                                     | | ----------------------- | ------------------------------------------------------------- | | `availability-zone`     | `contains` ` does-not-contain`                                | | `guest-os-family`       | `contains` ` does-not-contain`                                | | `instance-id`           | `contains` ` does-not-contain`                                | | `instance-name`         | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `instance-state`        | `in` ` not-in`                                                | | `instance-type`         | `in` ` not-in`                                                | | `ip-address`            | `in-range` ` not-in-range` ` is` ` is-not`                    | | `region`                | `in` ` not-in`                                                | | `vpc-id`                | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (DHCP)  This section documents search criteria information for DHCP discovery connections. The discovery connections must be the type `\"dhcp\"`.    The following table outlines the search criteria fields and the available operators for DHCP connections:  | Field           | Operators                                                     | | --------------- | ------------------------------------------------------------- | | `host-name`     | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `ip-address`    | `in-range` ` not-in-range` ` is` ` is-not`                    | | `mac-address`   | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (Sonar)  This section documents search criteria information for Sonar discovery connections. The discovery connections must be the type `\"sonar\"`.    The following table outlines the search criteria fields and the available operators for Sonar connections:  | Field               | Operators            | | ------------------- | -------------------- | | `search-domain`     | `contains` ` is`     | | `ip-address`        | `in-range` ` is`     | | `sonar-scan-date`   | `is-within-the-last` |  ##### Fields (vSphere)  This section documents search criteria information for vSphere discovery connections. The discovery connections must be the type `\"vsphere\"`.    The following table outlines the search criteria fields and the available operators for vSphere connections:  | Field                | Operators                                                                                  | | -------------------- | ------------------------------------------------------------------------------------------ | | `cluster`            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `data-center`        | `is` ` is-not`                                                                             | | `discovered-time`    | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `guest-os-family`    | `contains` ` does-not-contain`                                                             | | `host-name`          | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `ip-address`         | `in-range` ` not-in-range` ` is` ` is-not`                                                 | | `power-state`        | `in` ` not-in`                                                                             | | `resource-pool-path` | `contains` ` does-not-contain`                                                             | | `last-time-seen`     | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `vm`                 | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              |  ##### Enumerated Properties (vSphere)  The following fields have enumerated values:  | Field         | Acceptable Values                    | | ------------- | ------------------------------------ | | `power-state` | `poweredOn` `poweredOff` `suspended` |  ## HATEOAS  This API follows Hypermedia as the Engine of Application State (HATEOAS) principals and is therefore hypermedia friendly.  Hyperlinks are returned in the `links` property of any given resource and contain a fully-qualified hyperlink to the corresponding resource. The format of the hypermedia link adheres to both the <a target=\"_blank\" href=\"http://jsonapi.org\">{json:api} v1</a>  <a target=\"_blank\" href=\"http://jsonapi.org/format/#document-links\">\"Link Object\"</a> and  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html\">JSON Hyper-Schema</a>  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html#rfc.section.5.2\">\"Link Description Object\"</a> formats. For example:  ```json \"links\": [{   \"rel\": \"<relation>\",   \"href\": \"<href>\"   ... }] ```  Where appropriate link objects may also contain additional properties than the `rel` and `href` properties, such as `id`, `type`, etc.  See the [Root](#tag/Root) resources for the entry points into API discovery.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.range_resource import RangeResource  # noqa: F401,E501
from rapid7vmconsole.models.remediation_resource import RemediationResource  # noqa: F401,E501
from rapid7vmconsole.models.report_config_database_resource import ReportConfigDatabaseResource  # noqa: F401,E501
from rapid7vmconsole.models.report_config_filters_resource import ReportConfigFiltersResource  # noqa: F401,E501
from rapid7vmconsole.models.report_config_scope_resource import ReportConfigScopeResource  # noqa: F401,E501
from rapid7vmconsole.models.report_email import ReportEmail  # noqa: F401,E501
from rapid7vmconsole.models.report_frequency import ReportFrequency  # noqa: F401,E501
from rapid7vmconsole.models.report_storage import ReportStorage  # noqa: F401,E501
from rapid7vmconsole.models.risk_trend_resource import RiskTrendResource  # noqa: F401,E501


class Report(object):
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
        'baseline': 'object',
        'bureau': 'str',
        'component': 'str',
        'database': 'ReportConfigDatabaseResource',
        'email': 'ReportEmail',
        'enclave': 'str',
        'filters': 'ReportConfigFiltersResource',
        'format': 'str',
        'frequency': 'ReportFrequency',
        'id': 'int',
        'language': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'organization': 'str',
        'owner': 'int',
        'policies': 'list[int]',
        'policy': 'int',
        'query': 'str',
        'range': 'RangeResource',
        'remediation': 'RemediationResource',
        'risk_trend': 'RiskTrendResource',
        'scope': 'ReportConfigScopeResource',
        'storage': 'ReportStorage',
        'template': 'str',
        'timezone': 'str',
        'users': 'list[int]',
        'version': 'str'
    }

    attribute_map = {
        'baseline': 'baseline',
        'bureau': 'bureau',
        'component': 'component',
        'database': 'database',
        'email': 'email',
        'enclave': 'enclave',
        'filters': 'filters',
        'format': 'format',
        'frequency': 'frequency',
        'id': 'id',
        'language': 'language',
        'links': 'links',
        'name': 'name',
        'organization': 'organization',
        'owner': 'owner',
        'policies': 'policies',
        'policy': 'policy',
        'query': 'query',
        'range': 'range',
        'remediation': 'remediation',
        'risk_trend': 'riskTrend',
        'scope': 'scope',
        'storage': 'storage',
        'template': 'template',
        'timezone': 'timezone',
        'users': 'users',
        'version': 'version'
    }

    def __init__(self, baseline=None, bureau=None, component=None, database=None, email=None, enclave=None, filters=None, format=None, frequency=None, id=None, language=None, links=None, name=None, organization=None, owner=None, policies=None, policy=None, query=None, range=None, remediation=None, risk_trend=None, scope=None, storage=None, template=None, timezone=None, users=None, version=None):  # noqa: E501
        """Report - a model defined in Swagger"""  # noqa: E501

        self._baseline = None
        self._bureau = None
        self._component = None
        self._database = None
        self._email = None
        self._enclave = None
        self._filters = None
        self._format = None
        self._frequency = None
        self._id = None
        self._language = None
        self._links = None
        self._name = None
        self._organization = None
        self._owner = None
        self._policies = None
        self._policy = None
        self._query = None
        self._range = None
        self._remediation = None
        self._risk_trend = None
        self._scope = None
        self._storage = None
        self._template = None
        self._timezone = None
        self._users = None
        self._version = None
        self.discriminator = None

        if baseline is not None:
            self.baseline = baseline
        if bureau is not None:
            self.bureau = bureau
        if component is not None:
            self.component = component
        if database is not None:
            self.database = database
        if email is not None:
            self.email = email
        if enclave is not None:
            self.enclave = enclave
        if filters is not None:
            self.filters = filters
        if format is not None:
            self.format = format
        if frequency is not None:
            self.frequency = frequency
        if id is not None:
            self.id = id
        if language is not None:
            self.language = language
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if owner is not None:
            self.owner = owner
        if policies is not None:
            self.policies = policies
        if policy is not None:
            self.policy = policy
        if query is not None:
            self.query = query
        if range is not None:
            self.range = range
        if remediation is not None:
            self.remediation = remediation
        if risk_trend is not None:
            self.risk_trend = risk_trend
        if scope is not None:
            self.scope = scope
        if storage is not None:
            self.storage = storage
        if template is not None:
            self.template = template
        if timezone is not None:
            self.timezone = timezone
        if users is not None:
            self.users = users
        if version is not None:
            self.version = version

    @property
    def baseline(self):
        """Gets the baseline of this Report.  # noqa: E501

        If the template is `baseline-comparison` or `executive-overview` the baseline scan to compare against. This can be the `first` scan, the `previous` scan, or a scan as of a specified date.  # noqa: E501

        :return: The baseline of this Report.  # noqa: E501
        :rtype: object
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        """Sets the baseline of this Report.

        If the template is `baseline-comparison` or `executive-overview` the baseline scan to compare against. This can be the `first` scan, the `previous` scan, or a scan as of a specified date.  # noqa: E501

        :param baseline: The baseline of this Report.  # noqa: E501
        :type: object
        """

        self._baseline = baseline

    @property
    def bureau(self):
        """Gets the bureau of this Report.  # noqa: E501

        The name of the bureau for a CyberScope report. Only used when the format is `\"cyberscope-xml\"`.  # noqa: E501

        :return: The bureau of this Report.  # noqa: E501
        :rtype: str
        """
        return self._bureau

    @bureau.setter
    def bureau(self, bureau):
        """Sets the bureau of this Report.

        The name of the bureau for a CyberScope report. Only used when the format is `\"cyberscope-xml\"`.  # noqa: E501

        :param bureau: The bureau of this Report.  # noqa: E501
        :type: str
        """

        self._bureau = bureau

    @property
    def component(self):
        """Gets the component of this Report.  # noqa: E501

        The name of the component for a CyberScope report. Only used when the format is `\"cyberscope-xml\"`.  # noqa: E501

        :return: The component of this Report.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this Report.

        The name of the component for a CyberScope report. Only used when the format is `\"cyberscope-xml\"`.  # noqa: E501

        :param component: The component of this Report.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def database(self):
        """Gets the database of this Report.  # noqa: E501

        Configuration for database export. Only used when the format is `\"database-export\"`.  # noqa: E501

        :return: The database of this Report.  # noqa: E501
        :rtype: ReportConfigDatabaseResource
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this Report.

        Configuration for database export. Only used when the format is `\"database-export\"`.  # noqa: E501

        :param database: The database of this Report.  # noqa: E501
        :type: ReportConfigDatabaseResource
        """

        self._database = database

    @property
    def email(self):
        """Gets the email of this Report.  # noqa: E501

        Email distribution settings for the report.  # noqa: E501

        :return: The email of this Report.  # noqa: E501
        :rtype: ReportEmail
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Report.

        Email distribution settings for the report.  # noqa: E501

        :param email: The email of this Report.  # noqa: E501
        :type: ReportEmail
        """

        self._email = email

    @property
    def enclave(self):
        """Gets the enclave of this Report.  # noqa: E501

        The name of the enclave for a CyberScope report. Only used when the format is `\"cyberscope-xml\"`.  # noqa: E501

        :return: The enclave of this Report.  # noqa: E501
        :rtype: str
        """
        return self._enclave

    @enclave.setter
    def enclave(self, enclave):
        """Sets the enclave of this Report.

        The name of the enclave for a CyberScope report. Only used when the format is `\"cyberscope-xml\"`.  # noqa: E501

        :param enclave: The enclave of this Report.  # noqa: E501
        :type: str
        """

        self._enclave = enclave

    @property
    def filters(self):
        """Gets the filters of this Report.  # noqa: E501

        Filters applied to the contents of the report. The supported filters for a report vary  by format and template.  <div class=\"properties\">  <div class=\"property-info\">  <span class=\"property-name\">categories</span> <span class=\"param-type complex\">Object</span>  <div class=\"redoc-markdown-block\">The vulnerability categories to include or exclude in the report. Only included or excluded may be specified, not both.</div> </div>  <div class=\"properties nested\">  <div class=\"property-info\">  <span class=\"property-name\">included</span> <span class=\"param-type param-array-format integer\">Array[string]</span>  <div class=\"redoc-markdown-block\">The identifiers of the vulnerability categories to included in the report.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">excluded</span> <span class=\"param-type param-array-format integer\">Array[string]</span>  <div class=\"redoc-markdown-block\">The identifiers of the vulnerability categories to exclude in the report.</div>  </div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">severity</span> <span class=\"param-type\">string</span>  <div class=\"param-enum\">  <span class=\"param-enum-value string\">\"all\"</span>  <span class=\"param-enum-value string\">\"critical\"</span>  <span class=\"param-enum-value string\">\"critical-and-severe\"</span>  </div>  <div class=\"redoc-markdown-block\">The vulnerability severities to include in the report.</div> </div>  <div class=\"property-info\">  <span class=\"property-name\">statuses</span> <span class=\"param-type param-array-format integer\">Array[string]</span>  <div class=\"param-enum\">  <span class=\"param-enum-value string\">\"vulnerable\"</span>  <span class=\"param-enum-value string\">\"vulnerable-version\"</span>  <span class=\"param-enum-value string\">\"potentially-vulnerable\"</span>  <span class=\"param-enum-value string\">\"vulnerable-and-validated\"</span>  </div>  <div class=\"redoc-markdown-block\">The vulnerability statuses to include in the report. If <code>\"vulnerable-and-validated\"</code> is selected  no other values can be specified. </div>  </div>  </div>  The following filter elements may be defined for non-templatized report formats:  | Format                                | Categories     | Severity   | Statuses   |  | ------------------------------------- |:--------------:|:----------:|:----------:|  | `arf-xml`                             |                |            |            |  | `csv-export`                          | &check;        | &check;    | &check;    |  | `cyberscope-xml`                      |                |            |            |  | `database-export`                     |                |            |            |  | `nexpose-simple-xml`                  | &check;        | &check;    |            |  | `oval-xml`                            |                |            |            |  | `qualys-xml`                          | &check;        | &check;    |            |  | `scap-xml`                            | &check;        | &check;    |            |  | `sql-query`                           | &check;        | &check;    | &check;    |  | `xccdf-csv`                           |                |            |            |  | `xccdf-xml`                           | &check;        | &check;    |            |  | `xml-export`                          | &check;        | &check;    | &check;    |  | `xml-export-v2`                       | &check;        | &check;    | &check;    |   The following filter elements may be defined for templatized report formats:  | Template                                | Categories     | Severity   | Statuses   |  | --------------------------------------- |:--------------:|:----------:|:----------:|  | `audit-report`                          | &check;        | &check;    |            |  | `baseline-comparison`                   |                |            |            |  | `basic-vulnerability-check-results`     | &check;        | &check;    | &check;    |  | `executive-overview`                    |                |            |            |  | `highest-risk-vulns`                    |                |            |            |  | `pci-attestation-v12`                   |                |            |            |  | `pci-executive-summary-v12`             |                |            |            |  | `pci-vuln-details-v12`                  |                |            |            |  | `policy-details`                        | &check;        | &check;    | &check;    |  | `policy-eval`                           |                |            |            |  | `policy-summary`                        | &check;        | &check;    | &check;    |  | `prioritized-remediations`              | &check;        | &check;    | &check;    |  | `prioritized-remediations-with-details` | &check;        | &check;    | &check;    |  | `r7-discovered-assets`                  | &check;        | &check;    | &check;    |  | `r7-vulnerability-exceptions`           | &check;        | &check;    | &check;    |  | `remediation-plan`                      | &check;        | &check;    |            |  | `report-card`                           | &check;        | &check;    |            |  | `risk-scorecard`                        | &check;        | &check;    | &check;    |  | `rule-breakdown-summary`                | &check;        | &check;    | &check;    |  | `top-policy-remediations`               | &check;        | &check;    | &check;    |  | `top-policy-remediations-with-details`  | &check;        | &check;    | &check;    |  | `top-riskiest-assets`                   | &check;        | &check;    | &check;    |  | `top-vulnerable-assets`                 | &check;        | &check;    | &check;    |  | `vulnerability-trends`                  | &check;        | &check;    | &check;    |    # noqa: E501

        :return: The filters of this Report.  # noqa: E501
        :rtype: ReportConfigFiltersResource
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this Report.

        Filters applied to the contents of the report. The supported filters for a report vary  by format and template.  <div class=\"properties\">  <div class=\"property-info\">  <span class=\"property-name\">categories</span> <span class=\"param-type complex\">Object</span>  <div class=\"redoc-markdown-block\">The vulnerability categories to include or exclude in the report. Only included or excluded may be specified, not both.</div> </div>  <div class=\"properties nested\">  <div class=\"property-info\">  <span class=\"property-name\">included</span> <span class=\"param-type param-array-format integer\">Array[string]</span>  <div class=\"redoc-markdown-block\">The identifiers of the vulnerability categories to included in the report.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">excluded</span> <span class=\"param-type param-array-format integer\">Array[string]</span>  <div class=\"redoc-markdown-block\">The identifiers of the vulnerability categories to exclude in the report.</div>  </div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">severity</span> <span class=\"param-type\">string</span>  <div class=\"param-enum\">  <span class=\"param-enum-value string\">\"all\"</span>  <span class=\"param-enum-value string\">\"critical\"</span>  <span class=\"param-enum-value string\">\"critical-and-severe\"</span>  </div>  <div class=\"redoc-markdown-block\">The vulnerability severities to include in the report.</div> </div>  <div class=\"property-info\">  <span class=\"property-name\">statuses</span> <span class=\"param-type param-array-format integer\">Array[string]</span>  <div class=\"param-enum\">  <span class=\"param-enum-value string\">\"vulnerable\"</span>  <span class=\"param-enum-value string\">\"vulnerable-version\"</span>  <span class=\"param-enum-value string\">\"potentially-vulnerable\"</span>  <span class=\"param-enum-value string\">\"vulnerable-and-validated\"</span>  </div>  <div class=\"redoc-markdown-block\">The vulnerability statuses to include in the report. If <code>\"vulnerable-and-validated\"</code> is selected  no other values can be specified. </div>  </div>  </div>  The following filter elements may be defined for non-templatized report formats:  | Format                                | Categories     | Severity   | Statuses   |  | ------------------------------------- |:--------------:|:----------:|:----------:|  | `arf-xml`                             |                |            |            |  | `csv-export`                          | &check;        | &check;    | &check;    |  | `cyberscope-xml`                      |                |            |            |  | `database-export`                     |                |            |            |  | `nexpose-simple-xml`                  | &check;        | &check;    |            |  | `oval-xml`                            |                |            |            |  | `qualys-xml`                          | &check;        | &check;    |            |  | `scap-xml`                            | &check;        | &check;    |            |  | `sql-query`                           | &check;        | &check;    | &check;    |  | `xccdf-csv`                           |                |            |            |  | `xccdf-xml`                           | &check;        | &check;    |            |  | `xml-export`                          | &check;        | &check;    | &check;    |  | `xml-export-v2`                       | &check;        | &check;    | &check;    |   The following filter elements may be defined for templatized report formats:  | Template                                | Categories     | Severity   | Statuses   |  | --------------------------------------- |:--------------:|:----------:|:----------:|  | `audit-report`                          | &check;        | &check;    |            |  | `baseline-comparison`                   |                |            |            |  | `basic-vulnerability-check-results`     | &check;        | &check;    | &check;    |  | `executive-overview`                    |                |            |            |  | `highest-risk-vulns`                    |                |            |            |  | `pci-attestation-v12`                   |                |            |            |  | `pci-executive-summary-v12`             |                |            |            |  | `pci-vuln-details-v12`                  |                |            |            |  | `policy-details`                        | &check;        | &check;    | &check;    |  | `policy-eval`                           |                |            |            |  | `policy-summary`                        | &check;        | &check;    | &check;    |  | `prioritized-remediations`              | &check;        | &check;    | &check;    |  | `prioritized-remediations-with-details` | &check;        | &check;    | &check;    |  | `r7-discovered-assets`                  | &check;        | &check;    | &check;    |  | `r7-vulnerability-exceptions`           | &check;        | &check;    | &check;    |  | `remediation-plan`                      | &check;        | &check;    |            |  | `report-card`                           | &check;        | &check;    |            |  | `risk-scorecard`                        | &check;        | &check;    | &check;    |  | `rule-breakdown-summary`                | &check;        | &check;    | &check;    |  | `top-policy-remediations`               | &check;        | &check;    | &check;    |  | `top-policy-remediations-with-details`  | &check;        | &check;    | &check;    |  | `top-riskiest-assets`                   | &check;        | &check;    | &check;    |  | `top-vulnerable-assets`                 | &check;        | &check;    | &check;    |  | `vulnerability-trends`                  | &check;        | &check;    | &check;    |    # noqa: E501

        :param filters: The filters of this Report.  # noqa: E501
        :type: ReportConfigFiltersResource
        """

        self._filters = filters

    @property
    def format(self):
        """Gets the format of this Report.  # noqa: E501

        The output format of the report. The format will restrict the available templates and parameters that can be specified.  # noqa: E501

        :return: The format of this Report.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Report.

        The output format of the report. The format will restrict the available templates and parameters that can be specified.  # noqa: E501

        :param format: The format of this Report.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def frequency(self):
        """Gets the frequency of this Report.  # noqa: E501

        The recurring frequency with which to generate the report.  # noqa: E501

        :return: The frequency of this Report.  # noqa: E501
        :rtype: ReportFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this Report.

        The recurring frequency with which to generate the report.  # noqa: E501

        :param frequency: The frequency of this Report.  # noqa: E501
        :type: ReportFrequency
        """

        self._frequency = frequency

    @property
    def id(self):
        """Gets the id of this Report.  # noqa: E501

        The identifier of the report.  # noqa: E501

        :return: The id of this Report.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Report.

        The identifier of the report.  # noqa: E501

        :param id: The id of this Report.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def language(self):
        """Gets the language of this Report.  # noqa: E501

        The locale (language) in which the report is generated  # noqa: E501

        :return: The language of this Report.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Report.

        The locale (language) in which the report is generated  # noqa: E501

        :param language: The language of this Report.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def links(self):
        """Gets the links of this Report.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Report.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Report.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Report.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this Report.  # noqa: E501

        The name of the report.  # noqa: E501

        :return: The name of this Report.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Report.

        The name of the report.  # noqa: E501

        :param name: The name of this Report.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this Report.  # noqa: E501

        The organization used for a XCCDF XML report. Only used when the format is `\"xccdf-xml\"`.  # noqa: E501

        :return: The organization of this Report.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Report.

        The organization used for a XCCDF XML report. Only used when the format is `\"xccdf-xml\"`.  # noqa: E501

        :param organization: The organization of this Report.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def owner(self):
        """Gets the owner of this Report.  # noqa: E501

        The identifier of the report owner.  # noqa: E501

        :return: The owner of this Report.  # noqa: E501
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Report.

        The identifier of the report owner.  # noqa: E501

        :param owner: The owner of this Report.  # noqa: E501
        :type: int
        """

        self._owner = owner

    @property
    def policies(self):
        """Gets the policies of this Report.  # noqa: E501

        If the template is `rule-breakdown-summary`, `top-policy-remediations`, or `top-policy-remediations-with-details` the identifiers of the policies to report against.  # noqa: E501

        :return: The policies of this Report.  # noqa: E501
        :rtype: list[int]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this Report.

        If the template is `rule-breakdown-summary`, `top-policy-remediations`, or `top-policy-remediations-with-details` the identifiers of the policies to report against.  # noqa: E501

        :param policies: The policies of this Report.  # noqa: E501
        :type: list[int]
        """

        self._policies = policies

    @property
    def policy(self):
        """Gets the policy of this Report.  # noqa: E501

        The policy to report on. Only used when the format is `\"oval-xml\"`, `\"\"xccdf-csv\"`, or `\"xccdf-xml\"`.  # noqa: E501

        :return: The policy of this Report.  # noqa: E501
        :rtype: int
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this Report.

        The policy to report on. Only used when the format is `\"oval-xml\"`, `\"\"xccdf-csv\"`, or `\"xccdf-xml\"`.  # noqa: E501

        :param policy: The policy of this Report.  # noqa: E501
        :type: int
        """

        self._policy = policy

    @property
    def query(self):
        """Gets the query of this Report.  # noqa: E501

        SQL query to run against the Reporting Data Model. Only used when the format is `\"sql-query\"`.  # noqa: E501

        :return: The query of this Report.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Report.

        SQL query to run against the Reporting Data Model. Only used when the format is `\"sql-query\"`.  # noqa: E501

        :param query: The query of this Report.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def range(self):
        """Gets the range of this Report.  # noqa: E501

        If the template is `vulnerability-trends`, `r7-vulnerability-exceptions`, or `r7-discovered-assets` the date range to trend over.  # noqa: E501

        :return: The range of this Report.  # noqa: E501
        :rtype: RangeResource
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this Report.

        If the template is `vulnerability-trends`, `r7-vulnerability-exceptions`, or `r7-discovered-assets` the date range to trend over.  # noqa: E501

        :param range: The range of this Report.  # noqa: E501
        :type: RangeResource
        """

        self._range = range

    @property
    def remediation(self):
        """Gets the remediation of this Report.  # noqa: E501

        If the template is `prioritized-remediations`, `prioritized-remediations-with-details`, `top-policy-remediations`, or `top-policy-remediations-with-details` the remediation display settings.  # noqa: E501

        :return: The remediation of this Report.  # noqa: E501
        :rtype: RemediationResource
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this Report.

        If the template is `prioritized-remediations`, `prioritized-remediations-with-details`, `top-policy-remediations`, or `top-policy-remediations-with-details` the remediation display settings.  # noqa: E501

        :param remediation: The remediation of this Report.  # noqa: E501
        :type: RemediationResource
        """

        self._remediation = remediation

    @property
    def risk_trend(self):
        """Gets the risk_trend of this Report.  # noqa: E501

        Configuration details for risk trending output.  # noqa: E501

        :return: The risk_trend of this Report.  # noqa: E501
        :rtype: RiskTrendResource
        """
        return self._risk_trend

    @risk_trend.setter
    def risk_trend(self, risk_trend):
        """Sets the risk_trend of this Report.

        Configuration details for risk trending output.  # noqa: E501

        :param risk_trend: The risk_trend of this Report.  # noqa: E501
        :type: RiskTrendResource
        """

        self._risk_trend = risk_trend

    @property
    def scope(self):
        """Gets the scope of this Report.  # noqa: E501

        The scope of the report. Scope is an object that has the following properties that vary by format and template:  <div class=\"properties\">  <div class=\"property-info\">  <span class=\"property-name\">assets</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the assets to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">sites</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the sites to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">assetGroups</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the asset to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">tags</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the tag to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">scan</span> <span class=\"param-type param-array-format integer\">integer &lt;int32&gt;</span>  <div class=\"redoc-markdown-block\">The identifier of the scan to report on.</div>  </div>  </div>  The following scope elements may be defined for non-templatized report formats:  | Format                                | Assets     | Sites   | Asset Groups | Tags    | Scan      |  | ------------------------------------- |:----------:|:-------:|:------------:|:-------:|:---------:|  | `arf-xml`                             | &check;    | &check; | &check;      | &check; |           |  | `csv-export`                          | &check;    | &check; | &check;      | &check; | &check;   |  | `cyberscope-xml`                      | &check;    | &check; | &check;      | &check; | &check;   |  | `database-export`                     |            | &check; |              |         |           |  | `nexpose-simple-xml`                  | &check;    | &check; | &check;      | &check; | &check;   |  | `oval-xml`                            | &check;    | &check; | &check;      | &check; |           |  | `qualys-xml`                          | &check;    | &check; | &check;      | &check; | &check;   |  | `scap-xml`                            | &check;    | &check; | &check;      | &check; | &check;   |  | `sql-query`                           | &check;    | &check; | &check;      | &check; | &check;   |  | `xccdf-csv`                           | &check;    |         |              |         |           |  | `xccdf-xml`                           | &check;    | &check; | &check;      | &check; | &check;   |  | `xml-export`                          | &check;    | &check; | &check;      | &check; | &check;   |  | `xml-export-v2`                       | &check;    | &check; | &check;      | &check; | &check;   |   The following scope elements may be defined for templatized report formats:  | Template                                 | Assets     | Sites   | Asset Groups | Tags    | Scan    |  | -----------------------------------------|:----------:|:-------:|:------------:|:-------:|:-------:|  | `audit-report`                           | &check;    | &check; |  &check;     | &check; | &check; |  | `baseline-comparison`                    | &check;    | &check; |  &check;     | &check; |         |  | `basic-vulnerability-check-results`      | &check;    | &check; |  &check;     | &check; | &check; |  | `executive-overview`                     | &check;    | &check; |  &check;     | &check; |         |  | `highest-risk-vulns`                     | &check;    | &check; |  &check;     | &check; |         |  | `pci-attestation-v12`                    | &check;    | &check; |  &check;     | &check; | &check; |  | `pci-executive-summary-v12`              | &check;    | &check; |  &check;     | &check; | &check; |  | `pci-vuln-details-v12`                   | &check;    | &check; |  &check;     | &check; | &check; |  | `policy-details`                         | &check;    | &check; |  &check;     | &check; |         |  | `policy-eval`                            | &check;    | &check; |  &check;     | &check; |         |  | `policy-summary`                         | &check;    | &check; |  &check;     | &check; | &check; |  | `prioritized-remediations`               | &check;    | &check; |  &check;     | &check; | &check; |  | `prioritized-remediations-with-details`  | &check;    | &check; |  &check;     | &check; | &check; |  | `r7-discovered-assets`                   | &check;    | &check; |  &check;     | &check; | &check; |  | `r7-vulnerability-exceptions`            | &check;    | &check; |  &check;     | &check; | &check; |  | `remediation-plan`                       | &check;    | &check; |  &check;     | &check; | &check; |  | `report-card`                            | &check;    | &check; |  &check;     | &check; | &check; |  | `risk-scorecard`                         | &check;    | &check; |  &check;     | &check; |         |  | `rule-breakdown-summary`                 | &check;    | &check; |  &check;     | &check; |         |  | `top-policy-remediations`                | &check;    | &check; |  &check;     | &check; |         |  | `top-policy-remediations-with-details`   | &check;    | &check; |  &check;     | &check; |         |  | `top-riskiest-assets`                    | &check;    | &check; |  &check;     | &check; | &check; |  | `top-vulnerable-assets`                  | &check;    | &check; |  &check;     | &check; | &check; |  | `vulnerability-trends`                   | &check;    | &check; |  &check;     | &check; |         |  If a report supports specifying a scan as the scope and a scan is specified, no other scope elements may be defined.  In all other cases as many different types of supported scope elements can be specified in any combination. All  reports except the `sql-query` format require at least one element to be specified as the scope.   # noqa: E501

        :return: The scope of this Report.  # noqa: E501
        :rtype: ReportConfigScopeResource
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Report.

        The scope of the report. Scope is an object that has the following properties that vary by format and template:  <div class=\"properties\">  <div class=\"property-info\">  <span class=\"property-name\">assets</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the assets to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">sites</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the sites to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">assetGroups</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the asset to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">tags</span> <span class=\"param-type param-array-format integer\">Array[integer &lt;int32&gt;]</span>  <div class=\"redoc-markdown-block\">The identifiers of the tag to report on.</div>  </div>  <div class=\"property-info\">  <span class=\"property-name\">scan</span> <span class=\"param-type param-array-format integer\">integer &lt;int32&gt;</span>  <div class=\"redoc-markdown-block\">The identifier of the scan to report on.</div>  </div>  </div>  The following scope elements may be defined for non-templatized report formats:  | Format                                | Assets     | Sites   | Asset Groups | Tags    | Scan      |  | ------------------------------------- |:----------:|:-------:|:------------:|:-------:|:---------:|  | `arf-xml`                             | &check;    | &check; | &check;      | &check; |           |  | `csv-export`                          | &check;    | &check; | &check;      | &check; | &check;   |  | `cyberscope-xml`                      | &check;    | &check; | &check;      | &check; | &check;   |  | `database-export`                     |            | &check; |              |         |           |  | `nexpose-simple-xml`                  | &check;    | &check; | &check;      | &check; | &check;   |  | `oval-xml`                            | &check;    | &check; | &check;      | &check; |           |  | `qualys-xml`                          | &check;    | &check; | &check;      | &check; | &check;   |  | `scap-xml`                            | &check;    | &check; | &check;      | &check; | &check;   |  | `sql-query`                           | &check;    | &check; | &check;      | &check; | &check;   |  | `xccdf-csv`                           | &check;    |         |              |         |           |  | `xccdf-xml`                           | &check;    | &check; | &check;      | &check; | &check;   |  | `xml-export`                          | &check;    | &check; | &check;      | &check; | &check;   |  | `xml-export-v2`                       | &check;    | &check; | &check;      | &check; | &check;   |   The following scope elements may be defined for templatized report formats:  | Template                                 | Assets     | Sites   | Asset Groups | Tags    | Scan    |  | -----------------------------------------|:----------:|:-------:|:------------:|:-------:|:-------:|  | `audit-report`                           | &check;    | &check; |  &check;     | &check; | &check; |  | `baseline-comparison`                    | &check;    | &check; |  &check;     | &check; |         |  | `basic-vulnerability-check-results`      | &check;    | &check; |  &check;     | &check; | &check; |  | `executive-overview`                     | &check;    | &check; |  &check;     | &check; |         |  | `highest-risk-vulns`                     | &check;    | &check; |  &check;     | &check; |         |  | `pci-attestation-v12`                    | &check;    | &check; |  &check;     | &check; | &check; |  | `pci-executive-summary-v12`              | &check;    | &check; |  &check;     | &check; | &check; |  | `pci-vuln-details-v12`                   | &check;    | &check; |  &check;     | &check; | &check; |  | `policy-details`                         | &check;    | &check; |  &check;     | &check; |         |  | `policy-eval`                            | &check;    | &check; |  &check;     | &check; |         |  | `policy-summary`                         | &check;    | &check; |  &check;     | &check; | &check; |  | `prioritized-remediations`               | &check;    | &check; |  &check;     | &check; | &check; |  | `prioritized-remediations-with-details`  | &check;    | &check; |  &check;     | &check; | &check; |  | `r7-discovered-assets`                   | &check;    | &check; |  &check;     | &check; | &check; |  | `r7-vulnerability-exceptions`            | &check;    | &check; |  &check;     | &check; | &check; |  | `remediation-plan`                       | &check;    | &check; |  &check;     | &check; | &check; |  | `report-card`                            | &check;    | &check; |  &check;     | &check; | &check; |  | `risk-scorecard`                         | &check;    | &check; |  &check;     | &check; |         |  | `rule-breakdown-summary`                 | &check;    | &check; |  &check;     | &check; |         |  | `top-policy-remediations`                | &check;    | &check; |  &check;     | &check; |         |  | `top-policy-remediations-with-details`   | &check;    | &check; |  &check;     | &check; |         |  | `top-riskiest-assets`                    | &check;    | &check; |  &check;     | &check; | &check; |  | `top-vulnerable-assets`                  | &check;    | &check; |  &check;     | &check; | &check; |  | `vulnerability-trends`                   | &check;    | &check; |  &check;     | &check; |         |  If a report supports specifying a scan as the scope and a scan is specified, no other scope elements may be defined.  In all other cases as many different types of supported scope elements can be specified in any combination. All  reports except the `sql-query` format require at least one element to be specified as the scope.   # noqa: E501

        :param scope: The scope of this Report.  # noqa: E501
        :type: ReportConfigScopeResource
        """

        self._scope = scope

    @property
    def storage(self):
        """Gets the storage of this Report.  # noqa: E501

        The additional storage location and path.  # noqa: E501

        :return: The storage of this Report.  # noqa: E501
        :rtype: ReportStorage
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this Report.

        The additional storage location and path.  # noqa: E501

        :param storage: The storage of this Report.  # noqa: E501
        :type: ReportStorage
        """

        self._storage = storage

    @property
    def template(self):
        """Gets the template of this Report.  # noqa: E501

        The template for the report (only required if the format is templatized).  # noqa: E501

        :return: The template of this Report.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Report.

        The template for the report (only required if the format is templatized).  # noqa: E501

        :param template: The template of this Report.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def timezone(self):
        """Gets the timezone of this Report.  # noqa: E501

        The timezone the report generates in, such as `\"America/Los_Angeles\"`.  # noqa: E501

        :return: The timezone of this Report.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Report.

        The timezone the report generates in, such as `\"America/Los_Angeles\"`.  # noqa: E501

        :param timezone: The timezone of this Report.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def users(self):
        """Gets the users of this Report.  # noqa: E501

        The identifiers of the users granted explicit access to the report.  # noqa: E501

        :return: The users of this Report.  # noqa: E501
        :rtype: list[int]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Report.

        The identifiers of the users granted explicit access to the report.  # noqa: E501

        :param users: The users of this Report.  # noqa: E501
        :type: list[int]
        """

        self._users = users

    @property
    def version(self):
        """Gets the version of this Report.  # noqa: E501

        The version of the report Data Model to report against. Only used when the format is `\"sql-query\"`.  # noqa: E501

        :return: The version of this Report.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Report.

        The version of the report Data Model to report against. Only used when the format is `\"sql-query\"`.  # noqa: E501

        :param version: The version of this Report.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
