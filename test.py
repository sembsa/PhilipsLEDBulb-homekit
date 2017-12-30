import miio

led = miio.PhilipsBulb()

led.ip = "192.168.54.100"
too = "87a17187cd24121df6c90d77b7918044"
led.token = bytes(too, 'utf-8')

size = 16

arr = bytes(too, 'utf-8')

print(arr)

print(too)
print(led.token)

led.on()