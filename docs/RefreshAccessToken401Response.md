# RefreshAccessToken401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from urlr.models.refresh_access_token401_response import RefreshAccessToken401Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshAccessToken401Response from a JSON string
refresh_access_token401_response_instance = RefreshAccessToken401Response.from_json(json)
# print the JSON string representation of the object
print(RefreshAccessToken401Response.to_json())

# convert the object into a dict
refresh_access_token401_response_dict = refresh_access_token401_response_instance.to_dict()
# create an instance of RefreshAccessToken401Response from a dict
refresh_access_token401_response_from_dict = RefreshAccessToken401Response.from_dict(refresh_access_token401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


