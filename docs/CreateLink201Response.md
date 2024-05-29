# CreateLink201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Link API ID | [optional] 
**url** | **str** | Original URL | [optional] 
**team** | **str** | Team API ID | [optional] 
**folder_id** | **str** | Folder API ID | [optional] 
**domain_id** | **str** | Domain | [optional] 
**code** | **str** | Short code | [optional] 
**label** | **str** | Label | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Modification date | [optional] 
**expired_at** | **datetime** | Expiration date | [optional] 

## Example

```python
from urlr.models.create_link201_response import CreateLink201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLink201Response from a JSON string
create_link201_response_instance = CreateLink201Response.from_json(json)
# print the JSON string representation of the object
print(CreateLink201Response.to_json())

# convert the object into a dict
create_link201_response_dict = create_link201_response_instance.to_dict()
# create an instance of CreateLink201Response from a dict
create_link201_response_from_dict = CreateLink201Response.from_dict(create_link201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


