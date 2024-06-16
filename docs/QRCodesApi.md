# urlr.QRCodesApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_qr_code**](QRCodesApi.md#create_qr_code) | **POST** /qrcodes/create | Create a QR Code


# **create_qr_code**
> bytearray create_qr_code(create_qr_code_request=create_qr_code_request)

Create a QR Code

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urlr
from urlr.models.create_qr_code_request import CreateQrCodeRequest
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
    api_instance = urlr.QRCodesApi(api_client)
    create_qr_code_request = urlr.CreateQrCodeRequest() # CreateQrCodeRequest | Info of the QR Code to create (optional)

    try:
        # Create a QR Code
        api_response = api_instance.create_qr_code(create_qr_code_request=create_qr_code_request)
        print("The response of QRCodesApi->create_qr_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodesApi->create_qr_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_qr_code_request** | [**CreateQrCodeRequest**](CreateQrCodeRequest.md)| Info of the QR Code to create | [optional] 

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png, image/webp, image/svg+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | QR Code |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Failed |  -  |
**429** | Limits Exceeded |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

