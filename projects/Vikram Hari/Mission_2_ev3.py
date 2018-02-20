import mqtt_remote_method_calls as com
import robot_controller as robo
import time


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.arm_calibration()
    btn = robot.btn
    btn.on_up = lambda state: callback_button_press(state, mqtt_client)

    while True:
        btn.process()
        time.sleep(0.01)


def callback_button_press(button_state, mqtt_client):
    print('a')
    if button_state:
        mqtt_client.send_message('button_press')
        print('b')


main()
