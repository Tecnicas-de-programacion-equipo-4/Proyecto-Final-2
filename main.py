from Models.TemperatureControl import TemperatureManager
from Views.ManualVentView import ViewVentilator
from Views.ViewContainer import MainView
from Views.MainView import StartView
from CustomType.View import View
import serial
from serial.tools import list_ports

class MainApp():
    class Constants:
        baud = 115200
        port = 'COM3'
        protocol_delete = "WM_DELETE_WINDOW"
        temperature_limit = 23.0

    def __init__(self):
        for port in list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)
        self.__master = MainView()

        self.main_view = StartView(self.__master.container, change_view_hadler=self.__did_change_view)
        self.ventilator = ViewVentilator(self.__master.container, change_view_handler=self.__did_change_view, tap_handler = self.__toggle_did_change)


        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.protocol_delete, self.__on_closing)

        self.__frames = {
            View.Main_View: self.main_view,
            View.Ventilator_1: self.ventilator
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Main_View)
        self.__update_clock()


    def run(self):
        self.__master.mainloop()


    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

    def __toggle_did_change(self, state):
        self.ventilator.Constants.manual_mode = True
        value = str(1 if state else 0).encode('ascii')
        self.__arduino.write(value)


    def __handle_data(self, data):
        clean_values = data.split('\n\r')
        self.value_text = clean_values[0]
        self.main_view.update_text(self.value_text)

        if float(self.value_text) > self.Constants.temperature_limit and self.ventilator.Constants.manual_mode == False:
            value = str(1).encode('ascii')
            self.__arduino.write(value)
        elif self.ventilator.Constants.manual_mode == False:
            value = str(0).encode('ascii')
            self.__arduino.write(value)


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


