
# Pay Pal Wallet Attributes

Additional attributes associated with the use of this PayPal Wallet.

*This model accepts additional fields of type Any.*

## Structure

`PayPalWalletAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`PayPalWalletCustomerRequest`](../../doc/models/pay-pal-wallet-customer-request.md) | Optional | - |
| `vault` | [`PayPalWalletVaultInstruction`](../../doc/models/pay-pal-wallet-vault-instruction.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.name import Name
from paypal.models.pay_pal_payment_token_customer_type import PayPalPaymentTokenCustomerType
from paypal.models.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageType
from paypal.models.pay_pal_wallet_attributes import PayPalWalletAttributes
from paypal.models.pay_pal_wallet_customer_request import PayPalWalletCustomerRequest
from paypal.models.pay_pal_wallet_vault_instruction import PayPalWalletVaultInstruction
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.store_in_vault_instruction import StoreInVaultInstruction
from paypal.models.usage_pattern import UsagePattern

pay_pal_wallet_attributes = PayPalWalletAttributes(
    customer=PayPalWalletCustomerRequest(
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
        merchant_customer_id='merchant_customer_id2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    vault=PayPalWalletVaultInstruction(
        usage_type=PayPalPaymentTokenUsageType.MERCHANT,
        store_in_vault=StoreInVaultInstruction.ON_SUCCESS,
        description='description6',
        usage_pattern=UsagePattern.THRESHOLD_PREPAID,
        customer_type=PayPalPaymentTokenCustomerType.CONSUMER,
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

