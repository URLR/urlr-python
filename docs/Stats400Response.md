# Stats400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**error** | **int** |  | [optional] 

## Example

```python
from urlr.models.stats400_response import Stats400Response

# TODO update the JSON string below
json = "{}"
# create an instance of Stats400Response from a JSON string
stats400_response_instance = Stats400Response.from_json(json)
# print the JSON string representation of the object
print Stats400Response.to_json()

# convert the object into a dict
stats400_response_dict = stats400_response_instance.to_dict()
# create an instance of Stats400Response from a dict
stats400_response_form_dict = stats400_response.from_dict(stats400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


