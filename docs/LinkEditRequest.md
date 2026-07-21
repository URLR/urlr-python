# LinkEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to shorten | [optional] 
**folder_id** | **UUID** | Folder API ID | [optional] 
**domain** | **str** | Domain | [optional] 
**code** | **str** | Length must be between 2 and 50 characters if a custom domain is set, or between 2 and 49 characters otherwise. | [optional] 
**label** | **str** | Label | [optional] 
**password** | **str** | Password | [optional] 
**delete_at** | **datetime** | Scheduled deletion date | [optional] 
**expired_at** | **datetime** | Scheduled expiration date | [optional] 
**expired_url** | **str** | The URL to which users will be redirected after the link has expired | [optional] 
**expired_title** | **str** | The title displayed on the expiration page | [optional] 
**expired_text** | **str** | The text displayed on the expiration page | [optional] 
**delete_after_expiration** | **bool** | Whether the link should be deleted once it has expired | [optional] [default to False]
**tags** | **List[UUID]** | Tags | [optional] 
**qrcode** | [**LinkBaseRequestQrcode**](LinkBaseRequestQrcode.md) |  | [optional] 
**utm** | [**LinkUtm**](LinkUtm.md) |  | [optional] 
**metatag** | [**LinkBaseRequestMetatag**](LinkBaseRequestMetatag.md) |  | [optional] 
**geolinks** | [**List[LinkGeolinksInner]**](LinkGeolinksInner.md) | Dynamic routing conditions | [optional] 

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


