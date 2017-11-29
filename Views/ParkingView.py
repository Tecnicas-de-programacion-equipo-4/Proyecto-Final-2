from tkinter import Tk, N, S, E, W, Label, Button

class ParkingView(Tk):

    class Constants:
        title = "Control del estacionamiento"
        heigth = 300
        width = 300
        center = N + S + E + W
        event = "<Button-1>"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, parking_action=None):
        super().__init__()
        self.__parking_action = parking_action
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__configure_grid()

        self.__door_label = Label(self, text = "Estacionamiento", relief = "sunken")
        self.__door_label.grid(row=0, column=0, sticky=self.Constants.center)

        self.__open_door_button = Button(self)
        self.__open_door_button.configure(text="Abrir Estacionamiento")
        self.__open_door_button.grid(row=1, column=0, sticky=self.Constants.center)
        self.__open_door_button.bind(self.Constants.event, self.__did_tap_open)

        self.__close_door_button = Button(self)
        self.__close_door_button.configure(text="Cerrar Estacionamiento")
        self.__close_door_button.grid(row=2, column=0, sticky=self.Constants.center)
        self.__close_door_button.bind(self.Constants.event, self.__did_tap_close)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//4)
        self.grid_rowconfigure(2, weight=self.Constants.heigth//4)
        self.grid_columnconfigure(0, weight=self.Constants.width)

    def __did_tap_open(self, event):
        action = 'c'
        self.__parking_action(action)

    def __did_tap_close(self, event):
        action = 'd'
        self.__parking_action(action)
