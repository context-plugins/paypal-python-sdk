
# Setup Token Response Payment Source

The setup payment method details.

## Structure

`SetupTokenResponsePaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`SetupTokenResponseCard`](../../doc/models/setup-token-response-card.md) | Optional | - |
| `paypal` | [`PaypalPaymentToken`](../../doc/models/paypal-payment-token.md) | Optional, Read-only | Full representation of a PayPal Payment Token. |
| `venmo` | [`VenmoPaymentToken`](../../doc/models/venmo-payment-token.md) | Optional, Read-only | Full representation of a Venmo Payment Token. |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.fulfillment_type import FulfillmentType
from paypalserversdk.models.paypal_payment_token import PaypalPaymentToken
from paypalserversdk.models.paypal_payment_token_usage_type import PaypalPaymentTokenUsageType
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.setup_token_response_card import SetupTokenResponseCard
from paypalserversdk.models.setup_token_response_payment_source import SetupTokenResponsePaymentSource
from paypalserversdk.models.shipping_name import ShippingName
from paypalserversdk.models.usage_pattern import UsagePattern
from paypalserversdk.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails
from paypalserversdk.models.venmo_payment_token import VenmoPaymentToken

setup_token_response_payment_source = SetupTokenResponsePaymentSource(
    card=SetupTokenResponseCard(
        name='name6',
        last_digits='last_digits0',
        brand=CardBrand.CB_NATIONALE,
        expiry='expiry4',
        billing_address=CardResponseAddress(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0'
        )
    ),
    paypal=PaypalPaymentToken(
        description='description2',
        usage_pattern=UsagePattern.THRESHOLD_PREPAID,
        shipping=VaultedDigitalWalletShippingDetails(
            name=ShippingName(
                full_name='full_name6'
            ),
            email_address='email_address2',
            phone_number=PhoneNumberWithCountryCode(
                country_code='country_code2',
                national_number='national_number6'
            ),
            mtype=FulfillmentType.SHIPPING,
            address=Address(
                country_code='country_code6',
                address_line_1='address_line_16',
                address_line_2='address_line_26',
                admin_area_2='admin_area_20',
                admin_area_1='admin_area_12',
                postal_code='postal_code8'
            )
        ),
        permit_multiple_payment_tokens=False,
        usage_type=PaypalPaymentTokenUsageType.MERCHANT
    ),
    venmo=VenmoPaymentToken(
        description='description6',
        usage_pattern=UsagePattern.UNSCHEDULED_PREPAID,
        shipping=VaultedDigitalWalletShippingDetails(
            name=ShippingName(
                full_name='full_name6'
            ),
            email_address='email_address2',
            phone_number=PhoneNumberWithCountryCode(
                country_code='country_code2',
                national_number='national_number6'
            ),
            mtype=FulfillmentType.SHIPPING,
            address=Address(
                country_code='country_code6',
                address_line_1='address_line_16',
                address_line_2='address_line_26',
                admin_area_2='admin_area_20',
                admin_area_1='admin_area_12',
                postal_code='postal_code8'
            )
        ),
        permit_multiple_payment_tokens=False,
        usage_type=PaypalPaymentTokenUsageType.MERCHANT
    )
)
```

