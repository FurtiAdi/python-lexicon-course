import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.qos} {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

client.subscribe("sensor/temperature", 0)

client.loop_forever()

