import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import Mission_2


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Mars Rover")

    main_frame = ttk.Frame(root, padding=100)
    main_frame.grid()

    game_label = tkinter.Label(main_frame, text="Mars Rover\n\n\n", font=(
        "Helvetica", 24), fg='blue')
    game_label.grid(row=0, column=0)

    start_game_button = ttk.Button(main_frame, text="Start Game")
    start_game_button.grid(row=3, column=0)
    start_game_button['command'] = lambda: main_interface(root)

    exit_game_button = ttk.Button(main_frame, text="End Game")
    exit_game_button.grid(row=4, column=0)
    exit_game_button['command'] = lambda: quit(mqtt_client, True)

    root.mainloop()


def main_interface(root):
    root.withdraw()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    new_game_window = tkinter.Toplevel()
    new_game_window.title("Missions")

    frame_2 = ttk.Frame(new_game_window, padding=80)
    frame_2.grid()

    missions_label = tkinter.Label(frame_2, text="Missions\n", font=(
        "Helvetica", 24), fg='red')
    missions_label.grid(row=0, column=0)

    mission_1_button = tkinter.Button(frame_2, text="Mission 1\nFind "
                                                    "Beacon")
    mission_1_button.grid(row=1, column=0, pady=20)
    mission_1_button['command'] = lambda: callback_mission_1(new_game_window)

    mission_2_button = tkinter.Button(frame_2, text="Mission 2\nBring back "
                                                    "Beacon "
                                                    "via Sattelite")
    mission_2_button.grid(row=2, column=0, pady=20)
    mission_2_button['command'] = lambda: callback_mission_2(new_game_window)

    mission_3_button = tkinter.Button(frame_2, text="Mission 3\nFood and "
                                                    "Water")
    mission_3_button.grid(row=3, column=0, pady=20)
    mission_3_button['command'] = lambda: callback_mission_3(new_game_window)
    exit_game_button = ttk.Button(frame_2, text="End Game")
    exit_game_button.grid(row=4, column=0)
    exit_game_button['command'] = lambda: quit(mqtt_client, True)


def quit(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("\nNASA thanks you for your service!")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


def callback_mission_2(new_game_window):
    new_game_window.destroy()

    m2_window = tkinter.Toplevel()
    m2_window.title("Mission 2: Get Controller back via Remote Satellite")

    frame_m2 = ttk.Frame(m2_window, padding=80)
    frame_m2.grid()

    instructions_label = tkinter.Label(frame_m2, text="Run "
                                                      "Mission_2_ev3 on "
                                                      "ev3 using SSH Session")
    instructions_label.grid(row=0, column=0)

    request = tkinter.Label(frame_m2, text="Please enter speed "
                                           "for both "
                                           "motors, pick up beacon, "
                                           "and bring "
                                           "it back!!!\n")
    request.grid(row=1, column=0)

    done_button = ttk.Button(frame_m2, text="Press to go to Mission 3")
    done_button.grid(row=2, column=0)
    done_button['command'] = lambda: callback_mission_3(m2_window)

    Mission_2.main()


def callback_mission_1(new_game_window):
    new_game_window.destroy()

    m1_window = tkinter.Toplevel()
    m1_window.title("Mission 1: Find Beacon using our Sensor")

    frame_m1 = ttk.Frame(m1_window, padding=80)
    frame_m1.grid()

    instructions_label = tkinter.Label(frame_m1, text="Run Mission_1_ev3 on "
                                                      "ev3 using SSH Session")
    instructions_label.grid(row=0, column=0)

    done_button = ttk.Button(frame_m1, text="Press to go to Mission 2")

    done_button.grid(row=1, column=0)
    done_button['command'] = lambda: callback_mission_2(m1_window)


def callback_mission_3(m2_window):
    m2_window.destroy()

    m3_window = tkinter.Toplevel()
    m3_window.title("Mission 3: Use Beacon to search for food")

    frame_m3 = ttk.Frame(m3_window, padding=80)
    frame_m3.grid()

    instructions_label = tkinter.Label(frame_m3, text="Run Mission_3_ev3 "
                                                      "on SSH Terminal\n\nUse "
                                                      "Beacon to pick up and bring back food/water\n")
    instructions_label.grid(row=0, column=0)


main()
