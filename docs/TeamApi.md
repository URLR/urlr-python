# urlr.TeamApi

All URIs are relative to *https://urlr.me/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team**](TeamApi.md#team) | **GET** /team | Get teams of user


# **team**
> Team200Response team()

Get teams of user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.team200_response import Team200Response
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
    api_instance = urlr.TeamApi(api_client)

    try:
        # Get teams of user
        api_response = api_instance.team()
        print("The response of TeamApi->team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Team200Response**](Team200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams of user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

