from Models.TemperatureControl import TemperatureManager
from Views.ManualVentilator1View import ViewVentilator1
from Views.ManualVentilator2View import ViewVentilator2
from Views.ViewContainer import MainView
from Views.MainView import StartView
from CustomType.View import View
import serial
from serial.tools import list_ports

class MainApp():
    class Constants:
        baud = 9600
        port = 'COM3'
        protocol_delete = "WM_DELETE_WINDOW"
        temperature_limit = 23.0

    def __init__(self):
        for port in list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)
        self.__master = MainView()

        self.main_view = StartView(self.__master.container, change_view_hadler=self.__did_change_view)
        self.ventilator_1 = ViewVentilator1(self.__master.container, change_view_handler=self.__did_change_view, tap_handler = self.__toggle_1_did_change_)

        self.ventilator_2 = ViewVentilator2(self.__master.container, change_view_handler=self.__did_change_view, tap_handler=self.__toggle_2_did_change_)

        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.protocol_delete, self.__on_closing)

        self.__frames = {
            View.Main_View: self.main_view,
            View.Ventilator_1: self.ventilator_1,
            View.Ventilator_2: self.ventilator_2
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
        self.value_1 = clean_values[0]
        self.value_2 = clean_values[1]

        if float(self.value_2) > self.Constants.temperature_limit and self.ventilator_2.Constants.manual_mode == False:
            vent_2_value_1 = str(2).encode('ascii')
            self.__arduino.write(vent_2_value_1)
        elif float(self.value_1) > self.Constants.temperature_limit and self.ventilator_1.Constants.manual_mode == False:
            vent_1_value_1 = str(1).encode('ascii')
            self.__arduino.write(vent_1_value_1)
        elif self.ventilator_1.Constants.manual_mode == False and self.ventilator_2.Constants.manual_mode == False:
            value = str(0).encode('ascii')
            self.__arduino.write(value)

        self.main_view.update_text(self.value_1, self.value_2)


    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)


    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.run()


