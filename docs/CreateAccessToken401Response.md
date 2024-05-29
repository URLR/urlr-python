# CreateAccessToken401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from urlr.models.create_access_token401_response import CreateAccessToken401Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessToken401Response from a JSON string
create_access_token401_response_instance = CreateAccessToken401Response.from_json(json)
# print the JSON string representation of the object
print(CreateAccessToken401Response.to_json())

# convert the object into a dict
create_access_token401_response_dict = create_access_token401_response_instance.to_dict()
# create an instance of CreateAccessToken401Response from a dict
create_access_token401_response_from_dict = CreateAccessToken401Response.from_dict(create_access_token401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


