import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.arm_calibration()
    btn = ev3.Button()
    btn.on_up = lambda: mqtt_client.send_message('button_press')
    robot.loop_forever()

main()