# ListLinks200Response


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
from urlr.models.list_links200_response import ListLinks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListLinks200Response from a JSON string
list_links200_response_instance = ListLinks200Response.from_json(json)
# print the JSON string representation of the object
print(ListLinks200Response.to_json())

# convert the object into a dict
list_links200_response_dict = list_links200_response_instance.to_dict()
# create an instance of ListLinks200Response from a dict
list_links200_response_from_dict = ListLinks200Response.from_dict(list_links200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


