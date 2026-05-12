# DomainGet401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.domain_get401_response import DomainGet401Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGet401Response from a JSON string
domain_get401_response_instance = DomainGet401Response.from_json(json)
# print the JSON string representation of the object
print(DomainGet401Response.to_json())

# convert the object into a dict
domain_get401_response_dict = domain_get401_response_instance.to_dict()
# create an instance of DomainGet401Response from a dict
domain_get401_response_from_dict = DomainGet401Response.from_dict(domain_get401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


