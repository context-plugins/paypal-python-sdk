
# Transactions List

The list transactions for a subscription request details.

*This model accepts additional fields of type Any.*

## Structure

`TransactionsList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transactions` | [`List[SubscriptionTransactionDetails]`](../../doc/models/subscription-transaction-details.md) | Optional | An array of transactions.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `32767` |
| `total_items` | `int` | Optional | The total number of items.<br><br>**Constraints**: `>= 0`, `<= 500000000` |
| `total_pages` | `int` | Optional | The total number of pages.<br><br>**Constraints**: `>= 0`, `<= 100000000` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.capture_status import CaptureStatus
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.money import Money
from paypal.models.subscription_amount_with_breakdown import SubscriptionAmountWithBreakdown
from paypal.models.subscription_payer_name import SubscriptionPayerName
from paypal.models.subscription_transaction_details import SubscriptionTransactionDetails
from paypal.models.transactions_list import TransactionsList

transactions_list = TransactionsList(
    transactions=[
        SubscriptionTransactionDetails(
            id='id8',
            amount_with_breakdown=SubscriptionAmountWithBreakdown(
                gross_amount=Money(
                    currency_code='currency_code4',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                total_item_amount=Money(
                    currency_code='currency_code8',
                    value='value4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                fee_amount=Money(
                    currency_code='currency_code2',
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
                tax_amount=Money(
                    currency_code='currency_code2',
                    value='value8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                net_amount=Money(
                    currency_code='currency_code6',
                    value='value2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            time='time8',
            status=CaptureStatus.PARTIALLY_REFUNDED,
            payer_name=SubscriptionPayerName(
                prefix='prefix8',
                given_name='given_name2',
                surname='surname8',
                middle_name='middle_name0',
                suffix='suffix0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payer_email='payer_email6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SubscriptionTransactionDetails(
            id='id8',
            amount_with_breakdown=SubscriptionAmountWithBreakdown(
                gross_amount=Money(
                    currency_code='currency_code4',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                total_item_amount=Money(
                    currency_code='currency_code8',
                    value='value4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                fee_amount=Money(
                    currency_code='currency_code2',
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
                tax_amount=Money(
                    currency_code='currency_code2',
                    value='value8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                net_amount=Money(
                    currency_code='currency_code6',
                    value='value2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            time='time8',
            status=CaptureStatus.PARTIALLY_REFUNDED,
            payer_name=SubscriptionPayerName(
                prefix='prefix8',
                given_name='given_name2',
                surname='surname8',
                middle_name='middle_name0',
                suffix='suffix0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payer_email='payer_email6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    total_items=8,
    total_pages=44,
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

