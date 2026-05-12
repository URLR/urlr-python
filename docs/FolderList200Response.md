# FolderList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[Folder]**](Folder.md) |  | [optional] 

## Example

```python
from urlr.models.folder_list200_response import FolderList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FolderList200Response from a JSON string
folder_list200_response_instance = FolderList200Response.from_json(json)
# print the JSON string representation of the object
print(FolderList200Response.to_json())

# convert the object into a dict
folder_list200_response_dict = folder_list200_response_instance.to_dict()
# create an instance of FolderList200Response from a dict
folder_list200_response_from_dict = FolderList200Response.from_dict(folder_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


