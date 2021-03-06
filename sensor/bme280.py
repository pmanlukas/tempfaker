#Temp Faker by Lukas Pollmann
##imports

import time
import json
import paho.mqtt.client as mqtt
from Adafruit_BME280 import *

##init sensor
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

##variables
inputTrue = True
shouldRun = False
brokerAdress = "broker.hivemq.com"

##methods
#create a temperature
def createTempValue(temp):
    temp = sensor.read_temperature()
    return temp

#create client for MPTT
#callback function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(socket.gethostname(), 1883, 8000)
client.loop_start()

##program
#Loop for User input 
while inputTrue:
    x = input("Enter y to start: ")
    if x == "y" or x == "Y":
        shouldRun = True
        inputTrue = False
    else:
        print("Wrong input!")

temp = 20
while shouldRun:
    temp = createTempValue(temp)
    data = json.dumps({ "currentValue":temp }, separators=(',',':'))
    print(data)
    client.publish("forestfire/temp", data)
    time.sleep(5)

