# LinkTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from urlr.models.link_tags_inner import LinkTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTagsInner from a JSON string
link_tags_inner_instance = LinkTagsInner.from_json(json)
# print the JSON string representation of the object
print(LinkTagsInner.to_json())

# convert the object into a dict
link_tags_inner_dict = link_tags_inner_instance.to_dict()
# create an instance of LinkTagsInner from a dict
link_tags_inner_from_dict = LinkTagsInner.from_dict(link_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


