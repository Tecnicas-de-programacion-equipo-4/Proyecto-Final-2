from tkinter import N, S, E, W, Label, Button, Frame
from CustomType.View import View

#Este archivo ya no se modifica.

class Parking(Frame):
    class Constants:
        title = "Control del estacionamiento"
        text_button_back = "Back to Home"
        center = N + S + E + W
        event = "<Button-1>"
        heigth = 300
        width = 300

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, parent, change_view_handler=None, parking_action=None):
        super().__init__(parent)


        self.__change_view_handler = change_view_handler

        button1 = Button(self, text=self.Constants.text_button_back,
                         command=lambda: self.__did_tap_change_button(View.Main_View,),font=("Comic Sans MS", 18))
        button1.grid(row = 3)

        self.__parking_action = parking_action
        self.__configure_grid()

        self.__door_label = Label(self, text="Parking", relief="sunken",font=("Comic Sans MS", 40))
        self.__door_label.grid(row=0, column=0, sticky=self.Constants.center)

        self.__open_door_button = Button(self, font=("Comic Sans MS", 22), bg = "black", fg ="white")
        self.__open_door_button.configure(text="Open")
        self.__open_door_button.grid(row=1, column=0, sticky=self.Constants.center)
        self.__open_door_button.bind(self.Constants.event, self.__did_tap_open)

        self.__close_door_button = Button(self,font=("Comic Sans MS", 22), bg = "red", fg = "white")
        self.__close_door_button.configure(text="Close")
        self.__close_door_button.grid(row=2, column=0, sticky=self.Constants.center)
        self.__close_door_button.bind(self.Constants.event, self.__did_tap_close)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth // 2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth // 4)
        self.grid_rowconfigure(2, weight=self.Constants.heigth // 4)
        self.grid_columnconfigure(0, weight=self.Constants.width)

    def __did_tap_open(self, event):
        action = 'c'
        self.__parking_action(action)

    def __did_tap_close(self, event):
        action = 'd'
        self.__parking_action(action)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False
