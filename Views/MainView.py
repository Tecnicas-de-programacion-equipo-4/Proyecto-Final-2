from tkinter import Frame, Label, Button

from CustomType.View import View

class StartView(Frame):
    class Constants:
        label_text = "MainView Control de temperatura"
        label_size = 10
        ventilator_1_text = "Ventilator 1"
        color = "blue"
        color_font = "white"

    def __init__(self, parent, change_view_hadler = None):
        super().__init__(parent)

        self.__change_view_hadler = change_view_hadler
        label = Label(self, text = self.Constants.label_text)
        label.pack(pady = self.Constants.label_size, padx = self.Constants.label_size)
        button = Button(self, text = self.Constants.ventilator_1_text,
                           command=lambda: self.__did_tap_change_button(View.Ventilator_1))
        button.pack()

        self.__temperature_label= Label(self)

        self.__temperature_label.pack()
        self.update_text("0")

    def update_text(self, text):
        self.__temperature_label.configure(text = text, bg = self.Constants.color, fg = self.Constants.color_font)


    def __did_tap_change_button(self, view):
        if self.__change_view_hadler is None:
            return
        self.__change_view_hadler(view)