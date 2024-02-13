# urlr.StatsApi

All URIs are relative to *https://urlr.me/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats**](StatsApi.md#stats) | **POST** /stats | Get statistics of a link


# **stats**
> Stats200Response stats(stats_request=stats_request)

Get statistics of a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.stats200_response import Stats200Response
from urlr.models.stats_request import StatsRequest
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
    api_instance = urlr.StatsApi(api_client)
    stats_request = urlr.StatsRequest() # StatsRequest | Infos to provide to get statistics of a link (optional)

    try:
        # Get statistics of a link
        api_response = api_instance.stats(stats_request=stats_request)
        print("The response of StatsApi->stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_request** | [**StatsRequest**](StatsRequest.md)| Infos to provide to get statistics of a link | [optional] 

### Return type

[**Stats200Response**](Stats200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics of the link |  -  |
**400** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

