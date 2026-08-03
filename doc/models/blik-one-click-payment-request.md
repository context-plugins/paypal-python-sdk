
# Blik One Click Payment Request

Information used to pay using BLIK one-click flow.

*This model accepts additional fields of type Any.*

## Structure

`BlikOneClickPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_code` | `str` | Optional | The 6-digit code used to authenticate a consumer within BLIK.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6`, *Pattern*: `^[0-9]{6}$` |
| `consumer_reference` | `str` | Required | The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and a merchant.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[ -~]{3,64}$` |
| `alias_label` | `str` | Optional | A bank defined identifier used as a display name to allow the payer to differentiate between multiple registered bank accounts.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `35`, *Pattern*: `^[ -~]{8,35}$` |
| `alias_key` | `str` | Optional | A Blik-defined identifier for a specific Blik-enabled bank account that is associated with a given merchant. Used only in conjunction with a Consumer Reference.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `19`, *Pattern*: `^[0-9]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.blik_one_click_payment_request import BlikOneClickPaymentRequest

blik_one_click_payment_request = BlikOneClickPaymentRequest(
    consumer_reference='consumer_reference6',
    auth_code='auth_code8',
    alias_label='alias_label2',
    alias_key='alias_key6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

