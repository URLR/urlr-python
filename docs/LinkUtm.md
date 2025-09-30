# LinkUtm

UTM parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | **str** | utm_campaign | [optional] 
**medium** | **str** | utm_medium | [optional] 
**source** | **str** | utm_source | [optional] 
**content** | **str** | utm_content | [optional] 

## Example

```python
from urlr.models.link_utm import LinkUtm

# TODO update the JSON string below
json = "{}"
# create an instance of LinkUtm from a JSON string
link_utm_instance = LinkUtm.from_json(json)
# print the JSON string representation of the object
print(LinkUtm.to_json())

# convert the object into a dict
link_utm_dict = link_utm_instance.to_dict()
# create an instance of LinkUtm from a dict
link_utm_from_dict = LinkUtm.from_dict(link_utm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


