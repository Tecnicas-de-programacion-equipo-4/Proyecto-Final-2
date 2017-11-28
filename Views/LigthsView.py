from tkinter import Frame, N, S, E, W, Label, Button
from Views.ToggleButton import ToggleButton
from CustomType.View import View
class LightsView(Frame):
    class Constants:
        title = "Casa Inteligente"
        heigth = 300
        width = 375
        center = N + S + E + W
        text_button_back = "Back to home"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, parent, change_view_handler = None, toogle_handler = None, tap_handler = None):
        super().__init__(parent)
        self.__change_view_handler = change_view_handler

        self.__toogle_handler = toogle_handler
        #self.title(self.Constants.title)
        #self.geometry(self.Constants.size())

        self.__configure_grid()

        self.__bedroom_one_label = Label(self, text="Room\nOne", relief="sunken")
        self.__bedroom_one_label.grid(row=0, column=0, sticky=self.Constants.center)
        self.__bedroom_one_toogle = ToggleButton(self, "Bedroom One", action=self.__did_tap,
                                                 tap_toggle_handler=tap_handler)
        self.__bedroom_one_toogle.grid(row=1, column=0, sticky=self.Constants.center)

        self.__bedroom_two_label = Label(self, text="Room\nTwo", relief="sunken")
        self.__bedroom_two_label.grid(row=0, column=1, sticky=self.Constants.center)
        self.__bedroom_two_toogle = ToggleButton(self, "Bedroom Two", action=self.__did_tap,
                                                 tap_toggle_handler=tap_handler)
        self.__bedroom_two_toogle.grid(row=1, column=1, sticky=self.Constants.center)

        self.__living_label = Label(self, text="Living\nroom", relief="sunken")
        self.__living_label.grid(row=0, column=2, sticky=self.Constants.center)
        self.__living_toogle = ToggleButton(self, "Living room", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__living_toogle.grid(row=1, column=2, sticky=self.Constants.center)

        self.__dining_label = Label(self, text="Dining\nroom", relief="sunken")
        self.__dining_label.grid(row=0, column=3, sticky=self.Constants.center)
        self.__dining_toogle = ToggleButton(self, "Dining room", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__dining_toogle.grid(row=1, column=3, sticky=self.Constants.center)

        self.__bathroom_label = Label(self, text="Bath\nroom", relief="sunken")
        self.__bathroom_label.grid(row=0, column=4, sticky=self.Constants.center)
        self.__bathroom_toogle = ToggleButton(self, "Bathroom", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__bathroom_toogle.grid(row=1, column=4, sticky=self.Constants.center)

        button_back = Button(self, text=self.Constants.text_button_back,command=lambda: self.__did_tap_change_button(View.Main_View))
        button_back.grid(row = 2, column = 2, sticky = self.Constants.center)


    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(2, weight = self.Constants.heigth // 2)
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

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False