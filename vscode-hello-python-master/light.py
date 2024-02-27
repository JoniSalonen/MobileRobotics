#!/usr/bin/env python3

## Joni Salonen D23125498
## Enrique Juan Gamboa D23125488
## Tauno Koivisto D23128855

#Import the necessary libraries
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from time import sleep

#Define the color sensor input
colorSensor = ColorSensor(INPUT_1)
colorSensor.mode = 'COL-COLOR'

#Define the light sensor class
class LightSensor():

    def sensor():
        sensorValue = colorSensor.color
        print("color:", sensorValue)
        return sensorValue

