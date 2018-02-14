
import ev3dev.ev3 as ev3
import robot_controller as robo


def main():

    robot = robo.Snatch3r()

    plant_identification = robot.ColorSensor()

    if plant_identification:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Sound.speak("Plant Identified")

main()