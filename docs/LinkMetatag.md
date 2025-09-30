# LinkMetatag

Custom metadata for social previews

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the link | [optional] 
**description** | **str** | Description of the link | [optional] 
**image** | **str** | Image URL of the link | [optional] 

## Example

```python
from urlr.models.link_metatag import LinkMetatag

# TODO update the JSON string below
json = "{}"
# create an instance of LinkMetatag from a JSON string
link_metatag_instance = LinkMetatag.from_json(json)
# print the JSON string representation of the object
print(LinkMetatag.to_json())

# convert the object into a dict
link_metatag_dict = link_metatag_instance.to_dict()
# create an instance of LinkMetatag from a dict
link_metatag_from_dict = LinkMetatag.from_dict(link_metatag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


