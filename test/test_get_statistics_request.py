# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.3
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.get_statistics_request import GetStatisticsRequest

class TestGetStatisticsRequest(unittest.TestCase):
    """GetStatisticsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStatisticsRequest:
        """Test GetStatisticsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStatisticsRequest`
        """
        model = GetStatisticsRequest()
        if include_optional:
            return GetStatisticsRequest(
                link_id = '',
                var_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                include_bots = True
            )
        else:
            return GetStatisticsRequest(
                link_id = '',
        )
        """

    def testGetStatisticsRequest(self):
        """Test GetStatisticsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
