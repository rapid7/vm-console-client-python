# swagger_client.CredentialApi

All URIs are relative to *https://localhost:3780*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shared_credential**](CredentialApi.md#create_shared_credential) | **POST** /api/3/shared_credentials | Shared Credentials
[**delete_all_shared_credentials**](CredentialApi.md#delete_all_shared_credentials) | **DELETE** /api/3/shared_credentials | Shared Credentials
[**delete_shared_credential**](CredentialApi.md#delete_shared_credential) | **DELETE** /api/3/shared_credentials/{id} | Shared Credential
[**get_shared_credential**](CredentialApi.md#get_shared_credential) | **GET** /api/3/shared_credentials/{id} | Shared Credential
[**get_shared_credentials**](CredentialApi.md#get_shared_credentials) | **GET** /api/3/shared_credentials | Shared Credentials
[**update_shared_credential**](CredentialApi.md#update_shared_credential) | **PUT** /api/3/shared_credentials/{id} | Shared Credential


# **create_shared_credential**
> CreatedReferenceCredentialIDLink create_shared_credential(param0=param0)

Shared Credentials

Creates a new shared credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialApi()
param0 = swagger_client.SharedCredential() # SharedCredential | The specification of a shared credential. (optional)

try:
    # Shared Credentials
    api_response = api_instance.create_shared_credential(param0=param0)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->create_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param0** | [**SharedCredential**](SharedCredential.md)| The specification of a shared credential. | [optional] 

### Return type

[**CreatedReferenceCredentialIDLink**](CreatedReferenceCredentialIDLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_shared_credentials**
> Links delete_all_shared_credentials()

Shared Credentials

Deletes all shared credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialApi()

try:
    # Shared Credentials
    api_response = api_instance.delete_all_shared_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->delete_all_shared_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_credential**
> Links delete_shared_credential(id)

Shared Credential

Deletes the specified shared scan credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialApi()
id = 56 # int | The identifier of the credential.

try:
    # Shared Credential
    api_response = api_instance.delete_shared_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->delete_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the credential. | 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_credential**
> SharedCredential get_shared_credential(id)

Shared Credential

Retrieves the specified shared credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialApi()
id = 56 # int | The identifier of the credential.

try:
    # Shared Credential
    api_response = api_instance.get_shared_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->get_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the credential. | 

### Return type

[**SharedCredential**](SharedCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_credentials**
> ResourcesSharedCredential get_shared_credentials()

Shared Credentials

Retrieves all defined shared credential resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialApi()

try:
    # Shared Credentials
    api_response = api_instance.get_shared_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->get_shared_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourcesSharedCredential**](ResourcesSharedCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shared_credential**
> Links update_shared_credential(id, param1=param1)

Shared Credential

Updates the specified shared credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CredentialApi()
id = 56 # int | The identifier of the credential.
param1 = swagger_client.SharedCredential() # SharedCredential | The specification of the shared credential to update. (optional)

try:
    # Shared Credential
    api_response = api_instance.update_shared_credential(id, param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->update_shared_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the credential. | 
 **param1** | [**SharedCredential**](SharedCredential.md)| The specification of the shared credential to update. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

