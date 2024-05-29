# GetStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **str** | Link API ID | [optional] 
**var_from** | **datetime** | Get statistics from this date | [optional] 
**to** | **datetime** | Get statistics until this date | [optional] 
**include_bots** | **bool** | Whether include bots or not in statistics | [optional] [default to False]

## Example

```python
from urlr.models.get_statistics_request import GetStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsRequest from a JSON string
get_statistics_request_instance = GetStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(GetStatisticsRequest.to_json())

# convert the object into a dict
get_statistics_request_dict = get_statistics_request_instance.to_dict()
# create an instance of GetStatisticsRequest from a dict
get_statistics_request_from_dict = GetStatisticsRequest.from_dict(get_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


