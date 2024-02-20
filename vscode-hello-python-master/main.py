#!/usr/bin/env python3
import print
import motor
import touch
import light
import sonar
import gyroscope


def main():

    print.Print.print()
    touch.TouchSensor.clear()
    ##gyroscope.gyroscope.gyroscope()
    gyroscope.gyroscope.calibrate()
    ##sonar.SonarSensor.ultrasonicSensor()
    ##light.LightSensor.sensor()
    motor.Motors.motors()
 


if __name__ == '__main__':
    main()

