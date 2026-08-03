
# Vault Token Request 1

The Tokenized Payment Source representing a Request to Vault a Token.

*This model accepts additional fields of type Any.*

## Structure

`VaultTokenRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The PayPal-generated ID for the token.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Za-z_-]+$` |
| `mtype` | `str` | Required, Constant | The tokenization method that generated the ID.<br><br>**Value**: `"SETUP_TOKEN"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.vault_token_request_1 import VaultTokenRequest1

vault_token_request_1 = VaultTokenRequest1(
    id='id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

