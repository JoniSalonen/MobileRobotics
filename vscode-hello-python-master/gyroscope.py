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
    """
    A class representing a gyroscope.

    This class provides methods to calibrate and set the mode of the gyroscope.
    """

    def calibrate():
        """
        Calibrates the gyroscope.

        This function calibrates the gyroscope by calling the `calibrate()` method of the `gyro` object.
        It then sets the gyroscope mode to `MODE_GYRO_RATE` and `MODE_GYRO_ANG`.

        """
        gyro.calibrate()

        # Set the gyroscope mode to MODE_GYRO_RATE
        gyro.mode = gyro.MODE_GYRO_RATE

        # Set the gyroscope mode to MODE_GYRO_ANG
        gyro.mode = gyro.MODE_GYRO_ANG



