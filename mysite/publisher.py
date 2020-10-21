import paho.mqtt.client as mqtt

client_name = "Publisher"
topic = "mqtt/demo"
msg = "Hello"

client =mqtt.Client(client_name)
client.connect("mqtt.eclipse.org", 1883, 60)

client.publish(topic, msg)