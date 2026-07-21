# urlr.DomainsApi

All URIs are relative to *https://urlr.me/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_create**](DomainsApi.md#domain_create) | **POST** /domains | Create a domain
[**domain_get**](DomainsApi.md#domain_get) | **GET** /domains/{domain_id} | Get a domain
[**domain_list**](DomainsApi.md#domain_list) | **GET** /domains | List domains


# **domain_create**
> Domain domain_create(domain_create_request=domain_create_request)

Create a domain

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.domain import Domain
from urlr.models.domain_create_request import DomainCreateRequest
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
    api_instance = urlr.DomainsApi(api_client)
    domain_create_request = urlr.DomainCreateRequest() # DomainCreateRequest | You can use this endpoint to add a custom domain to URLR. (optional)

    try:
        # Create a domain
        api_response = api_instance.domain_create(domain_create_request=domain_create_request)
        print("The response of DomainsApi->domain_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domain_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_create_request** | [**DomainCreateRequest**](DomainCreateRequest.md)| You can use this endpoint to add a custom domain to URLR. | [optional] 

### Return type

[**Domain**](Domain.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain |  -  |
**401** | Unauthorized |  -  |
**429** | Limits Exceeded |  -  |
**409** | Conflict |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_get**
> Domain domain_get(domain_id)

Get a domain

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.domain import Domain
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
    api_instance = urlr.DomainsApi(api_client)
    domain_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Domain API ID

    try:
        # Get a domain
        api_response = api_instance.domain_get(domain_id)
        print("The response of DomainsApi->domain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **UUID**| Domain API ID | 

### Return type

[**Domain**](Domain.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_list**
> DomainList200Response domain_list()

List domains

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.domain_list200_response import DomainList200Response
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
    api_instance = urlr.DomainsApi(api_client)

    try:
        # List domains
        api_response = api_instance.domain_list()
        print("The response of DomainsApi->domain_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domain_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainList200Response**](DomainList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domains of user |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

