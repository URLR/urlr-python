# GetLink200ResponseGeolinksInnerConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the condition  | [optional] 
**value** | **str** | Value for the given type. Allowed values depend on \&quot;type\&quot;: e.g., \&quot;US\&quot;, \&quot;DE\&quot;, \&quot;FR\&quot; for type \&quot;country\&quot;; \&quot;en\&quot;, \&quot;fr\&quot;, \&quot;de\&quot; for type \&quot;language\&quot;; \&quot;Android\&quot;, \&quot;iOS\&quot; for type \&quot;system\&quot;. | [optional] 
**operator** | **str** | Operator to apply for the condition | [optional] 

## Example

```python
from urlr.models.get_link200_response_geolinks_inner_conditions_inner import GetLink200ResponseGeolinksInnerConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink200ResponseGeolinksInnerConditionsInner from a JSON string
get_link200_response_geolinks_inner_conditions_inner_instance = GetLink200ResponseGeolinksInnerConditionsInner.from_json(json)
# print the JSON string representation of the object
print(GetLink200ResponseGeolinksInnerConditionsInner.to_json())

# convert the object into a dict
get_link200_response_geolinks_inner_conditions_inner_dict = get_link200_response_geolinks_inner_conditions_inner_instance.to_dict()
# create an instance of GetLink200ResponseGeolinksInnerConditionsInner from a dict
get_link200_response_geolinks_inner_conditions_inner_from_dict = GetLink200ResponseGeolinksInnerConditionsInner.from_dict(get_link200_response_geolinks_inner_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


