import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    ev3.Sound.speak("Finding Food").wait()

    robot = robo.Snatch3r()
    robot.pixy.mode = "SIG1"
    turn_speed = 100
    robot.arm_calibration()

    while not robot.touch_sensor.is_pressed:

        x = robot.pixy.value(1)
        height = robot.pixy.value(4)

        if x < 150:
            robot.left(turn_speed, turn_speed)

        elif x > 170:
            robot.right(turn_speed, turn_speed)

        elif x > 150 and x < 170:
            robot.forward(150, 150)
            if height > 73:
                robot.stop()
                robot.arm_up()
                time.sleep(1)
                robot.arm_down()
                break

        time.sleep(0.25)


main()