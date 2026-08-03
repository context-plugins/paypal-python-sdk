
# Pay Pal Wallet Account Verification Status

The account status indicates whether the buyer has verified the financial details associated with their PayPal account.

*This model accepts additional fields of type Any.*

## Enumeration

`PayPalWalletAccountVerificationStatus`

## Fields

| Name | Description |
|  --- | --- |
| `VERIFIED` | The buyer has completed the verification of the financial details associated with this PayPal account. For example: confirming their bank account. |
| `UNVERIFIED` | The buyer has not completed the verification of the financial details associated with this PayPal account. For example: confirming their bank account. |

## Example

```python
from paypal.models.pay_pal_wallet_account_verification_status import PayPalWalletAccountVerificationStatus

pay_pal_wallet_account_verification_status = PayPalWalletAccountVerificationStatus.VERIFIED
```

