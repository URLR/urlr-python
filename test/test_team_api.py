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

from urlr.api.team_api import TeamApi


class TestTeamApi(unittest.TestCase):
    """TeamApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TeamApi()

    def tearDown(self) -> None:
        pass

    def test_team(self) -> None:
        """Test case for team

        Get teams of user
        """
        pass


if __name__ == '__main__':
    unittest.main()
