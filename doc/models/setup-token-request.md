
# Setup Token Request

Setup Token Request where the `source` defines the type of instrument to be stored.

*This model accepts additional fields of type Any.*

## Structure

`SetupTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`Customer`](../../doc/models/customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `payment_source` | [`SetupTokenRequestPaymentSource`](../../doc/models/setup-token-request-payment-source.md) | Required | The payment method to vault with the instrument details. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.apple_pay_request_card import ApplePayRequestCard
from paypal.models.card_brand import CardBrand
from paypal.models.card_type import CardType
from paypal.models.customer import Customer
from paypal.models.fulfillment_type import FulfillmentType
from paypal.models.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageType
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.setup_token_request import SetupTokenRequest
from paypal.models.setup_token_request_card import SetupTokenRequestCard
from paypal.models.setup_token_request_payment_source import SetupTokenRequestPaymentSource
from paypal.models.shipping_name import ShippingName
from paypal.models.usage_pattern import UsagePattern
from paypal.models.vault_apple_pay_request import VaultApplePayRequest
from paypal.models.vault_pay_pal_wallet_request import VaultPayPalWalletRequest
from paypal.models.vault_token_request import VaultTokenRequest
from paypal.models.vault_token_request_type import VaultTokenRequestType
from paypal.models.vault_venmo_request import VaultVenmoRequest
from paypal.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails

setup_token_request = SetupTokenRequest(
    payment_source=SetupTokenRequestPaymentSource(
        card=SetupTokenRequestCard(
            name='name6',
            number='number6',
            expiry='expiry4',
            security_code='security_code8',
            brand=CardBrand.CB_NATIONALE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        paypal=VaultPayPalWalletRequest(
            description='description2',
            usage_pattern=UsagePattern.THRESHOLD_PREPAID,
            shipping=VaultedDigitalWalletShippingDetails(
                name=ShippingName(
                    full_name='full_name6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                email_address='email_address2',
                phone_number=PhoneNumberWithCountryCode(
                    country_code='country_code2',
                    national_number='national_number6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                mtype=FulfillmentType.SHIPPING,
                address=Address(
                    country_code='country_code6',
                    address_line_1='address_line_16',
                    address_line_2='address_line_26',
                    admin_area_2='admin_area_20',
                    admin_area_1='admin_area_12',
                    postal_code='postal_code8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            permit_multiple_payment_tokens=False,
            usage_type=PayPalPaymentTokenUsageType.MERCHANT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        venmo=VaultVenmoRequest(
            description='description6',
            usage_pattern=UsagePattern.UNSCHEDULED_PREPAID,
            shipping=VaultedDigitalWalletShippingDetails(
                name=ShippingName(
                    full_name='full_name6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                email_address='email_address2',
                phone_number=PhoneNumberWithCountryCode(
                    country_code='country_code2',
                    national_number='national_number6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                mtype=FulfillmentType.SHIPPING,
                address=Address(
                    country_code='country_code6',
                    address_line_1='address_line_16',
                    address_line_2='address_line_26',
                    admin_area_2='admin_area_20',
                    admin_area_1='admin_area_12',
                    postal_code='postal_code8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            permit_multiple_payment_tokens=False,
            usage_type=PayPalPaymentTokenUsageType.MERCHANT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        apple_pay=VaultApplePayRequest(
            token='token6',
            card=ApplePayRequestCard(
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
        token=VaultTokenRequest(
            id='id6',
            mtype=VaultTokenRequestType.SETUP_TOKEN,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    customer=Customer(
        id='id0',
        merchant_customer_id='merchant_customer_id2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

