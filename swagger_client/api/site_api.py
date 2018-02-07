# coding: utf-8

"""
    InsightVM API

    # Overview   This guide documents the InsightVM Application Programming Interface (API) Version 3. This API supports the Representation State Transfer (REST) design pattern. Unless noted otherwise this API accepts and produces the `application/json` media type. This API uses Hypermedia as the Engine of Application State (HATEOAS) and is hypermedia friendly. All API connections must be made to the security console using HTTPS.  ## Versioning  Versioning is specified in the URL and the base path of this API is: `https://<host>:<port>/api/3/`.  ## Specification  An <a target=\"_blank\" href=\"https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md\">OpenAPI v2</a> specification (also  known as Swagger 2) of this API is available. Tools such as <a target=\"_blank\" href=\"https://github.com/swagger-api/swagger-codegen\">swagger-codegen</a> can be used to generate an API client in the language of your choosing using this specification document.  <p class=\"openapi\">Download the specification: <a class=\"openapi-button\" target=\"_blank\" download=\"\" href=\"/api/3/json\"> Download </a></p>  ## Authentication  Authorization to the API uses HTTP Basic Authorization  (see <a target=\"_blank\" href=\"https://www.ietf.org/rfc/rfc2617.txt\">RFC 2617</a> for more information). Requests must  supply authorization credentials in the `Authorization` header using a Base64 encoded hash of `\"username:password\"`.  <!-- ReDoc-Inject: <security-definitions> -->  ### 2FA  This API supports two-factor authentication (2FA) by supplying an authentication token in addition to the Basic Authorization. The token is specified using the `Token` request header. To leverage two-factor authentication, this must be enabled on the console and be configured for the account accessing the API.  ## Resources  ### Naming  Resource names represent nouns and identify the entity being manipulated or accessed. All collection resources are  pluralized to indicate to the client they are interacting with a collection of multiple resources of the same type. Singular resource names are used when there exists only one resource available to interact with.  The following naming conventions are used by this API:  | Type                                          | Case                     | | --------------------------------------------- | ------------------------ | | Resource names                                | `lower_snake_case`       | | Header, body, and query parameters parameters | `camelCase`              | | JSON fields and property names                | `camelCase`              |  #### Collections  A collection resource is a parent resource for instance resources, but can itself be retrieved and operated on  independently. Collection resources use a pluralized resource name. The resource path for collection resources follow  the convention:  ``` /api/3/{resource_name} ```  #### Instances  An instance resource is a \"leaf\" level resource that may be retrieved, optionally nested within a collection resource. Instance resources are usually retrievable with opaque identifiers. The resource path for instance resources follows  the convention:  ``` /api/3/{resource_name}/{instance_id}... ```  ## Verbs  The following HTTP operations are supported throughout this API. The general usage of the operation and both its failure and success status codes are outlined below.    | Verb      | Usage                                                                                 | Success     | Failure                                                        | | --------- | ------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | | `GET`     | Used to retrieve a resource by identifier, or a collection of resources by type.      | `200`       | `400`, `401`, `402`, `404`, `405`, `408`, `410`, `415`, `500`  | | `POST`    | Creates a resource with an application-specified identifier.                          | `201`       | `400`, `401`, `404`, `405`, `408`, `413`, `415`, `500`         | | `POST`    | Performs a request to queue an asynchronous job.                                      | `202`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `PUT`     | Creates a resource with a client-specified identifier.                                | `200`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `PUT`     | Performs a full update of a resource with a specified identifier.                     | `201`       | `400`, `401`, `403`, `405`, `408`, `410`, `413`, `415`, `500`  | | `DELETE`  | Deletes a resource by identifier or an entire collection of resources.                | `204`       | `400`, `401`, `405`, `408`, `410`, `413`, `415`, `500`         | | `OPTIONS` | Requests what operations are available on a resource.                                 | `200`       | `401`, `404`, `405`, `408`, `500`                              |  ### Common Operations  #### OPTIONS  All resources respond to the `OPTIONS` request, which allows discoverability of available operations that are supported.  The `OPTIONS` response returns the acceptable HTTP operations on that resource within the `Allow` header. The response is always a `200 OK` status.  ### Collection Resources  Collection resources can support the `GET`, `POST`, `PUT`, and `DELETE` operations.  #### GET  The `GET` operation invoked on a collection resource indicates a request to retrieve all, or some, of the entities  contained within the collection. This also includes the optional capability to filter or search resources during the request. The response from a collection listing is a paginated document. See  [hypermedia links](#section/Overview/Paging) for more information.  #### POST  The `POST` is a non-idempotent operation that allows for the creation of a new resource when the resource identifier  is not provided by the system during the creation operation (i.e. the Security Console generates the identifier). The content of the `POST` request is sent in the request body. The response to a successful `POST` request should be a  `201 CREATED` with a valid `Location` header field set to the URI that can be used to access to the newly  created resource.   The `POST` to a collection resource can also be used to interact with asynchronous resources. In this situation,  instead of a `201 CREATED` response, the `202 ACCEPTED` response indicates that processing of the request is not fully  complete but has been accepted for future processing. This request will respond similarly with a `Location` header with  link to the job-oriented asynchronous resource that was created and/or queued.  #### PUT  The `PUT` is an idempotent operation that either performs a create with user-supplied identity, or a full replace or update of a resource by a known identifier. The response to a `PUT` operation to create an entity is a `201 Created` with a valid `Location` header field set to the URI that can be used to access to the newly created resource.  `PUT` on a collection resource replaces all values in the collection. The typical response to a `PUT` operation that  updates an entity is hypermedia links, which may link to related resources caused by the side-effects of the changes  performed.  #### DELETE  The `DELETE` is an idempotent operation that physically deletes a resource, or removes an association between resources. The typical response to a `DELETE` operation is hypermedia links, which may link to related resources caused by the  side-effects of the changes performed.  ### Instance Resources  Instance resources can support the `GET`, `PUT`, `POST`, `PATCH` and `DELETE` operations.  #### GET  Retrieves the details of a specific resource by its identifier. The details retrieved can be controlled through  property selection and property views. The content of the resource is returned within the body of the response in the  acceptable media type.   #### PUT  Allows for and idempotent \"full update\" (complete replacement) on a specific resource. If the resource does not exist,  it will be created; if it does exist, it is completely overwritten. Any omitted properties in the request are assumed to  be undefined/null. For \"partial updates\" use `POST` or `PATCH` instead.   The content of the `PUT` request is sent in the request body. The identifier of the resource is specified within the URL  (not the request body). The response to a successful `PUT` request is a `201 CREATED` to represent the created status,  with a valid `Location` header field set to the URI that can be used to access to the newly created (or fully replaced)  resource.   #### POST  Performs a non-idempotent creation of a new resource. The `POST` of an instance resource most commonly occurs with the  use of nested resources (e.g. searching on a parent collection resource). The response to a `POST` of an instance  resource is typically a `200 OK` if the resource is non-persistent, and a `201 CREATED` if there is a resource  created/persisted as a result of the operation. This varies by endpoint.  #### PATCH  The `PATCH` operation is used to perform a partial update of a resource. `PATCH` is a non-idempotent operation that enforces an atomic mutation of a resource. Only the properties specified in the request are to be overwritten on the  resource it is applied to. If a property is missing, it is assumed to not have changed.  #### DELETE  Permanently removes the individual resource from the system. If the resource is an association between resources, only  the association is removed, not the resources themselves. A successful deletion of the resource should return  `204 NO CONTENT` with no response body. This operation is not fully idempotent, as follow-up requests to delete a  non-existent resource should return a `404 NOT FOUND`.  ## Requests  Unless otherwise indicated, the default request body media type is `application/json`.  ### Headers  Commonly used request headers include:  | Header             | Example                                       | Purpose                                                                                        |                    | ------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------------- | | `Accept`           | `application/json`                            | Defines what acceptable content types are allowed by the client. For all types, use `*/*`.     | | `Accept-Encoding`  | `deflate, gzip`                               | Allows for the encoding to be specified (such as gzip).                                        | | `Accept-Language`  | `en-US`                                       | Indicates to the server the client's locale (defaults `en-US`).                                | | `Authorization `   | `Basic Base64(\"username:password\")`           | Basic authentication                                                                           | | `Token `           | `123456`                                      | Two-factor authentication token (if enabled)                                                   |  ### Dates & Times  Dates and/or times are specified as strings in the ISO 8601 format(s). The following formats are supported as input:  | Value                       | Format                                                 | Notes                                                 | | --------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | | Date                        | YYYY-MM-DD                                             | Defaults to 12 am UTC (if used for a date & time      | | Date & time only            | YYYY-MM-DD'T'hh:mm:ss[.nnn]                            | Defaults to UTC                                       | | Date & time in UTC          | YYYY-MM-DD'T'hh:mm:ss[.nnn]Z                           |                                                       | | Date & time w/ offset       | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm             |                                                       | | Date & time w/ zone-offset  | YYYY-MM-DD'T'hh:mm:ss[.nnn][+&#124;-]hh:mm[<zone-id>]  |                                                       |   ### Timezones  Timezones are specified in the regional zone format, such as `\"America/Los_Angeles\"`, `\"Asia/Tokyo\"`, or `\"GMT\"`.   ### Paging  Pagination is supported on certain collection resources using a combination of two query parameters, `page` and `size`.  As these are control parameters, they are prefixed with the underscore character. The page parameter dictates the  zero-based index of the page to retrieve, and the `size` indicates the size of the page.   For example, `/resources?page=2&size=10` will return page 3, with 10 records per page, giving results 21-30.  The maximum page size for a request is 500.  ### Sorting  Sorting is supported on paginated resources with the `sort` query parameter(s). The sort query parameter(s) supports  identifying a single or multi-property sort with a single or multi-direction output. The format of the parameter is:  ``` sort=property[,ASC|DESC]... ```  Therefore, the request `/resources?sort=name,title,DESC` would return the results sorted by the name and title  descending, in that order. The sort directions are either ascending `ASC` or descending `DESC`. With single-order  sorting, all properties are sorted in the same direction. To sort the results with varying orders by property,  multiple sort parameters are passed.    For example, the request `/resources?sort=name,ASC&sort=title,DESC` would sort by name ascending and title  descending, in that order.  ## Responses  The following response statuses may be returned by this API.     | Status | Meaning                  | Usage                                                                                                                                                                    | | ------ | ------------------------ |------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `200`  | OK                       | The operation performed without error according to the specification of the request, and no more specific 2xx code is suitable.                                          | | `201`  | Created                  | A create request has been fulfilled and a resource has been created. The resource is available as the URI specified in the response, including the `Location` header.    | | `202`  | Accepted                 | An asynchronous task has been accepted, but not guaranteed, to be processed in the future.                                                                               | | `400`  | Bad Request              | The request was invalid or cannot be otherwise served. The request is not likely to succeed in the future without modifications.                                         | | `401`  | Unauthorized             | The user is unauthorized to perform the operation requested, or does not maintain permissions to perform the operation on the resource specified.                        | | `403`  | Forbidden                | The resource exists to which the user has access, but the operating requested is not permitted.                                                                          | | `404`  | Not Found                | The resource specified could not be located, does not exist, or an unauthenticated client does not have permissions to a resource.                                       | | `405`  | Method Not Allowed       | The operations may not be performed on the specific resource. Allowed operations are returned and may be performed on the resource.                                      | | `408`  | Request Timeout          | The client has failed to complete a request in a timely manner and the request has been discarded.                                                                       | | `413`  | Request Entity Too Large | The request being provided is too large for the server to accept processing.                                                                                             | | `415`  | Unsupported Media Type   | The media type is not supported for the requested resource.                                                                                                              | | `500`  | Internal Server Error    | An internal and unexpected error has occurred on the server at no fault of the client.                                                                                   |  ### Security  The response statuses 401, 403 and 404 need special consideration for security purposes. As necessary,  error statuses and messages may be obscured to strengthen security and prevent information exposure. The following is a  guideline for privileged resource response statuses:  | Use Case                                                           | Access             | Resource           | Permission   | Status       | | ------------------------------------------------------------------ | ------------------ |------------------- | ------------ | ------------ | | Unauthenticated access to an unauthenticated resource.             | Unauthenticated    | Unauthenticated    | Yes          | `20x`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Authenticated      | No           | `401`        | | Unauthenticated access to an authenticated resource.               | Unauthenticated    | Non-existent       | No           | `401`        | | Authenticated access to a unauthenticated resource.                | Authenticated      | Unauthenticated    | Yes          | `20x`        | | Authenticated access to an authenticated, unprivileged resource.   | Authenticated      | Authenticated      | No           | `404`        | | Authenticated access to an authenticated, privileged resource.     | Authenticated      | Authenticated      | Yes          | `20x`        | | Authenticated access to an authenticated, non-existent resource    | Authenticated      | Non-existent       | Yes          | `404`        |  ### Headers  Commonly used response headers include:  | Header                     |  Example                          | Purpose                                                         | | -------------------------- | --------------------------------- | --------------------------------------------------------------- | | `Allow`                    | `OPTIONS, GET`                    | Defines the allowable HTTP operations on a resource.            | | `Cache-Control`            | `no-store, must-revalidate`       | Disables caching of resources (as they are all dynamic).        | | `Content-Encoding`         | `gzip`                            | The encoding of the response body (if any).                     | | `Location`                 |                                   | Refers to the URI of the resource created by a request.         | | `Transfer-Encoding`        | `chunked`                         | Specified the encoding used to transform response.              | | `Retry-After`              | 5000                              | Indicates the time to wait before retrying a request.           | | `X-Content-Type-Options`   | `nosniff`                         | Disables MIME type sniffing.                                    | | `X-XSS-Protection`         | `1; mode=block`                   | Enables XSS filter protection.                                  | | `X-Frame-Options`          | `SAMEORIGIN`                      | Prevents rendering in a frame from a different origin.          | | `X-UA-Compatible`          | `IE=edge,chrome=1`                | Specifies the browser mode to render in.                        |  ### Format  When `application/json` is returned in the response body it is always pretty-printed (indented, human readable output).  Additionally, gzip compression/encoding is supported on all responses.   #### Dates & Times  Dates or times are returned as strings in the ISO 8601 'extended' format. When a date and time is returned (instant) the value is converted to UTC.  For example:  | Value           | Format                         | Example               | | --------------- | ------------------------------ | --------------------- | | Date            | `YYYY-MM-DD`                   | 2017-12-03            | | Date & Time     | `YYYY-MM-DD'T'hh:mm:ss[.nnn]Z` | 2017-12-03T10:15:30Z  |  #### Content  In some resources a Content data type is used. This allows for multiple formats of representation to be returned within resource, specifically `\"html\"` and `\"text\"`. The `\"text\"` property returns a flattened representation suitable for output in textual displays. The `\"html\"` property returns an HTML fragment suitable for display within an HTML  element. Note, the HTML returned is not a valid stand-alone HTML document.  #### Paging  The response to a paginated request follows the format:  ```json {    resources\": [        ...     ],    \"page\": {        \"number\" : ...,       \"size\" : ...,       \"totalResources\" : ...,       \"totalPages\" : ...    },    \"links\": [        \"first\" : {          \"href\" : \"...\"        },        \"prev\" : {          \"href\" : \"...\"        },        \"self\" : {          \"href\" : \"...\"        },        \"next\" : {          \"href\" : \"...\"        },        \"last\" : {          \"href\" : \"...\"        }     ] } ```  The `resources` property is an array of the resources being retrieved from the endpoint, each which should contain at  minimum a \"self\" relation hypermedia link. The `page` property outlines the details of the current page and total possible pages. The object for the page includes the following properties:  - number - The page number (zero-based) of the page returned. - size - The size of the pages, which is less than or equal to the maximum page size. - totalResources - The total amount of resources available across all pages. - totalPages - The total amount of pages.  The last property of the paged response is the `links` array, which contains all available hypermedia links. For  paginated responses, the \"self\", \"next\", \"previous\", \"first\", and \"last\" links are returned. The \"self\" link must always be returned and should contain a link to allow the client to replicate the original request against the  collection resource in an identical manner to that in which it was invoked.   The \"next\" and \"previous\" links are present if either or both there exists a previous or next page, respectively.  The \"next\" and \"previous\" links have hrefs that allow \"natural movement\" to the next page, that is all parameters  required to move the next page are provided in the link. The \"first\" and \"last\" links provide references to the first and last pages respectively.   Requests outside the boundaries of the pageable will result in a `404 NOT FOUND`. Paginated requests do not provide a  \"stateful cursor\" to the client, nor does it need to provide a read consistent view. Records in adjacent pages may  change while pagination is being traversed, and the total number of pages and resources may change between requests  within the same filtered/queries resource collection.  #### Property Views  The \"depth\" of the response of a resource can be configured using a \"view\". All endpoints supports two views that can  tune the extent of the information returned in the resource. The supported views are `summary` and `details` (the default).  View are specified using a query parameter, in this format:  ```bash /<resource>?view={viewName} ```  #### Error  Any error responses can provide a response body with a message to the client indicating more information (if applicable)  to aid debugging of the error. All 40x and 50x responses will return an error response in the body. The format of the  response is as follows:  ```json {    \"status\": <statusCode>,    \"message\": <message>,    \"links\" : [ {       \"rel\" : \"...\",       \"href\" : \"...\"     } ] }   ```   The `status` property is the same as the HTTP status returned in the response, to ease client parsing. The message  property is a localized message in the request client's locale (if applicable) that articulates the nature of the  error. The last property is the `links` property. This may contain additional  [hypermedia links](#section/Overview/Authentication) to troubleshoot.  #### Search Criteria <a section=\"section/Responses/SearchCriteria\"></a>  Multiple resources make use of search criteria to match assets. Search criteria is an array of search filters. Each  search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The operator is a type and property-specific operating performed on the filtered property. The valid values for fields and operators are outlined in the table below.  Every filter also defines one or more values that are supplied to the operator. The valid values vary by operator and are outlined below.  ##### Fields  The following table outlines the search criteria fields and the available operators:  | Field                             | Operators                                                                                                                      | | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | | `alternate-address-type`          | `in`                                                                                                                           | | `container-image`                 | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is like` ` not like`                              | | `container-status`                | `is` ` is not`                                                                                                                 | | `containers`                      | `are`                                                                                                                          | | `criticality-tag`                 | `is` ` is not` ` is greater than` ` is less than` ` is applied` ` is not applied`                                              | | `custom-tag`                      | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `cve`                             | `is` ` is not` ` contains` ` does not contain`                                                                                 | | `cvss-access-complexity`          | `is` ` is not`                                                                                                                 | | `cvss-authentication-required`    | `is` ` is not`                                                                                                                 | | `cvss-access-vector`              | `is` ` is not`                                                                                                                 | | `cvss-availability-impact`        | `is` ` is not`                                                                                                                 | | `cvss-confidentiality-impact`     | `is` ` is not`                                                                                                                 | | `cvss-integrity-impact`           | `is` ` is not`                                                                                                                 | | `cvss-v3-confidentiality-impact`  | `is` ` is not`                                                                                                                 | | `cvss-v3-integrity-impact`        | `is` ` is not`                                                                                                                 | | `cvss-v3-availability-impact`     | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-vector`           | `is` ` is not`                                                                                                                 | | `cvss-v3-attack-complexity`       | `is` ` is not`                                                                                                                 | | `cvss-v3-user-interaction`        | `is` ` is not`                                                                                                                 | | `cvss-v3-privileges-required`     | `is` ` is not`                                                                                                                 | | `host-name`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is empty` ` is not empty` ` is like` ` not like`  | | `host-type`                       | `in` ` not in`                                                                                                                 | | `ip-address`                      | `is` ` is not` ` in range` ` not in range` ` is like` ` not like`                                                              | | `ip-address-type`                 | `in` ` not in`                                                                                                                 | | `last-scan-date`                  | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `location-tag`                    | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `mobile-device-last-sync-time`    | `is-within-the-last` ` is earlier than`                                                                                        | | `open-ports`                      | `is` ` is not` ` in range`                                                                                                     | | `operating-system`                | `contains` ` does not contain` ` is empty` ` is not empty`                                                                     | | `owner-tag`                       | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain` ` is applied` ` is not applied`                     | | `pci-compliance`                  | `is`                                                                                                                           | | `risk-score`                      | `is` ` is not` ` in range` ` greater than` ` less than`                                                                        | | `service-name`                    | `contains` ` does not contain`                                                                                                 | | `site-id`                         | `in` ` not in`                                                                                                                 | | `software`                        | `contains` ` does not contain`                                                                                                 | | `vAsset-cluster`                  | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-datacenter`               | `is` ` is not`                                                                                                                 | | `vAsset-host-name`                | `is` ` is not` ` contains` ` does not contain` ` starts with`                                                                  | | `vAsset-power-state`              | `in` ` not in`                                                                                                                 | | `vAsset-resource-pool-path`       | `contains` ` does not contain`                                                                                                 | | `vulnerability-assessed`          | `is-on-or-before` ` is on or after` ` is between` ` is earlier than` ` is within the last`                                     | | `vulnerability-category`          | `is` ` is not` ` starts with` ` ends with` ` contains` ` does not contain`                                                     | | `vulnerability-cvss-v3-score`     | `is` ` is not`                                                                                                                 | | `vulnerability-cvss-score`        | `is` ` is not` ` in range` ` is greater than` ` is less than`                                                                  | | `vulnerability-exposures`         | `includes` ` does not include`                                                                                                 | | `vulnerability-title`             | `contains` ` does not contain` ` is` ` is not` ` starts with` ` ends with`                                                     | | `vulnerability-validated-status`  | `are`                                                                                                                          |  ##### Enumerated Properties  The following fields have enumerated values:  | Field                                     | Acceptable Values                                                                                             | | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- | | `alternate-address-type`                  | 0=IPv4, 1=IPv6                                                                                                | | `containers`                              | 0=present, 1=not present                                                                                      | | `container-status`                        | `created` `running` `paused` `restarting` `exited` `dead` `unknown`                                           | | `cvss-access-complexity`                  | <ul><li><code>L</code> = Low</li><li><code>M</code> = Medium</li><li><code>H</code> = High</li></ul>          | | `cvss-integrity-impact`                   | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-confidentiality-impact`             | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-availability-impact`                | <ul><li><code>N</code> = None</li><li><code>P</code> = Partial</li><li><code>C</code> = Complete</li></ul>    | | `cvss-access-vector`                      | <ul><li><code>L</code> = Local</li><li><code>A</code> = Adjacent</li><li><code>N</code> = Network</li></ul>   | | `cvss-authentication-required`            | <ul><li><code>N</code> = None</li><li><code>S</code> = Single</li><li><code>M</code> = Multiple</li></ul>     | | `cvss-v3-confidentiality-impact`     | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-integrity-impact`            | <ul><li><code>L</code> = Local</li><li><code>L</code> = Low</li><li><code>N</code> = None</li><li><code>H</code> = High</li></ul>          | | `cvss-v3-availability-impact`             | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `cvss-v3-attack-vector`                | <ul><li><code>N</code> = Network</li><li><code>A</code> = Adjacent</li><li><code>L</code> = Local</li><li><code>P</code> = Physical</li></ul>    | | `cvss-v3-attack-complexity`                      | <ul><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>   | | `cvss-v3-user-interaction`            | <ul><li><code>N</code> = None</li><li><code>R</code> = Required</li></ul>     | | `cvss-v3-privileges-required`         | <ul><li><code>N</code> = None</li><li><code>L</code> = Low</li><li><code>H</code> = High</li></ul>    | | `host-type`                               | 0=Unknown, 1=Guest, 2=Hypervisor, 3=Physical, 4=Mobile                                                        | | `ip-address-type`                         | 0=IPv4, 1=IPv6                                                                                                | | `pci-compliance`                          | 0=fail, 1=pass                                                                                                | | `vulnerability-validated-status`          | 0=present, 1=not present                                                                                      |  ##### Operator Properties <a section=\"section/Responses/SearchCriteria/OperatorProperties\"></a>  The following table outlines which properties are required for each operator and the appropriate data type(s):  | Operator              | `value`               | `lower`               | `upper`               | | ----------------------|-----------------------|-----------------------|-----------------------| | `are`                 | `string`              |                       |                       | | `contains`            | `string`              |                       |                       | | `does-not-contain`    | `string`              |                       |                       | | `ends with`           | `string`              |                       |                       | | `in`                  | `Array[ string ]`     |                       |                       | | `in-range`            |                       | `numeric`             | `numeric`             | | `includes`            | `Array[ string ]`     |                       |                       | | `is`                  | `string`              |                       |                       | | `is-applied`          |                       |                       |                       | | `is-between`          |                       | `numeric`             | `numeric`             | | `is-earlier-than`     | `numeric`             |                       |                       | | `is-empty`            |                       |                       |                       | | `is-greater-than`     | `numeric`             |                       |                       | | `is-on-or-after`      | `string` (yyyy-MM-dd) |                       |                       | | `is-on-or-before`     | `string` (yyyy-MM-dd) |                       |                       | | `is-not`              | `string`              |                       |                       | | `is-not-applied`      |                       |                       |                       | | `is-not-empty`        |                       |                       |                       | | `is-within-the-last`  | `string`              |                       |                       | | `less-than`           | `string`              |                       |                       | | `like`                | `string`              |                       |                       | | `not-contains`        | `string`              |                       |                       | | `not-in`              | `Array[ string ]`     |                       |                       | | `not-in-range`        |                       | `numeric`             | `numeric`             | | `not-like`            | `string`              |                       |                       | | `starts-with`         | `string`              |                       |                       |  #### Discovery Connection Search Criteria <a section=\"section/Responses/DiscoverySearchCriteria\"></a>  Dynamic sites make use of search criteria to match assets from a discovery connection. Search criteria is an array of search filters.    Each search filter has a generic format of:  ```json {     \"field\": \"<field-name>\",     \"operator\": \"<operator>\",     [\"value\": \"<value>\",]    [\"lower\": \"<value>\",]    [\"upper\": \"<value>\"] }     ```  Every filter defines two required properties `field` and `operator`. The field is the name of an asset property that is being filtered on. The list of supported fields vary depending on the type of discovery connection configured  for the dynamic site (e.g vSphere, ActiveSync, etc.). The operator is a type and property-specific operating  performed on the filtered property. The valid values for fields outlined in the tables below and are grouped by the  type of connection.    Every filter also defines one or more values that are supplied to the operator. See  <a href=\"#section/Responses/SearchCriteria/OperatorProperties\">Search Criteria Operator Properties</a> for more  information on the valid values for each operator.    ##### Fields (ActiveSync)  This section documents search criteria information for ActiveSync discovery connections. The discovery connections  must be one of the following types: `\"activesync-ldap\"`, `\"activesync-office365\"`, or `\"activesync-powershell\"`.    The following table outlines the search criteria fields and the available operators for ActiveSync connections:  | Field                             | Operators                                                     | | --------------------------------- | ------------------------------------------------------------- | | `last-sync-time`                  | `is-within-the-last` ` is-earlier-than`                       | | `operating-system`                | `contains` ` does-not-contain`                                | | `user`                            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (AWS)  This section documents search criteria information for AWS discovery connections. The discovery connections must be the type `\"aws\"`.    The following table outlines the search criteria fields and the available operators for AWS connections:  | Field                   | Operators                                                     | | ----------------------- | ------------------------------------------------------------- | | `availability-zone`     | `contains` ` does-not-contain`                                | | `guest-os-family`       | `contains` ` does-not-contain`                                | | `instance-id`           | `contains` ` does-not-contain`                                | | `instance-name`         | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `instance-state`        | `in` ` not-in`                                                | | `instance-type`         | `in` ` not-in`                                                | | `ip-address`            | `in-range` ` not-in-range` ` is` ` is-not`                    | | `region`                | `in` ` not-in`                                                | | `vpc-id`                | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (DHCP)  This section documents search criteria information for DHCP discovery connections. The discovery connections must be the type `\"dhcp\"`.    The following table outlines the search criteria fields and the available operators for DHCP connections:  | Field           | Operators                                                     | | --------------- | ------------------------------------------------------------- | | `host-name`     | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` | | `ip-address`    | `in-range` ` not-in-range` ` is` ` is-not`                    | | `mac-address`   | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with` |  ##### Fields (Sonar)  This section documents search criteria information for Sonar discovery connections. The discovery connections must be the type `\"sonar\"`.    The following table outlines the search criteria fields and the available operators for Sonar connections:  | Field               | Operators            | | ------------------- | -------------------- | | `search-domain`     | `contains` ` is`     | | `ip-address`        | `in-range` ` is`     | | `sonar-scan-date`   | `is-within-the-last` |  ##### Fields (vSphere)  This section documents search criteria information for vSphere discovery connections. The discovery connections must be the type `\"vsphere\"`.    The following table outlines the search criteria fields and the available operators for vSphere connections:  | Field                | Operators                                                                                  | | -------------------- | ------------------------------------------------------------------------------------------ | | `cluster`            | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `data-center`        | `is` ` is-not`                                                                             | | `discovered-time`    | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `guest-os-family`    | `contains` ` does-not-contain`                                                             | | `host-name`          | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              | | `ip-address`         | `in-range` ` not-in-range` ` is` ` is-not`                                                 | | `power-state`        | `in` ` not-in`                                                                             | | `resource-pool-path` | `contains` ` does-not-contain`                                                             | | `last-time-seen`     | `is-on-or-before` ` is-on-or-after` ` is-between` ` is-earlier-than` ` is-within-the-last` | | `vm`                 | `is` ` is-not` ` contains` ` does-not-contain` ` starts-with`                              |  ##### Enumerated Properties (vSphere)  The following fields have enumerated values:  | Field         | Acceptable Values                    | | ------------- | ------------------------------------ | | `power-state` | `poweredOn` `poweredOff` `suspended` |  ## HATEOAS  This API follows Hypermedia as the Engine of Application State (HATEOAS) principals and is therefore hypermedia friendly.  Hyperlinks are returned in the `links` property of any given resource and contain a fully-qualified hyperlink to the corresponding resource. The format of the hypermedia link adheres to both the <a target=\"_blank\" href=\"http://jsonapi.org\">{json:api} v1</a>  <a target=\"_blank\" href=\"http://jsonapi.org/format/#document-links\">\"Link Object\"</a> and  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html\">JSON Hyper-Schema</a>  <a target=\"_blank\" href=\"http://json-schema.org/latest/json-schema-hypermedia.html#rfc.section.5.2\">\"Link Description Object\"</a> formats. For example:  ```json \"links\": [{   \"rel\": \"<relation>\",   \"href\": \"<href>\"   ... }] ```  Where appropriate link objects may also contain additional properties than the `rel` and `href` properties, such as `id`, `type`, etc.  See the [Root](#tag/Root) resources for the entry points into API discovery.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SiteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_site_tag(self, id, tag_id, **kwargs):  # noqa: E501
        """Site Tag  # noqa: E501

        Adds a tag to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_site_tag(id, tag_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int tag_id: The identifier of the tag. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_site_tag_with_http_info(id, tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_site_tag_with_http_info(id, tag_id, **kwargs)  # noqa: E501
            return data

    def add_site_tag_with_http_info(self, id, tag_id, **kwargs):  # noqa: E501
        """Site Tag  # noqa: E501

        Adds a tag to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_site_tag_with_http_info(id, tag_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int tag_id: The identifier of the tag. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tag_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_site_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_site_tag`")  # noqa: E501
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `add_site_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/tags/{tagId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_site_user(self, id, **kwargs):  # noqa: E501
        """Site Users Access  # noqa: E501

        Grants a non-administrator user access to the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_site_user(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int param0: The identifier of the user.
        :return: ReferenceWithUserIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_site_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_site_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def add_site_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Users Access  # noqa: E501

        Grants a non-administrator user access to the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_site_user_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int param0: The identifier of the user.
        :return: ReferenceWithUserIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_site_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_site_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceWithUserIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_site(self, **kwargs):  # noqa: E501
        """Sites  # noqa: E501

        Creates a new site with the specified configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site(async=True)
        >>> result = thread.get()

        :param async bool
        :param SiteCreateResource param0: Resource for creating a site configuration.
        :return: ReferenceWithSiteIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_site_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_site_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_site_with_http_info(self, **kwargs):  # noqa: E501
        """Sites  # noqa: E501

        Creates a new site with the specified configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param SiteCreateResource param0: Resource for creating a site configuration.
        :return: ReferenceWithSiteIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_site" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceWithSiteIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_site_credential(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Creates a new site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_credential(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SiteCredential param1: The specification of a site credential.
        :return: CreatedReferenceCredentialIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_site_credential_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_site_credential_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_site_credential_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Creates a new site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_credential_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SiteCredential param1: The specification of a site credential.
        :return: CreatedReferenceCredentialIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param1']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_site_credential" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_site_credential`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param1' in params:
            body_params = params['param1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatedReferenceCredentialIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_site_scan_schedule(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Creates a new scan schedule for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_scan_schedule(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param ScanSchedule param0: Resource for a scan schedule.
        :return: ReferenceWithScanScheduleIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_site_scan_schedule_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_site_scan_schedule_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_site_scan_schedule_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Creates a new scan schedule for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_scan_schedule_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param ScanSchedule param0: Resource for a scan schedule.
        :return: ReferenceWithScanScheduleIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_site_scan_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_site_scan_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceWithScanScheduleIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_site_smtp_alert(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Creates a new SMTP alert for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_smtp_alert(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SmtpAlert param0: Resource for creating a new SMTP alert.
        :return: ReferenceWithAlertIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_site_smtp_alert_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_site_smtp_alert_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_site_smtp_alert_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Creates a new SMTP alert for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_smtp_alert_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SmtpAlert param0: Resource for creating a new SMTP alert.
        :return: ReferenceWithAlertIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_site_smtp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_site_smtp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceWithAlertIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_site_snmp_alert(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Creates a new SNMP alert for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_snmp_alert(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SnmpAlert param0: Resource for creating a new SNMP alert.
        :return: ReferenceWithAlertIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_site_snmp_alert_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_site_snmp_alert_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_site_snmp_alert_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Creates a new SNMP alert for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_snmp_alert_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SnmpAlert param0: Resource for creating a new SNMP alert.
        :return: ReferenceWithAlertIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_site_snmp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_site_snmp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceWithAlertIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_site_syslog_alert(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Creates a new Syslog alert for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_syslog_alert(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SyslogAlert param0: Resource for creating a new Syslog alert.
        :return: ReferenceWithAlertIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_site_syslog_alert_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_site_syslog_alert_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_site_syslog_alert_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Creates a new Syslog alert for the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_site_syslog_alert_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SyslogAlert param0: Resource for creating a new Syslog alert.
        :return: ReferenceWithAlertIDLink
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_site_syslog_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_site_syslog_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceWithAlertIDLink',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_site_alerts(self, id, **kwargs):  # noqa: E501
        """Site Alerts  # noqa: E501

        Deletes all alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_all_site_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_site_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_all_site_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Alerts  # noqa: E501

        Deletes all alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_site_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_all_site_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_site_credentials(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Deletes all site credentials from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_credentials(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_all_site_credentials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_site_credentials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_all_site_credentials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Deletes all site credentials from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_credentials_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_site_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_all_site_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_site_scan_schedules(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Deletes all scan schedules from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_scan_schedules(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_all_site_scan_schedules_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_site_scan_schedules_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_all_site_scan_schedules_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Deletes all scan schedules from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_scan_schedules_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_site_scan_schedules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_all_site_scan_schedules`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_site_smtp_alerts(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Deletes all SMTP alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_smtp_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_all_site_smtp_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_site_smtp_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_all_site_smtp_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Deletes all SMTP alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_smtp_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_site_smtp_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_all_site_smtp_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_site_snmp_alerts(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Deletes all SNMP alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_snmp_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_all_site_snmp_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_site_snmp_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_all_site_snmp_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Deletes all SNMP alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_snmp_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_site_snmp_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_all_site_snmp_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_site_syslog_alerts(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Deletes all Syslog alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_syslog_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_all_site_syslog_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_site_syslog_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_all_site_syslog_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Deletes all Syslog alerts from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_all_site_syslog_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_site_syslog_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_all_site_syslog_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_site(self, id, **kwargs):  # noqa: E501
        """Site  # noqa: E501

        site.delete.description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_site_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_site_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_site_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site  # noqa: E501

        site.delete.description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_site_credential(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Scan Credential  # noqa: E501

        Deletes the specified site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_credential(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
            return data

    def delete_site_credential_with_http_info(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Scan Credential  # noqa: E501

        Deletes the specified site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_credential_with_http_info(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'credential_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_site_credential" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_site_credential`")  # noqa: E501
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params or
                params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `delete_site_credential`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials/{credentialId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_site_scan_schedule(self, id, schedule_id, **kwargs):  # noqa: E501
        """Site Scan Schedule  # noqa: E501

        Deletes the specified scan schedule from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_scan_schedule(id, schedule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int schedule_id: The identifier of the scan schedule. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_site_scan_schedule_with_http_info(id, schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_site_scan_schedule_with_http_info(id, schedule_id, **kwargs)  # noqa: E501
            return data

    def delete_site_scan_schedule_with_http_info(self, id, schedule_id, **kwargs):  # noqa: E501
        """Site Scan Schedule  # noqa: E501

        Deletes the specified scan schedule from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_scan_schedule_with_http_info(id, schedule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int schedule_id: The identifier of the scan schedule. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'schedule_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_site_scan_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_site_scan_schedule`")  # noqa: E501
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `delete_site_scan_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules/{scheduleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_site_smtp_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SMTP Alert  # noqa: E501

        Deletes the specified SMTP alert from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_smtp_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_site_smtp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_site_smtp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def delete_site_smtp_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SMTP Alert  # noqa: E501

        Deletes the specified SMTP alert from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_smtp_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_site_smtp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_site_smtp_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `delete_site_smtp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp/{alertId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_site_snmp_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SNMP Alert  # noqa: E501

        Deletes the specified SNMP alert from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_snmp_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_site_snmp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_site_snmp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def delete_site_snmp_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SNMP Alert  # noqa: E501

        Deletes the specified SNMP alert from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_snmp_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_site_snmp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_site_snmp_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `delete_site_snmp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp/{alertId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_site_syslog_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site Syslog Alert  # noqa: E501

        Deletes the specified Syslog alert from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_syslog_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_site_syslog_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_site_syslog_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def delete_site_syslog_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site Syslog Alert  # noqa: E501

        Deletes the specified Syslog alert from the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_site_syslog_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_site_syslog_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_site_syslog_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `delete_site_syslog_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog/{alertId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_shared_credential_on_site(self, id, credential_id, **kwargs):  # noqa: E501
        """Assigned Shared Credential Enablement  # noqa: E501

        Enable or disable the shared credential for the site's scans.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_shared_credential_on_site(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the shared credential. (required)
        :param bool param0: Flag indicating whether the shared credential is enabled for the site's scans.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.enable_shared_credential_on_site_with_http_info(id, credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_shared_credential_on_site_with_http_info(id, credential_id, **kwargs)  # noqa: E501
            return data

    def enable_shared_credential_on_site_with_http_info(self, id, credential_id, **kwargs):  # noqa: E501
        """Assigned Shared Credential Enablement  # noqa: E501

        Enable or disable the shared credential for the site's scans.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_shared_credential_on_site_with_http_info(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the shared credential. (required)
        :param bool param0: Flag indicating whether the shared credential is enabled for the site's scans.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'credential_id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_shared_credential_on_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `enable_shared_credential_on_site`")  # noqa: E501
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params or
                params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `enable_shared_credential_on_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/shared_credentials/{credentialId}/enabled', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_site_credential(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Credential Enablement  # noqa: E501

        Enable or disable the site credential for scans.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_site_credential(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :param bool param0: Flag indicating whether the credential is enabled for use during the scan.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.enable_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
            return data

    def enable_site_credential_with_http_info(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Credential Enablement  # noqa: E501

        Enable or disable the site credential for scans.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_site_credential_with_http_info(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :param bool param0: Flag indicating whether the credential is enabled for use during the scan.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'credential_id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_site_credential" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `enable_site_credential`")  # noqa: E501
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params or
                params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `enable_site_credential`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials/{credentialId}/enabled', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_excluded_asset_groups(self, id, **kwargs):  # noqa: E501
        """Site Excluded Asset Groups  # noqa: E501

        Retrieves the excluded asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_excluded_asset_groups(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesAssetGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_excluded_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_excluded_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_excluded_asset_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Excluded Asset Groups  # noqa: E501

        Retrieves the excluded asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_excluded_asset_groups_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesAssetGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_excluded_asset_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_excluded_asset_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/excluded_asset_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesAssetGroup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_excluded_targets(self, id, **kwargs):  # noqa: E501
        """Site Excluded Targets  # noqa: E501

        Retrieves the excluded targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_excluded_targets(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanTargetsResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_excluded_targets_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_excluded_targets_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_excluded_targets_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Excluded Targets  # noqa: E501

        Retrieves the excluded targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_excluded_targets_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanTargetsResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_excluded_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_excluded_targets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/excluded_targets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScanTargetsResource',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_included_asset_groups(self, id, **kwargs):  # noqa: E501
        """Site Included Asset Groups  # noqa: E501

        Retrieves the included asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_included_asset_groups(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesAssetGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_included_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_included_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_included_asset_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Included Asset Groups  # noqa: E501

        Retrieves the included asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_included_asset_groups_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesAssetGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_included_asset_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_included_asset_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/included_asset_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesAssetGroup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_included_targets(self, id, **kwargs):  # noqa: E501
        """Site Included Targets  # noqa: E501

        Retrieves the included targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_included_targets(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanTargetsResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_included_targets_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_included_targets_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_included_targets_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Included Targets  # noqa: E501

        Retrieves the included targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_included_targets_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanTargetsResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_included_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_included_targets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/included_targets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScanTargetsResource',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site(self, id, **kwargs):  # noqa: E501
        """Site  # noqa: E501

        Retrieves the site with the specified identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Site
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site  # noqa: E501

        Retrieves the site with the specified identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Site
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Site',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_alerts(self, id, **kwargs):  # noqa: E501
        """Site Alerts  # noqa: E501

        Retrieve all alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Alerts  # noqa: E501

        Retrieve all alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_assets(self, id, **kwargs):  # noqa: E501
        """Site Assets  # noqa: E501

        Retrieves a paged resource of assets linked with the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_assets(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int page: The index of the page (zero-based) to retrieve.
        :param int size: The number of records per page to retrieve.
        :param list[str] sort: The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters.
        :return: PageOfAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_assets_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_assets_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_assets_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Assets  # noqa: E501

        Retrieves a paged resource of assets linked with the specified site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_assets_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int page: The index of the page (zero-based) to retrieve.
        :param int size: The number of records per page to retrieve.
        :param list[str] sort: The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters.
        :return: PageOfAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'size', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_assets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_assets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/assets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfAsset',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_credential(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Scan Credential  # noqa: E501

        Retrieves the specified site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_credential(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :return: SiteCredential
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
            return data

    def get_site_credential_with_http_info(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Scan Credential  # noqa: E501

        Retrieves the specified site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_credential_with_http_info(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :return: SiteCredential
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'credential_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_credential" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_credential`")  # noqa: E501
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params or
                params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `get_site_credential`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials/{credentialId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SiteCredential',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_credentials(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Retrieves all defined site credential resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_credentials(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSiteCredential
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_credentials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_credentials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_credentials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Retrieves all defined site credential resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_credentials_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSiteCredential
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesSiteCredential',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_discovery_connection(self, id, **kwargs):  # noqa: E501
        """Site Discovery Connection  # noqa: E501

        Retrieves the discovery connection assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_discovery_connection(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: SiteDiscoveryConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_discovery_connection_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_discovery_connection_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_discovery_connection_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Discovery Connection  # noqa: E501

        Retrieves the discovery connection assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_discovery_connection_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: SiteDiscoveryConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_discovery_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_discovery_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/discovery_connection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SiteDiscoveryConnection',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_discovery_search_criteria(self, id, **kwargs):  # noqa: E501
        """Site Discovery Search Criteria  # noqa: E501

        Retrieve the search criteria of the dynamic site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_discovery_search_criteria(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: DiscoverySearchCriteria
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_discovery_search_criteria_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_discovery_search_criteria_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_discovery_search_criteria_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Discovery Search Criteria  # noqa: E501

        Retrieve the search criteria of the dynamic site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_discovery_search_criteria_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: DiscoverySearchCriteria
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_discovery_search_criteria" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_discovery_search_criteria`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/discovery_search_criteria', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscoverySearchCriteria',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_organization(self, id, **kwargs):  # noqa: E501
        """Site Organization Information  # noqa: E501

        Retrieves the site organization information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_organization(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: SiteOrganization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_organization_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_organization_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_organization_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Organization Information  # noqa: E501

        Retrieves the site organization information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_organization_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: SiteOrganization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_organization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_organization`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/organization', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SiteOrganization',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_scan_engine(self, id, **kwargs):  # noqa: E501
        """Site Scan Engine  # noqa: E501

        Retrieves the resource of the scan engine assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_engine(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanEngine
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_scan_engine_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_scan_engine_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_scan_engine_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Engine  # noqa: E501

        Retrieves the resource of the scan engine assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_engine_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanEngine
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_scan_engine" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_scan_engine`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_engine', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScanEngine',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_scan_schedule(self, id, schedule_id, **kwargs):  # noqa: E501
        """Site Scan Schedule  # noqa: E501

        Retrieves the specified scan schedule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_schedule(id, schedule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int schedule_id: The identifier of the scan schedule. (required)
        :return: ScanSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_scan_schedule_with_http_info(id, schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_scan_schedule_with_http_info(id, schedule_id, **kwargs)  # noqa: E501
            return data

    def get_site_scan_schedule_with_http_info(self, id, schedule_id, **kwargs):  # noqa: E501
        """Site Scan Schedule  # noqa: E501

        Retrieves the specified scan schedule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_schedule_with_http_info(id, schedule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int schedule_id: The identifier of the scan schedule. (required)
        :return: ScanSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'schedule_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_scan_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_scan_schedule`")  # noqa: E501
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_site_scan_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules/{scheduleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScanSchedule',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_scan_schedules(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Returns all scan schedules for the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_schedules(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesScanSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_scan_schedules_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_scan_schedules_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_scan_schedules_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Returns all scan schedules for the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_schedules_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesScanSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_scan_schedules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_scan_schedules`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesScanSchedule',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_scan_template(self, id, **kwargs):  # noqa: E501
        """Site Scan Template  # noqa: E501

        Retrieves the resource of the scan template assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_scan_template_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_scan_template_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_scan_template_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Template  # noqa: E501

        Retrieves the resource of the scan template assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_scan_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ScanTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_scan_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_scan_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScanTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_shared_credentials(self, id, **kwargs):  # noqa: E501
        """Assigned Shared Credentials  # noqa: E501

        Retrieve all of the shared credentials assigned to the site. These shared credentials can be enabled/disabled for the site's scan.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_shared_credentials(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSiteSharedCredential
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_shared_credentials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_shared_credentials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_shared_credentials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Assigned Shared Credentials  # noqa: E501

        Retrieve all of the shared credentials assigned to the site. These shared credentials can be enabled/disabled for the site's scan.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_shared_credentials_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSiteSharedCredential
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_shared_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_shared_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/shared_credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesSiteSharedCredential',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_smtp_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SMTP Alert  # noqa: E501

        Retrieves the specified SMTP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_smtp_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: SmtpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_smtp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_smtp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def get_site_smtp_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SMTP Alert  # noqa: E501

        Retrieves the specified SMTP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_smtp_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: SmtpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_smtp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_smtp_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `get_site_smtp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp/{alertId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmtpAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_smtp_alerts(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Retrieves all SMTP alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_smtp_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSmtpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_smtp_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_smtp_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_smtp_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Retrieves all SMTP alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_smtp_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSmtpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_smtp_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_smtp_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesSmtpAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_snmp_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SNMP Alert  # noqa: E501

        Retrieves the specified SNMP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_snmp_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: SnmpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_snmp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_snmp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def get_site_snmp_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SNMP Alert  # noqa: E501

        Retrieves the specified SNMP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_snmp_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: SnmpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_snmp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_snmp_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `get_site_snmp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp/{alertId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnmpAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_snmp_alerts(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Retrieves all SNMP alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_snmp_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSnmpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_snmp_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_snmp_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_snmp_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Retrieves all SNMP alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_snmp_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSnmpAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_snmp_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_snmp_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesSnmpAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_syslog_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site Syslog Alert  # noqa: E501

        Retrieves the specified Syslog alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_syslog_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: SyslogAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_syslog_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_syslog_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def get_site_syslog_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site Syslog Alert  # noqa: E501

        Retrieves the specified Syslog alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_syslog_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :return: SyslogAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_syslog_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_syslog_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `get_site_syslog_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog/{alertId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SyslogAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_syslog_alerts(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Retrieves all Syslog alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_syslog_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSyslogAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_syslog_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_syslog_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_syslog_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Retrieves all Syslog alerts defined in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_syslog_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesSyslogAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_syslog_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_syslog_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesSyslogAlert',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_tags(self, id, **kwargs):  # noqa: E501
        """Site Tags  # noqa: E501

        Retrieves the list of tags added to the sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_tags(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_tags_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_tags_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_tags_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Tags  # noqa: E501

        Retrieves the list of tags added to the sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_tags_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesTag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_site_users(self, id, **kwargs):  # noqa: E501
        """Site Users Access  # noqa: E501

        Retrieve the list of non-administrator users that have access to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_users(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_site_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_site_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_site_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Users Access  # noqa: E501

        Retrieve the list of non-administrator users that have access to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_site_users_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_site_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sites(self, **kwargs):  # noqa: E501
        """Sites  # noqa: E501

        Retrieves a paged resource of accessible sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sites(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: The index of the page (zero-based) to retrieve.
        :param int size: The number of records per page to retrieve.
        :param list[str] sort: The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters.
        :return: PageOfSite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sites_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sites_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sites_with_http_info(self, **kwargs):  # noqa: E501
        """Sites  # noqa: E501

        Retrieves a paged resource of accessible sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sites_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: The index of the page (zero-based) to retrieve.
        :param int size: The number of records per page to retrieve.
        :param list[str] sort: The criteria to sort the records by, in the format: `property[,ASC|DESC]`. The default sort order is ascending. Multiple sort criteria can be specified using multiple sort query parameters.
        :return: PageOfSite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sites" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfSite',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_web_auth_html_forms(self, id, **kwargs):  # noqa: E501
        """Web Authentication HTML Forms  # noqa: E501

        Retrieves all HTML form authentications configured in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_web_auth_html_forms(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesWebFormAuthentication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_web_auth_html_forms_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_web_auth_html_forms_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_web_auth_html_forms_with_http_info(self, id, **kwargs):  # noqa: E501
        """Web Authentication HTML Forms  # noqa: E501

        Retrieves all HTML form authentications configured in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_web_auth_html_forms_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesWebFormAuthentication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_web_auth_html_forms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_web_auth_html_forms`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/web_authentication/html_forms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesWebFormAuthentication',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_web_auth_http_headers(self, id, **kwargs):  # noqa: E501
        """Web Authentication HTTP Headers  # noqa: E501

        Retrieves all HTTP header authentications configured in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_web_auth_http_headers(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesWebHeaderAuthentication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_web_auth_http_headers_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_web_auth_http_headers_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_web_auth_http_headers_with_http_info(self, id, **kwargs):  # noqa: E501
        """Web Authentication HTTP Headers  # noqa: E501

        Retrieves all HTTP header authentications configured in the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_web_auth_http_headers_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: ResourcesWebHeaderAuthentication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_web_auth_http_headers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_web_auth_http_headers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/web_authentication/http_headers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesWebHeaderAuthentication',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_all_excluded_asset_groups(self, id, **kwargs):  # noqa: E501
        """Site Excluded Asset Groups  # noqa: E501

        Removes all excluded asset groups from the specified static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_all_excluded_asset_groups(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_all_excluded_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_all_excluded_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_all_excluded_asset_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Excluded Asset Groups  # noqa: E501

        Removes all excluded asset groups from the specified static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_all_excluded_asset_groups_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_all_excluded_asset_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_all_excluded_asset_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/excluded_asset_groups', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_all_included_asset_groups(self, id, **kwargs):  # noqa: E501
        """Site Included Asset Groups  # noqa: E501

        Removes all included asset groups from the specified static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_all_included_asset_groups(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_all_included_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_all_included_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_all_included_asset_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Included Asset Groups  # noqa: E501

        Removes all included asset groups from the specified static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_all_included_asset_groups_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_all_included_asset_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_all_included_asset_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/included_asset_groups', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_asset_from_site(self, id, asset_id, **kwargs):  # noqa: E501
        """Site Asset  # noqa: E501

        Removes an asset from a site. The asset will only be deleted if it belongs to no other sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_asset_from_site(id, asset_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int asset_id: The identifier of the asset. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_asset_from_site_with_http_info(id, asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_asset_from_site_with_http_info(id, asset_id, **kwargs)  # noqa: E501
            return data

    def remove_asset_from_site_with_http_info(self, id, asset_id, **kwargs):  # noqa: E501
        """Site Asset  # noqa: E501

        Removes an asset from a site. The asset will only be deleted if it belongs to no other sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_asset_from_site_with_http_info(id, asset_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int asset_id: The identifier of the asset. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'asset_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_asset_from_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_asset_from_site`")  # noqa: E501
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `remove_asset_from_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'asset_id' in params:
            path_params['assetId'] = params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/assets/{assetId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_excluded_asset_group(self, id, asset_group_id, **kwargs):  # noqa: E501
        """Site Excluded Asset Group  # noqa: E501

        Removes the specified asset group from the excluded asset groups configured in the static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_excluded_asset_group(id, asset_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int asset_group_id: The identifier of the asset group. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_excluded_asset_group_with_http_info(id, asset_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_excluded_asset_group_with_http_info(id, asset_group_id, **kwargs)  # noqa: E501
            return data

    def remove_excluded_asset_group_with_http_info(self, id, asset_group_id, **kwargs):  # noqa: E501
        """Site Excluded Asset Group  # noqa: E501

        Removes the specified asset group from the excluded asset groups configured in the static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_excluded_asset_group_with_http_info(id, asset_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int asset_group_id: The identifier of the asset group. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'asset_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_excluded_asset_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_excluded_asset_group`")  # noqa: E501
        # verify the required parameter 'asset_group_id' is set
        if ('asset_group_id' not in params or
                params['asset_group_id'] is None):
            raise ValueError("Missing the required parameter `asset_group_id` when calling `remove_excluded_asset_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'asset_group_id' in params:
            path_params['assetGroupId'] = params['asset_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/excluded_asset_groups/{assetGroupId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_included_asset_group(self, id, asset_group_id, **kwargs):  # noqa: E501
        """Site Included Asset Group  # noqa: E501

        Removes the specified asset group from the included asset groups configured in the static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_included_asset_group(id, asset_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int asset_group_id: The identifier of the asset group. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_included_asset_group_with_http_info(id, asset_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_included_asset_group_with_http_info(id, asset_group_id, **kwargs)  # noqa: E501
            return data

    def remove_included_asset_group_with_http_info(self, id, asset_group_id, **kwargs):  # noqa: E501
        """Site Included Asset Group  # noqa: E501

        Removes the specified asset group from the included asset groups configured in the static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_included_asset_group_with_http_info(id, asset_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int asset_group_id: The identifier of the asset group. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'asset_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_included_asset_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_included_asset_group`")  # noqa: E501
        # verify the required parameter 'asset_group_id' is set
        if ('asset_group_id' not in params or
                params['asset_group_id'] is None):
            raise ValueError("Missing the required parameter `asset_group_id` when calling `remove_included_asset_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'asset_group_id' in params:
            path_params['assetGroupId'] = params['asset_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/included_asset_groups/{assetGroupId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_site_assets(self, id, **kwargs):  # noqa: E501
        """Site Assets  # noqa: E501

        Removes all assets from the specified site. Assets will be deleted entirely from the Security Console if either Asset Linking is disabled or if Asset Linking is enabled and the asset only existed in this site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_site_assets(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_site_assets_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_site_assets_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_site_assets_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Assets  # noqa: E501

        Removes all assets from the specified site. Assets will be deleted entirely from the Security Console if either Asset Linking is disabled or if Asset Linking is enabled and the asset only existed in this site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_site_assets_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_site_assets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_site_assets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/assets', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_site_tag(self, id, tag_id, **kwargs):  # noqa: E501
        """Site Tag  # noqa: E501

        Removes the specified tag from the site's tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_site_tag(id, tag_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int tag_id: The identifier of the tag. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_site_tag_with_http_info(id, tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_site_tag_with_http_info(id, tag_id, **kwargs)  # noqa: E501
            return data

    def remove_site_tag_with_http_info(self, id, tag_id, **kwargs):  # noqa: E501
        """Site Tag  # noqa: E501

        Removes the specified tag from the site's tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_site_tag_with_http_info(id, tag_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int tag_id: The identifier of the tag. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tag_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_site_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_site_tag`")  # noqa: E501
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `remove_site_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/tags/{tagId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_site_user(self, id, user_id, **kwargs):  # noqa: E501
        """Site User Access  # noqa: E501

        Removes the specified user from the site's access list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_site_user(id, user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int user_id: The identifier of the user. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_site_user_with_http_info(id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_site_user_with_http_info(id, user_id, **kwargs)  # noqa: E501
            return data

    def remove_site_user_with_http_info(self, id, user_id, **kwargs):  # noqa: E501
        """Site User Access  # noqa: E501

        Removes the specified user from the site's access list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_site_user_with_http_info(id, user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int user_id: The identifier of the user. (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_site_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_site_user`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `remove_site_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/users/{userId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_credentials(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Updates multiple site credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_credentials(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SiteCredential] param1: A list of site credentials resources.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_credentials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_credentials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_credentials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Credentials  # noqa: E501

        Updates multiple site credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_credentials_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SiteCredential] param1: A list of site credentials resources.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param1']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param1' in params:
            body_params = params['param1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_discovery_connection(self, id, **kwargs):  # noqa: E501
        """Site Discovery Connection  # noqa: E501

        Updates the discovery connection assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_discovery_connection(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int param0: The identifier of the discovery connection.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_discovery_connection_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_discovery_connection_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_discovery_connection_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Discovery Connection  # noqa: E501

        Updates the discovery connection assigned to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_discovery_connection_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int param0: The identifier of the discovery connection.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_discovery_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_discovery_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/discovery_connection', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_discovery_search_criteria(self, id, param1, **kwargs):  # noqa: E501
        """Site Discovery Search Criteria  # noqa: E501

        Update the search criteria of the dynamic site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_discovery_search_criteria(id, param1, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param DiscoverySearchCriteria param1: param1 (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_discovery_search_criteria_with_http_info(id, param1, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_discovery_search_criteria_with_http_info(id, param1, **kwargs)  # noqa: E501
            return data

    def set_site_discovery_search_criteria_with_http_info(self, id, param1, **kwargs):  # noqa: E501
        """Site Discovery Search Criteria  # noqa: E501

        Update the search criteria of the dynamic site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_discovery_search_criteria_with_http_info(id, param1, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param DiscoverySearchCriteria param1: param1 (required)
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param1']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_discovery_search_criteria" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_discovery_search_criteria`")  # noqa: E501
        # verify the required parameter 'param1' is set
        if ('param1' not in params or
                params['param1'] is None):
            raise ValueError("Missing the required parameter `param1` when calling `set_site_discovery_search_criteria`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param1' in params:
            body_params = params['param1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/discovery_search_criteria', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_scan_engine(self, id, **kwargs):  # noqa: E501
        """Site Scan Engine  # noqa: E501

        Updates the assigned scan engine to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_scan_engine(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int param0: The identifier of the scan engine.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_scan_engine_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_scan_engine_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_scan_engine_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Engine  # noqa: E501

        Updates the assigned scan engine to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_scan_engine_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int param0: The identifier of the scan engine.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_scan_engine" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_scan_engine`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_engine', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_scan_schedules(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Updates all scan schedules for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_scan_schedules(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[ScanSchedule] param0: Array of resources for updating all scan schedules defined in the site. Scan schedules defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_scan_schedules_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_scan_schedules_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_scan_schedules_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Schedules  # noqa: E501

        Updates all scan schedules for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_scan_schedules_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[ScanSchedule] param0: Array of resources for updating all scan schedules defined in the site. Scan schedules defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_scan_schedules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_scan_schedules`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_scan_template(self, id, **kwargs):  # noqa: E501
        """Site Scan Template  # noqa: E501

        Updates the assigned scan template to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_scan_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param str param0: The identifier of the scan template.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_scan_template_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_scan_template_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_scan_template_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Scan Template  # noqa: E501

        Updates the assigned scan template to the site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_scan_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param str param0: The identifier of the scan template.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_scan_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_scan_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_template', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_smtp_alerts(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Updates all SMTP alerts for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_smtp_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SmtpAlert] param0: Array of resources for updating all SMTP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_smtp_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_smtp_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_smtp_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SMTP Alerts  # noqa: E501

        Updates all SMTP alerts for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_smtp_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SmtpAlert] param0: Array of resources for updating all SMTP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_smtp_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_smtp_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_snmp_alerts(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Updates all SNMP alerts for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_snmp_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SnmpAlert] param0: Array of resources for updating all SNMP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_snmp_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_snmp_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_snmp_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site SNMP Alerts  # noqa: E501

        Updates all SNMP alerts for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_snmp_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SnmpAlert] param0: Array of resources for updating all SNMP alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_snmp_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_snmp_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_syslog_alerts(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Updates all Syslog alerts for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_syslog_alerts(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SyslogAlert] param0: Array of resources for updating all Syslog alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_syslog_alerts_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_syslog_alerts_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_syslog_alerts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Syslog Alerts  # noqa: E501

        Updates all Syslog alerts for the specified site in a single request using the array of resources defined in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_syslog_alerts_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[SyslogAlert] param0: Array of resources for updating all Syslog alerts defined in the site. Alerts defined in the site that are omitted from this request will be deleted from the site.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_syslog_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_syslog_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_tags(self, id, **kwargs):  # noqa: E501
        """Site Tags  # noqa: E501

        Updates the site's list of tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_tags(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param1: A list of tag identifiers to replace the site's tags.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_tags_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_tags_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_tags_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Tags  # noqa: E501

        Updates the site's list of tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_tags_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param1: A list of tag identifiers to replace the site's tags.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param1']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param1' in params:
            body_params = params['param1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/tags', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_site_users(self, id, **kwargs):  # noqa: E501
        """Site Users Access  # noqa: E501

        Updates the site's access list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_users(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param0: A list of user identifiers to replace the site's access list.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_site_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_site_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_site_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Users Access  # noqa: E501

        Updates the site's access list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_site_users_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param0: A list of user identifiers to replace the site's access list.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_site_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_site_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/users', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_excluded_asset_groups(self, id, **kwargs):  # noqa: E501
        """Site Excluded Asset Groups  # noqa: E501

        Updates the excluded asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_excluded_asset_groups(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param0: Array of asset group identifiers.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_excluded_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_excluded_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_excluded_asset_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Excluded Asset Groups  # noqa: E501

        Updates the excluded asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_excluded_asset_groups_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param0: Array of asset group identifiers.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_excluded_asset_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_excluded_asset_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/excluded_asset_groups', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_excluded_targets(self, id, **kwargs):  # noqa: E501
        """Site Excluded Targets  # noqa: E501

        Updates the excluded targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_excluded_targets(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[str] param0: List of addresses to be the site's new excluded scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_excluded_targets_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_excluded_targets_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_excluded_targets_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Excluded Targets  # noqa: E501

        Updates the excluded targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_excluded_targets_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[str] param0: List of addresses to be the site's new excluded scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_excluded_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_excluded_targets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/excluded_targets', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_included_asset_groups(self, id, **kwargs):  # noqa: E501
        """Site Included Asset Groups  # noqa: E501

        Updates the included asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_included_asset_groups(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param0: Array of asset group identifiers.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_included_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_included_asset_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_included_asset_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Included Asset Groups  # noqa: E501

        Updates the included asset groups in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_included_asset_groups_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[int] param0: Array of asset group identifiers.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_included_asset_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_included_asset_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/included_asset_groups', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_included_targets(self, id, **kwargs):  # noqa: E501
        """Site Included Targets  # noqa: E501

        Updates the included targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_included_targets(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[str] param0: List of addresses to be the site's new included scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_included_targets_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_included_targets_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_included_targets_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Included Targets  # noqa: E501

        Updates the included targets in a static site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_included_targets_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param list[str] param0: List of addresses to be the site's new included scan targets. Each address is a string that can represent either a hostname, ipv4 address, ipv4 address range, ipv6 address, or CIDR notation.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_included_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_included_targets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/included_targets', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site(self, id, **kwargs):  # noqa: E501
        """Site  # noqa: E501

        Updates the configuration of the site with the specified identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SiteUpdateResource param0: Resource for updating a site configuration.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_site_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site  # noqa: E501

        Updates the configuration of the site with the specified identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SiteUpdateResource param0: Resource for updating a site configuration.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site_credential(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Scan Credential  # noqa: E501

        Updates the specified site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_credential(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :param SiteCredential param2: The specification of the site credential to update.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_credential_with_http_info(id, credential_id, **kwargs)  # noqa: E501
            return data

    def update_site_credential_with_http_info(self, id, credential_id, **kwargs):  # noqa: E501
        """Site Scan Credential  # noqa: E501

        Updates the specified site credential.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_credential_with_http_info(id, credential_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int credential_id: The identifier of the site credential. (required)
        :param SiteCredential param2: The specification of the site credential to update.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'credential_id', 'param2']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site_credential" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site_credential`")  # noqa: E501
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params or
                params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `update_site_credential`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param2' in params:
            body_params = params['param2']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/site_credentials/{credentialId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site_organization(self, id, **kwargs):  # noqa: E501
        """Site Organization Information  # noqa: E501

        Updates the site organization information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_organization(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SiteOrganization param0: Resource for updating the specified site's organization information.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_organization_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_organization_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_site_organization_with_http_info(self, id, **kwargs):  # noqa: E501
        """Site Organization Information  # noqa: E501

        Updates the site organization information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_organization_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param SiteOrganization param0: Resource for updating the specified site's organization information.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site_organization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site_organization`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/organization', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site_scan_schedule(self, id, schedule_id, **kwargs):  # noqa: E501
        """Site Scan Schedule  # noqa: E501

        Updates the specified scan schedule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_scan_schedule(id, schedule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int schedule_id: The identifier of the scan schedule. (required)
        :param ScanSchedule param0: Resource for updating the specified scan schedule.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_scan_schedule_with_http_info(id, schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_scan_schedule_with_http_info(id, schedule_id, **kwargs)  # noqa: E501
            return data

    def update_site_scan_schedule_with_http_info(self, id, schedule_id, **kwargs):  # noqa: E501
        """Site Scan Schedule  # noqa: E501

        Updates the specified scan schedule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_scan_schedule_with_http_info(id, schedule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int schedule_id: The identifier of the scan schedule. (required)
        :param ScanSchedule param0: Resource for updating the specified scan schedule.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'schedule_id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site_scan_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site_scan_schedule`")  # noqa: E501
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `update_site_scan_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/scan_schedules/{scheduleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site_smtp_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SMTP Alert  # noqa: E501

        Updates the specified SMTP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_smtp_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :param SmtpAlert param0: Resource for updating the specified SMTP alert.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_smtp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_smtp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def update_site_smtp_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SMTP Alert  # noqa: E501

        Updates the specified SMTP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_smtp_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :param SmtpAlert param0: Resource for updating the specified SMTP alert.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site_smtp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site_smtp_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `update_site_smtp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/smtp/{alertId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site_snmp_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SNMP Alert  # noqa: E501

        Updates the specified SNMP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_snmp_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :param SnmpAlert param0: Resource for updating the specified SNMP alert.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_snmp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_snmp_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def update_site_snmp_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site SNMP Alert  # noqa: E501

        Updates the specified SNMP alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_snmp_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :param SnmpAlert param0: Resource for updating the specified SNMP alert.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site_snmp_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site_snmp_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `update_site_snmp_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/snmp/{alertId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_site_syslog_alert(self, id, alert_id, **kwargs):  # noqa: E501
        """Site Syslog Alert  # noqa: E501

        Updates the specified Syslog alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_syslog_alert(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :param SyslogAlert param0: Resource for updating the specified Syslog alert.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_site_syslog_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_site_syslog_alert_with_http_info(id, alert_id, **kwargs)  # noqa: E501
            return data

    def update_site_syslog_alert_with_http_info(self, id, alert_id, **kwargs):  # noqa: E501
        """Site Syslog Alert  # noqa: E501

        Updates the specified Syslog alert.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_site_syslog_alert_with_http_info(id, alert_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the site. (required)
        :param int alert_id: The identifier of the alert. (required)
        :param SyslogAlert param0: Resource for updating the specified Syslog alert.
        :return: Links
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'alert_id', 'param0']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_site_syslog_alert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_site_syslog_alert`")  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params or
                params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `update_site_syslog_alert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'param0' in params:
            body_params = params['param0']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/sites/{id}/alerts/syslog/{alertId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Links',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
