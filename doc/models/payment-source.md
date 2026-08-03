
# Payment Source

The payment source definition.

*This model accepts additional fields of type Any.*

## Structure

`PaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardRequest`](../../doc/models/card-request.md) | Optional | The payment card to use to fund a payment. Can be a credit or debit card. Note: Passing card number, cvv and expiry directly via the API requires PCI SAQ D compliance. *PayPal offers a mechanism by which you do not have to take on the PCI SAQ D burden by using hosted fields - refer to this Integration Guide*. |
| `token` | [`Token`](../../doc/models/token.md) | Optional | The tokenized payment source to fund a payment. |
| `paypal` | [`PayPalWallet`](../../doc/models/pay-pal-wallet.md) | Optional | A resource that identifies a PayPal Wallet is used for payment. |
| `bancontact` | [`BancontactPaymentRequest`](../../doc/models/bancontact-payment-request.md) | Optional | Information needed to pay using Bancontact. |
| `blik` | [`BlikPaymentRequest`](../../doc/models/blik-payment-request.md) | Optional | Information needed to pay using BLIK. |
| `eps` | [`EpsPaymentRequest`](../../doc/models/eps-payment-request.md) | Optional | Information needed to pay using eps. |
| `giropay` | [`GiropayPaymentRequest`](../../doc/models/giropay-payment-request.md) | Optional | Information needed to pay using giropay. |
| `ideal` | [`IdealPaymentRequest`](../../doc/models/ideal-payment-request.md) | Optional | Information needed to pay using iDEAL. |
| `mybank` | [`MyBankPaymentRequest`](../../doc/models/my-bank-payment-request.md) | Optional | Information needed to pay using MyBank. |
| `p_24` | [`P24PaymentRequest`](../../doc/models/p24-payment-request.md) | Optional | Information needed to pay using P24 (Przelewy24). |
| `sofort` | [`SofortPaymentRequest`](../../doc/models/sofort-payment-request.md) | Optional | Information needed to pay using Sofort. |
| `trustly` | [`TrustlyPaymentRequest`](../../doc/models/trustly-payment-request.md) | Optional | Information needed to pay using Trustly. |
| `apple_pay` | [`ApplePayRequest`](../../doc/models/apple-pay-request.md) | Optional | Information needed to pay using ApplePay. |
| `google_pay` | [`GooglePayRequest`](../../doc/models/google-pay-request.md) | Optional | Information needed to pay using Google Pay. |
| `venmo` | [`VenmoWalletRequest`](../../doc/models/venmo-wallet-request.md) | Optional | Information needed to pay using Venmo. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.application_context_shipping_preference import ApplicationContextShippingPreference
from paypal.models.bancontact_payment_request import BancontactPaymentRequest
from paypal.models.blik_experience_context import BlikExperienceContext
from paypal.models.blik_level_0_payment_object import BlikLevel0PaymentObject
from paypal.models.blik_one_click_payment_request import BlikOneClickPaymentRequest
from paypal.models.blik_payment_request import BlikPaymentRequest
from paypal.models.card_request import CardRequest
from paypal.models.experience_context import ExperienceContext
from paypal.models.name import Name
from paypal.models.pay_pal_wallet import PayPalWallet
from paypal.models.payment_source import PaymentSource
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.token import Token
from paypal.models.token_type import TokenType

payment_source = PaymentSource(
    card=CardRequest(
        name='name6',
        number='number6',
        expiry='expiry4',
        security_code='security_code8',
        billing_address=Address(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    token=Token(
        id='id6',
        mtype=TokenType.BILLING_AGREEMENT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    paypal=PayPalWallet(
        vault_id='vault_id0',
        email_address='email_address0',
        name=Name(
            given_name='given_name2',
            surname='surname8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        phone=PhoneWithType(
            phone_number=PhoneNumber(
                national_number='national_number6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            phone_type=PhoneType.OTHER,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        birth_date='birth_date8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bancontact=BancontactPaymentRequest(
        name='name0',
        country_code='country_code0',
        experience_context=ExperienceContext(
            brand_name='brand_name2',
            locale='locale6',
            shipping_preference=ApplicationContextShippingPreference.NO_SHIPPING,
            return_url='return_url4',
            cancel_url='cancel_url6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    blik=BlikPaymentRequest(
        name='name2',
        country_code='country_code2',
        email='email4',
        experience_context=BlikExperienceContext(
            brand_name='brand_name2',
            locale='locale6',
            shipping_preference=ApplicationContextShippingPreference.NO_SHIPPING,
            return_url='return_url4',
            cancel_url='cancel_url6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        level_0=BlikLevel0PaymentObject(
            auth_code='auth_code8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        one_click=BlikOneClickPaymentRequest(
            consumer_reference='consumer_reference2',
            auth_code='auth_code0',
            alias_label='alias_label6',
            alias_key='alias_key4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

