# urlr@3.2.0

![PyPI - Version](https://img.shields.io/pypi/v/urlr) ![PyPI - Downloads](https://img.shields.io/pypi/dm/urlr) ![PyPI - License](https://img.shields.io/pypi/l/urlr)

This SDK is automatically generated with the [OpenAPI Generator](https://openapi-generator.tech) project.

- API version: 2.1.0
- Package version: 3.2.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://urlr.me/en](https://urlr.me/en)

## Installation & Usage

## Requirements

Python 3.10+

### pip install

```sh
pip install urlr
```

Then import the package:
```python
import urlr
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import urlr
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import os
import urlr

api_key = os.getenv("URLR_API_KEY")  # to be defined on your side

configuration = urlr.Configuration()
configuration.api_key['ApiKeyAuth'] = api_key

# Create a link

with urlr.ApiClient(configuration) as api_client:
    links_api = urlr.LinksApi(api_client)
    link_create_request = urlr.LinkCreateRequest(
        url="",
    )

    try:
        link = links_api.link_create(link_create_request=link_create_request)
    except Exception as e:
        print("Exception when calling LinksApi->link_create: %s\n" % e)
```

Complete examples can be found in the [docs](https://github.com/URLR/urlr-python/tree/main/docs) directory of the client repository.

## API Endpoints

All URIs are relative to *https://urlr.me/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DomainsApi* | [**domain_create**](docs/DomainsApi.md#domain_create) | **POST** /domains | Create a domain
*DomainsApi* | [**domain_get**](docs/DomainsApi.md#domain_get) | **GET** /domains/{domain_id} | Get a domain
*DomainsApi* | [**domain_list**](docs/DomainsApi.md#domain_list) | **GET** /domains | List domains
*FoldersApi* | [**folder_create**](docs/FoldersApi.md#folder_create) | **POST** /folders | Create a folder
*FoldersApi* | [**folder_get**](docs/FoldersApi.md#folder_get) | **GET** /folders/{folder_id} | Get a folder
*FoldersApi* | [**folder_list**](docs/FoldersApi.md#folder_list) | **GET** /folders | List folders
*LinksApi* | [**link_create**](docs/LinksApi.md#link_create) | **POST** /links | Create a link
*LinksApi* | [**link_delete**](docs/LinksApi.md#link_delete) | **DELETE** /links/{link_id} | Delete a link
*LinksApi* | [**link_edit**](docs/LinksApi.md#link_edit) | **PATCH** /links/{link_id} | Edit a link
*LinksApi* | [**link_get**](docs/LinksApi.md#link_get) | **GET** /links/{link_id} | Get a link
*LinksApi* | [**link_list**](docs/LinksApi.md#link_list) | **GET** /links | List links
*QRCodesApi* | [**qrcode_create**](docs/QRCodesApi.md#qrcode_create) | **POST** /qrcodes | Create a QR Code
*StatisticsApi* | [**statistic_get**](docs/StatisticsApi.md#statistic_get) | **GET** /statistics | Get statistics


## Models

 - [Domain](docs/Domain.md)
 - [DomainCreate409Response](docs/DomainCreate409Response.md)
 - [DomainCreate429Response](docs/DomainCreate429Response.md)
 - [DomainCreateRequest](docs/DomainCreateRequest.md)
 - [DomainGet401Response](docs/DomainGet401Response.md)
 - [DomainGet404Response](docs/DomainGet404Response.md)
 - [DomainGet422Response](docs/DomainGet422Response.md)
 - [DomainGet500Response](docs/DomainGet500Response.md)
 - [DomainList200Response](docs/DomainList200Response.md)
 - [Folder](docs/Folder.md)
 - [FolderCreateRequest](docs/FolderCreateRequest.md)
 - [FolderList200Response](docs/FolderList200Response.md)
 - [Link](docs/Link.md)
 - [LinkBaseRequest](docs/LinkBaseRequest.md)
 - [LinkBaseRequestMetatag](docs/LinkBaseRequestMetatag.md)
 - [LinkBaseRequestQrcode](docs/LinkBaseRequestQrcode.md)
 - [LinkCreateRequest](docs/LinkCreateRequest.md)
 - [LinkEditRequest](docs/LinkEditRequest.md)
 - [LinkGeolinksInner](docs/LinkGeolinksInner.md)
 - [LinkGeolinksInnerConditionsInner](docs/LinkGeolinksInnerConditionsInner.md)
 - [LinkList200Response](docs/LinkList200Response.md)
 - [LinkMetatag](docs/LinkMetatag.md)
 - [LinkQrcode](docs/LinkQrcode.md)
 - [LinkTagsInner](docs/LinkTagsInner.md)
 - [LinkUtm](docs/LinkUtm.md)
 - [QrcodeCreateRequest](docs/QrcodeCreateRequest.md)
 - [QrcodeCreateRequestOneOf](docs/QrcodeCreateRequestOneOf.md)
 - [QrcodeCreateRequestOneOf1](docs/QrcodeCreateRequestOneOf1.md)
 - [StatisticGet200Response](docs/StatisticGet200Response.md)


<a id="documentation-for-authorization"></a>

## Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Get help / support

Please contact [contact@urlr.me](mailto:contact@urlr.me?subject=[GitHub]%urlr-python) and we can take more direct action toward finding a solution.
