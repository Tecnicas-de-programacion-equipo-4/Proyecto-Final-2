from tkinter import Tk, N, S, E, W, Label
from Views.ToggleButton import ToggleButton
from Views.KeypadView import KeypadView
class MainView(Tk):
    class Constants:
        title = "Casa Inteligente"
        heigth = 300
        width = 375
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, toogle_handler = None, tap_handler = None):
        super().__init__()
        self.__toogle_handler = toogle_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())



        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        self.grid_columnconfigure(0, weight=self.Constants.width//5)
        self.grid_columnconfigure(1, weight=self.Constants.width//5)
        self.grid_columnconfigure(2, weight=self.Constants.width//5)
        self.grid_columnconfigure(3, weight=self.Constants.width//5)
        self.grid_columnconfigure(4, weight=self.Constants.width//5)

    def __did_tap(self, sender):
        if self.__toogle_handler is None: return
        if sender == "Bedroom One": id = 1
        elif sender == "Bedroom Two": id = 2
        elif sender == "Living room": id = 3
        elif sender == "Dining room": id = 4
        elif sender == "Bathroom": id = 5
        self.__toogle_handler(id)