from tkinter import Tk, N, S, E, W, Label, Button
from Views.ToogleDoorButton import ToogleDoorButton

class DoorView(Tk):

    class Constants:
        title = "Control de la puerta"
        heigth = 300
        width = 300
        center = N + S + E + W
        event = "<Button-1>"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, door_action=None):
        super().__init__()
        self.__door_action = door_action
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__configure_grid()

        self.__door_label = Label(self, text = "Puerta\nPrincipal", relief = "sunken")
        self.__door_label.grid(row=0, column=0, sticky=self.Constants.center)

        self.__open_door_button = Button(self)
        self.__open_door_button.configure(text="Abrir Puerta")
        self.__open_door_button.grid(row=1, column=0, sticky=self.Constants.center)
        self.__open_door_button.bind(self.Constants.event, self.__did_tap_open)

        self.__close_door_button = Button(self)
        self.__close_door_button.configure(text="Cerrar Puerta")
        self.__close_door_button.grid(row=2, column=0, sticky=self.Constants.center)
        self.__close_door_button.bind(self.Constants.event, self.__did_tap_close)

        #self.__door_toogle = ToogleDoorButton(self, door_action=door_tap_handler)
        #self.__door_toogle.grid(row=0, column=1, sticky=self.Constants.center)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//4)
        self.grid_rowconfigure(2, weight=self.Constants.heigth//4)
        self.grid_columnconfigure(0, weight=self.Constants.width)

    def __did_tap_open(self, event):
        action = 'a'
        self.__door_action(action)

    def __did_tap_close(self, event):
        action = 'b'
        self.__door_action(action)
