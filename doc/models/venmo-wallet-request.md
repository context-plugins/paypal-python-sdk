
# Venmo Wallet Request

Information needed to pay using Venmo.

*This model accepts additional fields of type Any.*

## Structure

`VenmoWalletRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault_id` | `str` | Optional | The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the saved payment source can be used for future transactions.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9a-zA-Z_-]+$` |
| `email_address` | `str` | Optional | The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted @ sign exists.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `254`, *Pattern*: ``(?:[a-zA-Z0-9!#$%&'*+/=?^_`{\|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{\|}~-]+)*\|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]\|\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\|\[(?:(?:(2(5[0-5]\|[0-4][0-9])\|1[0-9][0-9]\|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]\|[0-4][0-9])\|1[0-9][0-9]\|[1-9]?[0-9])\|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]\|\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])`` |
| `experience_context` | [`VenmoWalletExperienceContext`](../../doc/models/venmo-wallet-experience-context.md) | Optional | Customizes the buyer experience during the approval process for payment with Venmo. Note: Partners and Marketplaces might configure shipping_preference during partner account setup, which overrides the request values. |
| `attributes` | [`VenmoWalletAdditionalAttributes`](../../doc/models/venmo-wallet-additional-attributes.md) | Optional | Additional attributes associated with the use of this Venmo Wallet. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.application_context_shipping_preference import ApplicationContextShippingPreference
from paypal.models.callback_configuration import CallbackConfiguration
from paypal.models.callback_events import CallbackEvents
from paypal.models.name import Name
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.store_in_vault_instruction import StoreInVaultInstruction
from paypal.models.venmo_payment_token_customer_type import VenmoPaymentTokenCustomerType
from paypal.models.venmo_payment_token_usage_pattern import VenmoPaymentTokenUsagePattern
from paypal.models.venmo_payment_token_usage_type import VenmoPaymentTokenUsageType
from paypal.models.venmo_wallet_additional_attributes import VenmoWalletAdditionalAttributes
from paypal.models.venmo_wallet_customer_information import VenmoWalletCustomerInformation
from paypal.models.venmo_wallet_experience_context import VenmoWalletExperienceContext
from paypal.models.venmo_wallet_experience_context_user_action import VenmoWalletExperienceContextUserAction
from paypal.models.venmo_wallet_request import VenmoWalletRequest
from paypal.models.venmo_wallet_vault_attributes import VenmoWalletVaultAttributes

venmo_wallet_request = VenmoWalletRequest(
    vault_id='vault_id6',
    email_address='email_address6',
    experience_context=VenmoWalletExperienceContext(
        brand_name='brand_name2',
        shipping_preference=ApplicationContextShippingPreference.NO_SHIPPING,
        order_update_callback_config=CallbackConfiguration(
            callback_events=[
                CallbackEvents.SHIPPING_OPTIONS,
                CallbackEvents.SHIPPING_ADDRESS,
                CallbackEvents.SHIPPING_OPTIONS
            ],
            callback_url='callback_url6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        user_action=VenmoWalletExperienceContextUserAction.CONTINUE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    attributes=VenmoWalletAdditionalAttributes(
        customer=VenmoWalletCustomerInformation(
            id='id0',
            email_address='email_address2',
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
            name=Name(
                given_name='given_name2',
                surname='surname8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        vault=VenmoWalletVaultAttributes(
            store_in_vault=StoreInVaultInstruction.ON_SUCCESS,
            usage_type=VenmoPaymentTokenUsageType.MERCHANT,
            description='description6',
            usage_pattern=VenmoPaymentTokenUsagePattern.THRESHOLD_PREPAID,
            customer_type=VenmoPaymentTokenCustomerType.CONSUMER,
            permit_multiple_payment_tokens=False,
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

