# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.7
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.api.access_tokens_api import AccessTokensApi


class TestAccessTokensApi(unittest.TestCase):
    """AccessTokensApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccessTokensApi()

    def tearDown(self) -> None:
        pass

    def test_create_access_token(self) -> None:
        """Test case for create_access_token

        Get an access token
        """
        pass

    def test_refresh_access_token(self) -> None:
        """Test case for refresh_access_token

        Refresh an access token
        """
        pass


if __name__ == '__main__':
    unittest.main()
