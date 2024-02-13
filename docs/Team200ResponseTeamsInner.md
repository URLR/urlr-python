# Team200ResponseTeamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Team ID | [optional] 
**name** | **str** | Team name | [optional] 

## Example

```python
from urlr.models.team200_response_teams_inner import Team200ResponseTeamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Team200ResponseTeamsInner from a JSON string
team200_response_teams_inner_instance = Team200ResponseTeamsInner.from_json(json)
# print the JSON string representation of the object
print Team200ResponseTeamsInner.to_json()

# convert the object into a dict
team200_response_teams_inner_dict = team200_response_teams_inner_instance.to_dict()
# create an instance of Team200ResponseTeamsInner from a dict
team200_response_teams_inner_form_dict = team200_response_teams_inner.from_dict(team200_response_teams_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


