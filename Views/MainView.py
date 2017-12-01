from tkinter import Frame, Label, Button, N, S, E, W
from CustomType.View import View

class StartView(Frame):
    class Constants:
        label_text = "Welcome :)"
        label_size = 20
        font = "Comic Sans MS"
        ventilator_1_text = "Ventilator 1"
        ventilator_2_text = "Ventilator 2"
        lights = "Lights control"
        alarm = "Security Alarm"
        parking = "Parking"
        door = "Entrance "
        color = "blue"
        color_font = "white"
        center = N + S + E + W


    def __init__(self, parent, change_view_hadler = None):
        super().__init__(parent)

        self.__change_view_hadler = change_view_hadler
        label = Label(self, text=self.Constants.label_text, bg="black",fg = "white", font = (self.Constants.font, self.Constants.label_size + 20))
        label.grid(columnspan =2, sticky = self.Constants.center)


        button_ventilator_1 = Button(self, text = self.Constants.ventilator_1_text, font = (self.Constants.font, self.Constants.label_size),  command=lambda: self.__did_tap_change_button(View.Ventilator_1))
        button_ventilator_1.grid(row = 1, column = 0, sticky = self.Constants.center)
        self.__temperature_label_1 = Label(self, font = (self.Constants.font, self.Constants.label_size))
        self.__temperature_label_1.grid(row = 2, column =0,  sticky = self.Constants.center)


        button_ventilator_2 = Button(self, font = (self.Constants.font, self.Constants.label_size), text=self.Constants.ventilator_2_text, command=lambda: self.__did_tap_change_button(View.Ventilator_2))
        button_ventilator_2.grid(row = 1, column = 1,  sticky = self.Constants.center)
        self.__temperature_label_2 = Label(self, font = (self.Constants.font, self.Constants.label_size))
        self.__temperature_label_2.grid(row = 2, column = 1, sticky = self.Constants.center)

        button_lights = Button(self,  font = (self.Constants.font, self.Constants.label_size), text = self.Constants.lights, command=lambda: self.__did_tap_change_button(View.Lights))
        button_lights.grid(row = 3,column = 0,  sticky = self.Constants.center)

        button_alarm = Button(self, font = (self.Constants.font, self.Constants.label_size), text = self.Constants.alarm, command=lambda: self.__did_tap_change_button(View.Alarm))
        button_alarm.grid(row = 4, column = 0,  sticky = self.Constants.center)

        button_parking = Button(self, font = (self.Constants.font, self.Constants.label_size), text=self.Constants.parking, command=lambda: self.__did_tap_change_button(View.Parking))
        button_parking.grid(row = 3, column = 1, sticky = self.Constants.center)

        button_door = Button(self, font = (self.Constants.font, self.Constants.label_size), text=self.Constants.door, command=lambda: self.__did_tap_change_button(View.Door))
        button_door.grid(row = 4, column =1, sticky = self.Constants.center)



        for v in range(0,2):
            self.rowconfigure(v, weight=True)
            self.columnconfigure(v, weight = True)

        self.rowconfigure(3, weight=True)
        self.rowconfigure(4, weight = True)


        self.update_text("0","0")


    def update_text(self, text_1, text_2):
        self.__temperature_label_1.configure(text = text_1, bg = self.Constants.color, fg = self.Constants.color_font)
        self.__temperature_label_2.configure(text=text_2, bg = "red", fg=self.Constants.color_font)

    def __did_tap_change_button(self, view):
        if self.__change_view_hadler is None:
            return
        self.__change_view_hadler(view)

