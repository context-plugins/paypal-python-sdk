
# Subscriptions Card Attributes

Additional attributes associated with the use of this card.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionsCardAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`CardCustomer`](../../doc/models/card-customer.md) | Optional | The details about a customer in PayPal's system of record. |
| `vault` | [`VaultInstructionBase`](../../doc/models/vault-instruction-base.md) | Optional | Basic vault instruction specification that can be extended by specific payment sources that supports vaulting. |
| `verification` | [`CardVerification`](../../doc/models/card-verification.md) | Optional | The API caller can opt in to verify the card through PayPal offered verification services (e.g. Smart Dollar Auth, 3DS). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_customer import CardCustomer
from paypal.models.card_verification import CardVerification
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.store_in_vault_instruction import StoreInVaultInstruction
from paypal.models.subscription_card_verification_method import SubscriptionCardVerificationMethod
from paypal.models.subscriptions_card_attributes import SubscriptionsCardAttributes
from paypal.models.vault_instruction_base import VaultInstructionBase

subscriptions_card_attributes = SubscriptionsCardAttributes(
    customer=CardCustomer(
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
        merchant_customer_id='merchant_customer_id2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    vault=VaultInstructionBase(
        store_in_vault=StoreInVaultInstruction.ON_SUCCESS,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    verification=CardVerification(
        method=SubscriptionCardVerificationMethod.ENUM_3D_SECURE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

