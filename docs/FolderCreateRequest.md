# FolderCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**parent_id** | **UUID** | Folder API ID | [optional] 
**color** | **str** | Color of folder | [optional] 

## Example

```python
from urlr.models.folder_create_request import FolderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreateRequest from a JSON string
folder_create_request_instance = FolderCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FolderCreateRequest.to_json())

# convert the object into a dict
folder_create_request_dict = folder_create_request_instance.to_dict()
# create an instance of FolderCreateRequest from a dict
folder_create_request_from_dict = FolderCreateRequest.from_dict(folder_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


