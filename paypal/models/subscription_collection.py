from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .subscription import Subscription, SubscriptionDict


class SubscriptionCollection(SdkBaseModel):
    """The list of subscriptions."""

    subscriptions: Optional[list[Subscription]] = UNSET
    """An array of subscriptions."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class SubscriptionCollectionDict(TypedDict):
    subscriptions: NotRequired[list[Subscription | SubscriptionDict]]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
