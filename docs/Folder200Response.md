# Folder200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[Folder200ResponseFoldersInner]**](Folder200ResponseFoldersInner.md) |  | [optional] 

## Example

```python
from urlr.models.folder200_response import Folder200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Folder200Response from a JSON string
folder200_response_instance = Folder200Response.from_json(json)
# print the JSON string representation of the object
print(Folder200Response.to_json())

# convert the object into a dict
folder200_response_dict = folder200_response_instance.to_dict()
# create an instance of Folder200Response from a dict
folder200_response_from_dict = Folder200Response.from_dict(folder200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


