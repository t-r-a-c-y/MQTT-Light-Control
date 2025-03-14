import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "/student_group/light_control"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    if message == "ON":
        print("💡 Light is TURNED ON")
    elif message == "OFF":
        print("💡 Light is TURNED OFF")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()
