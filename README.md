# PhilipsLEDBulb-homekit
This is my first project in Python, it combines the Philips Xiaomi LED bulb with HomeKit.

Script created for [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt)

> Thank you author: [python-mirobo](https://github.com/rytilahti/python-mirobo)

This is a script that connects MQTT with python-mirobo

**Requirements:**

Python => 3.6


## Configuration:

* `pip install -r requirements.txt`
* Go to `/usr/local/lib/python3.6/site-packages/mirobo`
* In file: device.py
* Change class by typing IP locally and token

>Token you will find using [miio](https://github.com/aholstenson/miio)
Thanks guys

## Instruction:
* (Unpain if you have a pair with MiHome)
* Install miio
* Connect with philips-bulb ****
* Run miio --discover (you will get a token bulb, save it important)
* Find the section below and change it as below

```
Class device:
    Def __init __ (self, ip: str = None, token: str = None,
                 Start_id: int = 0, debug: int = 0) -> None:
        Self.ip = "IP BATTERIES LOCAL"
        Self.port = 54321
        If token is None:
            Token = 32 * '0'
        If token is not None:
            Self.token = bytes.fromhex ("TOKEN")
        Self.debug = debug
```

In the file philips.py set your MQTT topics and the address to my MQTT server is "homekit.local"

## Usage:
`python philips.py`

## Note

You can set the script to start with system startup.

### Stuff used to make this:

* [python-mirobo](https://github.com/rytilahti/python-mirobo) Connect to bulb with miprotoocol
* [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) HomeKit to MQTT
* [miio](https://github.com/aholstenson/miio) Find token

