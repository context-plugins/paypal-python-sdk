
# Vault Token Request Type

The tokenization method that generated the ID.

*This model accepts additional fields of type Any.*

## Enumeration

`VaultTokenRequestType`

## Fields

| Name | Description |
|  --- | --- |
| `SETUP_TOKEN` | The setup token, which is a temporary reference to payment source. |

## Example

```python
from paypal.models.vault_token_request_type import VaultTokenRequestType

vault_token_request_type = VaultTokenRequestType.SETUP_TOKEN
```

