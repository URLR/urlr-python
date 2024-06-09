# GetLink200ResponseMetatag

Custom metadata for social previews

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the link | [optional] 
**description** | **str** | Description of the link | [optional] 
**image** | **str** | Image URL of the link | [optional] 

## Example

```python
from urlr.models.get_link200_response_metatag import GetLink200ResponseMetatag

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink200ResponseMetatag from a JSON string
get_link200_response_metatag_instance = GetLink200ResponseMetatag.from_json(json)
# print the JSON string representation of the object
print(GetLink200ResponseMetatag.to_json())

# convert the object into a dict
get_link200_response_metatag_dict = get_link200_response_metatag_instance.to_dict()
# create an instance of GetLink200ResponseMetatag from a dict
get_link200_response_metatag_from_dict = GetLink200ResponseMetatag.from_dict(get_link200_response_metatag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


