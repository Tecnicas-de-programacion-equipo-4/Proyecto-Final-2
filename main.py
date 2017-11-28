from Views.MainView import MainView
import serial
from serial.tools import list_ports

class MainApp():

    class Constants:
        port = "COM3"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):

        self.__master = MainView(toogle_handler = self.__handler_event, tap_handler = self.__toggle_did_change)
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update()

    def __update(self):
        data = self.__arduino.readline().decode()
        clean_data = data.strip(" \n\r").split(",")
        try:
            outside = clean_data[0]
            inside = clean_data[1]
            self.__master.sec(outside, inside)
        except:
            pass
        self.__master.after(1, self.__update)

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