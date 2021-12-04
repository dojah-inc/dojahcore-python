Financial
-----------

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

 - `The account Id returned by the widget from the financial widget`

 *Returns*
 
