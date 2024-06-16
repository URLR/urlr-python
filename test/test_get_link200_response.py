# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.2
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urlr.models.get_link200_response import GetLink200Response

class TestGetLink200Response(unittest.TestCase):
    """GetLink200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLink200Response:
        """Test GetLink200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLink200Response`
        """
        model = GetLink200Response()
        if include_optional:
            return GetLink200Response(
                id = '436b5d20-e174-4363-94e5-2b3dd4e74b5f',
                url = '',
                team = '',
                folder_id = '',
                domain = 'urlr.me',
                code = 'xxxxx',
                label = '',
                qrcode = urlr.models.get_link_200_response_qrcode.getLink_200_response_qrcode(
                    data = '', ),
                metatag = urlr.models.get_link_200_response_metatag.getLink_200_response_metatag(
                    title = '', 
                    description = '', 
                    image = '', ),
                geolinks = [
                    urlr.models.get_link_200_response_geolinks_inner.getLink_200_response_geolinks_inner(
                        type = '', 
                        value = '', 
                        url = '', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expired_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetLink200Response(
        )
        """

    def testGetLink200Response(self):
        """Test GetLink200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
