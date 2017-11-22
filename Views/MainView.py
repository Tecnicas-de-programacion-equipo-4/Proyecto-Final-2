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

<<<<<<< HEAD
=======
        self.__configure_grid()

        self.__bedroom_one_label = Label(self, text="Room\nOne", relief = "sunken")
        self.__bedroom_one_label.grid(row=0, column=0, sticky=self.Constants.center)
        self.__bedroom_one_toogle = ToggleButton(self, "Bedroom One", action=self.__did_tap, tap_toggle_handler= tap_handler)
        self.__bedroom_one_toogle.grid(row=1, column=0, sticky=self.Constants.center)
>>>>>>> e3bc90e3277f4f0bf38b71d8c1905831cdb58b00


    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        for column_index in range(5):
            self.grid_columnconfigure(column_index, weight=self.Constants.width//5)

    def __did_tap(self, sender):
        if self.__toogle_handler is None: return
        if sender == "Bedroom One": id = 1
        elif sender == "Bedroom Two": id = 2
        elif sender == "Living room": id = 3
        elif sender == "Dining room": id = 4
        elif sender == "Bathroom": id = 5
        self.__toogle_handler(id)