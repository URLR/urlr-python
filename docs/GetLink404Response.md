# GetLink404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.get_link404_response import GetLink404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink404Response from a JSON string
get_link404_response_instance = GetLink404Response.from_json(json)
# print the JSON string representation of the object
print(GetLink404Response.to_json())

# convert the object into a dict
get_link404_response_dict = get_link404_response_instance.to_dict()
# create an instance of GetLink404Response from a dict
get_link404_response_from_dict = GetLink404Response.from_dict(get_link404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


