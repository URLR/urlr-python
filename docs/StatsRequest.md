# StatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The short code of the URL | 
**var_from** | **str** | Get stats from this date | [optional] 
**to** | **str** | Get stats until this date | [optional] 
**include_bots** | **bool** | Whether include bots or not in statistics | [optional] 

## Example

```python
from urlr.models.stats_request import StatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StatsRequest from a JSON string
stats_request_instance = StatsRequest.from_json(json)
# print the JSON string representation of the object
print StatsRequest.to_json()

# convert the object into a dict
stats_request_dict = stats_request_instance.to_dict()
# create an instance of StatsRequest from a dict
stats_request_form_dict = stats_request.from_dict(stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


