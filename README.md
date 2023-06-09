# ForgeData
A Python package for generating random dummy data for testing purposes.

Installation:
```bash
pip install forgedata
```

Data types supported as of `v1.0.1`:\
👉 [Name](#name)\
👉 [Email](#email)\
👉 [Password](#password)\
👉 [Website](#website)\
👉 [Phone](#phone)\
👉 [Country](#country)

### Name
```python
from forgedata import generator as ge
ge.name(type, quantity, gender='all')
```
| Parameter | Type | Description |
| :-- | :-- | :-- |
| type | **firstname** | To generate firstnames |
|| **lastname** | To generate lastnames |
|| **fullname** | To generate fullnames |
| quantity | **numeric value** | Quantity of results to be generated |
| gender | **male** | To generate male names |
|| **female** | To generate female names |
|| **all** (*Default*) | To generate a mix of both male and female names |

Output type: `Python list []`

### Email
```python
from forgedata import generator as ge
ge.email(quantity, domain=None)
```
| Parameter | Type | Description |
| :-- | :-- | :-- |
| quantity | **numeric value** | Quantity of results to be generated |
| domain | **None** (*Default*) | No specific domains, results can contain any random domains |
|| **common** | To generate email addresses using only gmail.com, yahoo.com, outlook.com, hotmail.com |
|| **[list]** | To generate email addresses using only the domains specified in the list |

Output type: `Python list []`

### Password
```python
from forgedata import generator as ge
ge.password(quantity, length, difficulty="hard")
```
| Parameter | Type | Description |
| :-- | :-- | :-- |
| quantity | **numeric value** | Quantity of results to be generated |
| length | **numeric value** | Length of password |
| difficulty | **easy** | Password comprises only of **letters(upper and lower)** |
|| **medium** | Password comprises only of **letters(upper and lower)** and **digits** |
|| **hard** (*Default*) | Password comprises only of **letters(upper and lower)**, **digits** and **special characters** |

Output type: \
Single Password - `Python string` \
Mutilple Passwords - `Python list []`

### Website
```python
from forgedata import generator as ge
ge.website(quantity, domain=None, www=False)
```
| Parameter | Type | Description |
| :-- | :-- | :-- |
| quantity | **numeric value** | Quantity of results to be generated |
|domain|**None** (*Default*)|Domains can be both common and uncommon ones.|
||**common**| Only return common domain names|
|www|**False** (*Default*)|Donot prefix `www.` to the domains|
||**True**|Prefix `www.` to the domains|

Output type: `Python list []`

### Phone
```python
from forgedata import generator as ge
ge.phone(quantity)
```
| Parameter | Type | Description |
| :-- | :-- | :-- |
| quantity | **numeric value** | Quantity of results to be generated |

Output type: `Python list []`

### Country
```python
from forgedata import generator as ge
ge.country(quantity, countrycode=False)
```
| Parameter | Type | Description |
| :-- | :-- | :-- |
| quantity | **all** (*Default*) | Returns list of all countries |
|| **numeric value** | Quantity of results to be generated |
|countrycode|**False** (*Default*)|Donot provide country code along with name|
||**True**|Provide country code along with name|

Output type: `Python list []`