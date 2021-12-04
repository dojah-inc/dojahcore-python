General
------------


#### dojah.general.resolve_nuban(account_number,bank_code)

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    nunban_details =  api.general.resolve_nuban('0444074143','063')

    print(nunban_details)
except Exception as e:
    print(str(e))

```

*Arguements*

- `account_number`: A valid NUBAN
- `bank_code`: A bank Code

*Returns*

```json

{
   "account_number":"4146507207",
   "account_name":"FEMI ADEWALE KOLAWOLE"
}
```

#### dojah.general.bank() - Get all banks and codes

*Usage*

```python

from dojahcore.dojah import Dojah

try:
    banks =  api.general.banks()

    print(banks)
except Exception as e:
    print(str(e))

```

*Arguements*



*Returns*

```json

[
   {
      "name":"First Bank of Nigeria",
      "code":"011",
      "longcode":"011151003",
      "gateway":"ibank",
      "slug":"first-bank-of-nigeria",
      "country":"Nigeria",
      "currency":"NGN"
   },
   ...
]
```

#### dojah.general.resolve_card_bin(card_bin) - Returns the details of a card

*Usage*

```python

from dojahcore.dojah import Dojah

api =  Dojah()

try:
    bin_details =  api.general.resolve_card_bin('506118')

    print(bin_details)
except Exception as e:
    print(str(e))

```

*Arguements*

- `card_bin`: First 6 digits of your card

*Returns*

```json

{
    "bin": "506118",
    "brand": "Verve",
    "sub_brand": "",
    "country_code": "NG",
    "country_name": "Nigeria",
    "card_type": "DEBIT",
    "bank": "Ecobank Nigeria"
  }
```


#### dojah.general.purchase_airtime(amount, destination) - Buy airtime across all mobile network

*Usage*

*Works only in production*

```python

from dojahcore.dojah import Dojah

try:
    airtime_details =  api.general.purchase_airtime('200','2348102152847')

    print(airtime_details)
except Exception as e:
    print(str(e))

```

*Arguements*

- `amount`: Amount of airtime
- `destination`: number(s) to receive the airtime

*Returns*

```json

{
    "status": "Sent",
    "mobile": "+2348102152847",
    "amount": "NGN 200.0000"
}
```

#### dojah.general.data_plans() - Get all network plans

*Usage*

```python

from dojahcore.dojah import Dojah

api =  Dojah()
try:
    data_plans =  api.general.data_plans()

    print(data_plans)
except Exception as e:
    print(str(e))

```

*Arguements*



*Returns*

```json

[
   {
      "amount":1000,
      "description":"9MOBILE 1.5GB data bundle",
      "plan": "9MOBILE_1.5GB"
   },
   ...
]
```


#### dojah.general.purchase_data(plan, destination) - Buy Data across all mobile network

*Usage*

*Works only in production*

```python

from dojahcore.dojah import Dojah
api =  Dojah()
try:
    data_details =  api.general.purchase_data('9MOBILE_1.5GB', '09069983293')

    print(data_details)
except Exception as e:
    print(str(e))

```

*Arguements*

- `plan`: Plan Type
- `destination`: number(s) to receive the data

*Returns*

```json

{
    "phone_number": "2348012345678",
    "amount": 200,
    "network": "MTN 200 MB DATA BUNDLE",
    "reference_id": "dj_e076726b-b136-4e18-b63d-3eabc77d56c1"
}
```

#### dojah.general.my_dojah_balance() - Returns your Dojah wallet balance

*Usage*


```python

from dojahcore.dojah import Dojah
api =  Dojah()
try:
    balance =  api.general.my_dojah_balance()

    print(balance)
except Exception as e:
    print(str(e))

```

*Arguements*


*Returns*

```json
{
   "wallet_balance":"500.00",
   "transferable_balance":"500.00"
}
```