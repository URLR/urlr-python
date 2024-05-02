# AuthentificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Email | [optional] 
**password** | **str** | Password | [optional] 

## Example

```python
from urlr.models.authentification_request import AuthentificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthentificationRequest from a JSON string
authentification_request_instance = AuthentificationRequest.from_json(json)
# print the JSON string representation of the object
print(AuthentificationRequest.to_json())

# convert the object into a dict
authentification_request_dict = authentification_request_instance.to_dict()
# create an instance of AuthentificationRequest from a dict
authentification_request_from_dict = AuthentificationRequest.from_dict(authentification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


