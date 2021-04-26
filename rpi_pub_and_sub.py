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
x = 0
def led_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print(str(message.payload, "utf-8") + "\n")
    global x
    if message.payload.decode() == 'LED_ON':
        x = 1
    else:
        x = 0

def lcd_callback(client, userdata, message):
    setText_norefresh(message.payload.decode() + '     ')

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("horace/led")
    client.message_callback_add("horace/led", led_callback)
    client.subscribe("horace/lcd")
    client.message_callback_add("horace/lcd", lcd_callback)
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
    led = 4
    ult = 3
    grovepi.pinMode(led,"OUTPUT")
    button = 7
    grovepi.pinMode(button,"INPUT") 

    while True:
        if x == 1:
            grovepi.digitalWrite(led,1)
        if x == 0:
            grovepi.digitalWrite(led,0)
        client.publish("horace/ultrasonicRanger", grovepi.ultrasonicRead(ult))
        client.publish("horace/button",grovepi.digitalRead(button))

        time.sleep(1)

