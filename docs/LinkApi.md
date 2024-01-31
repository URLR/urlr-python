# urlr.LinkApi

All URIs are relative to *https://urlr.me/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reduce_link**](LinkApi.md#reduce_link) | **POST** /reduce-link | Reduce a link


# **reduce_link**
> ReduceLink200Response reduce_link(reduce_link_request=reduce_link_request)

Reduce a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import urlr
from urlr.models.reduce_link200_response import ReduceLink200Response
from urlr.models.reduce_link_request import ReduceLinkRequest
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
    api_instance = urlr.LinkApi(api_client)
    reduce_link_request = urlr.ReduceLinkRequest() # ReduceLinkRequest | Infos of the link to reduce (optional)

    try:
        # Reduce a link
        api_response = api_instance.reduce_link(reduce_link_request=reduce_link_request)
        print("The response of LinkApi->reduce_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->reduce_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reduce_link_request** | [**ReduceLinkRequest**](ReduceLinkRequest.md)| Infos of the link to reduce | [optional] 

### Return type

[**ReduceLink200Response**](ReduceLink200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shortened link |  -  |
**400** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

