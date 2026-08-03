
# Order Authorize Response Payment Source

The payment source used to fund the payment.

*This model accepts additional fields of type Any.*

## Structure

`OrderAuthorizeResponsePaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardResponse`](../../doc/models/card-response.md) | Optional | The payment card to use to fund a payment. Card can be a credit or debit card. |
| `paypal` | [`PayPalWalletResponse`](../../doc/models/pay-pal-wallet-response.md) | Optional | The PayPal Wallet response. |
| `apple_pay` | [`ApplePayPaymentObject`](../../doc/models/apple-pay-payment-object.md) | Optional | Information needed to pay using ApplePay. |
| `google_pay` | [`GooglePayWalletResponse`](../../doc/models/google-pay-wallet-response.md) | Optional | Google Pay Wallet payment data. |
| `venmo` | [`VenmoWalletResponse`](../../doc/models/venmo-wallet-response.md) | Optional | Venmo wallet response. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.apple_pay_payment_object import ApplePayPaymentObject
from paypal.models.card_brand import CardBrand
from paypal.models.card_response import CardResponse
from paypal.models.card_type import CardType
from paypal.models.google_pay_card_response import GooglePayCardResponse
from paypal.models.google_pay_wallet_response import GooglePayWalletResponse
from paypal.models.name import Name
from paypal.models.order_authorize_response_payment_source import OrderAuthorizeResponsePaymentSource
from paypal.models.pay_pal_wallet_account_verification_status import PayPalWalletAccountVerificationStatus
from paypal.models.pay_pal_wallet_response import PayPalWalletResponse
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.phone_type import PhoneType
from paypal.models.venmo_wallet_response import VenmoWalletResponse

order_authorize_response_payment_source = OrderAuthorizeResponsePaymentSource(
    card=CardResponse(
        name='name6',
        last_digits='last_digits0',
        brand=CardBrand.CB_NATIONALE,
        available_networks=[
            CardBrand.DELTA
        ],
        mtype=CardType.UNKNOWN,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    paypal=PayPalWalletResponse(
        email_address='email_address0',
        account_id='account_id4',
        account_status=PayPalWalletAccountVerificationStatus.VERIFIED,
        name=Name(
            given_name='given_name2',
            surname='surname8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        phone_type=PhoneType.FAX,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    apple_pay=ApplePayPaymentObject(
        id='id0',
        token='token6',
        name='name0',
        email_address='email_address8',
        phone_number=PhoneNumber(
            national_number='national_number6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    google_pay=GooglePayWalletResponse(
        name='name8',
        email_address='email_address6',
        phone_number=PhoneNumberWithCountryCode(
            country_code='country_code2',
            national_number='national_number6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        card=GooglePayCardResponse(
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
                postal_code='postal_code0',
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
    ),
    venmo=VenmoWalletResponse(
        email_address='email_address4',
        account_id='account_id8',
        user_name='user_name2',
        name=Name(
            given_name='given_name2',
            surname='surname8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        phone_number=PhoneNumber(
            national_number='national_number6',
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

