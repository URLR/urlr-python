# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.2
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.create_qr_code_request_one_of1 import CreateQrCodeRequestOneOf1

class TestCreateQrCodeRequestOneOf1(unittest.TestCase):
    """CreateQrCodeRequestOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateQrCodeRequestOneOf1:
        """Test CreateQrCodeRequestOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateQrCodeRequestOneOf1`
        """
        model = CreateQrCodeRequestOneOf1()
        if include_optional:
            return CreateQrCodeRequestOneOf1(
                link_id = ''
            )
        else:
            return CreateQrCodeRequestOneOf1(
                link_id = '',
        )
        """

    def testCreateQrCodeRequestOneOf1(self):
        """Test CreateQrCodeRequestOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
