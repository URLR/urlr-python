# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.7
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from urlr.models.get_link200_response_geolinks_inner import GetLink200ResponseGeolinksInner
from urlr.models.get_link200_response_metatag import GetLink200ResponseMetatag
from urlr.models.get_link200_response_qrcode import GetLink200ResponseQrcode
from urlr.models.get_link200_response_tags_inner import GetLink200ResponseTagsInner
from urlr.models.get_link200_response_utm import GetLink200ResponseUtm
from typing import Optional, Set
from typing_extensions import Self

class GetLink200Response(BaseModel):
    """
    GetLink200Response
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Link API ID")
    url: Optional[StrictStr] = Field(default=None, description="Original URL")
    team_id: Optional[StrictStr] = Field(default=None, description="Team API ID")
    folder_id: Optional[StrictStr] = Field(default=None, description="Folder API ID")
    domain: Optional[StrictStr] = Field(default=None, description="Domain")
    code: Optional[StrictStr] = Field(default=None, description="Short code")
    label: Optional[StrictStr] = Field(default=None, description="Label")
    tags: Optional[Annotated[List[GetLink200ResponseTagsInner], Field(max_length=3)]] = Field(default=None, description="Tags")
    qrcode: Optional[GetLink200ResponseQrcode] = None
    utm: Optional[GetLink200ResponseUtm] = None
    metatag: Optional[GetLink200ResponseMetatag] = None
    geolinks: Optional[List[GetLink200ResponseGeolinksInner]] = Field(default=None, description="Geographical targeting links")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Modification date")
    delete_at: Optional[datetime] = Field(default=None, description="Scheduled deletion date")
    expired_at: Optional[datetime] = Field(default=None, description="Scheduled expiration date")
    expired_url: Optional[StrictStr] = Field(default=None, description="Expiration URL")
    delete_after_expiration: Optional[StrictBool] = Field(default=False, description="Whether or not to remove the link after the expiry date")
    __properties: ClassVar[List[str]] = ["id", "url", "team_id", "folder_id", "domain", "code", "label", "tags", "qrcode", "utm", "metatag", "geolinks", "created_at", "updated_at", "delete_at", "expired_at", "expired_url", "delete_after_expiration"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetLink200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of qrcode
        if self.qrcode:
            _dict['qrcode'] = self.qrcode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm
        if self.utm:
            _dict['utm'] = self.utm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metatag
        if self.metatag:
            _dict['metatag'] = self.metatag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in geolinks (list)
        _items = []
        if self.geolinks:
            for _item_geolinks in self.geolinks:
                if _item_geolinks:
                    _items.append(_item_geolinks.to_dict())
            _dict['geolinks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLink200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "team_id": obj.get("team_id"),
            "folder_id": obj.get("folder_id"),
            "domain": obj.get("domain"),
            "code": obj.get("code"),
            "label": obj.get("label"),
            "tags": [GetLink200ResponseTagsInner.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "qrcode": GetLink200ResponseQrcode.from_dict(obj["qrcode"]) if obj.get("qrcode") is not None else None,
            "utm": GetLink200ResponseUtm.from_dict(obj["utm"]) if obj.get("utm") is not None else None,
            "metatag": GetLink200ResponseMetatag.from_dict(obj["metatag"]) if obj.get("metatag") is not None else None,
            "geolinks": [GetLink200ResponseGeolinksInner.from_dict(_item) for _item in obj["geolinks"]] if obj.get("geolinks") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "delete_at": obj.get("delete_at"),
            "expired_at": obj.get("expired_at"),
            "expired_url": obj.get("expired_url"),
            "delete_after_expiration": obj.get("delete_after_expiration") if obj.get("delete_after_expiration") is not None else False
        })
        return _obj


