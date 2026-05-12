# DomainCreate409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.domain_create409_response import DomainCreate409Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreate409Response from a JSON string
domain_create409_response_instance = DomainCreate409Response.from_json(json)
# print the JSON string representation of the object
print(DomainCreate409Response.to_json())

# convert the object into a dict
domain_create409_response_dict = domain_create409_response_instance.to_dict()
# create an instance of DomainCreate409Response from a dict
domain_create409_response_from_dict = DomainCreate409Response.from_dict(domain_create409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


