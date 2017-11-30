from tkinter import N, S, E, W, Label, Button, Frame
from CustomType.View import View

#Este archivo ya no se modifica.

class Entrance(Frame):
    class Constants:
        text_button_back = "Back to Home"
        heigth = 300
        width = 300
        center = N + S + E + W
        event = "<Button-1>"

    @classmethod
    def size(cls):
        return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, parent, change_view_handler=None, door_action=None):
        super().__init__(parent)

        self.__door_action = door_action
        self.__change_view_handler = change_view_handler

        self.__configure_grid()

        button1 = Button(self, text=self.Constants.text_button_back,
                         command=lambda: self.__did_tap_change_button(View.Main_View), font=("Comic Sans MS", 18))
        button1.grid(row = 3)

        self.__door_label = Label(self, text="Main\nDoor", relief="sunken",font=("Comic Sans MS", 40))
        self.__door_label.grid(row=0, column=0, sticky=self.Constants.center)

        self.__open_door_button = Button(self)
        self.__open_door_button.configure(text="Open", bg ="black", fg ="white", font=("Comic Sans MS", 22))
        self.__open_door_button.grid(row=1, column=0, sticky=self.Constants.center)
        self.__open_door_button.bind(self.Constants.event, self.__did_tap_open)

        self.__close_door_button = Button(self)
        self.__close_door_button.configure(text="Close", bg="red", fg= "white",font=("Comic Sans MS", 22))
        self.__close_door_button.grid(row=2, column=0, sticky=self.Constants.center)
        self.__close_door_button.bind(self.Constants.event, self.__did_tap_close)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth // 2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth // 4)
        self.grid_rowconfigure(2, weight=self.Constants.heigth // 4)
        self.grid_columnconfigure(0, weight=self.Constants.width)

    def __did_tap_open(self, event):
        action = 'a'
        self.__door_action(action)

    def __did_tap_close(self, event):
        action = 'b'
        self.__door_action(action)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False
