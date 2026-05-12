# DomainCreate429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.domain_create429_response import DomainCreate429Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreate429Response from a JSON string
domain_create429_response_instance = DomainCreate429Response.from_json(json)
# print the JSON string representation of the object
print(DomainCreate429Response.to_json())

# convert the object into a dict
domain_create429_response_dict = domain_create429_response_instance.to_dict()
# create an instance of DomainCreate429Response from a dict
domain_create429_response_from_dict = DomainCreate429Response.from_dict(domain_create429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


