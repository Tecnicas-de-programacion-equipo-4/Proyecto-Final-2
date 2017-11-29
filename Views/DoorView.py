from tkinter import Tk, N, S, E, W, Label
#from Views.ToggleDoorButton import ToggleDoorButton
class DoorView(Tk):

    class Constants:
        title = "Control de la puerta"
        heigth = 300
        width = 300
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__configure_grid()

        self.__door_label = Label(self, text = "Puerta\nPrincipal")
        self.__door_label.grid(row=0, column=0, sticky=self.Constants.center)



    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        self.grid_columnconfigure(0, weight=self.Constants.width)