# urlr.LinksApi

All URIs are relative to *https://urlr.me/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_create**](LinksApi.md#link_create) | **POST** /links | Create a link
[**link_delete**](LinksApi.md#link_delete) | **DELETE** /links/{link_id} | Delete a link
[**link_edit**](LinksApi.md#link_edit) | **PATCH** /links/{link_id} | Edit a link
[**link_get**](LinksApi.md#link_get) | **GET** /links/{link_id} | Get a link
[**link_list**](LinksApi.md#link_list) | **GET** /links | List links


# **link_create**
> Link link_create(link_create_request=link_create_request)

Create a link

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.link import Link
from urlr.models.link_create_request import LinkCreateRequest
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
    api_instance = urlr.LinksApi(api_client)
    link_create_request = urlr.LinkCreateRequest() # LinkCreateRequest | Info of the link to create (optional)

    try:
        # Create a link
        api_response = api_instance.link_create(link_create_request=link_create_request)
        print("The response of LinksApi->link_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->link_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_create_request** | [**LinkCreateRequest**](LinkCreateRequest.md)| Info of the link to create | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **link_delete**
> link_delete(link_id)

Delete a link

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
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
    api_instance = urlr.LinksApi(api_client)
    link_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Link API ID

    try:
        # Delete a link
        api_instance.link_delete(link_id)
    except Exception as e:
        print("Exception when calling LinksApi->link_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **UUID**| Link API ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Link deleted |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_edit**
> Link link_edit(link_id, link_edit_request=link_edit_request)

Edit a link

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.link import Link
from urlr.models.link_edit_request import LinkEditRequest
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
    api_instance = urlr.LinksApi(api_client)
    link_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Link API ID
    link_edit_request = urlr.LinkEditRequest() # LinkEditRequest | Info of the link to edit (optional)

    try:
        # Edit a link
        api_response = api_instance.link_edit(link_id, link_edit_request=link_edit_request)
        print("The response of LinksApi->link_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->link_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **UUID**| Link API ID | 
 **link_edit_request** | [**LinkEditRequest**](LinkEditRequest.md)| Info of the link to edit | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_get**
> Link link_get(link_id)

Get a link

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.link import Link
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
    api_instance = urlr.LinksApi(api_client)
    link_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Link API ID

    try:
        # Get a link
        api_response = api_instance.link_get(link_id)
        print("The response of LinksApi->link_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->link_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **UUID**| Link API ID | 

### Return type

[**Link**](Link.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **link_list**
> LinkList200Response link_list(folder_id=folder_id, tag_id=tag_id, limit=limit, page=page)

List links

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.link_list200_response import LinkList200Response
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
    api_instance = urlr.LinksApi(api_client)
    folder_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by Folder API ID (optional)
    tag_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by Tag API ID (optional)
    limit = 10 # int | Number of items per page (optional) (default to 10)
    page = 1 # int | Page number (optional) (default to 1)

    try:
        # List links
        api_response = api_instance.link_list(folder_id=folder_id, tag_id=tag_id, limit=limit, page=page)
        print("The response of LinksApi->link_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->link_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **UUID**| Filter by Folder API ID | [optional] 
 **tag_id** | **UUID**| Filter by Tag API ID | [optional] 
 **limit** | **int**| Number of items per page | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**LinkList200Response**](LinkList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of links |  -  |
**422** | Validation Failed |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

