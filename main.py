from Views.ManualVentilatorView import ViewVentilator
from Views.ViewContainer import MainView
from Views.MainView import StartView
from Views.LigthsView import LightsView
from Views.AlarmView import Alarm
from Views.ParkingView import Parking
from Views.EntranceView import Entrance
from CustomType.View import View


#Hay que revisar como va a entregar los datos en la version final del arcchivo de arduino para el update
import serial


class MainApp():

    class Constants:
        port = ''
        protocol_delete = "WM_DELETE_WINDOW"
        temperature_limit = 23.0
        ventilator_manual_1 = "Manual Control Ventilator 1"
        ventilator_manual_2 = "Manual Control Ventilator 2"

    def __init__(self):
        self.__master = MainView()
        self.__main_view = StartView(self.__master.container, change_view_hadler=self.__did_change_view)
        self.__ventilator_1 = ViewVentilator(self.__master.container, change_view_handler=self.__did_change_view,tap_handler=self.__toggle_1_did_change_,text_view=self.Constants.ventilator_manual_1)
        self.__ventilator_2 = ViewVentilator(self.__master.container, change_view_handler=self.__did_change_view, tap_handler=self.__toggle_2_did_change_,text_view=self.Constants.ventilator_manual_2)

        #{Este chung ya no se modifica...
        self.__lights = LightsView(self.__master.container, change_view_handler=self.__did_change_view, toogle_handler=self.__handler_event, tap_handler=self.__toggle_did_change)
        self.__parking = Parking(self.__master.container, change_view_handler=self.__did_change_view, parking_action=self.__did_change_servo_position)
        self.__entrance = Entrance(self.__master.container, change_view_handler=self.__did_change_view, door_action=self.__did_change_servo_position)
#..Hasta acá.}
        self.__alarm = Alarm(self.__master.container, change_view_handler=self.__did_change_view)

        self.__arduino = serial.Serial('/dev/cu.usbmodem1411', 9600)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

        self.__frames = {
            View.Main_View: self.__main_view,
            View.Ventilator_1: self.__ventilator_1,
            View.Ventilator_2: self.__ventilator_2,
            View.Lights: self.__lights,
            View.Alarm: self.__alarm,
            View.Parking: self.__parking,
            View.Door: self.__entrance
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
        self.__ventilator_1.Constants.manual_mode = True
        vent_1_on = str("e" if state else "f").encode('ascii')

        self.__arduino.write(vent_1_on)



    def __toggle_2_did_change_(self, state):
        self.__ventilator_2.Constants.manual_mode = True
        vent_2_on = str("g" if state else "h").encode('ascii')

        self.__arduino.write(vent_2_on)




    def __handle_data(self, data):
        clean_values = data.split(',')
        try:

            self.temperature_1 = float(clean_values[0])
            self.temperature_2 = float(clean_values[1])

        except Exception:
            print('ERROR DATA')

        if self.temperature_2 > self.Constants.temperature_limit and self.__ventilator_2.Constants.manual_mode == False:
            vent_2_on = str("e").encode('ascii')
            self.__arduino.write(vent_2_on)
        elif self.temperature_1 > self.Constants.temperature_limit and self.__ventilator_1.Constants.manual_mode == False:
            vent_1_on = str("f").encode('ascii')
            self.__arduino.write(vent_1_on)
        elif self.__ventilator_1.Constants.manual_mode == False and self.__ventilator_2.Constants.manual_mode == False:
            value = str(0).encode('ascii')
            self.__arduino.write(value)


        self.__main_view.update_text(self.temperature_1, self.temperature_2)


    def __update_clock(self):
        #Temperatura
        data = self.__arduino.readline().decode()
        self.__handle_data(data)

        #Seguridad
        clean_data = data.strip(" \n\r").split(",")
        try:
            outside = clean_data[0]
            inside = clean_data[1]
            self.__master.sec(outside, inside)
        except:
            pass
        self.__master.after(1, self.__update_clock)


#{Este chung ya no se modifiica...
    def __did_change_servo_position(self, instruction):
        self.__instruction = instruction
        servo_instruction = str(self.__instruction).encode('ascii')
        self.__arduino.write(servo_instruction)

    def __handler_event(self, id):
        self.__id = id

    def __toggle_did_change(self, state):
        print("{} , {}".format(self.__id, state))
        if (self.__id == 1) and (state == True): self.__valor = 1
        if (self.__id == 1) and (state == False): self.__valor = 2
        if (self.__id == 2) and (state == True): self.__valor = 3
        if (self.__id == 2) and (state == False): self.__valor = 4
        if (self.__id == 3) and (state == True): self.__valor = 5
        if (self.__id == 3) and (state == False): self.__valor = 6
        if (self.__id == 4) and (state == True): self.__valor = 7
        if (self.__id == 4) and (state == False): self.__valor = 8
        print(self.__valor)
        value = str(self.__valor).encode('ascii')
        self.__arduino.write(value)
#... hasta acá


    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()

