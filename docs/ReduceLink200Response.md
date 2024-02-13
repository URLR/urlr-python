# ReduceLink200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Original URL | [optional] 
**expired_at** | **str** | Expiration date | [optional] 
**team** | **int** | Team ID (displayed on dashboard) | [optional] 
**folder** | **int** | Folder ID (displayed on dashboard) | [optional] 
**url_code** | **str** | Short code | [optional] 
**domain** | **str** | Domain | [optional] 
**code** | **int** | HTTP status code | [optional] 

## Example

```python
from urlr.models.reduce_link200_response import ReduceLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReduceLink200Response from a JSON string
reduce_link200_response_instance = ReduceLink200Response.from_json(json)
# print the JSON string representation of the object
print ReduceLink200Response.to_json()

# convert the object into a dict
reduce_link200_response_dict = reduce_link200_response_instance.to_dict()
# create an instance of ReduceLink200Response from a dict
reduce_link200_response_form_dict = reduce_link200_response.from_dict(reduce_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


