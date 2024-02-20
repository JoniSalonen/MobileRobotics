#!/usr/bin/env python3

import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *


motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_D)
left_motor = motorA
right_motor = motorB

tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)
#tank_dr.gyro = GyroSensor()
#tank_dr.gyro.calibrate()

while True:
    tank_dr.on_for_degrees(30, -30, 180)

    tank_dr.on_for_rotations(30, 30, 3)



