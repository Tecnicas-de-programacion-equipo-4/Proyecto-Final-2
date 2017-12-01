from tkinter import  Label, Button, Frame
from CustomType.View import View
from Views.Ventilator_Button import VentilatorButton


class ViewVentilator(Frame):
    class Constants:
        label_size = 10
        toggle_size = 20
        text_button_back = "Back to Home"
        manual_mode = False


    def __init__(self, parent, change_view_handler = None, tap_handler = None, text_view = None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler
        label = Label(self, text = text_view)
        label.pack(pady = self.Constants.label_size, padx = self.Constants.label_size)

        self.__toogle = VentilatorButton(self, tap_toggle_handler = tap_handler)
        self.__toogle.pack(pady = self.Constants.toggle_size, padx = self.Constants.toggle_size)


        self.back_button = Button(self, text = self.Constants.text_button_back,
                            command = lambda: self.__did_tap_change_button(View.Main_View))
        self.back_button.pack()


    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False


