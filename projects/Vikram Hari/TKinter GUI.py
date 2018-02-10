
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com

def main():

    root = tkinter.Tk()
    root.title("Mars Rover")

    main_frame = ttk.Frame(root, padding=200)
    main_frame.grid()

    game_label = ttk.Label(main_frame, text="Mars Rover", font=("Helvetica", 16))
    game_label.grid(row=0, column=0)

    start_game_button = ttk.Button(main_frame, text="Start Game")
    start_game_button.grid(row=1, column=0)

    exit_game_button = ttk.Button(main_frame, text="End Game")
    exit_game_button.grid(row=2, column=0)

    root.mainloop()


main()