#!/usr/bin/env python3
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from time import sleep


gyro = GyroSensor(INPUT_2)
gyro.calibrate()

gyro.mode = gyro.MODE_GYRO_RATE
sleep(1)
gyro.mode = gyro.MODE_GYRO_ANG

class gyroscope():
    
    def calibrate():
        gyro.calibrate()

        gyro.mode = gyro.MODE_GYRO_RATE
        sleep(1)
        gyro.mode = gyro.MODE_GYRO_ANG   


    def gyroscope():
         tangle = 90
         while True:
              sensorvalue = gyro.angle
              print(sensorvalue)
              sleep(1)

              if sensorvalue > tangle:
                   break