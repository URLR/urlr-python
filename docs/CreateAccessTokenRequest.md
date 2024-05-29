# CreateAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Email | 
**password** | **str** | Password | 

## Example

```python
from urlr.models.create_access_token_request import CreateAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessTokenRequest from a JSON string
create_access_token_request_instance = CreateAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccessTokenRequest.to_json())

# convert the object into a dict
create_access_token_request_dict = create_access_token_request_instance.to_dict()
# create an instance of CreateAccessTokenRequest from a dict
create_access_token_request_from_dict = CreateAccessTokenRequest.from_dict(create_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


