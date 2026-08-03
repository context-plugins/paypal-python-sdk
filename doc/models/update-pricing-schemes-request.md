
# Update Pricing Schemes Request

The update pricing scheme request details.

*This model accepts additional fields of type Any.*

## Structure

`UpdatePricingSchemesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_schemes` | [`List[UpdatePricingScheme]`](../../doc/models/update-pricing-scheme.md) | Required | An array of pricing schemes.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `99` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.money import Money
from paypal.models.pricing_tier import PricingTier
from paypal.models.subscription_pricing_model import SubscriptionPricingModel
from paypal.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypal.models.update_pricing_scheme import UpdatePricingScheme
from paypal.models.update_pricing_schemes_request import UpdatePricingSchemesRequest

update_pricing_schemes_request = UpdatePricingSchemesRequest(
    pricing_schemes=[
        UpdatePricingScheme(
            billing_cycle_sequence=34,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

