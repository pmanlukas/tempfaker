#TODO: reimplement the code as objects
import time
import json
import paho.mqtt.client as mqtt


#class that implements a fake sensor, that can deliver various temp data
class sensor():

    def __init__(self):
        self. interval = 0.1
        self.isMetric = True
        
    def get_temp():
        print("2000 Grad Celsius")
    def get_pressure():
        print(str(10))
    def set_interval(interval):
    
    def set_format(isMetric):

#class that implements a mqtt client, to send the sensor data
class mqtt_client():