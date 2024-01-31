# urlr.AuthentificationApi

All URIs are relative to *https://urlr.me/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentification**](AuthentificationApi.md#authentification) | **POST** /login_check | Get an access token


# **authentification**
> Authentification200Response authentification(authentification_request=authentification_request)

Get an access token

### Example


```python
import time
import os
import urlr
from urlr.models.authentification200_response import Authentification200Response
from urlr.models.authentification_request import AuthentificationRequest
from urlr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlr.me/api
# See configuration.py for a list of all supported configuration parameters.
configuration = urlr.Configuration(
    host = "https://urlr.me/api"
)


# Enter a context with an instance of the API client
with urlr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlr.AuthentificationApi(api_client)
    authentification_request = urlr.AuthentificationRequest() # AuthentificationRequest | Your credentials (optional)

    try:
        # Get an access token
        api_response = api_instance.authentification(authentification_request=authentification_request)
        print("The response of AuthentificationApi->authentification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthentificationApi->authentification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentification_request** | [**AuthentificationRequest**](AuthentificationRequest.md)| Your credentials | [optional] 

### Return type

[**Authentification200Response**](Authentification200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Your token is ready! |  -  |
**401** | Invalid credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

