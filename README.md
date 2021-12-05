#dojahcore-python


Python plugin for [Dojah](https://dojah.io/) 


## Installation

```shell
pip install -i https://test.pypi.org/simple/ dojahcore
```
The dojah library reads the configuration keys from your .env file, ensure to add the following in your .env file


```shell
DOJAH_API_KEY = YOUR API KEY
DOJAH_APP_ID = YOUR APP ID
```
The app uses default test credentials if the following keys are not found

> Get your credentials from [dojah](https://dojah.io)

## Instantiate Dojah


```python
from dojahcore.dojah import Dojah


dojah_api = Dojah()

# to use the general class
dojah_api.general.data_plans()

# to use the financial class

dojah_api.financial.account_information(account_id)

# to use the identification class

dojah_api.identification.validate_bvn(bvn)

```

## Please reference the docs folder for other methods