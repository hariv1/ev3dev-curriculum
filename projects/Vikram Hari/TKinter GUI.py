
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import Mission_1
import Mission_2
import Mission_3

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

    frame_2 = ttk.Frame(new_game_window,padding=80)
    frame_2.grid()

    missions_label = tkinter.Label(frame_2, text="Missions\n", font=(
        "Helvetica", 24), fg='red')
    missions_label.grid(row=0, column=0)

    mission_1_button = tkinter.Button(frame_2, text="Mission 1\nFind "
                                                    "Controller")
    mission_1_button.grid(row=1, column=0, pady= 20)
    mission_1_button['command'] = mqtt_client.send_message()

    mission_2_button = tkinter.Button(frame_2, text="Mission 2\nDrive back "
                                                    "via Satellite")
    mission_2_button.grid(row=2, column=0, pady= 20)
    mission_2_button['command'] = lambda: Mission_2.main()

    mission_3_button = tkinter.Button(frame_2, text="Mission 3\nFood and "
                                                    "Water")
    mission_3_button.grid(row=3, column=0, pady= 20)
    mission_3_button['command'] = lambda: Mission_3.main()

    exit_game_button = ttk.Button(frame_2, text="End Game")
    exit_game_button.grid(row=4, column=0)
    exit_game_button['command'] = lambda: quit(mqtt_client, True)



def quit(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("\nNASA thanks you for your service!")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()




main()