from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkHttpMethod(str, Enum):
    """The HTTP method required to make the related call."""

    GET = "GET"
    """The HTTP GET method."""

    POST = "POST"
    """The HTTP POST method."""

    PUT = "PUT"
    """The HTTP PUT method."""

    DELETE = "DELETE"
    """The HTTP DELETE method."""

    HEAD = "HEAD"
    """The HTTP HEAD method."""

    CONNECT = "CONNECT"
    """The HTTP CONNECT method."""

    OPTIONS = "OPTIONS"
    """The HTTP OPTIONS method."""

    PATCH = "PATCH"
    """The HTTP PATCH method."""

    __str__ = str.__str__


LinkHttpMethodOrStr: TypeAlias = Annotated[LinkHttpMethod | str, open_enum_validator(LinkHttpMethod)]
