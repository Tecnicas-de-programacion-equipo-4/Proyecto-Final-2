from tkinter import Tk, N, S, E, W, Label
from Views.ToggleButton import ToggleButton

class MainView(Tk):
    class Constants:
        title = "Toggle Led"
        heigth = 300
        width = 300
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, tap_handler = None):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__bedroom_one_label = Label(self, text="Room\nOne", bg="red")
        self.__bedroom_one_label.grid(row=0, column=0, sticky=self.Constants.center)
        self.__bedroom_one_toogle = ToggleButton(self, tap_toggle_handler=tap_handler)
        self.__bedroom_one_toogle.grid(row=1, column=0, sticky=self.Constants.center)

        self.__bedroom_two_label = Label(self, text="Room\nTwo", bg="yellow")
        self.__bedroom_two_label.grid(row=0, column=1, sticky=self.Constants.center)
        self.__bedroom_two_toogle = ToggleButton(self, tap_toggle_handler=tap_handler)
        self.__bedroom_two_toogle.grid(row=1, column=1, sticky=self.Constants.center)

        self.__living_label = Label(self, text="Living\nroom", bg="blue")
        self.__living_label.grid(row=0, column=2, sticky=self.Constants.center)
        self.__living_toogle = ToggleButton(self, tap_toggle_handler=tap_handler)
        self.__living_toogle.grid(row=1, column=2, sticky=self.Constants.center)

        self.__dining_label = Label(self, text="Dining\nroom", bg="green")
        self.__dining_label.grid(row=0, column=3, sticky=self.Constants.center)
        self.__dining_toogle = ToggleButton(self, tap_toggle_handler=tap_handler)
        self.__dining_toogle.grid(row=1, column=3, sticky=self.Constants.center)


        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        self.grid_columnconfigure(0, weight=self.Constants.width//4)
        self.grid_columnconfigure(1, weight=self.Constants.width//4)
        self.grid_columnconfigure(2, weight=self.Constants.width//4)
        self.grid_columnconfigure(3, weight=self.Constants.width//4)
