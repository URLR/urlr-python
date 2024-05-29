# CreateLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to shorten | 
**team_id** | **str** | Team API ID | 
**folder_id** | **str** | Folder API ID | [optional] 
**code** | **str** | Custom short code | [optional] 
**label** | **str** | Label | [optional] 
**password** | **str** | Password | [optional] 
**expired_at** | **datetime** | Expiration date | [optional] 

## Example

```python
from urlr.models.create_link_request import CreateLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLinkRequest from a JSON string
create_link_request_instance = CreateLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateLinkRequest.to_json())

# convert the object into a dict
create_link_request_dict = create_link_request_instance.to_dict()
# create an instance of CreateLinkRequest from a dict
create_link_request_from_dict = CreateLinkRequest.from_dict(create_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


