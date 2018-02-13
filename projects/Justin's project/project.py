import robot_controller
import tkinter
from tkinter import ttk
import math
import mqtt_remote_method_calls as com


class MyDelegate(object):
    def __init__(self, canvas):
        self.canvas = canvas

    def on_circle_draw(self, color, x, y):
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color,
                                width=3)


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    # create a tkinter window
    window = tkinter.Tk()
    window.title = "EV3 controller"

    main_frame = ttk.Frame(window, padding=5)
    main_frame.grid()

    # set up the instruction and make a tkinter.Canvas
    instructions = "Click the window to make path for robot"
    label = ttk.Label(main_frame, text=instructions)
    label.grid(columnspan=2)
    canvas = tkinter.Canvas(main_frame, background="lightgray", width=1000,
                            height=600)
    canvas.grid(columnspan=2)

    canvas.bind("<Button-1>", lambda event: add_path(event, mqtt_client))


def add_path(event, mqtt_client):
    # click mouse to add point and connect each points to make path
    print("You clicked location ({},{})".format(event.x, event.y))
    my_color = "black"
    mqtt_client.send_message("on_circle_draw", [my_color, event.x, event.y])

def clear(canvas):
    # clear all the path
    canvas.delete("all")

# def start(convas):

def end(mqtt_client):
    # end the program
    if mqtt_client:
        mqtt_client.close()
    exit()


main()
