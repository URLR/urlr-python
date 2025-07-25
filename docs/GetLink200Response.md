# GetLink200Response


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
**tags** | [**List[GetLink200ResponseTagsInner]**](GetLink200ResponseTagsInner.md) | Tags | [optional] 
**qrcode** | [**GetLink200ResponseQrcode**](GetLink200ResponseQrcode.md) |  | [optional] 
**utm** | [**GetLink200ResponseUtm**](GetLink200ResponseUtm.md) |  | [optional] 
**metatag** | [**GetLink200ResponseMetatag**](GetLink200ResponseMetatag.md) |  | [optional] 
**geolinks** | [**List[GetLink200ResponseGeolinksInner]**](GetLink200ResponseGeolinksInner.md) | Dynamic routing conditions | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Modification date | [optional] 
**delete_at** | **datetime** | Scheduled deletion date | [optional] 
**expired_at** | **datetime** | Scheduled expiration date | [optional] 
**expired_url** | **str** | Expiration URL | [optional] 
**delete_after_expiration** | **bool** | Whether or not to remove the link after the expiry date | [optional] [default to False]

## Example

```python
from urlr.models.get_link200_response import GetLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink200Response from a JSON string
get_link200_response_instance = GetLink200Response.from_json(json)
# print the JSON string representation of the object
print(GetLink200Response.to_json())

# convert the object into a dict
get_link200_response_dict = get_link200_response_instance.to_dict()
# create an instance of GetLink200Response from a dict
get_link200_response_from_dict = GetLink200Response.from_dict(get_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


