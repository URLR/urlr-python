# CreateLinkRequestQrcode

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
from urlr.models.create_link_request_qrcode import CreateLinkRequestQrcode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLinkRequestQrcode from a JSON string
create_link_request_qrcode_instance = CreateLinkRequestQrcode.from_json(json)
# print the JSON string representation of the object
print(CreateLinkRequestQrcode.to_json())

# convert the object into a dict
create_link_request_qrcode_dict = create_link_request_qrcode_instance.to_dict()
# create an instance of CreateLinkRequestQrcode from a dict
create_link_request_qrcode_from_dict = CreateLinkRequestQrcode.from_dict(create_link_request_qrcode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


