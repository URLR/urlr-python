# urlr.WorkspacesApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_teams**](WorkspacesApi.md#get_teams) | **GET** /teams | Get workspaces of user


# **get_teams**
> GetTeams200Response get_teams()

Get workspaces of user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.get_teams200_response import GetTeams200Response
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
    api_instance = urlr.WorkspacesApi(api_client)

    try:
        # Get workspaces of user
        api_response = api_instance.get_teams()
        print("The response of WorkspacesApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_teams: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTeams200Response**](GetTeams200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspaces of user |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

