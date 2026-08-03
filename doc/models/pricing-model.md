
# Pricing Model

The pricing model for the billing cycle.

*This model accepts additional fields of type Any.*

## Enumeration

`PricingModel`

## Fields

| Name | Description |
|  --- | --- |
| `FIXED` | A fixed pricing scheme where the customer is charged a fixed amount. |
| `VARIABLE` | A variable pricing scheme where the customer is charged a variable amount. |
| `AUTO_RELOAD` | A auto-reload pricing scheme where the customer is charged a fixed amount for reload. |

## Example

```python
from paypal.models.pricing_model import PricingModel

pricing_model = PricingModel.AUTO_RELOAD
```

