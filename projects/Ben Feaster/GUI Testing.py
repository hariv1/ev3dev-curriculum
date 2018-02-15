
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
    root.configure(background="blue")

    nb = ttk.Notebook(root)
    root.geometry('500x500')
    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page0 = ttk.Frame(nb)
    page1 = ttk.Frame(nb)
    page2 = ttk.Frame(nb)
    page3 = ttk.Frame(nb)


    nb.add(page0, text='Main Menu')

    find_plant_choice = tkinter.Button(page0, text="Tell Wall-E\n to find "
                                                       "Plant")
    find_plant_choice.configure(background="grey")
    find_plant_choice.grid(row=1, column=1, pady=0)
    find_plant_choice['command'] = lambda: find_plant(page0)

    identify_plant_choice = tkinter.Button(page0, text="Tell Wall-E\n to "
                                                       "identify "
                                                       "Plant")
    identify_plant_choice.configure(background="grey")
    identify_plant_choice.grid(row=1, column=2, pady=0)
    identify_plant_choice['command'] = lambda: identify_plant(page0)

    find_plant_choice = tkinter.Button(page0, text="Tell Wall-E to\nTransport "
                                                   "Plant")
    find_plant_choice.configure(background="grey")
    find_plant_choice.grid(row=1, column=3, pady=0)
    find_plant_choice['command'] = lambda: find_plant(page0)

    find_plant_choice = tkinter.Button(page0, text="Control Wall-E "
                                                   "\nYourself")
    find_plant_choice.configure(background="grey")
    find_plant_choice.grid(row=1, column=4, pady=0)
    find_plant_choice['command'] = lambda: find_plant(page0)

    exit_game_button = tkinter.Button(page0, text="Exit Program   \n")
    exit_game_button.configure(background="grey")
    exit_game_button.grid(row=1, column=5, pady=0)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)



    nb.add(page1, text='Find Plant Info')
    find_plant_choice = tkinter.Button(page1, text="Choice #1\nFind Plant")
    find_plant_choice.grid(row=1, column=0, pady=0)
    find_plant_choice['command'] = lambda: find_plant(page1)

    exit_game_button = tkinter.Button(page1, text="Nevermind\n")
    exit_game_button.grid(row=1, column=1, pady=0)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)


    nb.add(page2, text='Identify Plant Info')
    identify_plant_choice = tkinter.Button(page2, text="Tell Wall-E\n to find "
                                                       "Plant")
    identify_plant_choice.grid(row=1, column=0, pady=0)
    identify_plant_choice['command'] = lambda: identify_plant(page2)

    exit_game_button = tkinter.Button(page2, text="Exit\n")
    exit_game_button.grid(row=1, column=1, pady=0)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)


    nb.add(page3, text='Transport Plant Info')

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


def identify_plant(window):
    print("Hello")


if __name__ == "__main__":
    demo()