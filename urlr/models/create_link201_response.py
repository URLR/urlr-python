# coding: utf-8

"""
    URLR API Reference

    API powering the features of URLR.<br><br>Note that in order to facilitate integration, we provide SDKs for various languages at https://github.com/URLR.<br><br>Key API principles:<br>         <ul><li>All dates follow **ISO-8601** format</li><li>Most errors follow **RFC 9457** standard</li><li>All responses are delivered in English</li></ul>

    The version of the OpenAPI document: 1.0
    Contact: contact@urlr.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateLink201Response(BaseModel):
    """
    CreateLink201Response
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Link API ID")
    url: Optional[StrictStr] = Field(default=None, description="Original URL")
    team: Optional[StrictStr] = Field(default=None, description="Team API ID")
    folder_id: Optional[StrictStr] = Field(default=None, description="Folder API ID")
    domain_id: Optional[StrictStr] = Field(default=None, description="Domain")
    code: Optional[StrictStr] = Field(default=None, description="Short code")
    label: Optional[StrictStr] = Field(default=None, description="Label")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Modification date")
    expired_at: Optional[datetime] = Field(default=None, description="Expiration date")
    __properties: ClassVar[List[str]] = ["id", "url", "team", "folder_id", "domain_id", "code", "label", "created_at", "updated_at", "expired_at"]

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
        """Create an instance of CreateLink201Response from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateLink201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "team": obj.get("team"),
            "folder_id": obj.get("folder_id"),
            "domain_id": obj.get("domain_id"),
            "code": obj.get("code"),
            "label": obj.get("label"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "expired_at": obj.get("expired_at")
        })
        return _obj

