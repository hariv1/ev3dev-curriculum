
import ev3dev.ev3 as ev3
import robot_controller as robo
import time


def main():
    robot = robo.Snatch3r()

    plant_search = robot.seek_beacon()

    if robot.ir_sensor.proximity < 10:
        ev3.Sound.beep()
        time.sleep(1.5)
    time.sleep(0.1)

    if plant_search:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Sound.speak("Plant Found")


main()