
import traceback

import ev3dev.ev3 as ev3
import time
import math

import robot_controller as robo


def main():
    print("\nBeacon the controller\n")
    ev3.Sound.speak("Find the controller or we can't get back home").wait()

    robot = robo.Snatch3r()

    while True:
        find_the_beacon = robot.seek_beacon()
        if find_the_beacon:
            ev3.Sound.speak("I got the beacon")
            robot.arm_up()
            time.sleep(1)
            robot.arm_down()

main()
