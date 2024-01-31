# Authentification401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from urlr.models.authentification401_response import Authentification401Response

# TODO update the JSON string below
json = "{}"
# create an instance of Authentification401Response from a JSON string
authentification401_response_instance = Authentification401Response.from_json(json)
# print the JSON string representation of the object
print Authentification401Response.to_json()

# convert the object into a dict
authentification401_response_dict = authentification401_response_instance.to_dict()
# create an instance of Authentification401Response from a dict
authentification401_response_form_dict = authentification401_response.from_dict(authentification401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


