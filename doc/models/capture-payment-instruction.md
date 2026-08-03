
# Capture Payment Instruction

Any additional payment instructions to be consider during payment processing. This processing instruction is applicable for Capturing an order or Authorizing an Order.

*This model accepts additional fields of type Any.*

## Structure

`CapturePaymentInstruction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `platform_fees` | [`List[PlatformFee]`](../../doc/models/platform-fee.md) | Optional | An array of platform or partner fees, commissions, or brokerage fees that associated with the captured payment.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `1` |
| `disbursement_mode` | [`DisbursementMode`](../../doc/models/disbursement-mode.md) | Optional | The funds that are held on behalf of the merchant.<br><br>**Default**: `"INSTANT"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16`, *Pattern*: `^[A-Z_]+$` |
| `payee_receivable_fx_rate_id` | `str` | Optional | FX identifier generated returned by PayPal to be used for payment processing in order to honor FX rate (for eligible integrations) to be used when amount is settled/received into the payee account.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `4000`, *Pattern*: `^.*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.capture_payment_instruction import CapturePaymentInstruction
from paypal.models.disbursement_mode import DisbursementMode
from paypal.models.money import Money
from paypal.models.payee_base import PayeeBase
from paypal.models.platform_fee import PlatformFee

capture_payment_instruction = CapturePaymentInstruction(
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
    payee_receivable_fx_rate_id='payee_receivable_fx_rate_id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

