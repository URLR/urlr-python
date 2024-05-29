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

from urlr.models.get_statistics200_response import GetStatistics200Response

class TestGetStatistics200Response(unittest.TestCase):
    """GetStatistics200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStatistics200Response:
        """Test GetStatistics200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStatistics200Response`
        """
        model = GetStatistics200Response()
        if include_optional:
            return GetStatistics200Response(
                link_id = '',
                clicks = 32,
                unique_clicks = 51
            )
        else:
            return GetStatistics200Response(
        )
        """

    def testGetStatistics200Response(self):
        """Test GetStatistics200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
