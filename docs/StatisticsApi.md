# urlr.StatisticsApi

All URIs are relative to *https://urlr.me/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistic_get**](StatisticsApi.md#statistic_get) | **GET** /statistics | Get statistics


# **statistic_get**
> StatisticGet200Response statistic_get(link_id, var_from=var_from, to=to)

Get statistics

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.statistic_get200_response import StatisticGet200Response
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
    api_instance = urlr.StatisticsApi(api_client)
    link_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Link API ID
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Get statistics from this date (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Get statistics until this date (optional)

    try:
        # Get statistics
        api_response = api_instance.statistic_get(link_id, var_from=var_from, to=to)
        print("The response of StatisticsApi->statistic_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistic_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **UUID**| Link API ID | 
 **var_from** | **datetime**| Get statistics from this date | [optional] 
 **to** | **datetime**| Get statistics until this date | [optional] 

### Return type

[**StatisticGet200Response**](StatisticGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

