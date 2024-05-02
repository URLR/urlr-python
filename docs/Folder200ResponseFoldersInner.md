# Folder200ResponseFoldersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Folder ID | [optional] 
**name** | **str** | Folder name | [optional] 

## Example

```python
from urlr.models.folder200_response_folders_inner import Folder200ResponseFoldersInner

# TODO update the JSON string below
json = "{}"
# create an instance of Folder200ResponseFoldersInner from a JSON string
folder200_response_folders_inner_instance = Folder200ResponseFoldersInner.from_json(json)
# print the JSON string representation of the object
print(Folder200ResponseFoldersInner.to_json())

# convert the object into a dict
folder200_response_folders_inner_dict = folder200_response_folders_inner_instance.to_dict()
# create an instance of Folder200ResponseFoldersInner from a dict
folder200_response_folders_inner_from_dict = Folder200ResponseFoldersInner.from_dict(folder200_response_folders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


