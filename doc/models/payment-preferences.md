
# Payment Preferences

The payment preferences for a subscription., The payment preferences to override at subscription level.

*This model accepts additional fields of type Any.*

## Structure

`PaymentPreferences`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_bill_outstanding` | `bool` | Optional | Indicates whether to automatically bill the outstanding amount in the next billing cycle.<br><br>**Default**: `True` |
| `setup_fee` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `setup_fee_failure_action` | [`SetupFeeFailureAction`](../../doc/models/setup-fee-failure-action.md) | Optional | The action to take on the subscription if the initial payment for the setup fails.<br><br>**Default**: `"CANCEL"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `payment_failure_threshold` | `int` | Optional | The maximum number of payment failures before a subscription is suspended. For example, if `payment_failure_threshold` is `2`, the subscription automatically updates to the `SUSPEND` state if two consecutive payments fail.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.money import Money
from paypal.models.payment_preferences import PaymentPreferences
from paypal.models.setup_fee_failure_action import SetupFeeFailureAction

payment_preferences = PaymentPreferences(
    auto_bill_outstanding=True,
    setup_fee=Money(
        currency_code='currency_code8',
        value='value4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    setup_fee_failure_action=SetupFeeFailureAction.CANCEL,
    payment_failure_threshold=0,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

