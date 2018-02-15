
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


def demo():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tk.Tk()
    root.title("ttk.Notebook")

    nb = ttk.Notebook(root)
    root.geometry('500x500')
    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page0 = ttk.Frame(nb)
    page1 = ttk.Frame(nb)
    page2 = ttk.Frame(nb)
    page3 = ttk.Frame(nb)

    nb.add(page0, text='Main Menu')
    find_plant_choice = tkinter.Button(page0, text="Choice #1\nFind Plant")
    find_plant_choice.grid(row=1, column=0, pady=100)
    find_plant_choice['command'] = lambda: find_plant(page0)

    exit_game_button = tkinter.Button(page0, text="Nevermind\n")
    exit_game_button.grid(row=1, column=1, pady=100)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)

    nb.add(page1, text='Find Plant')
    find_plant_choice = tkinter.Button(page1, text="Choice #1\nFind Plant")
    find_plant_choice.grid(row=1, column=0, pady=100)
    find_plant_choice['command'] = lambda: find_plant(page1)

    exit_game_button = tkinter.Button(page1, text="Nevermind\n")
    exit_game_button.grid(row=1, column=1, pady=100)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)

    nb.add(page2, text='Identify Plant')
    nb.add(page3, text='Transport Plant')

    nb.pack(expand=1, fill="both")

    root.mainloop()


def shutdown(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("\nWall-E is going to sleep")
        mqtt_client.send_message("Sleeping...")
    mqtt_client.close()
    exit()


def find_plant(window):
    m1_window = tkinter.Toplevel()
    m1_window.title("Mission 1: Find Beacon using our Sensor")

    frame_m1 = ttk.Frame(m1_window, padding=80)
    frame_m1.grid()

    instructions_label = tkinter.Label(frame_m1, text="Run Mission_1_ev3 on "
                                                      "ev3 using SSH Session")
    instructions_label.grid(row=0, column=0)


if __name__ == "__main__":
    demo()