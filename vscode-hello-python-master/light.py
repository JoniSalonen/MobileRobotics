#!/usr/bin/env python3

#Import the necessary libraries
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
<<<<<<< HEAD
from time import sleep

#Define the color sensor input
colorSensor = ColorSensor(INPUT_1)
colorSensor.mode = 'COL-COLOR'
=======

#Define the color sensor input
colorSensor = ColorSensor(INPUT_1)
>>>>>>> adb36066e15306b6cda527b86e0fcce5c155b014

#Define the light sensor class
class LightSensor():

    #Define the light sensor method and return the sensor value
<<<<<<< HEAD
    def sensor():
        sensorValue = colorSensor.color
        print("color:", sensorValue)
        sleep(10)

       
=======
    def sensor(self):
        sensorValue = ColorSensor.color
        print("color:", sensorValue)
        return sensorValue
>>>>>>> adb36066e15306b6cda527b86e0fcce5c155b014
