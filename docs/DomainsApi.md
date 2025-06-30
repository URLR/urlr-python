# urlr.DomainsApi

All URIs are relative to *https://urlr.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainsApi.md#create_domain) | **POST** /domains/create | Create a domain


# **create_domain**
> CreateDomain200Response create_domain(create_domain_request=create_domain_request)

Create a domain

### Example


```python
import urlr
from urlr.models.create_domain200_response import CreateDomain200Response
from urlr.models.create_domain_request import CreateDomainRequest
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
    api_instance = urlr.DomainsApi(api_client)
    create_domain_request = urlr.CreateDomainRequest() # CreateDomainRequest | You can use this endpoint to add a custom domain to URLR. (optional)

    try:
        # Create a domain
        api_response = api_instance.create_domain(create_domain_request=create_domain_request)
        print("The response of DomainsApi->create_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->create_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_domain_request** | [**CreateDomainRequest**](CreateDomainRequest.md)| You can use this endpoint to add a custom domain to URLR. | [optional] 

### Return type

[**CreateDomain200Response**](CreateDomain200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain |  -  |
**401** | Unauthorized |  -  |
**429** | Limits Exceeded |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

