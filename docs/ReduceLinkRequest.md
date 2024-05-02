# ReduceLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to shorten | 
**team** | **str** | Team ID (displayed on dashboard) | 
**folder** | **str** | Folder ID (displayed on dashboard) | [optional] 
**code** | **str** | Custom short code | [optional] 
**label** | **str** | Label | [optional] 
**password** | **str** | Password | [optional] 
**expired_at** | **str** | Expiration date | [optional] 

## Example

```python
from urlr.models.reduce_link_request import ReduceLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReduceLinkRequest from a JSON string
reduce_link_request_instance = ReduceLinkRequest.from_json(json)
# print the JSON string representation of the object
print(ReduceLinkRequest.to_json())

# convert the object into a dict
reduce_link_request_dict = reduce_link_request_instance.to_dict()
# create an instance of ReduceLinkRequest from a dict
reduce_link_request_from_dict = ReduceLinkRequest.from_dict(reduce_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


