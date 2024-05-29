# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.0
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.create_link201_response import CreateLink201Response

class TestCreateLink201Response(unittest.TestCase):
    """CreateLink201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateLink201Response:
        """Test CreateLink201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateLink201Response`
        """
        model = CreateLink201Response()
        if include_optional:
            return CreateLink201Response(
                id = '',
                url = '',
                team = '',
                folder_id = '',
                domain_id = 'urlr.me',
                code = 'xxxxx',
                label = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expired_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CreateLink201Response(
        )
        """

    def testCreateLink201Response(self):
        """Test CreateLink201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
