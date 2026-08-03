
# Pay Pal Wallet Vault Instruction

*This model accepts additional fields of type Any.*

## Structure

`PayPalWalletVaultInstruction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `store_in_vault` | [`StoreInVaultInstruction`](../../doc/models/store-in-vault-instruction.md) | Optional | Defines how and when the payment source gets vaulted.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `description` | `str` | Optional | The description displayed to PayPal consumer on the approval flow for PayPal, as well as on the PayPal payment token management experience on PayPal.com.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `usage_pattern` | [`UsagePattern`](../../doc/models/usage-pattern.md) | Optional | Expected business/pricing model for the billing agreement.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30` |
| `usage_type` | [`PayPalPaymentTokenUsageType`](../../doc/models/pay-pal-payment-token-usage-type.md) | Required | The usage type associated with the PayPal payment token.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `customer_type` | [`PayPalPaymentTokenCustomerType`](../../doc/models/pay-pal-payment-token-customer-type.md) | Optional | The customer type associated with the PayPal payment token. This is to indicate whether the customer acting on the merchant / platform is either a business or a consumer.<br><br>**Default**: `"CONSUMER"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `permit_multiple_payment_tokens` | `bool` | Optional | Create multiple payment tokens for the same payer, merchant/platform combination. Use this when the customer has not logged in at merchant/platform. The payment token thus generated, can then also be used to create the customer account at merchant/platform. Use this also when multiple payment tokens are required for the same payer, different customer at merchant/platform. This helps to identify customers distinctly even though they may share the same PayPal account. This only applies to PayPal payment source.<br><br>**Default**: `False` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.pay_pal_payment_token_customer_type import PayPalPaymentTokenCustomerType
from paypal.models.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageType
from paypal.models.pay_pal_wallet_vault_instruction import PayPalWalletVaultInstruction
from paypal.models.store_in_vault_instruction import StoreInVaultInstruction
from paypal.models.usage_pattern import UsagePattern

pay_pal_wallet_vault_instruction = PayPalWalletVaultInstruction(
    usage_type=PayPalPaymentTokenUsageType.MERCHANT,
    store_in_vault=StoreInVaultInstruction.ON_SUCCESS,
    description='description4',
    usage_pattern=UsagePattern.INSTALLMENT_PREPAID,
    customer_type=PayPalPaymentTokenCustomerType.CONSUMER,
    permit_multiple_payment_tokens=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

