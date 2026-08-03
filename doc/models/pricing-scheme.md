
# Pricing Scheme

The pricing scheme details.

*This model accepts additional fields of type Any.*

## Structure

`PricingScheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `pricing_model` | [`PricingModel`](../../doc/models/pricing-model.md) | Required | The pricing model for the billing cycle.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `reload_threshold_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.money import Money
from paypal.models.pricing_model import PricingModel
from paypal.models.pricing_scheme import PricingScheme

pricing_scheme = PricingScheme(
    pricing_model=PricingModel.AUTO_RELOAD,
    price=Money(
        currency_code='currency_code8',
        value='value4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reload_threshold_amount=Money(
        currency_code='currency_code0',
        value='value6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

