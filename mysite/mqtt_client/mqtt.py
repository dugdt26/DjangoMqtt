import paho.mqtt.client as mqtt
topic = "mqtt/demo"
def on_conect(client,userdata,flags, rc):
    client.subscribe(topic)

def on_messenge(client,userdata, msg):
    import json
    from.models import PostMqtt
    if(msg.topic == topic):
        print(msg.payload)
client =mqtt.Client("mqtt_demo")
client.on_connect = on_conect
client.on_message = on_messenge

client.connect("mqtt.eclipse.org", 1883, 60)


