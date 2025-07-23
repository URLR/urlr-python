# EditLink500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.edit_link500_response import EditLink500Response

# TODO update the JSON string below
json = "{}"
# create an instance of EditLink500Response from a JSON string
edit_link500_response_instance = EditLink500Response.from_json(json)
# print the JSON string representation of the object
print(EditLink500Response.to_json())

# convert the object into a dict
edit_link500_response_dict = edit_link500_response_instance.to_dict()
# create an instance of EditLink500Response from a dict
edit_link500_response_from_dict = EditLink500Response.from_dict(edit_link500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


