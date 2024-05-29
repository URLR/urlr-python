# GetTeams200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[GetTeams200ResponseTeamsInner]**](GetTeams200ResponseTeamsInner.md) |  | [optional] 

## Example

```python
from urlr.models.get_teams200_response import GetTeams200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeams200Response from a JSON string
get_teams200_response_instance = GetTeams200Response.from_json(json)
# print the JSON string representation of the object
print(GetTeams200Response.to_json())

# convert the object into a dict
get_teams200_response_dict = get_teams200_response_instance.to_dict()
# create an instance of GetTeams200Response from a dict
get_teams200_response_from_dict = GetTeams200Response.from_dict(get_teams200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


