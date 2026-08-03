
# Venmo Wallet Additional Attributes

Additional attributes associated with the use of this Venmo Wallet.

*This model accepts additional fields of type Any.*

## Structure

`VenmoWalletAdditionalAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`VenmoWalletCustomerInformation`](../../doc/models/venmo-wallet-customer-information.md) | Optional | The details about a customer in PayPal's system of record. |
| `vault` | [`VenmoWalletVaultAttributes`](../../doc/models/venmo-wallet-vault-attributes.md) | Optional | Resource consolidating common request and response attirbutes for vaulting Venmo Wallet. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

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
from paypal.models.venmo_wallet_vault_attributes import VenmoWalletVaultAttributes

venmo_wallet_additional_attributes = VenmoWalletAdditionalAttributes(
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
)
```

