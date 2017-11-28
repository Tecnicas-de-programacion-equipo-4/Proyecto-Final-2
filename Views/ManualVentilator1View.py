from tkinter import  N, S, E, W, Label, Button, Frame
from CustomType.View import View
from Views.Ventilator_Button import VentilatorButton


class ViewVentilator1(Frame):
    class Constants:
        title = "Toggle Ventilator"
        text = "Control Manual Ventilator 1"
        center = N + S + E + W
        label_size = 10
        toggle_size = 20
        text_button_back = "Back to Home"
        manual_mode = False


    def __init__(self, parent, change_view_handler = None, tap_handler = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler
        label = Label(self, text = self.Constants.text)
        label.pack(pady = self.Constants.label_size, padx = self.Constants.label_size)

        self.__toogle = VentilatorButton(self, tap_toggle_handler = tap_handler)
        self.__toogle.pack(pady = self.Constants.toggle_size, padx = self.Constants.toggle_size)


        button1 = Button(self, text = self.Constants.text_button_back,
                            command = lambda: self.__did_tap_change_button(View.Main_View))
        button1.pack()


    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False


