# CreateLink500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.create_link500_response import CreateLink500Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLink500Response from a JSON string
create_link500_response_instance = CreateLink500Response.from_json(json)
# print the JSON string representation of the object
print(CreateLink500Response.to_json())

# convert the object into a dict
create_link500_response_dict = create_link500_response_instance.to_dict()
# create an instance of CreateLink500Response from a dict
create_link500_response_from_dict = CreateLink500Response.from_dict(create_link500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


