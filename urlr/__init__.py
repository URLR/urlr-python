# coding: utf-8

# flake8: noqa

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.7
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "2.8.0"

# import apis into sdk package
from urlr.api.access_tokens_api import AccessTokensApi
from urlr.api.folders_api import FoldersApi
from urlr.api.links_api import LinksApi
from urlr.api.qr_codes_api import QRCodesApi
from urlr.api.statistics_api import StatisticsApi
from urlr.api.teams_api import TeamsApi

# import ApiClient
from urlr.api_response import ApiResponse
from urlr.api_client import ApiClient
from urlr.configuration import Configuration
from urlr.exceptions import OpenApiException
from urlr.exceptions import ApiTypeError
from urlr.exceptions import ApiValueError
from urlr.exceptions import ApiKeyError
from urlr.exceptions import ApiAttributeError
from urlr.exceptions import ApiException

# import models into sdk package
from urlr.models.create_access_token200_response import CreateAccessToken200Response
from urlr.models.create_access_token401_response import CreateAccessToken401Response
from urlr.models.create_access_token_request import CreateAccessTokenRequest
from urlr.models.create_link429_response import CreateLink429Response
from urlr.models.create_link500_response import CreateLink500Response
from urlr.models.create_link_request import CreateLinkRequest
from urlr.models.create_link_request_metatag import CreateLinkRequestMetatag
from urlr.models.create_link_request_qrcode import CreateLinkRequestQrcode
from urlr.models.create_qr_code_request import CreateQrCodeRequest
from urlr.models.create_qr_code_request_one_of import CreateQrCodeRequestOneOf
from urlr.models.create_qr_code_request_one_of1 import CreateQrCodeRequestOneOf1
from urlr.models.get_folders200_response import GetFolders200Response
from urlr.models.get_folders200_response_folders_inner import GetFolders200ResponseFoldersInner
from urlr.models.get_link200_response import GetLink200Response
from urlr.models.get_link200_response_geolinks_inner import GetLink200ResponseGeolinksInner
from urlr.models.get_link200_response_metatag import GetLink200ResponseMetatag
from urlr.models.get_link200_response_qrcode import GetLink200ResponseQrcode
from urlr.models.get_link200_response_tags_inner import GetLink200ResponseTagsInner
from urlr.models.get_link200_response_utm import GetLink200ResponseUtm
from urlr.models.get_link401_response import GetLink401Response
from urlr.models.get_link404_response import GetLink404Response
from urlr.models.get_link422_response import GetLink422Response
from urlr.models.get_statistics200_response import GetStatistics200Response
from urlr.models.get_statistics_request import GetStatisticsRequest
from urlr.models.get_teams200_response import GetTeams200Response
from urlr.models.get_teams200_response_teams_inner import GetTeams200ResponseTeamsInner
from urlr.models.refresh_access_token401_response import RefreshAccessToken401Response
from urlr.models.refresh_access_token_request import RefreshAccessTokenRequest
