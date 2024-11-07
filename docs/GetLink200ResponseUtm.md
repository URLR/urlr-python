# GetLink200ResponseUtm

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
from urlr.models.get_link200_response_utm import GetLink200ResponseUtm

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink200ResponseUtm from a JSON string
get_link200_response_utm_instance = GetLink200ResponseUtm.from_json(json)
# print the JSON string representation of the object
print(GetLink200ResponseUtm.to_json())

# convert the object into a dict
get_link200_response_utm_dict = get_link200_response_utm_instance.to_dict()
# create an instance of GetLink200ResponseUtm from a dict
get_link200_response_utm_from_dict = GetLink200ResponseUtm.from_dict(get_link200_response_utm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


