
# Sepa Debit Experience Context 1

Customizes the payer experience during the approval process for the SEPA Debit payment.

*This model accepts additional fields of type Any.*

## Structure

`SepaDebitExperienceContext1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locale` | `str` | Optional | The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](https://developer.paypal.com/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/).<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `10`, *Pattern*: `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}\|[0-9]{3}))?$` |
| `return_url` | `str` | Required | Describes the URL. |
| `cancel_url` | `str` | Required | Describes the URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.sepa_debit_experience_context_1 import SepaDebitExperienceContext1

sepa_debit_experience_context_1 = SepaDebitExperienceContext1(
    return_url='return_url6',
    cancel_url='cancel_url8',
    locale='locale8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

