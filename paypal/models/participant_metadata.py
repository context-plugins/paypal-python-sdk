from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ParticipantMetadata(SdkBaseModel):
    """Profile information of the sender or receiver."""

    ip_address: Optional[str] = UNSET
    """An Internet Protocol address (IP address). This address assigns a numerical label to each device that is
    connected to a computer network through the Internet Protocol. Supports IPv4 and IPv6 addresses."""


class ParticipantMetadataDict(TypedDict):
    ip_address: NotRequired[str]
