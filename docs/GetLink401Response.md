# GetLink401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.get_link401_response import GetLink401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink401Response from a JSON string
get_link401_response_instance = GetLink401Response.from_json(json)
# print the JSON string representation of the object
print(GetLink401Response.to_json())

# convert the object into a dict
get_link401_response_dict = get_link401_response_instance.to_dict()
# create an instance of GetLink401Response from a dict
get_link401_response_from_dict = GetLink401Response.from_dict(get_link401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


