"""
Team Member: Horace Xu, Tianyi Yang
Repo link: https://github.com/usc-ee250-spring2021/lab05-horacexu/tree/lab5/ee250/lab05
ssh: git@github.com:usc-ee250-spring2021/lab05-horacexu.git
"""
"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
def ul_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    
    print('VM: {}cm'.format(message.payload.decode()))

def button_callback(client, userdata, message):
    if message.payload.decode() == '1':
        print('Button pressed!')

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("horace/ultrasonicRanger")
    client.message_callback_add("horace/ultrasonicRanger", ul_callback)
    client.subscribe("horace/button")
    client.message_callback_add("horace/button", button_callback)
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
            

