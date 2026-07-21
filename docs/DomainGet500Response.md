# DomainGet500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.domain_get500_response import DomainGet500Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGet500Response from a JSON string
domain_get500_response_instance = DomainGet500Response.from_json(json)
# print the JSON string representation of the object
print(DomainGet500Response.to_json())

# convert the object into a dict
domain_get500_response_dict = domain_get500_response_instance.to_dict()
# create an instance of DomainGet500Response from a dict
domain_get500_response_from_dict = DomainGet500Response.from_dict(domain_get500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


