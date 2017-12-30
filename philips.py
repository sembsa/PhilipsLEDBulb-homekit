import mirobo
import paho.mqtt.client as mqtt

print("Skrypt sterowania Philips Xiaomi LED Bulb")

# Inicjacja zarowki z biblioteki mirobo
led = mirobo.Ceil()

# Set MQTT Topic
setOnMQTT = "/home/setOn"
statusOnMQTT = "/home/statusOn"
setBrightnessMQTT = "/home/setB"
statusBrightness = "/home/statusB"
setColorTemperatureMQTT = "/home/setColor"
statusColorTemperature = "/home/statusColorTemperature"

# Metody Paho-MQTT

# Gdy polaczony
def on_connect(client, userdata, flasgs, rc):
    print("Connect with result code: " + str(rc))

    client.subscribe(setOnMQTT)
    client.subscribe(setBrightnessMQTT)
    client.subscribe(setColorTemperatureMQTT)


# Gdy odbiera wiadomosc
def on_message(client, userdata, message):
    if message.topic == setOnMQTT:
        on = bool(int(message.payload))
        if on == True:
            setPowerOn(True)
        else:
            setPowerOn(False)
    if message.topic == setBrightnessMQTT:
        setBrightness(int(message.payload))
    if message.topic == setColorTemperatureMQTT:
        print(int(message.payload))
        setColorTemperature(int(message.payload))

# -------------------------
# Metody sterowania zarowka
def setPowerOn(on):
    if on == True:
        print("<INFO> Philips Xiaomi LED Bulb ON: True")

        try:
            led.on()
        except mirobo.device.DeviceException:
            print("<ERROR> Nie odnaleziono zarowki")
            client.publish(statusOnMQTT, 0)
        else:
            client.publish(statusOnMQTT, 1)
    else:
        print("<INFO> Philips Xiaomi LED Bulb ON: False")
        try:
            led.off()
        except mirobo.device.DeviceException:
            print("<ERROR> Nie odnaleziono zarowki")
            client.publish(statusOnMQTT, 1)
        else:
            client.publish(statusOnMQTT, 0)

def setBrightness(value):
    print("<INFO> Philips Xiaomi LED Bulb Brightness: " + str(value))
    try:
        led.set_bright(value)
    except mirobo.device.DeviceException:
        print("<ERROR> Nie odnaleziono zarowki")
        client.publish(statusOnMQTT, 0)
    else:
        client.publish(statusBrightness, value)

def setColorTemperature(value):
    print("<INFO> Philips Xiaomi LED CCT: " + str(value))
    try:
        led.set_cct(calculateColorTemperature(value, 140, 500, 100, 1))
    except mirobo.device.DeviceException:
        print("<ERROR> Nie odnaleziono zarowki")
        client.publish(statusOnMQTT, 0)
    else:
        client.publish(statusColorTemperature, value)

# Metoda obliczania map
def calculateColorTemperature(x, in_min, in_max, out_min, out_max):
    result = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return result

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("homekit.local", 1883, 60)

client.loop_forever()
