# urlr.QRCodesApi

All URIs are relative to *https://urlr.me/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qrcode_create**](QRCodesApi.md#qrcode_create) | **POST** /qrcodes | Create a QR Code


# **qrcode_create**
> bytes qrcode_create(qrcode_create_request=qrcode_create_request)

Create a QR Code

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import urlr
from urlr.models.qrcode_create_request import QrcodeCreateRequest
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
    api_instance = urlr.QRCodesApi(api_client)
    qrcode_create_request = urlr.QrcodeCreateRequest() # QrcodeCreateRequest | Info of the QR Code to create (optional)

    try:
        # Create a QR Code
        api_response = api_instance.qrcode_create(qrcode_create_request=qrcode_create_request)
        print("The response of QRCodesApi->qrcode_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodesApi->qrcode_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qrcode_create_request** | [**QrcodeCreateRequest**](QrcodeCreateRequest.md)| Info of the QR Code to create | [optional] 

### Return type

**bytes**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png, image/webp, image/svg+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | QR Code |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Failed |  -  |
**429** | Limits Exceeded |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

