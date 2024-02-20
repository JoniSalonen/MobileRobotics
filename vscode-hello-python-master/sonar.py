#!/usr/bin/env python3

from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
from time import sleep


sonar = UltrasonicSensor(INPUT_4)
sonar.MODE_US_DIST_CM = 'US-DIST-CM'

class SonarSensor():


    def ultrasonicSensor():
        while True:
            sensorValue = sonar.distance_centimeters_continuous
            print(sensorValue)
            sleep(1)

            if sensorValue < 25.0:
                break




            