
# Tax Amount

The tax levied by a government on the purchase of goods or services.

*This model accepts additional fields of type Any.*

## Structure

`TaxAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.money import Money
from paypal.models.tax_amount import TaxAmount

tax_amount = TaxAmount(
    tax_amount=Money(
        currency_code='currency_code2',
        value='value8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

