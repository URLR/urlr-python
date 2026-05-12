# urlr.WorkspacesApi

All URIs are relative to *https://urlr.me/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspace_get**](WorkspacesApi.md#workspace_get) | **GET** /workspaces/{workspace_id} | Get a workspace
[**workspace_list**](WorkspacesApi.md#workspace_list) | **GET** /workspaces | List workspaces of user


# **workspace_get**
> Workspace workspace_get(workspace_id)

Get a workspace

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.workspace import Workspace
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
    api_instance = urlr.WorkspacesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace API ID

    try:
        # Get a workspace
        api_response = api_instance.workspace_get(workspace_id)
        print("The response of WorkspacesApi->workspace_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspace_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace API ID | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_list**
> WorkspaceList200Response workspace_list()

List workspaces of user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.workspace_list200_response import WorkspaceList200Response
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
    api_instance = urlr.WorkspacesApi(api_client)

    try:
        # List workspaces of user
        api_response = api_instance.workspace_list()
        print("The response of WorkspacesApi->workspace_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspace_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceList200Response**](WorkspaceList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspaces of user |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

