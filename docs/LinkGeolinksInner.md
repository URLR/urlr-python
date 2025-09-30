# LinkGeolinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[LinkGeolinksInnerConditionsInner]**](LinkGeolinksInnerConditionsInner.md) | Conditions for dynamic routing | [optional] 
**url** | **str** | URL to redirect to when conditions match | [optional] 

## Example

```python
from urlr.models.link_geolinks_inner import LinkGeolinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of LinkGeolinksInner from a JSON string
link_geolinks_inner_instance = LinkGeolinksInner.from_json(json)
# print the JSON string representation of the object
print(LinkGeolinksInner.to_json())

# convert the object into a dict
link_geolinks_inner_dict = link_geolinks_inner_instance.to_dict()
# create an instance of LinkGeolinksInner from a dict
link_geolinks_inner_from_dict = LinkGeolinksInner.from_dict(link_geolinks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


