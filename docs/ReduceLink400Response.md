# ReduceLink400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | HTTP status code | [optional] 
**error** | **int** |  | [optional] 
**message** | **str** | Message describing the error | [optional] 

## Example

```python
from urlr.models.reduce_link400_response import ReduceLink400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReduceLink400Response from a JSON string
reduce_link400_response_instance = ReduceLink400Response.from_json(json)
# print the JSON string representation of the object
print ReduceLink400Response.to_json()

# convert the object into a dict
reduce_link400_response_dict = reduce_link400_response_instance.to_dict()
# create an instance of ReduceLink400Response from a dict
reduce_link400_response_form_dict = reduce_link400_response.from_dict(reduce_link400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


