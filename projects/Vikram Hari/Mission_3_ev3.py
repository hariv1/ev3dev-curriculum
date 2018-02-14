import ev3dev.ev3 as ev3
import time

import robot_controller as robo


class DataContainer(object):
    def __init__(self):
        self.running = True


def main():

    robot = robo.Snatch3r()
    dc = DataContainer()

    btn = ev3.Button()
    btn.on_backspace = lambda state: handle_shutdown(state, dc)

    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    assert left_motor.connected
    assert right_motor.connected

    rc1 = ev3.RemoteControl(channel=1)
    rc1.on_red_up = lambda button_state: robot.red_up(button_state)
    rc1.on_red_down = lambda button_state: robot.red_down(button_state)
    rc1.on_blue_up = lambda button_state: robot.blue_up(button_state)
    rc1.on_blue_down = lambda button_state: robot.blue_down(button_state)


    rc2 = ev3.RemoteControl(channel=2)
    rc2.on_red_up = lambda button_state: handle_arm_up_button(button_state, robot)
    rc2.on_red_down = lambda button_state: handle_arm_down_button(button_state, robot)
    rc2.on_blue_up = lambda button_state: handle_calibrate_button(button_state, robot)


    btn.on_backspace = lambda button_state: handle_shutdown(button_state, dc, robot)



    while dc.running:
        rc1.process()
        rc2.process()
        btn.process()
        time.sleep(0.01)

    robot.shutdown()



def handle_arm_up_button(button_state, robot):
    if button_state:
        robot.arm_up()


def handle_arm_down_button(button_state, robot):
    if button_state:
        robot.arm_down()


def handle_calibrate_button(button_state, robot):
    if button_state:
        robot.arm_calibration()


def handle_shutdown(button_state, dc, robot):
    if button_state:
        dc.running = False

    time.sleep(0.01)
    robot.shutdown()


main()
