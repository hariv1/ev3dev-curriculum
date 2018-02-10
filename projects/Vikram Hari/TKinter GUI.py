
import tkinter
import time
from tkinter import ttk
import mqtt_remote_method_calls as com

def main():

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Mars Rover")

    main_frame = ttk.Frame(root, padding=200)
    main_frame.grid()

    game_label = tkinter.Label(main_frame, text="Mars Rover", font=(
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

    new_game_window = tkinter.Toplevel()
    new_game_window.title("Missions")

    frame_2 = ttk.Frame(new_game_window,padding=200)
    frame_2.grid()

    mission_1_button = ttk.Button(frame_2, text="Mission 1:\nA New Era")
    mission_1_button.grid(row=0, column=0)
    mission_1_button['command'] = lambda:




def quit(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("\nNASA thanks you for your service!")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()














main()