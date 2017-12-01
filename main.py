from Models.TemperatureControl import TemperatureManager
from Views.ManualVentilatorView import ViewVentilator
from Views.ViewContainer import MainView
from Views.MainView import StartView
from CustomType.View import View

from Views.LigthsView import LightsView

from Views.AlarmView import Alarm
from Views.ParkingView import Parking
from Views.EntranceView import Entrance


import serial
from serial.tools import list_ports

class MainApp():

    class Constants:
        baud = 9600
        port = 'COM3'
        protocol_delete = "WM_DELETE_WINDOW"
        temperature_limit = 23.0
        ventilator_manual_1 = "Manual Control Ventilator 1"
        ventilator_manual_2 = "Manual Control Ventilator 2"

    def __init__(self):
        for port in list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)
        self.__master = MainView()

        self.main_view = StartView(self.__master.container, change_view_hadler=self.__did_change_view)
        self.ventilator_1 = ViewVentilator(self.__master.container, change_view_handler=self.__did_change_view,tap_handler=self.__toggle_1_did_change_,text_view=self.Constants.ventilator_manual_1)
        self.ventilator_2 = ViewVentilator(self.__master.container, change_view_handler=self.__did_change_view,tap_handler=self.__toggle_2_did_change_,text_view=self.Constants.ventilator_manual_2)

        self.lights = LightsView(self.__master.container, change_view_handler=self.__did_change_view, toogle_handler=self.__handler_event, tap_handler=self.__toggle_did_change)
        self.alarm = Alarm(self.__master.container, change_view_handler=self.__did_change_view)
        self.parking = Parking(self.__master.container, change_view_handler=self.__did_change_view)
        self.entrance = Entrance(self.__master.container, change_view_handler=self.__did_change_view)




        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.protocol_delete, self.__on_closing)

        self.__frames = {
            View.Main_View: self.main_view,
            View.Ventilator_1: self.ventilator_1,
            View.Ventilator_2: self.ventilator_2,
            View.Lights: self.lights,
            View.Alarm: self.alarm,
            View.Parking: self.parking,
            View.Door: self.entrance
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Main_View)
        self.__update_clock()



    def run(self):
        self.__master.mainloop()



    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

    def __toggle_1_did_change_(self, state):
        self.ventilator_1.Constants.manual_mode = True
        value_1 = str(1 if state else 0).encode('ascii')
        self.__arduino.write(value_1)


    def __toggle_2_did_change_(self, state):
        self.ventilator_2.Constants.manual_mode = True
        value_2 = str(2 if state else 0).encode('ascii')
        self.__arduino.write(value_2)


    def __handle_data(self, data):
        clean_values = data.split(',')
        try:
            self.temperature_1 = float(clean_values[0])
            self.temperature_2 = float(clean_values[1])
        except Exception:
            print('ERROR DATA')

        if self.temperature_2 > self.Constants.temperature_limit and self.ventilator_2.Constants.manual_mode == False:
            vent_2_value_1 = str(2).encode('ascii')
            self.__arduino.write(vent_2_value_1)
        elif self.temperature_1 > self.Constants.temperature_limit and self.ventilator_1.Constants.manual_mode == False:
            vent_1_value_1 = str(1).encode('ascii')
            self.__arduino.write(vent_1_value_1)
        elif self.ventilator_1.Constants.manual_mode == False and self.ventilator_2.Constants.manual_mode == False:
            value = str(0).encode('ascii')
            self.__arduino.write(value)

        self.main_view.update_text(self.temperature_1, self.temperature_2)


    def __update_clock(self):
        try:
            data = self.__arduino.readline().decode()
            self.__handle_data(data)
            self.__master.after(1, self.__update_clock)
        except UnicodeDecodeError:
            print('ERROR DATA')



    def __handler_event(self, id):
        self.__id = id

    def __toggle_did_change(self, state):
        if (self.__id == 1) and (state == True): self.__valor = 1
        if (self.__id == 1) and (state == False): self.__valor = 2
        if (self.__id == 2) and (state == True): self.__valor = 3
        if (self.__id == 2) and (state == False): self.__valor = 4
        if (self.__id == 3) and (state == True): self.__valor = 5
        if (self.__id == 3) and (state == False): self.__valor = 6
        if (self.__id == 4) and (state == True): self.__valor = 7
        if (self.__id == 4) and (state == False): self.__valor = 8
        if (self.__id == 5) and (state == True): self.__valor = 9
        if (self.__id == 5) and (state == False): self.__valor = 'a'
        value = str(self.__valor).encode('ascii')
        self.__arduino.write(value)


    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()





if __name__ == "__main__":
    app = MainApp()
    app.run()

