
# Update Pricing Scheme

The update pricing scheme request details.

*This model accepts additional fields of type Any.*

## Structure

`UpdatePricingScheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_cycle_sequence` | `int` | Required | The billing cycle sequence.<br><br>**Constraints**: `>= 1`, `<= 99` |
| `pricing_scheme` | [`SubscriptionPricingScheme`](../../doc/models/subscription-pricing-scheme.md) | Required | The pricing scheme details. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.money import Money
from paypal.models.pricing_tier import PricingTier
from paypal.models.subscription_pricing_model import SubscriptionPricingModel
from paypal.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypal.models.update_pricing_scheme import UpdatePricingScheme

update_pricing_scheme = UpdatePricingScheme(
    billing_cycle_sequence=99,
    pricing_scheme=SubscriptionPricingScheme(
        version=10,
        fixed_price=Money(
            currency_code='currency_code4',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        pricing_model=SubscriptionPricingModel.VOLUME,
        tiers=[
            PricingTier(
                starting_quantity='starting_quantity8',
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ending_quantity='ending_quantity6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PricingTier(
                starting_quantity='starting_quantity8',
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ending_quantity='ending_quantity6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PricingTier(
                starting_quantity='starting_quantity8',
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ending_quantity='ending_quantity6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        create_time='create_time4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

