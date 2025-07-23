# LinkEditRequest


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
**qrcode** | [**LinkBaseRequestQrcode**](LinkBaseRequestQrcode.md) |  | [optional] 
**utm** | [**GetLink200ResponseUtm**](GetLink200ResponseUtm.md) |  | [optional] 
**metatag** | [**LinkBaseRequestMetatag**](LinkBaseRequestMetatag.md) |  | [optional] 
**geolinks** | [**List[GetLink200ResponseGeolinksInner]**](GetLink200ResponseGeolinksInner.md) | Dynamic routing conditions | [optional] 
**delete_at** | **datetime** | Scheduled deletion date | [optional] 
**expired_at** | **datetime** | Scheduled expiration date | [optional] 
**expired_url** | **str** | Expiration URL | [optional] 
**delete_after_expiration** | **bool** | Whether or not to remove the link after the expiry date | [optional] [default to False]

## Example

```python
from urlr.models.link_edit_request import LinkEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkEditRequest from a JSON string
link_edit_request_instance = LinkEditRequest.from_json(json)
# print the JSON string representation of the object
print(LinkEditRequest.to_json())

# convert the object into a dict
link_edit_request_dict = link_edit_request_instance.to_dict()
# create an instance of LinkEditRequest from a dict
link_edit_request_from_dict = LinkEditRequest.from_dict(link_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


