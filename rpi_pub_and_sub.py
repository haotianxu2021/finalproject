"""
Team Member: Horace Xu, Tianyi Yang
Repo link: https://github.com/usc-ee250-spring2021/lab05-horacexu/tree/lab5/ee250/lab05
ssh: git@github.com:usc-ee250-spring2021/lab05-horacexu.git
"""
"""EE 250L Lab 04 Starter Code

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
    
    ult = 3
    
    

    while True:
        
        aaa = grovepi.ultrasonicRead(ult)
        client.publish("horace/ultrasonicRanger", aaa)

        time.sleep(10)

