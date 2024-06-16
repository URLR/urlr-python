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

from urlr.models.create_access_token_request import CreateAccessTokenRequest

class TestCreateAccessTokenRequest(unittest.TestCase):
    """CreateAccessTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAccessTokenRequest:
        """Test CreateAccessTokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAccessTokenRequest`
        """
        model = CreateAccessTokenRequest()
        if include_optional:
            return CreateAccessTokenRequest(
                username = '',
                password = ''
            )
        else:
            return CreateAccessTokenRequest(
                username = '',
                password = '',
        )
        """

    def testCreateAccessTokenRequest(self):
        """Test CreateAccessTokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
