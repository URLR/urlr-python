# Folder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Folder API ID | [optional] 
**name** | **str** | Name | [optional] 
**workspace_id** | **UUID** | Workspace API ID | [optional] 
**parent_id** | **UUID** | Parent Folder API ID | [optional] 
**parent_name** | **str** | Parent Folder name | [optional] 
**color** | **str** | Color of folder | [optional] 
**domain** | **str** | Domain | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Modification date | [optional] 

## Example

```python
from urlr.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print(Folder.to_json())

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_from_dict = Folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


