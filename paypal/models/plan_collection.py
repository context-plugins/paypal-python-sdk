from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_plan import BillingPlan, BillingPlanDict
from .link_description import LinkDescription, LinkDescriptionDict


class PlanCollection(SdkBaseModel):
    """The list of plans with details."""

    plans: Optional[list[BillingPlan]] = UNSET
    """An array of plans."""

    total_items: Optional[int] = UNSET
    """The total number of items."""

    total_pages: Optional[int] = UNSET
    """The total number of pages."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class PlanCollectionDict(TypedDict):
    plans: NotRequired[list[BillingPlan | BillingPlanDict]]
    total_items: NotRequired[int]
    total_pages: NotRequired[int]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
