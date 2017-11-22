from tkinter import Tk, N, S, E, W, Label
from Views.ToggleButton import ToggleButton

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