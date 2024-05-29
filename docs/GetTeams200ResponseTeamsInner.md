# GetTeams200ResponseTeamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Team API ID | [optional] 
**name** | **str** | Team name | [optional] 

## Example

```python
from urlr.models.get_teams200_response_teams_inner import GetTeams200ResponseTeamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeams200ResponseTeamsInner from a JSON string
get_teams200_response_teams_inner_instance = GetTeams200ResponseTeamsInner.from_json(json)
# print the JSON string representation of the object
print(GetTeams200ResponseTeamsInner.to_json())

# convert the object into a dict
get_teams200_response_teams_inner_dict = get_teams200_response_teams_inner_instance.to_dict()
# create an instance of GetTeams200ResponseTeamsInner from a dict
get_teams200_response_teams_inner_from_dict = GetTeams200ResponseTeamsInner.from_dict(get_teams200_response_teams_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


