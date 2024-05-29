# urlr.AccessTokensApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](AccessTokensApi.md#create_access_token) | **POST** /access_tokens/create | Get an access token
[**refresh_access_token**](AccessTokensApi.md#refresh_access_token) | **POST** /access_tokens/refresh | Refresh an access token


# **create_access_token**
> CreateAccessToken200Response create_access_token(create_access_token_request=create_access_token_request)

Get an access token

### Example


```python
import urlr
from urlr.models.create_access_token200_response import CreateAccessToken200Response
from urlr.models.create_access_token_request import CreateAccessTokenRequest
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v1"
)


# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.AccessTokensApi(api_client)
    create_access_token_request = urlr.CreateAccessTokenRequest() # CreateAccessTokenRequest | You can use this endpoint to get an access token to access the API. (optional)

    try:
        # Get an access token
        api_response = api_instance.create_access_token(create_access_token_request=create_access_token_request)
        print("The response of AccessTokensApi->create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_access_token_request** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)| You can use this endpoint to get an access token to access the API. | [optional] 

### Return type

[**CreateAccessToken200Response**](CreateAccessToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access token |  -  |
**401** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_access_token**
> CreateAccessToken200Response refresh_access_token(refresh_access_token_request=refresh_access_token_request)

Refresh an access token

### Example


```python
import urlr
from urlr.models.create_access_token200_response import CreateAccessToken200Response
from urlr.models.refresh_access_token_request import RefreshAccessTokenRequest
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api/v1"
)


# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.AccessTokensApi(api_client)
    refresh_access_token_request = urlr.RefreshAccessTokenRequest() # RefreshAccessTokenRequest | You can use this endpoint to refresh your access token without credentials. (optional)

    try:
        # Refresh an access token
        api_response = api_instance.refresh_access_token(refresh_access_token_request=refresh_access_token_request)
        print("The response of AccessTokensApi->refresh_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokensApi->refresh_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_access_token_request** | [**RefreshAccessTokenRequest**](RefreshAccessTokenRequest.md)| You can use this endpoint to refresh your access token without credentials. | [optional] 

### Return type

[**CreateAccessToken200Response**](CreateAccessToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refreshed access token |  -  |
**401** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

