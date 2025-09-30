# CreateFolder200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** | Team API ID | [optional] 
**name** | **str** | Name | [optional] 
**parent_id** | **str** | Parent Folder API ID (if any) | [optional] 
**parent_name** | **str** | Parent Folder name (if any) | [optional] 
**color** | **str** | Color of folder | [optional] 

## Example

```python
from urlr.models.create_folder200_response import CreateFolder200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolder200Response from a JSON string
create_folder200_response_instance = CreateFolder200Response.from_json(json)
# print the JSON string representation of the object
print(CreateFolder200Response.to_json())

# convert the object into a dict
create_folder200_response_dict = create_folder200_response_instance.to_dict()
# create an instance of CreateFolder200Response from a dict
create_folder200_response_from_dict = CreateFolder200Response.from_dict(create_folder200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


