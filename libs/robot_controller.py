"""
 v Library of EV3 robot functions that are useful in many different
 applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    # done: Implement the Snatch3r class as needed when working the sandox
    # exercises
    # (and delete these comments)

    def __init__(self):

        self.MAX_SPEED = 900
        self.running = True

        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.remote_contol = ev3.RemoteControl()
        self.color_sensor = ev3.ColorSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.pixy = ev3.Sensor(driver_name="pixy-lego")

        assert self.pixy.connected
        assert self.ir_sensor.connected
        assert self.color_sensor.connected
        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected
        assert self.touch_sensor.connected

    def drive_inches(self, inches_target, speed_deg_per_sec):
        """drive left and right motor, a given distance (inch), a given speed(
        degree per second, drive forward if the position is positive,
        backward if the position is negative)"""

        position = 90 * inches_target
        self.left_motor.run_to_rel_pos(position_sp=position,
                                       speed_sp=speed_deg_per_sec,
                                       stop_action='brake')
        self.right_motor.run_to_rel_pos(position_sp=position,
                                        speed_sp=speed_deg_per_sec,
                                        stop_action='brake')
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        """turn left and right motors a given number of degree and given
        speed(degree per second. If the degree_to_turn is positive,
        robot turn right. If degree_to_turn is negative, robot turn left)"""
        position = degrees_to_turn * 4
        if degrees_to_turn > 0:
            self.left_motor.run_to_rel_pos(position_sp=position,
                                           speed_sp=turn_speed_sp,
                                           stop_action='brake')
            self.right_motor.run_to_rel_pos(position_sp=-position,
                                            speed_sp=turn_speed_sp,
                                            stop_action='brake')
            self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        elif degrees_to_turn < 0:
            self.left_motor.run_to_rel_pos(position_sp=-position,
                                           speed_sp=turn_speed_sp,
                                           stop_action='brake')
            self.right_motor.run_to_rel_pos(position_sp=position,
                                            speed_sp=turn_speed_sp,
                                            stop_action='brake')
            self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

        ev3.Sound.beep().wait()

    def arm_calibration(self):
        """"(Raise the arm until it hit the touch sensor, then tern back to
        position 0)"""

        self.arm_motor.run_forever(speed_sp= self.MAX_SPEED)
        while True:
            if self.touch_sensor.is_pressed:
                break
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep()

        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(
            position_sp=-arm_revolutions_for_full_range,
            speed_sp=self.MAX_SPEED)
        self.arm_motor.wait_while(self.arm_motor.STATE_RUNNING)
        ev3.Sound.beep()

        self.arm_motor.position = 0

    def arm_up(self):
        """(Moves the  arm to the up position.)"""
        self.arm_motor.run_forever(speed_sp=self.MAX_SPEED)
        while True:
            if self.touch_sensor.is_pressed:
                break
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep()

    def arm_down(self):
        """(Moves the Snatch3r arm to the down position.)"""
        self.arm_motor.run_to_abs_pos(position_sp= 0, speed_sp=900)
        self.arm_motor.wait_while(self.arm_motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def red_up(self, bs):
        """(Moves the left motor of the robot forward)."""
        if bs:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            self.left_motor.run_forever(speed_sp=600)
        else:
            self.left_motor.stop()

    def red_down(self, bs):
        """(Moves the left motor of the robot backward)."""
        if bs:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
            self.left_motor.run_forever(speed_sp=-600)

        else:
            self.left_motor.stop()

    def blue_up(self, bs):
        """(Moves the right motor of the robot forward)."""
        if bs:
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
            self.right_motor.run_forever(speed_sp=600)
        else:
            self.right_motor.stop()

    def blue_down(self, bs):
        """(Moves the right motor of the robot backward)."""
        if bs:
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
            self.right_motor.run_forever(speed_sp=-600)
        else:
            self.right_motor.stop()

    def shutdown(self):
        """turn off the motors and leds"""

        self.running = False
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()

    def loop_forever(self):
        """robot run forever"""

        self.running = True
        while self.running:
            time.sleep(0.1)

    def forward(self, speed_left, speed_right):
        """robot run forward"""
        self.left_motor.run_forever(speed_sp=speed_left)
        self.right_motor.run_forever(speed_sp=speed_right)

    def left(self, speed_left, speed_right):
        """robot tern left"""
        self.left_motor.run_forever(speed_sp=-speed_left)
        self.right_motor.run_forever(speed_sp=speed_right)

    def right(self, speed_left, speed_right):
        """robot tern right"""
        self.left_motor.run_forever(speed_sp=speed_left)
        self.right_motor.run_forever(speed_sp=-speed_right)

    def back(self, speed_left, speed_right):
        """robot go back"""
        self.left_motor.run_forever(speed_sp=-speed_left)
        self.right_motor.run_forever(speed_sp=-speed_right)

    def stop(self):
        """robot (motors) stop"""
        self.left_motor.stop()
        self.right_motor.stop()

    def seek_beacon(self):
        """(Seeks beacon using IR sensor)."""

        my_becon_seeker = ev3.BeaconSeeker(channel=1)

        forward_speed = 300
        turn_speed = 100

        while not self.touch_sensor.is_pressed:

            current_heading = my_becon_seeker.heading
            current_distance = my_becon_seeker.distance
            if current_distance == -128:
                self.stop()
                print("IR Remote not found. Distance is -128. Turning in "
                      "attempt to find the beacon!")
                self.right(turn_speed, turn_speed)

            else:
                if math.fabs(current_heading) < 2:
                    print("On the right heading. Distance: ", current_distance)
                    if current_distance <= 2:
                        self.stop()
                        self.arm_up()
                        time.sleep(1)
                        self.arm_down()
                        time.sleep(1)
                        return True
                    elif current_distance > 5:
                        self.forward(forward_speed, forward_speed)

                elif math.fabs(current_heading) < 15 and math.fabs(
                        current_heading) > 2:

                    print("Adjusting heading")
                    if current_heading < 0:
                        self.right(turn_speed, turn_speed)

                    elif current_heading > 0:
                        self.left(turn_speed, turn_speed)

                elif math.fabs(current_heading) > 15:
                    self.stop()
                    print("Heading too far. Turning in attempt to find "
                          "beacon!")
                    self.right(turn_speed, turn_speed)

            time.sleep(0.2)

        print("Abandon ship!")
        self.stop()
        return False
