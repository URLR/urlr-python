# CreateAccessToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Access token (JWT) valid for 1 hour | [optional] 
**refresh_token** | **str** | Refresh token valid for 1 month | [optional] 

## Example

```python
from urlr.models.create_access_token200_response import CreateAccessToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessToken200Response from a JSON string
create_access_token200_response_instance = CreateAccessToken200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAccessToken200Response.to_json())

# convert the object into a dict
create_access_token200_response_dict = create_access_token200_response_instance.to_dict()
# create an instance of CreateAccessToken200Response from a dict
create_access_token200_response_from_dict = CreateAccessToken200Response.from_dict(create_access_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


