# QrcodeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The size of the QR code (px) | [optional] [default to 600]
**format** | **str** | The format of the QR code | [optional] [default to 'png']
**margin** | **int** | The margin around the QR code (px) | [optional] [default to 0]
**background_color** | **str** | The background color of the QR code (hexadecimal) | [optional] [default to '#ffffff']
**foreground_color** | **str** | The foreground color of the QR code (hexadecimal) | [optional] [default to '#000000']
**url** | **str** | URL of the QR Code | 
**workspace_id** | **UUID** | Workspace API ID | 
**link_id** | **UUID** | Link API ID of the QR Code | 

## Example

```python
from urlr.models.qrcode_create_request import QrcodeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QrcodeCreateRequest from a JSON string
qrcode_create_request_instance = QrcodeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QrcodeCreateRequest.to_json())

# convert the object into a dict
qrcode_create_request_dict = qrcode_create_request_instance.to_dict()
# create an instance of QrcodeCreateRequest from a dict
qrcode_create_request_from_dict = QrcodeCreateRequest.from_dict(qrcode_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


