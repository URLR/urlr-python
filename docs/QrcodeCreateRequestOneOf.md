# QrcodeCreateRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the QR Code | 

## Example

```python
from urlr.models.qrcode_create_request_one_of import QrcodeCreateRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of QrcodeCreateRequestOneOf from a JSON string
qrcode_create_request_one_of_instance = QrcodeCreateRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(QrcodeCreateRequestOneOf.to_json())

# convert the object into a dict
qrcode_create_request_one_of_dict = qrcode_create_request_one_of_instance.to_dict()
# create an instance of QrcodeCreateRequestOneOf from a dict
qrcode_create_request_one_of_from_dict = QrcodeCreateRequestOneOf.from_dict(qrcode_create_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


