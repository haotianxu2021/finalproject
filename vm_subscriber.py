"""
Team Member: Horace Xu, Tianyi Yang

"""
"""EE 250L final project

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
import requests
def temp_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    temps = message.payload.decode()
    s = requests.get('https://dweet.io/dweet/for/mytestf?temp='+temps)
    

def li_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    lights = message.payload.decode()
    s = requests.get('https://dweet.io/dweet/for/lightfinal?light='+lights)
    
def sound_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message   
    sound = message.payload.decode()
    s = requests.get('https://dweet.io/dweet/for/soundfinal?sounds='+sound)

def hum_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message   
    hums = message.payload.decode()
    s = requests.get('https://dweet.io/dweet/for/humilfinal?hum='+hums)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("project/temperature")
    client.message_callback_add("project/temperature", temp_callback)
    client.subscribe("project/lightsensor")
    client.message_callback_add("project/lightsensor", li_callback)
    client.subscribe("project/sound")
    client.message_callback_add("project/sound", sound_callback)
    client.subscribe("project/hum")
    client.message_callback_add("project/hum", hum_callback)
    
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
        
        time.sleep(1)
            

