import ev3dev.ev3 as ev3
import robot_controller as robo


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")

    print("--------------------------------------------")
    ev3.Sound.speak("Drive to the color").wait()
    print("Press Back to exit this program.")

    robot = robo.Snatch3r()

    ev3.Sound.speak("Seeking ")

    # DONE: 3. Implement the task as stated in this module's initial
    # comment block
    # It is recommended that you add to your Snatch3r class's constructor the color_sensor, as shown
    #   self.color_sensor = ev3.ColorSensor()
    #   assert self.color_sensor
    # Then here you can use a command like robot.color_sensor.color to check the value

    while True:

        if robot.color_sensor.color == 3:  # Green color = id: 3
            robot.stop()
            ev3.Sound.speak("Found ")
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