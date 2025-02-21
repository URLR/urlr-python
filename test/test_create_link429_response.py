# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.5
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.create_link429_response import CreateLink429Response

class TestCreateLink429Response(unittest.TestCase):
    """CreateLink429Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateLink429Response:
        """Test CreateLink429Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateLink429Response`
        """
        model = CreateLink429Response()
        if include_optional:
            return CreateLink429Response(
                type = '',
                title = '',
                status = 429,
                detail = ''
            )
        else:
            return CreateLink429Response(
        )
        """

    def testCreateLink429Response(self):
        """Test CreateLink429Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
