# BaseLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to shorten | [optional] 
**folder_id** | **str** | Folder API ID | [optional] 
**domain** | **str** | Domain | [optional] 
**code** | **str** | Custom short code | [optional] 
**label** | **str** | Label | [optional] 
**tags** | **List[str]** | Tags | [optional] 
**password** | **str** | Password | [optional] 
**qrcode** | [**BaseLinkRequestQrcode**](BaseLinkRequestQrcode.md) |  | [optional] 
**utm** | [**LinkUtm**](LinkUtm.md) |  | [optional] 
**metatag** | [**BaseLinkRequestMetatag**](BaseLinkRequestMetatag.md) |  | [optional] 
**geolinks** | [**List[LinkGeolinksInner]**](LinkGeolinksInner.md) | Dynamic routing conditions | [optional] 
**delete_at** | **datetime** | Scheduled deletion date | [optional] 
**expired_at** | **datetime** | Scheduled expiration date | [optional] 
**expired_url** | **str** | Expiration URL | [optional] 
**delete_after_expiration** | **bool** | Whether or not to remove the link after the expiry date | [optional] [default to False]

## Example

```python
from urlr.models.base_link_request import BaseLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseLinkRequest from a JSON string
base_link_request_instance = BaseLinkRequest.from_json(json)
# print the JSON string representation of the object
print(BaseLinkRequest.to_json())

# convert the object into a dict
base_link_request_dict = base_link_request_instance.to_dict()
# create an instance of BaseLinkRequest from a dict
base_link_request_from_dict = BaseLinkRequest.from_dict(base_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


