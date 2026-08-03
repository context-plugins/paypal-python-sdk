
# Subscription Collection

The list of subscriptions.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscriptions` | [`List[Subscription]`](../../doc/models/subscription.md) | Optional | An array of subscriptions.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `32767` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.money import Money
from paypal.models.subscription import Subscription
from paypal.models.subscription_collection import SubscriptionCollection

subscription_collection = SubscriptionCollection(
    subscriptions=[
        Subscription(
            id='id6',
            plan_id='plan_id8',
            start_time='start_time0',
            quantity='quantity2',
            shipping_amount=Money(
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
    ],
    links=[
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
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

