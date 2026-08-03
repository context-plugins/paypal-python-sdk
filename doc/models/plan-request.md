
# Plan Request

The create plan request details.

*This model accepts additional fields of type Any.*

## Structure

`PlanRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `str` | Required | The ID of the product created through Catalog Products API.<br><br>**Constraints**: *Minimum Length*: `22`, *Maximum Length*: `22`, *Pattern*: `^PROD-[A-Z0-9]*$` |
| `name` | `str` | Required | The plan name.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `status` | [`PlanRequestStatus`](../../doc/models/plan-request-status.md) | Optional | The initial state of the plan. Allowed input values are CREATED and ACTIVE.<br><br>**Default**: `"ACTIVE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `description` | `str` | Optional | The detailed description of the plan.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `billing_cycles` | [`List[SubscriptionBillingCycle]`](../../doc/models/subscription-billing-cycle.md) | Required | An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and only one regular cycle.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `12` |
| `payment_preferences` | [`PaymentPreferences`](../../doc/models/payment-preferences.md) | Required | The payment preferences for a subscription. |
| `merchant_preferences` | [`MerchantPreferences`](../../doc/models/merchant-preferences.md) | Optional | The merchant preferences for a subscription. |
| `taxes` | [`Taxes`](../../doc/models/taxes.md) | Optional | The tax details. |
| `quantity_supported` | `bool` | Optional | Indicates whether you can subscribe to this plan by providing a quantity for the goods or service.<br><br>**Default**: `False` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.frequency import Frequency
from paypal.models.interval_unit import IntervalUnit
from paypal.models.merchant_preferences import MerchantPreferences
from paypal.models.money import Money
from paypal.models.payment_preferences import PaymentPreferences
from paypal.models.plan_request import PlanRequest
from paypal.models.plan_request_status import PlanRequestStatus
from paypal.models.pricing_tier import PricingTier
from paypal.models.setup_fee_failure_action import SetupFeeFailureAction
from paypal.models.subscription_billing_cycle import SubscriptionBillingCycle
from paypal.models.subscription_pricing_model import SubscriptionPricingModel
from paypal.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypal.models.taxes import Taxes
from paypal.models.tenure_type import TenureType

plan_request = PlanRequest(
    product_id='product_id8',
    name='name2',
    billing_cycles=[
        SubscriptionBillingCycle(
            frequency=Frequency(
                interval_unit=IntervalUnit.DAY,
                interval_count=1,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            tenure_type=TenureType.REGULAR,
            sequence=8,
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
    ],
    payment_preferences=PaymentPreferences(
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
    ),
    status=PlanRequestStatus.ACTIVE,
    description='description2',
    merchant_preferences=MerchantPreferences(
        return_url='return_url4',
        cancel_url='cancel_url6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    taxes=Taxes(
        percentage='percentage8',
        inclusive=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    quantity_supported=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

