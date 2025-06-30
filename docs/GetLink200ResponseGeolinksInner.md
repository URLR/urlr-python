# GetLink200ResponseGeolinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[GetLink200ResponseGeolinksInnerConditionsInner]**](GetLink200ResponseGeolinksInnerConditionsInner.md) | Conditions for dynamic routing | [optional] 
**url** | **str** | URL to redirect to when conditions match | [optional] 

## Example

```python
from urlr.models.get_link200_response_geolinks_inner import GetLink200ResponseGeolinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink200ResponseGeolinksInner from a JSON string
get_link200_response_geolinks_inner_instance = GetLink200ResponseGeolinksInner.from_json(json)
# print the JSON string representation of the object
print(GetLink200ResponseGeolinksInner.to_json())

# convert the object into a dict
get_link200_response_geolinks_inner_dict = get_link200_response_geolinks_inner_instance.to_dict()
# create an instance of GetLink200ResponseGeolinksInner from a dict
get_link200_response_geolinks_inner_from_dict = GetLink200ResponseGeolinksInner.from_dict(get_link200_response_geolinks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


