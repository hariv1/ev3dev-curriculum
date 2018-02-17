
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Wall-E Decisions")
    root.geometry('500x5'
                  '00')
    main_frame = ttk.Frame(root, padding=100)
    main_frame.grid()

    game_label = tkinter.Label(main_frame, text="Wall-E Robot\n\n\n", font=(
        "Helvetica", 30), fg='brown')
    game_label.grid(row=0, column=0)

    start_game_button = ttk.Button(main_frame, text="Decision Matrix")
    start_game_button.grid(row=3, column=0)
    start_game_button['command'] = lambda: main_menu(root)

    exit_game_button = ttk.Button(main_frame, text="Nevermind")
    exit_game_button.grid(row=4, column=0)
    exit_game_button['command'] = lambda: shutdown(mqtt_client, True)

    root.mainloop()


def main_menu(root):
    root.withdraw()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    window = tkinter.Toplevel()
    window.title("Wall-E Decisions")

    tab1 = ttk.Frame(window, padding=80)
    tab1.grid()

    title = tkinter.Label(tab1, text="Decisions\n", font=(
        "Rustic", 24), fg='brown')
    title.grid(row=0, column=0)

    find_plant_choice = tkinter.Button(tab1, text="Choice #1\nFind Plant")
    find_plant_choice.grid(row=1, column=0, pady=20)
    find_plant_choice['command'] = lambda: find_plant(window)


def shutdown(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("\nWall-E is going to sleep")
        mqtt_client.send_message("Sleeping...")
    mqtt_client.close()
    exit()


def find_plant(window):
    window.destroy()

    m1_window = tkinter.Toplevel()
    m1_window.title("Mission 1: Find Beacon using our Sensor")

    frame_m1 = ttk.Frame(m1_window, padding=80)
    frame_m1.grid()

    instructions_label = tkinter.Label(frame_m1, text="Run Mission_1_ev3 on "
                                                      "ev3 using SSH Session")
    instructions_label.grid(row=0, column=0)



main()
