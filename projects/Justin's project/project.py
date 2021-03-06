import robot_controller as robo
import ev3dev.ev3 as ev3
import tkinter
from tkinter import ttk
import math
import mqtt_remote_method_calls as com


class Drawer(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x = 0
        self.start_y = 0
        self.distance_list = []
        self.angle_list = []

    def draw_circle(self, color, x, y):
        # draw a small circle when mouse click the canvas
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color,
                                width=1)

    def set_point(self, x, y):
        # set event.x and event.y to be the start point
        self.start_x = x
        self.start_y = y

    def draw_line(self, color, x1, y1):
        # connect start point to the event point
        self.canvas.create_line(self.start_x, self.start_y, x1, y1, fill=color)

        # def path_data(self, x1, y1):
        #     angle = math.atan((x1 - self.start_x)/(y1 - self.start_y))
        #     distance = math.sqrt((x1 - self.start_x) ^ 2 + (y1 - self.start_y) ^ 2)


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
    drawer = Drawer(canvas)

    # make call back to add_path function
    canvas.bind("<ButtonPress-1>", lambda event: add_path(event, drawer))

    # close the canvas and the mqtt
    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=3, column=0)
    quit_button["command"] = lambda: end(mqtt_client)

    start_button = ttk.Button(main_frame, text="Start")
    start_button.grid(row=3, column=1)
    start_button["command"] = lambda: start_path(drawer, mqtt_client)

    # print_button = ttk.Button(main_frame, text="print")
    # print_button.grid(row=3, column=2)
    # print_button["command"] = lambda: print_list(drawer)

    window.mainloop()


def add_path(event, drawer):
    print("You clicked location ({},{})".format(event.x, event.y))
    my_color = "black"
    drawer.draw_circle(my_color, event.x, event.y)

    if drawer.start_x != 0:
        drawer.draw_line(my_color, event.x, event.y)

        # calculate the angel and distance robot need to run
        angle = math.atan2((event.x - drawer.start_x),
                           (drawer.start_y - event.y))
        # change angle from radius to degree
        angle_degree = math.degrees(angle)

        # If -180 < angel < -359 : new angel=360-angle
        # If 180 < angle < 359 : new angle=angle-360
        if math.fabs(angle_degree) > 180:
            if angle_degree < 0:
                angle_degree = 360 - angle_degree
            if angle_degree > 0:
                angle_degree = angle_degree - 360

        distance = math.sqrt(
            (event.x - drawer.start_x) ** 2 + (event.y - drawer.start_y) ** 2)
        # add angle and distance to the lists
        drawer.distance_list.append(distance)
        drawer.angle_list.append(angle_degree)

    drawer.set_point(event.x, event.y)


def start_path(drawer, mqtt_client):


    # correct the angle that need to turn
    angle_new_list = [drawer.angle_list[0]]
    for k in range(1, len(drawer.angle_list)):
        new_add = drawer.angle_list[k] - drawer.angle_list[k - 1]
        angle_new_list.append(new_add)


    # let the mqtt send message to ev3 for running
    mqtt_client.send_message("new_run_path", [angle_new_list, drawer.distance_list])


    # for k in range(len(drawer.distance_list)):
    #
    #     drawer.distance_list[k] *= (0.1 * scale_select)
    #     mqtt_client.send_message("turn_degrees", [angle_new_list[k], 900])
    #     mqtt_client.send_message("drive_inches_ir", [drawer.distance_list[k], 900])
    #     print(angle_new_list[k])


def end(mqtt_client):
    # end the program
    if mqtt_client:
        mqtt_client.close()
    exit()


main()
