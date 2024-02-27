#!/usr/bin/env python3

## Joni Salonen D23125498
## Enrique Juan Gamboa D23125488
## Tauno Koivisto D23128855

import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from time import sleep

class Motors():
    """
    This class represents the motors of a mobile robot.
    """

    def motors_turn(angle):
        """
        Turns the motors of the robot by a specified angle.

        Args:
            angle (int): The angle in degrees to turn the motors.
        """
        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)
        tank_dr.gyro = GyroSensor()
        tank_dr.gyro.calibrate()

        tank_dr.turn_degrees(50, angle)

    def drive(speed):
        """
        Drives the motors of the robot at a specified speed.

        Args:
            speed (int): The speed at which to drive the motors.
        """
        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)

        tank_dr.on(speed, speed)
        if speed == 0:
            tank_dr.stop()

    def drive_unit(unit):
        """
        Drives the motors of the robot for a specified unit.

        Args:
            unit (int): The number of units to drive the motors.
        """
        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)

        tank_dr.on_for_degrees(50, 50, unit * 90)











