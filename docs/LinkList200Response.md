# LinkList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) | List of links | [optional] 
**total** | **int** | Total number of links | [optional] 
**limit** | **int** | Number of items per page | [optional] 
**pages** | **int** | Total number of pages | [optional] 
**page** | **int** | Current page number | [optional] 

## Example

```python
from urlr.models.link_list200_response import LinkList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LinkList200Response from a JSON string
link_list200_response_instance = LinkList200Response.from_json(json)
# print the JSON string representation of the object
print(LinkList200Response.to_json())

# convert the object into a dict
link_list200_response_dict = link_list200_response_instance.to_dict()
# create an instance of LinkList200Response from a dict
link_list200_response_from_dict = LinkList200Response.from_dict(link_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


