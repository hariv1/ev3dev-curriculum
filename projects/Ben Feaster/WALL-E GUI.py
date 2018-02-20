import tkinter as tk
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import Transport_plant


def demo():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tk.Tk()
    root.title("Wall-E GUI")
    root.configure(background="blue")

    nb = ttk.Notebook(root)
    root.geometry('500x300')
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
    find_plant_choice.grid(row=1, column=1, pady=10)
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
    find_plant_choice['command'] = lambda: transport_plant(page0)

    exit_game_button = tkinter.Button(page0, text="Exit Program   \n")
    exit_game_button.configure(background="grey")
    exit_game_button.grid(row=1, column=5, pady=0)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)

    nb.add(page1, text='Find Plant Info')
    game_label = tkinter.Label(page1, text="Robot first finds the IR "
                                           "remote\n which "
                                           "acts as a plant. Also "
                                           "swerves away from humans.\nRobot "
                                           "then "
                                           "picks up plant\n and says 'found "
                                           "plant'."
                                           "\n ", font=("Helvetica", 10),
                               fg='blue')
    game_label.grid(row=0, column=0)

    nb.add(page2, text='Identify Plant Info')
    game_label = tkinter.Label(page2, text="Robot uses the Pixie camera to\n "
                                           "identify a green 'plant' "
                                           "while turning\n to scan for "
                                           "plants. Says "
                                           "'found plant' after identified.\n",
                               font=(
                                   "Helvetica", 10), fg='brown')
    game_label.grid(row=0, column=0)

    nb.add(page3, text='Transport Plant Info')
    game_label = tkinter.Label(page3, text="Robot picks up the IR remote "
                                           "acting as a plant,\n "
                                           "it then lets the PC take \n"
                                           "control of Wall-E",
                               font=("Helvetica", 10), fg='brown')
    game_label.grid(row=0, column=0)
    nb.pack(expand=1, fill="both")

    root.mainloop()


def shutdown(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("\nWall-E is going to sleep")
        mqtt_client.send_message("Sleeping...")
    mqtt_client.close()
    exit()


def find_plant(page1):
    page1.grid_location(250, 250)
    find_plant_window = tkinter.Toplevel()
    find_plant_window.title("Decision 1: Tell Wall-E to find plant.")

    frame_find_plant = ttk.Frame(find_plant_window, padding=80)
    frame_find_plant.grid()

    text = tkinter.Label(frame_find_plant, text="Use SSH terminal to "
                                                "start please")
    text.grid(row=0, column=0)


def identify_plant(page2):
    page2.grid_location(250, 250)
    find_plant_window = tkinter.Toplevel()
    find_plant_window.title("Decision 2: Tell Wall-E to identify a plant.")

    frame_find_plant = ttk.Frame(find_plant_window, padding=80)
    frame_find_plant.grid()

    text = tkinter.Label(frame_find_plant, text="Use SSH terminal to "
                                                "start please")
    text.grid(row=0, column=0)


def transport_plant(page3):
    page3.grid_location(250, 250)
    find_plant_window = tkinter.Toplevel()
    find_plant_window.title("Decision 3: Take control of Wall-E.")

    frame_find_plant = ttk.Frame(find_plant_window, padding=80)
    frame_find_plant.grid()

    text = tkinter.Label(frame_find_plant, text="Use SSH terminal to "
                                                "start please")
    text.grid(row=0, column=0)
    Transport_plant.main()


if __name__ == "__main__":
    demo()
