
# Billing Cycle Override

The billing cycle details to override at subscription level. The subscription billing cycle definition has to adhere to the plan billing cycle definition.

*This model accepts additional fields of type Any.*

## Structure

`BillingCycleOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`SubscriptionPricingScheme`](../../doc/models/subscription-pricing-scheme.md) | Optional | The pricing scheme details. |
| `sequence` | `int` | Required | The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a `sequence` of `1` while a regular billing cycle has a `sequence` of `2`, so that trial cycle runs before the regular cycle.<br><br>**Constraints**: `>= 1`, `<= 99` |
| `total_cycles` | `int` | Optional | The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of 0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles).<br><br>**Constraints**: `>= 0`, `<= 999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.billing_cycle_override import BillingCycleOverride
from paypal.models.money import Money
from paypal.models.pricing_tier import PricingTier
from paypal.models.subscription_pricing_model import SubscriptionPricingModel
from paypal.models.subscription_pricing_scheme import SubscriptionPricingScheme

billing_cycle_override = BillingCycleOverride(
    sequence=99,
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
    total_cycles=118,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

