# CreateDomain409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.create_domain409_response import CreateDomain409Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomain409Response from a JSON string
create_domain409_response_instance = CreateDomain409Response.from_json(json)
# print the JSON string representation of the object
print(CreateDomain409Response.to_json())

# convert the object into a dict
create_domain409_response_dict = create_domain409_response_instance.to_dict()
# create an instance of CreateDomain409Response from a dict
create_domain409_response_from_dict = CreateDomain409Response.from_dict(create_domain409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


