
# Payment Collection

The collection of payments, or transactions, for a purchase unit in an order. For example, authorized payments, captured payments, and refunds.

*This model accepts additional fields of type Any.*

## Structure

`PaymentCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorizations` | [`List[AuthorizationWithAdditionalData]`](../../doc/models/authorization-with-additional-data.md) | Optional | An array of authorized payments for a purchase unit. A purchase unit can have zero or more authorized payments. |
| `captures` | [`List[OrdersCapture]`](../../doc/models/orders-capture.md) | Optional | An array of captured payments for a purchase unit. A purchase unit can have zero or more captured payments. |
| `refunds` | [`List[Refund]`](../../doc/models/refund.md) | Optional | An array of refunds for a purchase unit. A purchase unit can have zero or more refunds. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.authorization_incomplete_reason import AuthorizationIncompleteReason
from paypal.models.authorization_status import AuthorizationStatus
from paypal.models.authorization_status_details import AuthorizationStatusDetails
from paypal.models.authorization_with_additional_data import AuthorizationWithAdditionalData
from paypal.models.capture_incomplete_reason import CaptureIncompleteReason
from paypal.models.capture_status import CaptureStatus
from paypal.models.capture_status_details import CaptureStatusDetails
from paypal.models.money import Money
from paypal.models.orders_capture import OrdersCapture
from paypal.models.payment_collection import PaymentCollection
from paypal.models.refund import Refund
from paypal.models.refund_incomplete_reason import RefundIncompleteReason
from paypal.models.refund_status import RefundStatus
from paypal.models.refund_status_details import RefundStatusDetails

payment_collection = PaymentCollection(
    authorizations=[
        AuthorizationWithAdditionalData(
            status=AuthorizationStatus.DENIED,
            status_details=AuthorizationStatusDetails(
                reason=AuthorizationIncompleteReason.PENDING_REVIEW,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id2',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AuthorizationWithAdditionalData(
            status=AuthorizationStatus.DENIED,
            status_details=AuthorizationStatusDetails(
                reason=AuthorizationIncompleteReason.PENDING_REVIEW,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id2',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AuthorizationWithAdditionalData(
            status=AuthorizationStatus.DENIED,
            status_details=AuthorizationStatusDetails(
                reason=AuthorizationIncompleteReason.PENDING_REVIEW,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id2',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    captures=[
        OrdersCapture(
            status=CaptureStatus.REFUNDED,
            status_details=CaptureStatusDetails(
                reason=CaptureIncompleteReason.VERIFICATION_REQUIRED,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id4',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        OrdersCapture(
            status=CaptureStatus.REFUNDED,
            status_details=CaptureStatusDetails(
                reason=CaptureIncompleteReason.VERIFICATION_REQUIRED,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id4',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    refunds=[
        Refund(
            status=RefundStatus.CANCELLED,
            status_details=RefundStatusDetails(
                reason=RefundIncompleteReason.ECHECK,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id8',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Refund(
            status=RefundStatus.CANCELLED,
            status_details=RefundStatusDetails(
                reason=RefundIncompleteReason.ECHECK,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id8',
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            invoice_id='invoice_id8',
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

