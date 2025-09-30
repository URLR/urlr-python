# urlr.FoldersApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /folders/create | Create a folder
[**get_folders**](FoldersApi.md#get_folders) | **GET** /folders/{team_id} | Get folders of workspace


# **create_folder**
> CreateFolder200Response create_folder(create_folder_request=create_folder_request)

Create a folder

### Example


```python
import urlr
from urlr.models.create_folder200_response import CreateFolder200Response
from urlr.models.create_folder_request import CreateFolderRequest
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v1"
)


# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.FoldersApi(api_client)
    create_folder_request = urlr.CreateFolderRequest() # CreateFolderRequest | You can use this endpoint to add a folder to URLR. (optional)

    try:
        # Create a folder
        api_response = api_instance.create_folder(create_folder_request=create_folder_request)
        print("The response of FoldersApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder_request** | [**CreateFolderRequest**](CreateFolderRequest.md)| You can use this endpoint to add a folder to URLR. | [optional] 

### Return type

[**CreateFolder200Response**](CreateFolder200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder |  -  |
**401** | Unauthorized |  -  |
**429** | Limits Exceeded |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> GetFolders200Response get_folders(team_id)

Get folders of workspace

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.get_folders200_response import GetFolders200Response
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = urlr.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.FoldersApi(api_client)
    team_id = 'ffefc6c4-d970-4373-a867-2a69c8be2c89' # str | Workspace API ID

    try:
        # Get folders of workspace
        api_response = api_instance.get_folders(team_id)
        print("The response of FoldersApi->get_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Workspace API ID | 

### Return type

[**GetFolders200Response**](GetFolders200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

