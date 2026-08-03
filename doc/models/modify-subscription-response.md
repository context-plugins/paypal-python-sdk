
# Modify Subscription Response

The response to a request to update the quantity of the product or service in a subscription. You can also use this method to switch the plan and update the `shipping_amount` and `shipping_address` values for the subscription. This type of update requires the buyer's consent.

*This model accepts additional fields of type Any.*

## Structure

`ModifySubscriptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Optional | The unique PayPal-generated ID for the plan.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26`, *Pattern*: `^P-[A-Z0-9]*$` |
| `quantity` | `str` | Optional | The quantity of the product or service in the subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^([0-9]+\|([0-9]+)?[.][0-9]+)$` |
| `shipping_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping_address` | [`ShippingDetails`](../../doc/models/shipping-details.md) | Optional | The shipping details. |
| `plan` | [`PlanOverride`](../../doc/models/plan-override.md) | Optional | An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object. |
| `plan_overridden` | `bool` | Optional, Read-only | Indicates whether the subscription has overridden any plan attributes. |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.billing_cycle_override import BillingCycleOverride
from paypal.models.fulfillment_type import FulfillmentType
from paypal.models.modify_subscription_response import ModifySubscriptionResponse
from paypal.models.money import Money
from paypal.models.payment_preferences_override import PaymentPreferencesOverride
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.plan_override import PlanOverride
from paypal.models.pricing_tier import PricingTier
from paypal.models.setup_fee_failure_action import SetupFeeFailureAction
from paypal.models.shipping_details import ShippingDetails
from paypal.models.shipping_name import ShippingName
from paypal.models.shipping_option import ShippingOption
from paypal.models.shipping_type import ShippingType
from paypal.models.subscription_pricing_model import SubscriptionPricingModel
from paypal.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypal.models.taxes_override import TaxesOverride

modify_subscription_response = ModifySubscriptionResponse(
    plan_id='plan_id8',
    quantity='quantity2',
    shipping_amount=Money(
        currency_code='currency_code0',
        value='value6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    shipping_address=ShippingDetails(
        name=ShippingName(
            full_name='full_name6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        email_address='email_address8',
        phone_number=PhoneNumberWithCountryCode(
            country_code='country_code2',
            national_number='national_number6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mtype=FulfillmentType.PICKUP_IN_STORE,
        options=[
            ShippingOption(
                id='id2',
                label='label2',
                selected=False,
                mtype=ShippingType.SHIPPING,
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
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
    ),
    plan=PlanOverride(
        billing_cycles=[
            BillingCycleOverride(
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
                total_cycles=198,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            BillingCycleOverride(
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
                total_cycles=198,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        payment_preferences=PaymentPreferencesOverride(
            auto_bill_outstanding=False,
            setup_fee=Money(
                currency_code='currency_code8',
                value='value4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            setup_fee_failure_action=SetupFeeFailureAction.CONTINUE,
            payment_failure_threshold=104,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        taxes=TaxesOverride(
            percentage='percentage8',
            inclusive=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

