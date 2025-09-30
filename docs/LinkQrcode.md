# LinkQrcode

QR Code associated to the short link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | QR Code Data URL | [optional] 

## Example

```python
from urlr.models.link_qrcode import LinkQrcode

# TODO update the JSON string below
json = "{}"
# create an instance of LinkQrcode from a JSON string
link_qrcode_instance = LinkQrcode.from_json(json)
# print the JSON string representation of the object
print(LinkQrcode.to_json())

# convert the object into a dict
link_qrcode_dict = link_qrcode_instance.to_dict()
# create an instance of LinkQrcode from a dict
link_qrcode_from_dict = LinkQrcode.from_dict(link_qrcode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


