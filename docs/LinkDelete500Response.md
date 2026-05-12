# LinkDelete500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from urlr.models.link_delete500_response import LinkDelete500Response

# TODO update the JSON string below
json = "{}"
# create an instance of LinkDelete500Response from a JSON string
link_delete500_response_instance = LinkDelete500Response.from_json(json)
# print the JSON string representation of the object
print(LinkDelete500Response.to_json())

# convert the object into a dict
link_delete500_response_dict = link_delete500_response_instance.to_dict()
# create an instance of LinkDelete500Response from a dict
link_delete500_response_from_dict = LinkDelete500Response.from_dict(link_delete500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


