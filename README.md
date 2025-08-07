# urlr@2.11.0

![PyPI - Version](https://img.shields.io/pypi/v/urlr) ![PyPI - Downloads](https://img.shields.io/pypi/dm/urlr) ![PyPI - License](https://img.shields.io/pypi/l/urlr)

This SDK is automatically generated with the [OpenAPI Generator](https://openapi-generator.tech) project.

- API version: 1.10
- Package version: 2.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://urlr.me/en](https://urlr.me/en)

## Installation & Usage

## Requirements

Python 3.9+

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
import urlr
from urlr.rest import ApiException
from pprint import pprint

# Access Tokens

with urlr.ApiClient() as api_client:
    access_tokens_api = urlr.AccessTokensApi(api_client)
    
    access_tokens_request = urlr.AccessTokensRequest.from_json('{"username": "","password": ""}')

    try:
        api_response = access_tokens_api.create_access_token(access_tokens_request=access_tokens_request)
    except ApiException as e:
        print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
        quit()

# Link shortening

configuration = urlr.Configuration(
    access_token = api_response.token
)

with urlr.ApiClient(configuration) as api_client:
    link_api = urlr.LinksApi(api_client)
    create_link_request = urlr.CreateLinkRequest.from_json('{"url": "","team_id": ""}')

    try:
        # Create a link
        api_response = link_api.create_link(create_link_request=create_link_request)
        print(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->create_link: %s\n" % e)
```

A complete example is [available here](examples/example1.py).

## API Endpoints

All URIs are relative to *https://urlr.me/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessTokensApi* | [**create_access_token**](docs/AccessTokensApi.md#create_access_token) | **POST** /access_tokens/create | Get an access token
*AccessTokensApi* | [**refresh_access_token**](docs/AccessTokensApi.md#refresh_access_token) | **POST** /access_tokens/refresh | Refresh an access token
*DomainsApi* | [**create_domain**](docs/DomainsApi.md#create_domain) | **POST** /domains/create | Create a domain
*FoldersApi* | [**get_folders**](docs/FoldersApi.md#get_folders) | **GET** /folders/{team_id} | Get folders of workspace
*LinksApi* | [**create_link**](docs/LinksApi.md#create_link) | **POST** /links/create | Create a link
*LinksApi* | [**edit_link**](docs/LinksApi.md#edit_link) | **PATCH** /links/{link_id} | Edit a link
*LinksApi* | [**get_link**](docs/LinksApi.md#get_link) | **GET** /links/{link_id} | Get a link
*QRCodesApi* | [**create_qr_code**](docs/QRCodesApi.md#create_qr_code) | **POST** /qrcodes/create | Create a QR Code
*StatisticsApi* | [**get_statistics**](docs/StatisticsApi.md#get_statistics) | **POST** /statistics | Get statistics of a link
*WorkspacesApi* | [**get_teams**](docs/WorkspacesApi.md#get_teams) | **GET** /teams | Get workspaces of user


## Models

 - [BaseLinkRequest](docs/BaseLinkRequest.md)
 - [BaseLinkRequestMetatag](docs/BaseLinkRequestMetatag.md)
 - [BaseLinkRequestQrcode](docs/BaseLinkRequestQrcode.md)
 - [CreateAccessToken200Response](docs/CreateAccessToken200Response.md)
 - [CreateAccessToken401Response](docs/CreateAccessToken401Response.md)
 - [CreateAccessTokenRequest](docs/CreateAccessTokenRequest.md)
 - [CreateDomain200Response](docs/CreateDomain200Response.md)
 - [CreateDomain409Response](docs/CreateDomain409Response.md)
 - [CreateDomainRequest](docs/CreateDomainRequest.md)
 - [CreateLink429Response](docs/CreateLink429Response.md)
 - [CreateLinkRequest](docs/CreateLinkRequest.md)
 - [CreateQrCodeRequest](docs/CreateQrCodeRequest.md)
 - [CreateQrCodeRequestOneOf](docs/CreateQrCodeRequestOneOf.md)
 - [CreateQrCodeRequestOneOf1](docs/CreateQrCodeRequestOneOf1.md)
 - [EditLink500Response](docs/EditLink500Response.md)
 - [EditLinkRequest](docs/EditLinkRequest.md)
 - [GetFolders200Response](docs/GetFolders200Response.md)
 - [GetFolders200ResponseFoldersInner](docs/GetFolders200ResponseFoldersInner.md)
 - [GetLink200Response](docs/GetLink200Response.md)
 - [GetLink200ResponseGeolinksInner](docs/GetLink200ResponseGeolinksInner.md)
 - [GetLink200ResponseGeolinksInnerConditionsInner](docs/GetLink200ResponseGeolinksInnerConditionsInner.md)
 - [GetLink200ResponseMetatag](docs/GetLink200ResponseMetatag.md)
 - [GetLink200ResponseQrcode](docs/GetLink200ResponseQrcode.md)
 - [GetLink200ResponseTagsInner](docs/GetLink200ResponseTagsInner.md)
 - [GetLink200ResponseUtm](docs/GetLink200ResponseUtm.md)
 - [GetLink401Response](docs/GetLink401Response.md)
 - [GetLink404Response](docs/GetLink404Response.md)
 - [GetLink422Response](docs/GetLink422Response.md)
 - [GetStatistics200Response](docs/GetStatistics200Response.md)
 - [GetStatisticsRequest](docs/GetStatisticsRequest.md)
 - [GetTeams200Response](docs/GetTeams200Response.md)
 - [GetTeams200ResponseTeamsInner](docs/GetTeams200ResponseTeamsInner.md)
 - [RefreshAccessToken401Response](docs/RefreshAccessToken401Response.md)
 - [RefreshAccessTokenRequest](docs/RefreshAccessTokenRequest.md)


<a id="documentation-for-authorization"></a>

## Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Get help / support

Please contact [contact@urlr.me](mailto:contact@urlr.me?subject=[GitHub]%urlr-python) and we can take more direct action toward finding a solution.
