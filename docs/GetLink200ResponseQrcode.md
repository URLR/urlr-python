# GetLink200ResponseQrcode

QR Code associated to the short link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | QR Code Data URL | [optional] 

## Example

```python
from urlr.models.get_link200_response_qrcode import GetLink200ResponseQrcode

# TODO update the JSON string below
json = "{}"
# create an instance of GetLink200ResponseQrcode from a JSON string
get_link200_response_qrcode_instance = GetLink200ResponseQrcode.from_json(json)
# print the JSON string representation of the object
print(GetLink200ResponseQrcode.to_json())

# convert the object into a dict
get_link200_response_qrcode_dict = get_link200_response_qrcode_instance.to_dict()
# create an instance of GetLink200ResponseQrcode from a dict
get_link200_response_qrcode_from_dict = GetLink200ResponseQrcode.from_dict(get_link200_response_qrcode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


