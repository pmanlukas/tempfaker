#Temp Faker by Lukas Pollmann
##imports
import random
import time
from Adafruit_BME280 import *

#this is just a simple comment

#init sensor
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

##variables
inputTrue = True
shouldRun = False
#brokerAdress = "192.168.1.1"

##methods
#create a temperature
def createTempValue():
    temp = sensor.read_temperature()
    return temp

def createHumValue():
    hum = sensor.read_humidity()
    return hum

def createPressureValue():
    pressure = read_pressure()
    return pressure

#create client for MPTT

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
    temp = createTempValue()
    print(temp)
    hum = createHumValue()
    print(hum)
    pressure = createPressureValue
    print(pressure)

    #sleep 1 second
    time.sleep(1)

