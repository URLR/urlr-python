# coding: utf-8

"""
    Developer API - URLR

    API powering the features of URLR.

    The version of the OpenAPI document: 0.3
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.stats_request import StatsRequest

class TestStatsRequest(unittest.TestCase):
    """StatsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatsRequest:
        """Test StatsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatsRequest`
        """
        model = StatsRequest()
        if include_optional:
            return StatsRequest(
                code = 'zA9LCSLv1C1ylmgd0-Y2TA5',
                var_from = 'dd/mm/yyyy',
                to = 'dd/mm/yyyy',
                include_bots = True
            )
        else:
            return StatsRequest(
                code = 'zA9LCSLv1C1ylmgd0-Y2TA5',
        )
        """

    def testStatsRequest(self):
        """Test StatsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
