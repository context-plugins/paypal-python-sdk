
# Pay Pal Wallet Stored Credential

Provides additional details to process a payment using the PayPal wallet billing agreement or a vaulted payment method that has been stored or is intended to be stored.

*This model accepts additional fields of type Any.*

## Structure

`PayPalWalletStoredCredential`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_initiator` | [`PaymentInitiator`](../../doc/models/payment-initiator.md) | Required | The person or party who initiated or triggered the payment.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `charge_pattern` | [`UsagePattern`](../../doc/models/usage-pattern.md) | Optional | DEPRECATED. Expected business/pricing model for the billing agreement, Please use usage_pattern instead.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30`, *Pattern*: `^[A-Z0-9_]+$` |
| `usage_pattern` | [`UsagePattern`](../../doc/models/usage-pattern.md) | Optional | Expected business/pricing model for the billing agreement.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30`, *Pattern*: `^[A-Z0-9_]+$` |
| `usage` | [`StoredPaymentSourceUsageType`](../../doc/models/stored-payment-source-usage-type.md) | Optional | Indicates if this is a `first` or `subsequent` payment using a stored payment source (also referred to as stored credential or card on file).<br><br>**Default**: `"DERIVED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.pay_pal_wallet_stored_credential import PayPalWalletStoredCredential
from paypal.models.payment_initiator import PaymentInitiator
from paypal.models.stored_payment_source_usage_type import StoredPaymentSourceUsageType
from paypal.models.usage_pattern import UsagePattern

pay_pal_wallet_stored_credential = PayPalWalletStoredCredential(
    payment_initiator=PaymentInitiator.CUSTOMER,
    charge_pattern=UsagePattern.RECURRING_PREPAID,
    usage_pattern=UsagePattern.RECURRING_PREPAID,
    usage=StoredPaymentSourceUsageType.DERIVED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

