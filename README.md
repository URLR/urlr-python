# urlr@1.0.0

This SDK is automatically generated with the [OpenAPI Generator](https://openapi-generator.tech) project.

- API version: 0.2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://urlr.me/en](https://urlr.me/en)

## Installation & Usage

## Requirements

Python 3.7+

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

# Authentification

with urlr.ApiClient() as api_client:
    authentification_api = urlr.AuthentificationApi(api_client)
    
    authentification_request = urlr.AuthentificationRequest.from_json('{"username": "","password": ""}')

    try:
        api_response = authentification_api.authentification(authentification_request=authentification_request)
    except ApiException as e:
        print("Exception when calling AuthentificationApi->authentification: %s\n" % e)
        quit()

# Link shortening

configuration = urlr.Configuration(
    access_token = api_response.token
)

with urlr.ApiClient(configuration) as api_client:
    link_api = urlr.LinkApi(api_client)
    reduce_link_request = urlr.ReduceLinkRequest.from_json('{"url": "","team": ""}')

    try:
        # Reduce a link
        api_response = link_api.reduce_link(reduce_link_request=reduce_link_request)
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->reduce_link: %s\n" % e)
```

A complete example is [available here](examples/example1.py).

## API Endpoints

All URIs are relative to *https://urlr.me/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthentificationApi* | [**authentification**](docs/AuthentificationApi.md#authentification) | **POST** /login_check | Get an access token
*LinkApi* | [**reduce_link**](docs/LinkApi.md#reduce_link) | **POST** /reduce-link | Reduce a link
*StatsApi* | [**stats**](docs/StatsApi.md#stats) | **POST** /stats | Get statistics of a link


## Models

 - [Authentification200Response](docs/Authentification200Response.md)
 - [Authentification401Response](docs/Authentification401Response.md)
 - [AuthentificationRequest](docs/AuthentificationRequest.md)
 - [ReduceLink200Response](docs/ReduceLink200Response.md)
 - [ReduceLink400Response](docs/ReduceLink400Response.md)
 - [ReduceLinkRequest](docs/ReduceLinkRequest.md)
 - [Stats200Response](docs/Stats200Response.md)
 - [Stats400Response](docs/Stats400Response.md)
 - [StatsRequest](docs/StatsRequest.md)


<a id="documentation-for-authorization"></a>

## Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Get help / support

Please contact [contact@urlr.me](mailto:contact@urlr.me?subject=[GitHub]%urlr-python) and we can take more direct action toward finding a solution.
