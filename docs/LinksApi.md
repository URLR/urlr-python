# urlr.LinksApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_link**](LinksApi.md#create_link) | **POST** /links/create | Create a link
[**get_link**](LinksApi.md#get_link) | **GET** /links/{link_id} | Get a link


# **create_link**
> CreateLink201Response create_link(create_link_request=create_link_request)

Create a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.create_link201_response import CreateLink201Response
from urlr.models.create_link_request import CreateLinkRequest
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
    api_instance = urlr.LinksApi(api_client)
    create_link_request = urlr.CreateLinkRequest() # CreateLinkRequest | Info of the link to create (optional)

    try:
        # Create a link
        api_response = api_instance.create_link(create_link_request=create_link_request)
        print("The response of LinksApi->create_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->create_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_link_request** | [**CreateLinkRequest**](CreateLinkRequest.md)| Info of the link to create | [optional] 

### Return type

[**CreateLink201Response**](CreateLink201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Link |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**429** | Limits Exceeded |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link**
> GetLink200Response get_link(link_id)

Get a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.get_link200_response import GetLink200Response
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
    api_instance = urlr.LinksApi(api_client)
    link_id = 'ffefc6c4-d970-4373-a867-2a69c8be2c89' # str | Link API ID

    try:
        # Get a link
        api_response = api_instance.get_link(link_id)
        print("The response of LinksApi->get_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->get_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**| Link API ID | 

### Return type

[**GetLink200Response**](GetLink200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

