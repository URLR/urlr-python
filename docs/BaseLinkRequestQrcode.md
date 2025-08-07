# BaseLinkRequestQrcode

QR Code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The size of the QR code (px) | [optional] [default to 600]
**format** | **str** | The format of the QR code | [optional] [default to 'png']
**margin** | **int** | The margin around the QR code (px) | [optional] [default to 0]
**background_color** | **str** | The background color of the QR code (hexadecimal) | [optional] [default to '#ffffff']
**foreground_color** | **str** | The foreground color of the QR code (hexadecimal) | [optional] [default to '#000000']

## Example

```python
from urlr.models.base_link_request_qrcode import BaseLinkRequestQrcode

# TODO update the JSON string below
json = "{}"
# create an instance of BaseLinkRequestQrcode from a JSON string
base_link_request_qrcode_instance = BaseLinkRequestQrcode.from_json(json)
# print the JSON string representation of the object
print(BaseLinkRequestQrcode.to_json())

# convert the object into a dict
base_link_request_qrcode_dict = base_link_request_qrcode_instance.to_dict()
# create an instance of BaseLinkRequestQrcode from a dict
base_link_request_qrcode_from_dict = BaseLinkRequestQrcode.from_dict(base_link_request_qrcode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


