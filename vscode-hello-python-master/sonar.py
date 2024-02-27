#!/usr/bin/env python3

## Joni Salonen D23125498
## Enrique Juan Gamboa D23125488
## Tauno Koivisto D23128855

from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
from time import sleep


sonar = UltrasonicSensor(INPUT_4)
sonar.MODE_US_DIST_CM = 'US-DIST-CM'

class SonarSensor():
    """
    Represents a Sonar Sensor used for measuring distances.
    """

    def ultrasonicSensor():
        """
        Returns the distance measured by the ultrasonic sensor in centimeters.
        """
        sensorValue = sonar.distance_centimeters_continuous
        return sensorValue





