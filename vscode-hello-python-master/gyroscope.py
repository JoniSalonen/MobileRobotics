#!/usr/bin/env python3

## Joni Salonen D23125498
## Enrique Juan Gamboa D23125488
## Tauno Koivisto D23128855

from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from time import sleep


gyro = GyroSensor(INPUT_2)

gyro.mode = gyro.MODE_GYRO_RATE
gyro.mode = gyro.MODE_GYRO_ANG

class gyroscope():

    def calibrate():
        gyro.calibrate()

        gyro.mode = gyro.MODE_GYRO_RATE
        gyro.mode = gyro.MODE_GYRO_ANG



