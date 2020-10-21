import paho.mqtt.client as mqtt
import json

client_name = "Publisher"
topic = "mqtt/demo"
msg = {"temp":30, "hud":60, "pm1": 355, "pm2":50, "pm3":100}
# data = json.loads(msg)
data = json.dumps(msg)
client =mqtt.Client(client_name)
client.connect("mqtt.eclipse.org", 1883, 60)

client.publish(topic, data)