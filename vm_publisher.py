"""
Team Member: Horace Xu, Tianyi Yang
Repo link: https://github.com/usc-ee250-spring2021/lab05-horacexu/tree/lab5/ee250/lab05
ssh: git@github.com:usc-ee250-spring2021/lab05-horacexu.git
"""
"""EE 250L Lab 04 Starter Code

Run vm_publisher.py in a separate terminal on your VM."""

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
    client.subscribe("horace/lcd")
    client.message_callback_add("horace/lcd", custom_callback)
    client.subscribe("horace/led")
    client.message_callback_add("horace/led", custom_callback)
#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    
    if k == 'w':
        print("w")
        #send "w" character to rpi
        client.publish("horace/lcd", "w")
    elif k == 'a':
        print("a")
        # send "a" character to rpi
        client.publish("horace/lcd", "a")
        #send "LED_ON"
        client.publish("horace/led", "LED_ON")
    elif k == 's':
        print("s")
        client.publish("horace/lcd", "s")
        # send "s" character to rpi
    elif k == 'd':
        print("d")
        # send "d" character to rpi
        client.publish("horace/lcd", "d")
        # send "LED_OFF"
        client.publish("horace/led", "LED_OFF")

if __name__ == '__main__':
    #setup the keyboard event listener
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread

    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        on_press(input())


        time.sleep(1)
            

