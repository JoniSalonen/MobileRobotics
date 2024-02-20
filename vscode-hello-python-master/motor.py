#!/usr/bin/env python3

import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from time import sleep

class Motors():

    def motors():
        motorA = LargeMotor(OUTPUT_A)
        motorB = LargeMotor(OUTPUT_D)
        touch = TouchSensor(INPUT_3)


        left_motor = motorA
        right_motor = motorB

        tank_dr = MoveTank(OUTPUT_A, OUTPUT_D)
        tank_dr.gyro = GyroSensor(INPUT_2)
        tank_dr.gyro.calibrate()



        tank_dr.gyro.mode = tank_dr.gyro.MODE_GYRO_RATE
        sleep(1)
        tank_dr.gyro.mode = tank_dr.gyro.MODE_GYRO_ANG
        sleep(1)

        touched = False
        timer = time.time_ns + 2 * 1000

        while True:
            tangle = tank_dr.gyro.angle - 90
            if touch.is_pressed:
                tangle -= 90
                print("OUCH!")
                tank_dr.on_for_rotations(-30, -30, 2)
                while tank_dr.gyro.angle > tangle:
                    tank_dr.on_for_degrees(30, -30, 5)
                    print("Gyro Angle:", tank_dr.gyro.angle, "\n Deg to target:", tank_dr.gyro.angle - tangle)
                    while tank_dr.gyro.angle < tangle:
                        tank_dr.on_for_degrees(-30, 30, 1)
                        print("Correcting...", "\n Deg to target:", tank_dr.gyro.angle - tangle)
            elif time.time_ns > timer:

                while tank_dr.gyro.angle > tangle:
                    tank_dr.on_for_degrees(30, -30, 5)
                    print("Gyro Angle:", tank_dr.gyro.angle, "\n Deg to target:", tank_dr.gyro.angle - tangle)
                    while tank_dr.gyro.angle < tangle:
                        tank_dr.on_for_degrees(-30, 30, 1)
                        print("Correcting...", "\n Deg to target:", tank_dr.gyro.angle - tangle)
                timer = time.time_ns + 2 * 1000

            tank_dr.on(30, 30)







