
# Vault Token Request

The Tokenized Payment Source representing a Request to Vault a Token.

*This model accepts additional fields of type Any.*

## Structure

`VaultTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The PayPal-generated ID for the token.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Za-z_-]+$` |
| `mtype` | [`VaultTokenRequestType`](../../doc/models/vault-token-request-type.md) | Required | The tokenization method that generated the ID.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_-]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.vault_token_request import VaultTokenRequest
from paypal.models.vault_token_request_type import VaultTokenRequestType

vault_token_request = VaultTokenRequest(
    id='id2',
    mtype=VaultTokenRequestType.SETUP_TOKEN,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

