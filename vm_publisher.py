"""
Team Member: Horace Xu, Tianyi Yang

"""
"""not use"""

import paho.mqtt.client as mqtt
import time
from pynput import keyboard
def custom_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print(str(message.payload, "utf-8") + "\n")


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    #client.subscribe("horace/defaultCallback")
    
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

    while True:


        time.sleep(10)
            

