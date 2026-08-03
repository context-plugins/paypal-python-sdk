
# Capture Request

Captures either a portion or the full authorized amount of an authorized payment.

*This model accepts additional fields of type Any.*

## Structure

`CaptureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `invoice_id` | `str` | Optional | The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.<br><br>**Constraints**: *Maximum Length*: `127` |
| `final_capture` | `bool` | Optional | Indicates whether you can make additional captures against the authorized payment. Set to `true` if you do not intend to capture additional payments against the authorization. Set to `false` if you intend to capture additional payments against the authorization.<br><br>**Default**: `False` |
| `payment_instruction` | [`CapturePaymentInstruction`](../../doc/models/capture-payment-instruction.md) | Optional | Any additional payment instructions to be consider during payment processing. This processing instruction is applicable for Capturing an order or Authorizing an Order. |
| `note_to_payer` | `str` | Optional | An informational note about this settlement. Appears in both the payer's transaction history and the emails that the payer receives.<br><br>**Constraints**: *Maximum Length*: `255` |
| `soft_descriptor` | `str` | Optional | The payment descriptor on the payer's account statement.<br><br>**Constraints**: *Maximum Length*: `22` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.capture_payment_instruction import CapturePaymentInstruction
from paypal.models.capture_request import CaptureRequest
from paypal.models.disbursement_mode import DisbursementMode
from paypal.models.money import Money
from paypal.models.payee_base import PayeeBase
from paypal.models.platform_fee import PlatformFee

capture_request = CaptureRequest(
    amount=Money(
        currency_code='currency_code6',
        value='value0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    invoice_id='invoice_id6',
    final_capture=False,
    payment_instruction=CapturePaymentInstruction(
        platform_fees=[
            PlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                payee=PayeeBase(
                    email_address='email_address4',
                    merchant_id='merchant_id6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                payee=PayeeBase(
                    email_address='email_address4',
                    merchant_id='merchant_id6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PlatformFee(
                amount=Money(
                    currency_code='currency_code6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                payee=PayeeBase(
                    email_address='email_address4',
                    merchant_id='merchant_id6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        disbursement_mode=DisbursementMode.INSTANT,
        payee_receivable_fx_rate_id='payee_receivable_fx_rate_id0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    note_to_payer='note_to_payer8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

