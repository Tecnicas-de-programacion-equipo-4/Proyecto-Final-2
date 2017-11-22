from tkinter import Tk, N, S, E, W, Label
from Views.ToggleButton import ToggleButton
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

        self.__bedroom_one_label = Label(self, text="Room\nOne", relief = "sunken")
        self.__bedroom_one_label.grid(row=0, column=0, sticky=self.Constants.center)
        self.__bedroom_one_toogle = ToggleButton(self, "Bedroom One", action=self.__did_tap, tap_toggle_handler= tap_handler)
        self.__bedroom_one_toogle.grid(row=1, column=0, sticky=self.Constants.center)

        self.__bedroom_two_label = Label(self, text="Room\nTwo", relief = "sunken")
        self.__bedroom_two_label.grid(row=0, column=1, sticky=self.Constants.center)
        self.__bedroom_two_toogle = ToggleButton(self, "Bedroom Two", action=self.__did_tap, tap_toggle_handler= tap_handler)
        self.__bedroom_two_toogle.grid(row=1, column=1, sticky=self.Constants.center)

        self.__living_label = Label(self, text="Living\nroom", relief = "sunken")
        self.__living_label.grid(row=0, column=2, sticky=self.Constants.center)
        self.__living_toogle = ToggleButton(self, "Living room", action=self.__did_tap, tap_toggle_handler= tap_handler)
        self.__living_toogle.grid(row=1, column=2, sticky=self.Constants.center)

        self.__dining_label = Label(self, text="Dining\nroom", relief = "sunken")
        self.__dining_label.grid(row=0, column=3, sticky=self.Constants.center)
        self.__dining_toogle = ToggleButton(self, "Dining room", action=self.__did_tap, tap_toggle_handler= tap_handler)
        self.__dining_toogle.grid(row=1, column=3, sticky=self.Constants.center)

        self.__bathroom_label = Label(self, text="Bath\nroom", relief = "sunken")
        self.__bathroom_label.grid(row=0, column=4, sticky=self.Constants.center)
        self.__bathroom_toogle = ToggleButton(self, "Bathroom", action=self.__did_tap, tap_toggle_handler= tap_handler)
        self.__bathroom_toogle.grid(row=1, column=4, sticky=self.Constants.center)

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