# urlr.StatisticsApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics**](StatisticsApi.md#get_statistics) | **POST** /statistics | Get statistics of a link


# **get_statistics**
> GetStatistics200Response get_statistics(get_statistics_request=get_statistics_request)

Get statistics of a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.get_statistics200_response import GetStatistics200Response
from urlr.models.get_statistics_request import GetStatisticsRequest
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
    api_instance = urlr.StatisticsApi(api_client)
    get_statistics_request = urlr.GetStatisticsRequest() # GetStatisticsRequest | Infos to provide to get statistics of a link (optional)

    try:
        # Get statistics of a link
        api_response = api_instance.get_statistics(get_statistics_request=get_statistics_request)
        print("The response of StatisticsApi->get_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_statistics_request** | [**GetStatisticsRequest**](GetStatisticsRequest.md)| Infos to provide to get statistics of a link | [optional] 

### Return type

[**GetStatistics200Response**](GetStatistics200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics of the link |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

