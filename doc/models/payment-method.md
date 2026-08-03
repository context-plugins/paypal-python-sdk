
# Payment Method

The customer and merchant payment preferences.

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payee_preferred` | [`PayeePaymentMethodPreference`](../../doc/models/payee-payment-method-preference.md) | Optional | The merchant-preferred payment methods.<br><br>**Default**: `"UNRESTRICTED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.payee_payment_method_preference import PayeePaymentMethodPreference
from paypal.models.payment_method import PaymentMethod

payment_method = PaymentMethod(
    payee_preferred=PayeePaymentMethodPreference.UNRESTRICTED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

