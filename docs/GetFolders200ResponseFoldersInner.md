# GetFolders200ResponseFoldersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Folder API ID | [optional] 
**name** | **str** | Folder name | [optional] 

## Example

```python
from urlr.models.get_folders200_response_folders_inner import GetFolders200ResponseFoldersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFolders200ResponseFoldersInner from a JSON string
get_folders200_response_folders_inner_instance = GetFolders200ResponseFoldersInner.from_json(json)
# print the JSON string representation of the object
print(GetFolders200ResponseFoldersInner.to_json())

# convert the object into a dict
get_folders200_response_folders_inner_dict = get_folders200_response_folders_inner_instance.to_dict()
# create an instance of GetFolders200ResponseFoldersInner from a dict
get_folders200_response_folders_inner_from_dict = GetFolders200ResponseFoldersInner.from_dict(get_folders200_response_folders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


