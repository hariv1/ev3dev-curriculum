
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


def main():

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title('Wall-E Menu')
    root.geometry('500x500')

    # Defines and places the tab widget
    nb = ttk.Notebook(main)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')


def main_menu():

    # Defines and places the tab widget
    nb = ttk.Notebook(main)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

    main_frame = ttk.Frame(root, padding=100)
    main_frame.grid()

    # Adds tab 1
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Find Plant')
    top = page1

    # Draws Wall-E picture to GUI
    filename = PhotoImage(file="C:\\Users\\feastebj\\Desktop\\walle1.png")
    background_label = Label(top, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Adds tab 2 of the notebook
    page2 = ttk.Frame(nb)
    nb.add(page2, text='Transport Plant')

    # Draws Wall-E picture to GUI
    filename = PhotoImage(file="C:\\Users\\feastebj\\Desktop\\walle1.png")
    background_label = Label(top, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Adds tab 3 of the notebook
    page3 = ttk.Frame(nb)
    nb.add(page3, text='Identify Plant')

    main.mainloop()