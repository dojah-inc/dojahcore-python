Messaging
------------


#### dojah.messaging.register_sender_id(sender_id):

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    sender_id  = api.messaging.register_sender_id('Test')
    print(sender_id)
except Exception as e:
    print(str(e))

```

*Arguements*

- `sender_id`: The sender id to register

*Returns*

```json

{
   "message":""
}
```

#### dojah.messaging.fetch_sender_ids()

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    sender_ids  = api.messaging.fetch_sender_ids()
    print(sender_ids)
except Exception as e:
    print(str(e))

```

*Arguements*


*Returns*

```json

[
    {
        "sender_id":"",
        "activated": True,
        "createdAt": ""
    
    }
]
```

#### dojah.messaging.send_message(sender_id, channel, destination,message, priority=False) - Deliver Transaction message to customer

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    msg  = api.messaging.send_message("Test", "sms", "09099909878","message",True)
    print(msg)
except Exception as e:
    print(str(e))

```

*Arguements*
- `sender_id:`   Registered sender Id
- `channel`:     sms or whatsapp
- `destination`: Phone number of recipient
- `message`: Body of message
- `priority`:(optional) Indicates if you want to send in priority mode

*Returns*

```json
{
   "status":"Sent",
   "mobile":"2349099909878",
   "message_id":"dj_e59ceeb2-a880-4f14-8385-c4275a08b552",
   "reference_id":"5490f226-0bf6-4e4c-892a-b06c4d77b6a1"
}
```

#### dojah.messaging.get_status(message_id) - Get status of message

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    msg  = api.messaging.get_status("dj_e59ceeb2-a880-4f14-8385-c4275a08b552")
    print(msg)
except Exception as e:
    print(str(e))

```

*Arguements*
- `message_id:`   Message Id

*Returns*

```json
{
   "status":"Sent"
}
```

#### dojah.messaging.send_otp(sender_id,destination,channel,expiry=10,length=6, priority=False, otp=None) - Deliver OTPs to your users

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    otp  = api.messaging.send_otp("sender_id","destination","whatsapp",expiry=10,length=6, priority=False, otp=None)
    print(otp)
except Exception as e:
    print(str(e))

```

*Arguements*
- `sender_id:`   The sender Id to associate the message with
- `destination:` The receiver's phone number
- `channel`:  whatsapp, voice or sms
- `expiry` (optional ): Number of minutes before token expires
- `length` (optional): length of token, 4-6 characters, default is 6
- `priority` (optional): Indicate whether to send in priority mode
- `otp` (optional): The Otp

*Returns*

```json
[
   {
      "reference_id":"40a31bb4-20e8-45ad-b645-294b11dde250",
      "destination":"09069983293",
      "status_id":"dj_88cdabb2-98b8-4f6b-b3bf-2c9f84a0d7c6",
      "status":"voice OTP sent successfully "
   }
]
```

#### dojah.messaging.validate_otp(code, reference_id) - Validaes the token received by the user

*Usage*

```python

from dojahcore.dojah import Dojah

api = Dojah()
try:
    otp  = api.messaging.validate_otp('2345','40a31bb4-20e8-45ad-b645-294b11dde250')
    print(otp)
except Exception as e:
    print(str(e))

```

*Arguements*
- `code:`   The Otp code from the user
- `reference_id`: Refrerence Id
*Returns*

```json
{
   "valid":"True"
}
```