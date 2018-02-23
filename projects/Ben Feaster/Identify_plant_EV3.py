import ev3dev.ev3 as ev3
import robot_controller as robo
import time


class DataContainer(object):
    """ Helper class that might be useful to communicate between
    different callbacks."""

    def __init__(self):
        self.running = True


def main():
    """First, performs an arm calibration, then robot maintains a straight
    path unless it detects a human motion with the IR sensor or it detects
    a color with the color sensor. If the color
    sensor sees green, the robot will stop moving."""

    print("--------------------------------------------")
    print("------------Identify Plant------------------")
    print("--------------------------------------------")
    ev3.Sound.speak("Identifying plant").wait()
    print("Press Back to exit this program.")

    robot = robo.Snatch3r()
    robot.arm_calibration()

    while True:
        if robot.ir_sensor.proximity < 10:
            ev3.Sound.beep()
            robot.right(50, 50)  # swerves away from human
            time.sleep(2.0)
        if robot.color_sensor.color == 3:  # Green color = id: 3
            robot.stop()
            ev3.Sound.speak("Identified plant")
            break

        robot.forward(50, 50)


def handle_shutdown(button_state, dc):
    """Exit the program."""
    if button_state:
        dc.running = False


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()