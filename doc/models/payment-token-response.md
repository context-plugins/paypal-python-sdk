
# Payment Token Response

Full representation of a saved payment token.

## Structure

`PaymentTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the saved payment source can be used for future transactions.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9a-zA-Z_-]+$` |
| `customer` | [`CustomerResponse`](../../doc/models/customer-response.md) | Optional | Customer in merchant's or partner's system of records. |
| `payment_source` | [`PaymentTokenResponsePaymentSource`](../../doc/models/payment-token-response-payment-source.md) | Optional | The vaulted payment method details. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of related [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32` |

## Example

```python
from paypalserversdk.models.address import Address
from paypalserversdk.models.apple_pay_card import ApplePayCard
from paypalserversdk.models.apple_pay_payment_token import ApplePayPaymentToken
from paypalserversdk.models.card_brand import CardBrand
from paypalserversdk.models.card_payment_token_entity import CardPaymentTokenEntity
from paypalserversdk.models.card_response_address import CardResponseAddress
from paypalserversdk.models.card_type import CardType
from paypalserversdk.models.customer_response import CustomerResponse
from paypalserversdk.models.fulfillment_type import FulfillmentType
from paypalserversdk.models.link_description import LinkDescription
from paypalserversdk.models.link_http_method import LinkHttpMethod
from paypalserversdk.models.payment_token_response import PaymentTokenResponse
from paypalserversdk.models.payment_token_response_payment_source import PaymentTokenResponsePaymentSource
from paypalserversdk.models.paypal_payment_token import PaypalPaymentToken
from paypalserversdk.models.paypal_payment_token_usage_type import PaypalPaymentTokenUsageType
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.shipping_name import ShippingName
from paypalserversdk.models.usage_pattern import UsagePattern
from paypalserversdk.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails
from paypalserversdk.models.venmo_payment_token import VenmoPaymentToken

payment_token_response = PaymentTokenResponse(
    id='id6',
    customer=CustomerResponse(
        id='id0',
        merchant_customer_id='merchant_customer_id2'
    ),
    payment_source=PaymentTokenResponsePaymentSource(
        card=CardPaymentTokenEntity(
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
        ),
        apple_pay=ApplePayPaymentToken(
            card=ApplePayCard(
                name='name6',
                last_digits='last_digits0',
                mtype=CardType.UNKNOWN,
                brand=CardBrand.CB_NATIONALE,
                billing_address=Address(
                    country_code='country_code8',
                    address_line_1='address_line_12',
                    address_line_2='address_line_28',
                    admin_area_2='admin_area_28',
                    admin_area_1='admin_area_14',
                    postal_code='postal_code0'
                )
            )
        )
    ),
    links=[
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD
        ),
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD
        )
    ]
)
```

