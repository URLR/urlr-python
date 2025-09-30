# Link


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Link API ID | [optional] 
**url** | **str** | Original URL | [optional] 
**team_id** | **str** | Workspace API ID | [optional] 
**folder_id** | **str** | Folder API ID | [optional] 
**domain** | **str** | Domain | [optional] 
**code** | **str** | Short code | [optional] 
**label** | **str** | Label | [optional] 
**tags** | [**List[LinkTagsInner]**](LinkTagsInner.md) | Tags | [optional] 
**password** | **str** | Password: \&quot;**********\&quot; means a password exists; null means no password. | [optional] 
**qrcode** | [**LinkQrcode**](LinkQrcode.md) |  | [optional] 
**utm** | [**LinkUtm**](LinkUtm.md) |  | [optional] 
**metatag** | [**LinkMetatag**](LinkMetatag.md) |  | [optional] 
**geolinks** | [**List[LinkGeolinksInner]**](LinkGeolinksInner.md) | Dynamic routing conditions | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Modification date | [optional] 
**delete_at** | **datetime** | Scheduled deletion date | [optional] 
**expired_at** | **datetime** | Scheduled expiration date | [optional] 
**expired_url** | **str** | Expiration URL | [optional] 
**delete_after_expiration** | **bool** | Whether or not to remove the link after the expiry date | [optional] [default to False]

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


