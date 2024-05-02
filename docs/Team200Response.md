# Team200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[Team200ResponseTeamsInner]**](Team200ResponseTeamsInner.md) |  | [optional] 

## Example

```python
from urlr.models.team200_response import Team200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Team200Response from a JSON string
team200_response_instance = Team200Response.from_json(json)
# print the JSON string representation of the object
print(Team200Response.to_json())

# convert the object into a dict
team200_response_dict = team200_response_instance.to_dict()
# create an instance of Team200Response from a dict
team200_response_from_dict = Team200Response.from_dict(team200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


