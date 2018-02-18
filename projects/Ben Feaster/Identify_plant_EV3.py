import ev3dev.ev3 as ev3
import robot_controller as robo
import time


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")

    print("--------------------------------------------")
    ev3.Sound.speak("Identifying plant").wait()
    print("Press Back to exit this program.")

    robot = robo.Snatch3r()

    robot.arm_calibration()
    # DONE: 3. Implement the task as stated in this module's initial
    # comment block
    # It is recommended that you add to your Snatch3r class's constructor the color_sensor, as shown
    #   self.color_sensor = ev3.ColorSensor()
    #   assert self.color_sensor
    # Then here you can use a command like robot.color_sensor.color to check the value

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