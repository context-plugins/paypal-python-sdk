from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.order_application_context_landing_page import OrderApplicationContextLandingPageOrStr
from .enums.order_application_context_shipping_preference import OrderApplicationContextShippingPreferenceOrStr
from .enums.order_application_context_user_action import OrderApplicationContextUserActionOrStr
from .payment_method_preference import PaymentMethodPreference, PaymentMethodPreferenceDict
from .stored_payment_source import StoredPaymentSource, StoredPaymentSourceDict


class OrderApplicationContext(SdkBaseModel):
    """Customizes the payer experience during the approval process for the payment with PayPal. Note: Partners and
    Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the
    request values."""

    brand_name: Optional[str] = UNSET
    """DEPRECATED. The label that overrides the business name in the PayPal account on the PayPal site. The fields in
    ``application_context`` are now available in the ``experience_context`` object under the ``payment_source`` which
    supports them (eg. ``payment_source.paypal.experience_context.brand_name``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object."""

    locale: Optional[str] = UNSET
    """DEPRECATED. The BCP 47-formatted locale of pages that the PayPal payment experience shows. PayPal supports a
    five-character code. For example, ``da-DK``, ``he-IL``, ``id-ID``, ``ja-JP``, ``no-NO``, ``pt-BR``, ``ru-RU``,
    ``sv-SE``, ``th-TH``, ``zh-CN``, ``zh-HK``, or ``zh-TW``. The fields in ``application_context`` are now available in
    the ``experience_context`` object under the ``payment_source`` which supports them (eg.
    ``payment_source.paypal.experience_context.locale``). Please specify this field in the ``experience_context`` object
    instead of the ``application_context`` object."""

    landing_page: Optional[OrderApplicationContextLandingPageOrStr] = UNSET
    """DEPRECATED. DEPRECATED. The type of landing page to show on the PayPal site for customer checkout. The fields in
    ``application_context`` are now available in the ``experience_context`` object under the ``payment_source`` which
    supports them (eg. ``payment_source.paypal.experience_context.landing_page``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object."""

    shipping_preference: Optional[OrderApplicationContextShippingPreferenceOrStr] = UNSET
    """DEPRECATED. DEPRECATED. The shipping preference: Displays the shipping address to the customer. Enables the
    customer to choose an address on the PayPal site. Restricts the customer from changing the address during the
    payment-approval process. . The fields in ``application_context`` are now available in the ``experience_context``
    object under the ``payment_source`` which supports them (eg.
    ``payment_source.paypal.experience_context.shipping_preference``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object."""

    user_action: Optional[OrderApplicationContextUserActionOrStr] = UNSET
    """DEPRECATED. Configures a Continue or Pay Now checkout flow. The fields in ``application_context`` are now
    available in the ``experience_context`` object under the ``payment_source`` which supports them (eg.
    ``payment_source.paypal.experience_context.user_action``). Please specify this field in the ``experience_context``
    object instead of the ``application_context`` object."""

    payment_method: Optional[PaymentMethodPreference] = UNSET
    """DEPRECATED. The customer and merchant payment preferences. The fields in ``application_context`` are now
    available in the ``experience_context`` object under the ``payment_source`` which supports them (eg.
    ``payment_source.paypal.experience_context.payment_method_selected``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object.."""

    return_url: Optional[str] = UNSET
    """DEPRECATED. The URL where the customer is redirected after the customer approves the payment. The fields in
    ``application_context`` are now available in the ``experience_context`` object under the ``payment_source`` which
    supports them (eg. ``payment_source.paypal.experience_context.return_url``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object."""

    cancel_url: Optional[str] = UNSET
    """DEPRECATED. The URL where the customer is redirected after the customer cancels the payment. The fields in
    ``application_context`` are now available in the ``experience_context`` object under the ``payment_source`` which
    supports them (eg. ``payment_source.paypal.experience_context.cancel_url``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object."""

    stored_payment_source: Optional[StoredPaymentSource] = UNSET
    """DEPRECATED. Provides additional details to process a payment using a ``payment_source`` that has been stored or
    is intended to be stored (also referred to as stored_credential or card-on-file). Parameter compatibility:
    ``payment_type=ONE_TIME`` is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only
    with ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or
    ``previous_network_transaction_reference`` is compatible only with ``payment_initiator=MERCHANT``. Only one of the
    parameters - ``previous_transaction_reference`` and ``previous_network_transaction_reference`` - can be present in
    the request. . The fields in ``stored_payment_source`` are now available in the ``stored_credential`` object under
    the ``payment_source`` which supports them (eg. ``payment_source.card.stored_credential.payment_initiator``). Please
    specify this field in the ``payment_source`` object instead of the ``application_context`` object."""


class OrderApplicationContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    landing_page: NotRequired[OrderApplicationContextLandingPageOrStr]
    shipping_preference: NotRequired[OrderApplicationContextShippingPreferenceOrStr]
    user_action: NotRequired[OrderApplicationContextUserActionOrStr]
    payment_method: NotRequired[PaymentMethodPreference | PaymentMethodPreferenceDict]
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
    stored_payment_source: NotRequired[StoredPaymentSource | StoredPaymentSourceDict]
