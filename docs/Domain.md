# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Domain API ID | [optional] 
**domain** | **str** | Domain | [optional] 
**root_url** | **str** | Redirect URL for the root of the domain | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Modification date | [optional] 

## Example

```python
from urlr.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


