# CreateDomain200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain | [optional] 
**root_url** | **str** | Redirect URL for the root of the domain | [optional] 

## Example

```python
from urlr.models.create_domain200_response import CreateDomain200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomain200Response from a JSON string
create_domain200_response_instance = CreateDomain200Response.from_json(json)
# print the JSON string representation of the object
print(CreateDomain200Response.to_json())

# convert the object into a dict
create_domain200_response_dict = create_domain200_response_instance.to_dict()
# create an instance of CreateDomain200Response from a dict
create_domain200_response_from_dict = CreateDomain200Response.from_dict(create_domain200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


