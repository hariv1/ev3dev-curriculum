import ev3dev.ev3 as ev3

left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
assert left_motor.connected

speed = 500


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")
    print(" Identify a Plant")
    print("--------------------------------------------")
    print("Press Back to exit this program.")

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


def identify_plant(button_state, robot):
    if button_state:
        ev3.Sound.speak("Identifying plant").wait()

        while True:
            while left_motor.run_forever(speed_sp=speed):
                if robot.color_sensor.color == "Green":
                    robot.stop()
                    ev3.Sound.speak("Identified plant").wait()
                    break
    else:
        robot.stop()


def handle_shutdown(button_state, dc):
    """Exit the program."""
    if button_state:
        dc.running = False
