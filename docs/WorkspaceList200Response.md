# WorkspaceList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[Workspace]**](Workspace.md) |  | [optional] 

## Example

```python
from urlr.models.workspace_list200_response import WorkspaceList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceList200Response from a JSON string
workspace_list200_response_instance = WorkspaceList200Response.from_json(json)
# print the JSON string representation of the object
print(WorkspaceList200Response.to_json())

# convert the object into a dict
workspace_list200_response_dict = workspace_list200_response_instance.to_dict()
# create an instance of WorkspaceList200Response from a dict
workspace_list200_response_from_dict = WorkspaceList200Response.from_dict(workspace_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


