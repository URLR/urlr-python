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

from urlr.models.team200_response_teams_inner import Team200ResponseTeamsInner

class TestTeam200ResponseTeamsInner(unittest.TestCase):
    """Team200ResponseTeamsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Team200ResponseTeamsInner:
        """Test Team200ResponseTeamsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Team200ResponseTeamsInner`
        """
        model = Team200ResponseTeamsInner()
        if include_optional:
            return Team200ResponseTeamsInner(
                id = 131,
                name = 'the best team'
            )
        else:
            return Team200ResponseTeamsInner(
        )
        """

    def testTeam200ResponseTeamsInner(self):
        """Test Team200ResponseTeamsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
