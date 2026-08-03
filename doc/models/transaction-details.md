
# Transaction Details

The transaction details.

*This model accepts additional fields of type Any.*

## Structure

`TransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_info` | [`TransactionInformation`](../../doc/models/transaction-information.md) | Optional | The transaction information. |
| `payer_info` | [`PayerInformation`](../../doc/models/payer-information.md) | Optional | The payer information. |
| `shipping_info` | [`ShippingInformation`](../../doc/models/shipping-information.md) | Optional | The shipping information. |
| `cart_info` | [`CartInformation`](../../doc/models/cart-information.md) | Optional | The cart information. |
| `store_info` | [`StoreInformation`](../../doc/models/store-information.md) | Optional | The store information. |
| `auction_info` | [`AuctionInformation`](../../doc/models/auction-information.md) | Optional | The auction information. |
| `incentive_info` | [`IncentiveInformation`](../../doc/models/incentive-information.md) | Optional | The incentive details. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.cart_information import CartInformation
from paypal.models.item_details import ItemDetails
from paypal.models.pay_pal_reference_id_type import PayPalReferenceIdType
from paypal.models.payer_information import PayerInformation
from paypal.models.phone import Phone
from paypal.models.shipping_information import ShippingInformation
from paypal.models.simple_postal_address_coarse_grained import SimplePostalAddressCoarseGrained
from paypal.models.store_information import StoreInformation
from paypal.models.transaction_details import TransactionDetails
from paypal.models.transaction_information import TransactionInformation

transaction_details = TransactionDetails(
    transaction_info=TransactionInformation(
        paypal_account_id='paypal_account_id4',
        transaction_id='transaction_id0',
        paypal_reference_id='paypal_reference_id2',
        paypal_reference_id_type=PayPalReferenceIdType.ODR,
        transaction_event_code='transaction_event_code6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payer_info=PayerInformation(
        account_id='account_id2',
        email_address='email_address2',
        phone_number=Phone(
            country_code='country_code2',
            national_number='national_number6',
            extension_number='extension_number8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        address_status='address_status2',
        payer_status='payer_status2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    shipping_info=ShippingInformation(
        name='name0',
        method='method4',
        address=SimplePostalAddressCoarseGrained(
            line_1='line18',
            city='city6',
            country_code='country_code6',
            line_2='line20',
            state='state2',
            postal_code='postal_code8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        secondary_shipping_address=SimplePostalAddressCoarseGrained(
            line_1='line16',
            city='city4',
            country_code='country_code4',
            line_2='line28',
            state='state0',
            postal_code='postal_code6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cart_info=CartInformation(
        item_details=[
            ItemDetails(
                item_code='item_code0',
                item_name='item_name8',
                item_description='item_description4',
                item_options='item_options2',
                item_quantity='item_quantity2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ItemDetails(
                item_code='item_code0',
                item_name='item_name8',
                item_description='item_description4',
                item_options='item_options2',
                item_quantity='item_quantity2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        tax_inclusive=False,
        paypal_invoice_id='paypal_invoice_id6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    store_info=StoreInformation(
        store_id='store_id2',
        terminal_id='terminal_id6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

