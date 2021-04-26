"""
Team Member: Horace Xu, Tianyi Yang

"""
"""EE 250L Final Project

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
import grovepi
from grove_rgb_lcd import *



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    
#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    light = 0
    ult = 3
    dht_sensor_port = 7
    sound_sensor = 1
    buzzer = 3
    grovepi.pinMode(buzzer, "OUTPUT")
    grovepi.digitalWrite(buzzer, 0)
    while True:
        li = grovepi.analogRead(light)
        client.publish("project/lightsensor", li)
        [ temp,hum ] = grovepi.dht(dht_sensor_port,0)
        sound_int=grovepi.analogRead(sound_sensor)
        client.publish("project/temperature", temp)
        client.publish("project/hum", hum)
        client.publish("project/sound", sound_int)
        print("temp =", temp, "C\thumidity =", hum,"%"," light = ",li, " sound = ",sound_int)
        if temp >=28: #supposed to be 65; just test here
            grovepi.digitalWrite(buzzer, 1)
            time.sleep(0.5)
            grovepi.digitalWrite(buzzer, 0)

        time.sleep(3)

