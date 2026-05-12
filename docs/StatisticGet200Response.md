# StatisticGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **UUID** | Link API ID | [optional] 
**visits** | **int** | Total number of visits, combining clicks and scans | [optional] 
**unique_visits** | **int** | Number of unique visitors, combining clicks and scans | [optional] 
**clicks** | **int** | Number of clicks | [optional] 
**scans** | **int** | Number of scans | [optional] 

## Example

```python
from urlr.models.statistic_get200_response import StatisticGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticGet200Response from a JSON string
statistic_get200_response_instance = StatisticGet200Response.from_json(json)
# print the JSON string representation of the object
print(StatisticGet200Response.to_json())

# convert the object into a dict
statistic_get200_response_dict = statistic_get200_response_instance.to_dict()
# create an instance of StatisticGet200Response from a dict
statistic_get200_response_from_dict = StatisticGet200Response.from_dict(statistic_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


