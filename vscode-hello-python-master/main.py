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
    # Print module
    p.Print.print()

    # Check if touch sensor is pressed
    touched1 = touch.TouchSensor.clear()
    if touched1 == 1:
        motor.Motors.drive(50)
        while True:
            # Check ultrasonic sensor distance
            distance = sonar.SonarSensor.ultrasonicSensor()
            if distance <= 25.0:
                motor.Motors.drive(0)
                break

    print("Ultrasound completed")

    # Calibrate gyroscope
    gyroscope.gyroscope.calibrate()
    print("Calibrating...")

    # Turn motors 180 degrees
    motor.Motors.motors_turn(180)
    print("Rotation 1 (180) completed")

    # Drive motors forward for 20 units
    motor.Motors.drive_unit(20)
    print("Driving 20 units completed")

    # Calibrate gyroscope again
    gyroscope.gyroscope.calibrate()
    print("Calibrating...")

    # Turn motors -90 degrees
    motor.Motors.motors_turn(-90)
    print("Rotation 2 (-90) completed")

    # Drive motors forward until light sensor detects black color
    motor.Motors.drive(50)
    while True:
        color = light.LightSensor.sensor()
        if color == 1:
            motor.Motors.drive(0)
            break

    print("Black detected")

    # Stop motors
    motor.Motors.drive(0)
    print("Motors stopped")

    # Calibrate gyroscope again
    gyroscope.gyroscope.calibrate()
    print("Calibrating...")

    # Turn motors -90 degrees
    motor.Motors.motors_turn(-90)
    print("Rotation 3 (-90) completed")

    # Drive motors in reverse until touch sensor is pressed
    motor.Motors.drive(-50)
    while True:
        touched = touch.TouchSensor.is_pressed()
        if touched == 1:
            motor.Motors.drive(0)
            break

    print("Reverse completed")

    # Stop motors
    motor.Motors.drive(0)
    print("Motors stopped")

if __name__ == '__main__':
    main()
