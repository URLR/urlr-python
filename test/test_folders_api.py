# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.4
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.api.folders_api import FoldersApi


class TestFoldersApi(unittest.TestCase):
    """FoldersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FoldersApi()

    def tearDown(self) -> None:
        pass

    def test_get_folders(self) -> None:
        """Test case for get_folders

        Get folders of team
        """
        pass


if __name__ == '__main__':
    unittest.main()
