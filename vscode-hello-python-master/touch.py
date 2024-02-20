#!/usr/bin/env python3

from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from os import system


touch = TouchSensor(INPUT_3)

class TouchSensor():
    
    def clear():
        while True:
            if touch.is_pressed:
                system('clear')
                break