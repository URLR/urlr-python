# urlr.LinksApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_link**](LinksApi.md#create_link) | **POST** /links/create | Create a link
[**edit_link**](LinksApi.md#edit_link) | **PATCH** /links/{link_id} | Edit a link
[**get_link**](LinksApi.md#get_link) | **GET** /links/{link_id} | Get a link
[**list_links**](LinksApi.md#list_links) | **GET** /links | List links


# **create_link**
> Link create_link(create_link_request=create_link_request)

Create a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.create_link_request import CreateLinkRequest
from urlr.models.link import Link
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

[**Link**](Link.md)

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

# **edit_link**
> Link edit_link(link_id, edit_link_request=edit_link_request)

Edit a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.edit_link_request import EditLinkRequest
from urlr.models.link import Link
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
    edit_link_request = urlr.EditLinkRequest() # EditLinkRequest | Info of the link to edit (optional)

    try:
        # Edit a link
        api_response = api_instance.edit_link(link_id, edit_link_request=edit_link_request)
        print("The response of LinksApi->edit_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->edit_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**| Link API ID | 
 **edit_link_request** | [**EditLinkRequest**](EditLinkRequest.md)| Info of the link to edit | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link**
> Link get_link(link_id)

Get a link

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.link import Link
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

[**Link**](Link.md)

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

# **list_links**
> ListLinks200Response list_links(team_id=team_id, folder_id=folder_id, tag_id=tag_id, limit=limit, page=page)

List links

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.list_links200_response import ListLinks200Response
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
    team_id = 'team_id_example' # str | Filter by Workspace API ID (optional)
    folder_id = 'folder_id_example' # str | Filter by Folder API ID (optional)
    tag_id = 'tag_id_example' # str | Filter by Tag API ID (optional)
    limit = 10 # int | Number of items per page (optional) (default to 10)
    page = 1 # int | Page number (optional) (default to 1)

    try:
        # List links
        api_response = api_instance.list_links(team_id=team_id, folder_id=folder_id, tag_id=tag_id, limit=limit, page=page)
        print("The response of LinksApi->list_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->list_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Filter by Workspace API ID | [optional] 
 **folder_id** | **str**| Filter by Folder API ID | [optional] 
 **tag_id** | **str**| Filter by Tag API ID | [optional] 
 **limit** | **int**| Number of items per page | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**ListLinks200Response**](ListLinks200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

