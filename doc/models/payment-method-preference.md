
# Payment Method Preference

The customer and merchant payment preferences.

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethodPreference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payee_preferred` | [`PayeePaymentMethodPreference`](../../doc/models/payee-payment-method-preference.md) | Optional | The merchant-preferred payment methods.<br><br>**Default**: `"UNRESTRICTED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `standard_entry_class_code` | [`StandardEntryClassCode`](../../doc/models/standard-entry-class-code.md) | Optional | NACHA (the regulatory body governing the ACH network) requires that API callers (merchants, partners) obtain the consumer’s explicit authorization before initiating a transaction. To stay compliant, you’ll need to make sure that you retain a compliant authorization for each transaction that you originate to the ACH Network using this API. ACH transactions are categorized (using SEC codes) by how you capture authorization from the Receiver (the person whose bank account is being debited or credited). PayPal supports the following SEC codes.<br><br>**Default**: `"WEB"`<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `255` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.payee_payment_method_preference import PayeePaymentMethodPreference
from paypal.models.payment_method_preference import PaymentMethodPreference
from paypal.models.standard_entry_class_code import StandardEntryClassCode

payment_method_preference = PaymentMethodPreference(
    payee_preferred=PayeePaymentMethodPreference.UNRESTRICTED,
    standard_entry_class_code=StandardEntryClassCode.WEB,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

