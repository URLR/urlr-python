# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.1
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.create_access_token200_response import CreateAccessToken200Response

class TestCreateAccessToken200Response(unittest.TestCase):
    """CreateAccessToken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAccessToken200Response:
        """Test CreateAccessToken200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAccessToken200Response`
        """
        model = CreateAccessToken200Response()
        if include_optional:
            return CreateAccessToken200Response(
                token = '',
                refresh_token = ''
            )
        else:
            return CreateAccessToken200Response(
        )
        """

    def testCreateAccessToken200Response(self):
        """Test CreateAccessToken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
