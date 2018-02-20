import traceback
import ev3dev.ev3 as ev3
import time
import math
import robot_controller as robo



def main():

    print("--------------------------------------------")
    print(" Find Plant")
    print("--------------------------------------------")
    ev3.Sound.speak("Find Plant")
    forward_speed = 300
    robot = robo.Snatch3r()
    robot.arm_calibration()
    try:
        while True:
            seek_beacon(robot)
            robot.forward(forward_speed, forward_speed)
            time.sleep(3)
            robot.forward(0, 0)
            robot.arm_up()
            time.sleep(1)
            ev3.Sound.speak("Found plant")


            command = input("Hit enter to find another plant or enter x "
                            "to quit: ")
            if command == "x":
                break
    except:
        traceback.print_exc()
        ev3.Sound.speak("Error")

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


def seek_beacon(robot):
    """Robot uses the IR controller to seek it"""

    my_beacon_seeker = ev3.BeaconSeeker(channel=1)
    forward_speed = 300
    turn_speed = 100
    while not robot.touch_sensor.is_pressed:
        # The touch sensor can be used to abort the attempt (sometimes handy during testing)

        current_heading = my_beacon_seeker.heading  # use the beacon_seeker
        # heading
        current_distance = my_beacon_seeker.distance  # use the
        # beacon_seeker distance
        if current_distance == -128:
            # If the IR Remote is not found just sit idle for this program until it is moved.
            print("IR Remote not found. Distance is -128")
            time.sleep(0.1)
            robot.stop()
        else:
            # If the absolute value of the current_heading is less than 2, you are on the right heading.
            #     If the current_distance is 0 return from this function, you have found the beacon!  return True
            #     If the current_distance is greater than 0 drive straight forward (forward_speed, forward_speed)
            # If the absolute value of the current_heading is NOT less than 2 but IS less than 10, you need to spin
            #     If the current_heading is less than 0 turn left (-turn_speed, turn_speed)
            #     If the current_heading is greater than 0 turn right  (turn_speed, -turn_speed)
            # If the absolute value of current_heading is greater than 10, then stop and print Heading too far off
            #
            # Using that plan you should find the beacon if the beacon is in range.  If the beacon is not in range your
            # robot should just sit still until the beacon is placed into view.  It is recommended that you always print
            # something each pass through the loop to help you debug what is going on.  Examples:
            #    print("On the right heading. Distance: ", current_distance)
            #    print("Adjusting heading: ", current_heading)
            #    print("Heading is too far off to fix: ", current_heading)

            if math.fabs(current_heading) < 2:
                # Close enough of a heading to move forward
                print("On the right heading. Distance: ", current_distance)
                # You add more!
                if current_distance <= 2:

                    robot.stop()
                    print("Found plant!")
                    return True
                elif current_distance > 0:
                    robot.forward(forward_speed, forward_speed)

            elif math.fabs(current_heading) < 10 and math.fabs(
                    current_heading) > 0:

                print("Adjusting heading")
                if current_heading < 0:
                    robot.left(turn_speed, turn_speed)

                elif current_heading > 0:
                    robot.right(turn_speed, turn_speed)


            elif math.fabs(current_heading) > 10:
                robot.forward(forward_speed, forward_speed)
                time.sleep(1)
                robot.stop()
                print("out of reach")
                break

        time.sleep(0.2)

    # The touch_sensor was pressed to abort the attempt if this code runs.
    print("Abandon ship!")
    robot.stop()
    return False


main()
