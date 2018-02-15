import ev3dev.ev3 as ev3
import robot_controller as robo


def main():
    robot = robo.Snatch3r()

    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

    found_the_beacon = robot.seek_beacon()

    if found_the_beacon:
        ev3.Sound.speak("Oh no, it seems like my autonomous driving "
                        "features do not work")
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)

        ev3.Sound.speak("Follow Mission 2 to drive me back via Satellite")

main()