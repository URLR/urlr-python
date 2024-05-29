# GetStatistics200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **str** | Link API ID | [optional] 
**clicks** | **int** | Clicks | [optional] 
**unique_clicks** | **int** | Unique clicks | [optional] 

## Example

```python
from urlr.models.get_statistics200_response import GetStatistics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatistics200Response from a JSON string
get_statistics200_response_instance = GetStatistics200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatistics200Response.to_json())

# convert the object into a dict
get_statistics200_response_dict = get_statistics200_response_instance.to_dict()
# create an instance of GetStatistics200Response from a dict
get_statistics200_response_from_dict = GetStatistics200Response.from_dict(get_statistics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


