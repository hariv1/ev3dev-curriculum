import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class MyDelegateOnPc(object):
    def __init__(self):
        self.running = True

    def button_press(self):
        """Method that creates a new Toplevel when up button is pressed on ev3"""
        button_press_window = tkinter.Toplevel()
        button_press_window.title("Beacon")

        frame = ttk.Frame(button_press_window, padding=80)
        frame.grid()

        label = ttk.Label(frame,
                          text="Congratulations. You have got the Holy "
                               "Beacon!")
        label.grid(row=0, column=0)


def main():
    my_pc_delegate = MyDelegateOnPc()
    mqtt_client = com.MqttClient(my_pc_delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Satellite Remote Drive")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)

    left_speed_entry = ttk.Entry(main_frame, width=10)
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)

    right_speed_entry = ttk.Entry(main_frame, width=10)
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: callback_forward(mqtt_client,
                                                         left_speed_entry,
                                                         right_speed_entry)
    root.bind('<Up>',
              lambda event: callback_forward(mqtt_client, left_speed_entry,
                                             right_speed_entry))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: callback_left(mqtt_client,
                                                   left_speed_entry,
                                                   right_speed_entry)
    root.bind('<Left>', lambda event: callback_left(mqtt_client,
                                                    left_speed_entry,
                                                    right_speed_entry))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: callback_right(mqtt_client,
                                                     left_speed_entry,
                                                     right_speed_entry)

    root.bind('<Right>',
              lambda event: callback_right(mqtt_client, left_speed_entry,
                                           right_speed_entry))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: callback_back(mqtt_client,
                                                   left_speed_entry,
                                                   right_speed_entry)
    root.bind('<Down>', lambda event: callback_back(mqtt_client,
                                                    left_speed_entry,
                                                    right_speed_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: callback_stop(mqtt_client)
    root.bind('<space>', lambda event: callback_stop(mqtt_client))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def callback_forward(mqtt_client, left_speed_entry, right_speed_entry):
    """Method that allows mqtt to call forward method on robot controller"""
    print("Forward")
    mqtt_client.send_message("forward", [int(left_speed_entry.get()),
                                         int(right_speed_entry.get())])


def callback_left(mqtt_client, left_speed_entry, right_speed_entry):
    """Method that allows mqtt to call left method on robot controller"""
    print("Left")
    mqtt_client.send_message("left", [int(left_speed_entry.get()),
                                      int(right_speed_entry.get())])


def callback_right(mqtt_client, left_speed_entry, right_speed_entry):
    """Method that allows mqtt to call right method on robot controller"""
    print("Right")
    mqtt_client.send_message("right", [int(left_speed_entry.get()),
                                       int(right_speed_entry.get())])


def callback_back(mqtt_client, left_speed_entry, right_speed_entry):
    """Method that allows mqtt to call back method on robot controller"""
    print("Back")
    mqtt_client.send_message("back", [int(left_speed_entry.get()),
                                      int(right_speed_entry.get())])


def callback_stop(mqtt_client):
    """Method that allows mqtt to call stop method on robot controller"""
    print("Stop")
    mqtt_client.send_message("stop")


def send_up(mqtt_client):
    """Method that allows mqtt to call send_up method on robot controller"""
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    """Method that allows mqtt to call send_down method on robot controller"""
    print("arm_down")
    mqtt_client.send_message("arm_down")


def quit_program(mqtt_client, shutdown_ev3):
    """Method that allows mqtt to call shutdown method on robot controller"""
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()
