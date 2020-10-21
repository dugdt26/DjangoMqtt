import paho.mqtt.client as mqtt
#topic = "mqtt/demo"
topic = "ThuatDH/topic"


def on_conect(client, userdata, flags, rc):
    client.subscribe(topic)


def on_messenge(client, userdata, msg):
    import json
    from.models import PostMqtt
    if(msg.topic == topic):

        data = json .loads(msg.payload.decode("utf8"))
        tmp = PostMqtt.objects.create(
            # temp=data["temp"], hud=data["hud"], pm1=data["pm1"], pm2=data["pm2"], pm3=data["pm3"])
            temp=data["Env_temp"], hud=data["Env_humidity"], pm1=1, pm2=2, pm3=3)
        tmp.save()
       # print(msg.payload)


client = mqtt.Client()
client.on_connect = on_conect
client.on_message = on_messenge

client.connect("mqtt.eclipse.org", 1883, 60)
