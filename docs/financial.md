Financial
-----------
This service works with the Financial Widget from https://dojah.io

#### financial.account_information(account_id) -  Retrieves the bank account information of a customer.

*Usage*

```python
from dojahcore.dojah import Dojah

api = Dojah()
try:

    financial = api.financial.account_information(account_id)
    print(financial)
except Exception as e:
    print(str(e))
```

*Arguments*

 - `account_id` The account Id returned by the widget from the financial widget

 *Returns*

 ```json
{
  "name": "BENJAMIN, RAMON ABDUL",
  "account_number": "015***7834",
  "account_bvn_last_four": "5556",
  "account_type": "GT Crea8-e-savers",
  "currency": "Naira",
  "account_status": "Active",
  "balance": "34,976.80"
}

 ```
