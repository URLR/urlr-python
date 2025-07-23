# CreateQrCodeRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the QR Code | 
**team_id** | **str** | Workspace API ID | 

## Example

```python
from urlr.models.create_qr_code_request_one_of import CreateQrCodeRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQrCodeRequestOneOf from a JSON string
create_qr_code_request_one_of_instance = CreateQrCodeRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(CreateQrCodeRequestOneOf.to_json())

# convert the object into a dict
create_qr_code_request_one_of_dict = create_qr_code_request_one_of_instance.to_dict()
# create an instance of CreateQrCodeRequestOneOf from a dict
create_qr_code_request_one_of_from_dict = CreateQrCodeRequestOneOf.from_dict(create_qr_code_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


