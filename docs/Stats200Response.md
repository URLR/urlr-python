# Stats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clicks** | **int** |  | [optional] 
**unique_clicks** | **int** |  | [optional] 

## Example

```python
from urlr.models.stats200_response import Stats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Stats200Response from a JSON string
stats200_response_instance = Stats200Response.from_json(json)
# print the JSON string representation of the object
print Stats200Response.to_json()

# convert the object into a dict
stats200_response_dict = stats200_response_instance.to_dict()
# create an instance of Stats200Response from a dict
stats200_response_form_dict = stats200_response.from_dict(stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


