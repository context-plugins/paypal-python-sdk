
# Plan

The merchant level Recurring Billing plan metadata for the Billing Agreement.

*This model accepts additional fields of type Any.*

## Structure

`Plan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_cycles` | [`List[BillingCycle]`](../../doc/models/billing-cycle.md) | Required | An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `3` |
| `one_time_charges` | [`OneTimeCharge`](../../doc/models/one-time-charge.md) | Required | The one-time charge info at the time of checkout. |
| `name` | `str` | Optional | Name of the recurring plan.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^[A-Za-z0-9() +',.:-]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.billing_cycle import BillingCycle
from paypal.models.money import Money
from paypal.models.one_time_charge import OneTimeCharge
from paypal.models.plan import Plan
from paypal.models.pricing_model import PricingModel
from paypal.models.pricing_scheme import PricingScheme
from paypal.models.tenure_type import TenureType

plan = Plan(
    billing_cycles=[
        BillingCycle(
            tenure_type=TenureType.REGULAR,
            pricing_scheme=PricingScheme(
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
            ),
            total_cycles=1,
            sequence=1,
            start_date='start_date6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    one_time_charges=OneTimeCharge(
        total_amount=Money(
            currency_code='currency_code2',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        setup_fee=Money(
            currency_code='currency_code8',
            value='value4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        shipping_amount=Money(
            currency_code='currency_code0',
            value='value6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        taxes=Money(
            currency_code='currency_code6',
            value='value2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        product_price=Money(
            currency_code='currency_code6',
            value='value2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        subtotal=Money(
            currency_code='currency_code2',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    name='name4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

