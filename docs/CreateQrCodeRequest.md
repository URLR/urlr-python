# CreateQrCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The size of the QR code (px) | [optional] [default to 600]
**format** | **str** | The format of the QR code | [optional] [default to 'png']
**margin** | **int** | The margin around the QR code (px) | [optional] [default to 0]
**background_color** | **str** | The background color of the QR code (hexadecimal) | [optional] [default to '#ffffff']
**foreground_color** | **str** | The foreground color of the QR code (hexadecimal) | [optional] [default to '#000000']
**url** | **str** | URL of the QR Code | 
**team_id** | **str** | Workspace API ID | 
**link_id** | **str** | Link API ID of the QR Code | 

## Example

```python
from urlr.models.create_qr_code_request import CreateQrCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQrCodeRequest from a JSON string
create_qr_code_request_instance = CreateQrCodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQrCodeRequest.to_json())

# convert the object into a dict
create_qr_code_request_dict = create_qr_code_request_instance.to_dict()
# create an instance of CreateQrCodeRequest from a dict
create_qr_code_request_from_dict = CreateQrCodeRequest.from_dict(create_qr_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


