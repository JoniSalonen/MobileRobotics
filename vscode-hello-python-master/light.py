#!/usr/bin/env python3

#Import the necessary libraries
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

#Define the color sensor input
colorSensor = ColorSensor(INPUT_1)

#Define the light sensor class
class LightSensor():

    #Define the light sensor method and return the sensor value
    def sensor(self):
        sensorValue = ColorSensor.color
        print("color:", sensorValue)
        return sensorValue
