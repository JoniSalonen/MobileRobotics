#!/usr/bin/env python3

## Joni Salonen D23125498
## Enrique Juan Gamboa D23125488
## Tauno Koivisto D23128855

import print as p
import motor
import touch
import light
import sonar
import gyroscope

def main():

    p.Print.print()
    touched1 = touch.TouchSensor.clear()
    if touched1 == 1:
        motor.Motors.drive(50)
        while(True):
            distance = sonar.SonarSensor.ultrasonicSensor()
            if(distance <= 25.0):
                motor.Motors.drive(0)
                break


    print("Ultrasound completed")

    gyroscope.gyroscope.calibrate()
    print("calibrating...")
    motor.Motors.motors_turn(180)
    print("Rotation 1 (180) completed")

    motor.Motors.drive_unit(20)
    print("Driving 20 units completed")
    gyroscope.gyroscope.calibrate()
    print("calibrating...")
    motor.Motors.motors_turn(-90)
    print("Rotation 2 (-90) completed")
    motor.Motors.drive(50)
    while(True):
        color = light.LightSensor.sensor()
        if(color == 1):
            motor.Motors.drive(0)
            break

    print("Black detected")

    motor.Motors.drive(0)
    print("Motors stopped")


    gyroscope.gyroscope.calibrate()
    print("calibrating...")
    motor.Motors.motors_turn(-90)
    print("Rotation 3 (-90) completed")

    motor.Motors.drive(-50)
    while(True):
        touched = touch.TouchSensor.is_pressed()
        if(touched == 1):
            motor.Motors.drive(0)
            break
    print("Reverse completed")



    motor.Motors.drive(0)
    print("Motors stopped")





if __name__ == '__main__':
    main()

