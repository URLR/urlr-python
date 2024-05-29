# GetFolders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[GetFolders200ResponseFoldersInner]**](GetFolders200ResponseFoldersInner.md) |  | [optional] 

## Example

```python
from urlr.models.get_folders200_response import GetFolders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFolders200Response from a JSON string
get_folders200_response_instance = GetFolders200Response.from_json(json)
# print the JSON string representation of the object
print(GetFolders200Response.to_json())

# convert the object into a dict
get_folders200_response_dict = get_folders200_response_instance.to_dict()
# create an instance of GetFolders200Response from a dict
get_folders200_response_from_dict = GetFolders200Response.from_dict(get_folders200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


