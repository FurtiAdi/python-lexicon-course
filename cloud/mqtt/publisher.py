import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temperature = random.randint(20, 30)
    message = f"{temperature}°C"
    
    client.publish("sensor/temperature", message)
    print("Published:", message)

    time.sleep(2)