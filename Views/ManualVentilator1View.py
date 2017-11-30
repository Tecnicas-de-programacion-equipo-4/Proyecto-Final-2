from tkinter import  N, S, E, W, Label, Button, Frame
from CustomType.View import View
from Views.Ventilator_Button import VentilatorButton


class ViewVentilator1(Frame):
    class Constants:
        title = "Toggle Ventilator"
        text = "Manual Control Ventilator 1"
        center = N + S + E + W
        label_size = 40
        toggle_size = 20
        text_button_back = "Back to Home"
        manual_mode = False
        font = "Comic Sans MS"

    def __init__(self, parent, change_view_handler = None, tap_handler = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler
        label = Label(self, text = self.Constants.text, bg = "black", fg ="white",  font = (self.Constants.font, self.Constants.label_size))
        label.grid(row = 0, sticky = self.Constants.center)

        self.__toogle = VentilatorButton(self, tap_toggle_handler = tap_handler)
        self.__toogle.grid(row = 1, sticky = self.Constants.center)


        button1 = Button(self, text = self.Constants.text_button_back,font = (self.Constants.font, self.Constants.label_size), command = lambda: self.__did_tap_change_button(View.Main_View))
        button1.grid(row = 2,sticky = self.Constants.center)


    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False


