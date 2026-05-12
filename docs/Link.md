# Link


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Link API ID | [optional] 
**url** | **str** | Original URL | [optional] 
**workspace_id** | **UUID** | Workspace API ID | [optional] 
**folder_id** | **UUID** | Folder API ID | [optional] 
**user** | **str** | User | [optional] 
**domain** | **str** | Domain | [optional] 
**code** | **str** | Short code | [optional] 
**label** | **str** | Label | [optional] 
**password** | **str** | Password: \&quot;**********\&quot; means a password exists; null means no password. | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Modification date | [optional] 
**delete_at** | **datetime** | Scheduled deletion date | [optional] 
**expired_at** | **datetime** | Scheduled expiration date | [optional] 
**expired_url** | **str** | The URL to which users will be redirected after the link has expired | [optional] 
**expired_title** | **str** | The title displayed on the expiration page | [optional] 
**expired_text** | **str** | The text displayed on the expiration page | [optional] 
**delete_after_expiration** | **bool** | Whether the link should be deleted once it has expired | [optional] [default to False]
**tags** | [**List[LinkTagsInner]**](LinkTagsInner.md) | Tags | [optional] 
**qrcode** | [**LinkQrcode**](LinkQrcode.md) |  | [optional] 
**utm** | [**LinkUtm**](LinkUtm.md) |  | [optional] 
**metatag** | [**LinkMetatag**](LinkMetatag.md) |  | [optional] 
**geolinks** | [**List[LinkGeolinksInner]**](LinkGeolinksInner.md) | Dynamic routing conditions | [optional] 

## Example

```python
from urlr.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print(Link.to_json())

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_from_dict = Link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


