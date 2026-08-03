
# Create Subscription Request

The create subscription request details.

*This model accepts additional fields of type Any.*

## Structure

`CreateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Required | The ID of the plan.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26`, *Pattern*: `^P-[A-Z0-9]*$` |
| `start_time` | `str` | Optional | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does not reject all invalid dates.<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `64`, *Pattern*: `^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[1-2][0-9]\|3[0-1])[T,t]([0-1][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?([Zz]\|[+-][0-9]{2}:[0-9]{2})$` |
| `quantity` | `str` | Optional | The quantity of the product in the subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^([0-9]+\|([0-9]+)?[.][0-9]+)$` |
| `shipping_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `subscriber` | [`SubscriberRequest`](../../doc/models/subscriber-request.md) | Optional | The subscriber request information . |
| `auto_renewal` | `bool` | Optional | DEPRECATED. Indicates whether the subscription auto-renews after the billing cycles complete.<br><br>**Default**: `False` |
| `application_context` | [`SubscriptionApplicationContext`](../../doc/models/subscription-application-context.md) | Optional | DEPRECATED. The application context, which customizes the payer experience during the subscription approval process with PayPal. |
| `custom_id` | `str` | Optional | The custom id for the subscription. Can be invoice id.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^[\x20-\x7E]+` |
| `plan` | [`PlanOverride`](../../doc/models/plan-override.md) | Optional | An inline plan object to customise the subscription. You can override plan level default attributes by providing customised values for the subscription in this object. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_type import CardType
from paypal.models.create_subscription_request import CreateSubscriptionRequest
from paypal.models.fulfillment_type import FulfillmentType
from paypal.models.money import Money
from paypal.models.name import Name
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.shipping_details import ShippingDetails
from paypal.models.shipping_name import ShippingName
from paypal.models.shipping_option import ShippingOption
from paypal.models.shipping_type import ShippingType
from paypal.models.subscriber_request import SubscriberRequest
from paypal.models.subscription_card_request import SubscriptionCardRequest
from paypal.models.subscription_payment_source import SubscriptionPaymentSource

create_subscription_request = CreateSubscriptionRequest(
    plan_id='plan_id6',
    start_time='start_time8',
    quantity='quantity0',
    shipping_amount=Money(
        currency_code='currency_code0',
        value='value6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    subscriber=SubscriberRequest(
        email_address='email_address8',
        payer_id='payer_id8',
        name=Name(
            given_name='given_name2',
            surname='surname8',
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
        payment_source=SubscriptionPaymentSource(
            card=SubscriptionCardRequest(
                name='name6',
                number='number6',
                expiry='expiry4',
                security_code='security_code8',
                mtype=CardType.UNKNOWN,
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
    ),
    auto_renewal=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

