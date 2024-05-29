# RefreshAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | Refresh token | 

## Example

```python
from urlr.models.refresh_access_token_request import RefreshAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshAccessTokenRequest from a JSON string
refresh_access_token_request_instance = RefreshAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshAccessTokenRequest.to_json())

# convert the object into a dict
refresh_access_token_request_dict = refresh_access_token_request_instance.to_dict()
# create an instance of RefreshAccessTokenRequest from a dict
refresh_access_token_request_from_dict = RefreshAccessTokenRequest.from_dict(refresh_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


