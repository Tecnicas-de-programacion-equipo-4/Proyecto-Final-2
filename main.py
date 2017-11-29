from Views.LightsView import LightsView
from Views.DoorView import DoorView
import serial
from serial.tools import list_ports

class MainApp():

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

        self.__master = LightsView(toogle_handler = self.__handler_event, tap_handler = self.__toggle_did_change)
        self.__doorView = DoorView(door_action = self.__toggle_did_change_door)
        self.__arduino = serial.Serial('/dev/cu.usbmodem33', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def run(self):
        self.__master.mainloop()

    def __toggle_did_change_door(self, action):
        self.__action = action
        door_instruction = str(self.__action).encode('ascii')
        self.__arduino.write(door_instruction)



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

    def __door_handler_event(self, instruction):
        self.__instruction = instruction
        print(self.__instruction)


    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()



if __name__ == "__main__":
    app = MainApp()
    app.run()