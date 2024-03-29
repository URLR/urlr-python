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

from urlr.api.stats_api import StatsApi


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatsApi()

    def tearDown(self) -> None:
        pass

    def test_stats(self) -> None:
        """Test case for stats

        Get statistics of a link
        """
        pass


if __name__ == '__main__':
    unittest.main()
