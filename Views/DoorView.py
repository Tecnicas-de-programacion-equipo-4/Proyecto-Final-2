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