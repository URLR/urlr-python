# urlr.FolderApi

All URIs are relative to *https://urlr.me/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder**](FolderApi.md#folder) | **GET** /folder | Get folders of team


# **folder**
> Folder200Response folder(folder_request=folder_request)

Get folders of team

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.folder200_response import Folder200Response
from urlr.models.folder_request import FolderRequest
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api"
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
    api_instance = urlr.FolderApi(api_client)
    folder_request = urlr.FolderRequest() # FolderRequest | Infos to provide to get folders of team (optional)

    try:
        # Get folders of team
        api_response = api_instance.folder(folder_request=folder_request)
        print("The response of FolderApi->folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_request** | [**FolderRequest**](FolderRequest.md)| Infos to provide to get folders of team | [optional] 

### Return type

[**Folder200Response**](Folder200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders of team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

