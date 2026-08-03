
# Order Authorize Request Payment Source

The payment source definition.

*This model accepts additional fields of type Any.*

## Structure

`OrderAuthorizeRequestPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardRequest`](../../doc/models/card-request.md) | Optional | The payment card to use to fund a payment. Can be a credit or debit card. Note: Passing card number, cvv and expiry directly via the API requires PCI SAQ D compliance. *PayPal offers a mechanism by which you do not have to take on the PCI SAQ D burden by using hosted fields - refer to this Integration Guide*. |
| `token` | [`Token`](../../doc/models/token.md) | Optional | The tokenized payment source to fund a payment. |
| `paypal` | [`PayPalWallet`](../../doc/models/pay-pal-wallet.md) | Optional | A resource that identifies a PayPal Wallet is used for payment. |
| `apple_pay` | [`ApplePayRequest`](../../doc/models/apple-pay-request.md) | Optional | Information needed to pay using ApplePay. |
| `google_pay` | [`GooglePayRequest`](../../doc/models/google-pay-request.md) | Optional | Information needed to pay using Google Pay. |
| `venmo` | [`VenmoWalletRequest`](../../doc/models/venmo-wallet-request.md) | Optional | Information needed to pay using Venmo. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.apple_pay_decrypted_token_data import ApplePayDecryptedTokenData
from paypal.models.apple_pay_payment_data import ApplePayPaymentData
from paypal.models.apple_pay_payment_data_type import ApplePayPaymentDataType
from paypal.models.apple_pay_request import ApplePayRequest
from paypal.models.apple_pay_tokenized_card import ApplePayTokenizedCard
from paypal.models.card_brand import CardBrand
from paypal.models.card_request import CardRequest
from paypal.models.card_type import CardType
from paypal.models.google_pay_authentication_method import GooglePayAuthenticationMethod
from paypal.models.google_pay_card import GooglePayCard
from paypal.models.google_pay_decrypted_token_data import GooglePayDecryptedTokenData
from paypal.models.google_pay_payment_method import GooglePayPaymentMethod
from paypal.models.google_pay_request import GooglePayRequest
from paypal.models.google_pay_request_card import GooglePayRequestCard
from paypal.models.money import Money
from paypal.models.name import Name
from paypal.models.order_authorize_request_payment_source import OrderAuthorizeRequestPaymentSource
from paypal.models.pay_pal_wallet import PayPalWallet
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.token import Token
from paypal.models.token_type import TokenType

order_authorize_request_payment_source = OrderAuthorizeRequestPaymentSource(
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
    apple_pay=ApplePayRequest(
        id='id0',
        name='name0',
        email_address='email_address8',
        phone_number=PhoneNumber(
            national_number='national_number6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        decrypted_token=ApplePayDecryptedTokenData(
            tokenized_card=ApplePayTokenizedCard(
                name='name4',
                number='number2',
                expiry='expiry2',
                card_type=CardBrand.VISA,
                mtype=CardType.UNKNOWN,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            transaction_amount=Money(
                currency_code='currency_code6',
                value='value2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            device_manufacturer_id='device_manufacturer_id6',
            payment_data_type=ApplePayPaymentDataType.ENUM_3DSECURE,
            payment_data=ApplePayPaymentData(
                cryptogram='cryptogram6',
                eci_indicator='eci_indicator0',
                emv_data='emv_data0',
                pin='pin4',
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
    google_pay=GooglePayRequest(
        name='name8',
        email_address='email_address6',
        phone_number=PhoneNumberWithCountryCode(
            country_code='country_code2',
            national_number='national_number6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        card=GooglePayRequestCard(
            name='name6',
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
        decrypted_token=GooglePayDecryptedTokenData(
            payment_method=GooglePayPaymentMethod.CARD,
            card=GooglePayCard(
                name='name6',
                number='number6',
                expiry='expiry4',
                last_digits='last_digits0',
                mtype=CardType.UNKNOWN,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            authentication_method=GooglePayAuthenticationMethod.PAN_ONLY,
            message_id='message_id0',
            message_expiration='message_expiration2',
            cryptogram='cryptogram6',
            eci_indicator='eci_indicator0',
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

