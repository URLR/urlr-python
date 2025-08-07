# BaseLinkRequestMetatag

Custom metadata for social previews

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title for the link | [optional] 
**description** | **str** | Description for the link | [optional] 
**image** | **str** | Image URL for the link. Recommended: 1200X630px&lt;br&gt;Maximum size: 3Mb - Formats: PNG, JPEG, WebP and GIF. | [optional] 

## Example

```python
from urlr.models.base_link_request_metatag import BaseLinkRequestMetatag

# TODO update the JSON string below
json = "{}"
# create an instance of BaseLinkRequestMetatag from a JSON string
base_link_request_metatag_instance = BaseLinkRequestMetatag.from_json(json)
# print the JSON string representation of the object
print(BaseLinkRequestMetatag.to_json())

# convert the object into a dict
base_link_request_metatag_dict = base_link_request_metatag_instance.to_dict()
# create an instance of BaseLinkRequestMetatag from a dict
base_link_request_metatag_from_dict = BaseLinkRequestMetatag.from_dict(base_link_request_metatag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


