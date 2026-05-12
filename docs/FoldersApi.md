# urlr.FoldersApi

All URIs are relative to *https://urlr.me/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_create**](FoldersApi.md#folder_create) | **POST** /folders | Create a folder
[**folder_get**](FoldersApi.md#folder_get) | **GET** /folders/{folder_id} | Get a folder
[**folder_list**](FoldersApi.md#folder_list) | **GET** /folders | List folders


# **folder_create**
> Folder folder_create(folder_create_request=folder_create_request)

Create a folder

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.folder import Folder
from urlr.models.folder_create_request import FolderCreateRequest
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.FoldersApi(api_client)
    folder_create_request = urlr.FolderCreateRequest() # FolderCreateRequest | You can use this endpoint to add a folder to URLR. (optional)

    try:
        # Create a folder
        api_response = api_instance.folder_create(folder_create_request=folder_create_request)
        print("The response of FoldersApi->folder_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_create_request** | [**FolderCreateRequest**](FolderCreateRequest.md)| You can use this endpoint to add a folder to URLR. | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Folder |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Limits Exceeded |  -  |
**409** | Conflict |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_get**
> Folder folder_get(folder_id)

Get a folder

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.folder import Folder
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.FoldersApi(api_client)
    folder_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Folder API ID

    try:
        # Get a folder
        api_response = api_instance.folder_get(folder_id)
        print("The response of FoldersApi->folder_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **UUID**| Folder API ID | 

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_list**
> FolderList200Response folder_list(workspace_id)

List folders

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.folder_list200_response import FolderList200Response
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.FoldersApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace API ID

    try:
        # List folders
        api_response = api_instance.folder_list(workspace_id)
        print("The response of FoldersApi->folder_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace API ID | 

### Return type

[**FolderList200Response**](FolderList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders of workspace |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

