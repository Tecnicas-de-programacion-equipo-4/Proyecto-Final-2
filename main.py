from Views.MainView import MainView
import serial
from serial.tools import list_ports

class MainApp():

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

        self.__master = MainView(toogle_handler = self.__handler_event, tap_handler = self.__toggle_did_change)
        self.__arduino = serial.Serial('/dev/cu.usbmodem1411', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def run(self):
        self.__master.mainloop()

    def __handler_event(self, id):
        self.__id = id

    def __toggle_did_change(self, state):
        value = str(1 if state else 0).encode('ascii')
        id = str(self.__id).encode('ascii')
        self.__arduino.write(id+value)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()



if __name__ == "__main__":
    app = MainApp()
    app.run()