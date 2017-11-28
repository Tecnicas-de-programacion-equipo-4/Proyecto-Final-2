from tkinter import  N, S, E, W, Label, Button, Frame
from CustomType.View import View

class Alarm(Frame):
    class Constants:
        text_button_back = "Back to Home"

    def __init__(self, parent, change_view_handler=None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler


        button1 = Button(self, text=self.Constants.text_button_back,
                         command=lambda: self.__did_tap_change_button(View.Main_View))
        button1.pack()

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False
