#!/usr/bin/env python3

## Joni Salonen D23125498
## Enrique Juan Gamboa D23125488
## Tauno Koivisto D23128855

from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from os import system


touch = TouchSensor(INPUT_3)

class TouchSensor():
    """
    Represents a touch sensor.

    Methods:
    - clear(): Clears the screen when the touch sensor is pressed.
    - is_pressed(): Checks if the touch sensor is pressed.
    """

    def clear():
        while True:
            if touch.is_pressed:
                system('clear')
                break
        return 1

    def is_pressed():
        if touch.is_pressed:
            return 1
