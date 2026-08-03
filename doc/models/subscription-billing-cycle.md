
# Subscription Billing Cycle

The billing cycle details.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionBillingCycle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`SubscriptionPricingScheme`](../../doc/models/subscription-pricing-scheme.md) | Optional | The pricing scheme details. |
| `frequency` | [`Frequency`](../../doc/models/frequency.md) | Required | The frequency of the billing cycle. |
| `tenure_type` | [`TenureType`](../../doc/models/tenure-type.md) | Required | The tenure type of the billing cycle. In case of a plan having trial cycle, only 2 trial cycles are allowed per plan.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `sequence` | `int` | Required | The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a `sequence` of `1` while a regular billing cycle has a `sequence` of `2`, so that trial cycle runs before the regular cycle.<br><br>**Constraints**: `>= 1`, `<= 99` |
| `total_cycles` | `int` | Optional | The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of 0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles).<br><br>**Default**: `1`<br><br>**Constraints**: `>= 0`, `<= 999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.frequency import Frequency
from paypal.models.interval_unit import IntervalUnit
from paypal.models.money import Money
from paypal.models.pricing_tier import PricingTier
from paypal.models.subscription_billing_cycle import SubscriptionBillingCycle
from paypal.models.subscription_pricing_model import SubscriptionPricingModel
from paypal.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypal.models.tenure_type import TenureType

subscription_billing_cycle = SubscriptionBillingCycle(
    frequency=Frequency(
        interval_unit=IntervalUnit.DAY,
        interval_count=1,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    tenure_type=TenureType.REGULAR,
    sequence=30,
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
    total_cycles=1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

