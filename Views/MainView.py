from tkinter import Frame, Label, Button

from CustomType.View import View

class StartView(Frame):
    class Constants:
        label_text = "Main View "
        label_size = 10
        ventilator_1_text = "Ventilator 1"
        ventilator_2_text = "Ventilator 2"
        lights = "Lights control"
        alarm = "Security Alarm"
        parking = "Parking"
        door = "Entrance "
        color = "blue"
        color_font = "white"

    def __init__(self, parent, change_view_hadler = None):
        super().__init__(parent)

        self.__change_view_hadler = change_view_hadler
        label = Label(self, text = self.Constants.label_text)
        label.pack(pady = self.Constants.label_size, padx = self.Constants.label_size)


        button_ventilator_1 = Button(self, text = self.Constants.ventilator_1_text,
                           command=lambda: self.__did_tap_change_button(View.Ventilator_1))
        button_ventilator_1.pack()
        self.__temperature_label_1 = Label(self)
        self.__temperature_label_1.pack()


        button_ventilator_2 = Button(self, text=self.Constants.ventilator_2_text,
                                     command=lambda: self.__did_tap_change_button(View.Ventilator_2))
        button_ventilator_2.pack()
        self.__temperature_label_2 = Label(self)
        self.__temperature_label_2.pack()

        button_lights = Button(self, text = self.Constants.lights, command=lambda: self.__did_tap_change_button(View.Lights))
        button_lights.pack()

        button_alarm = Button(self, text = self.Constants.alarm, command=lambda: self.__did_tap_change_button(View.Alarm))
        button_alarm.pack()

        button_parking = Button(self, text=self.Constants.parking, command=lambda: self.__did_tap_change_button(View.Parking))
        button_parking.pack()

        button_door = Button(self, text=self.Constants.door, command=lambda: self.__did_tap_change_button(View.Door))
        button_door.pack()


        self.update_text("0","0")

    def update_text(self, text_1, text_2):
        self.__temperature_label_1.configure(text = text_1, bg = self.Constants.color, fg = self.Constants.color_font)
        self.__temperature_label_2.configure(text=text_2, bg = "red", fg=self.Constants.color_font)

    def __did_tap_change_button(self, view):
        if self.__change_view_hadler is None:
            return
        self.__change_view_hadler(view)