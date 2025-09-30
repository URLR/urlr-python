# CreateFolder409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.create_folder409_response import CreateFolder409Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolder409Response from a JSON string
create_folder409_response_instance = CreateFolder409Response.from_json(json)
# print the JSON string representation of the object
print(CreateFolder409Response.to_json())

# convert the object into a dict
create_folder409_response_dict = create_folder409_response_instance.to_dict()
# create an instance of CreateFolder409Response from a dict
create_folder409_response_from_dict = CreateFolder409Response.from_dict(create_folder409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


