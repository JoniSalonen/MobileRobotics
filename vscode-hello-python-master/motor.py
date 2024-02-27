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


    def motors_turn(angle):
        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)
        tank_dr.gyro = GyroSensor()
        tank_dr.gyro.calibrate()

        tank_dr.turn_degrees(50, angle)
        # while True:


        #     tank_dr.on_for_rotations(30, 30, 3)

    def drive(speed):
        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)

        tank_dr.on(speed,speed)
        if(speed == 0):
            tank_dr.stop()

    def drive_unit(unit):
        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)

        tank_dr.on_for_degrees(50, 50, unit * 90)











