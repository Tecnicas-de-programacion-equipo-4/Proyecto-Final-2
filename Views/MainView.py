from tkinter import Tk, N, S, E, W, Label, Button
from Views.ToggleButton import ToggleButton
from smtplib import SMTP
from correo import send_email, send_password
#from Views.KeypadView import KeypadView
class MainView(Tk):
    class Constants:
        title = "Casa Inteligente"
        heigth = 300
        width = 1000
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, toogle_handler = None, tap_handler = None):
        super().__init__()
        self.__toogle_handler = toogle_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__configure_grid()

        self.__bedroom_one_label = Label(self, text="Room\nOne", relief="sunken")
        self.__bedroom_one_label.grid(row=0, column=0, sticky=self.Constants.center)
        self.__bedroom_one_toogle = ToggleButton(self, "Bedroom One", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__bedroom_one_toogle.grid(row=1, column=0, sticky=self.Constants.center)

        self.__bedroom_two_label = Label(self, text="Room\nTwo", relief="sunken")
        self.__bedroom_two_label.grid(row=0, column=1, sticky=self.Constants.center)
        self.__bedroom_two_toogle = ToggleButton(self, "Bedroom Two", action=self.__did_tap,
                                                 tap_toggle_handler=tap_handler)
        self.__bedroom_two_toogle.grid(row=1, column=1, sticky=self.Constants.center)

        self.__living_label = Label(self, text="Living\nroom", relief="sunken")
        self.__living_label.grid(row=0, column=2, sticky=self.Constants.center)
        self.__living_toogle = ToggleButton(self, "Living room", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__living_toogle.grid(row=1, column=2, sticky=self.Constants.center)

        self.__dining_label = Label(self, text="Dining\nroom", relief="sunken")
        self.__dining_label.grid(row=0, column=3, sticky=self.Constants.center)
        self.__dining_toogle = ToggleButton(self, "Dining room", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__dining_toogle.grid(row=1, column=3, sticky=self.Constants.center)

        self.__bathroom_label = Label(self, text="Bath\nroom", relief="sunken")
        self.__bathroom_label.grid(row=0, column=4, sticky=self.Constants.center)
        self.__bathroom_toogle = ToggleButton(self, "Bathroom", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__bathroom_toogle.grid(row=1, column=4, sticky=self.Constants.center)

        self.is_active = False
        self.current_pos = 0
        self.inside_count = -1
        self.outside_count = 0
        self.inside_send = False
        self.outside_send = False

        self.__top_text = Label(self, text="Control de Alarma", bg="#666699", font=("Comic Sans MS", 30))
        self.__activate = Button(self, text="Activar alarma", bg="black", fg="white", command=self.act, font=("Comic Sans MS", 18))
        self.__outside_label = Label(self, text="Alarma", bg="#666699", font=("Comic Sans MS", 18))
        self.__inside_label = Label(self, text="Desactivada", bg="#666699", font=("Comic Sans MS", 18))
        self.__bottom_text = Label(self, text="Si se detectan parametros ariesgados se le notificara", font=("Comic Sans MS", 15))
        self.__outside_value = Label(self, text=" ", font=("Comic Sans MS", 20), bg="#666699")
        self.__inside_value = Label(self, text=" ", font=("Comic Sans MS", 20), bg="#666699")

        self.__top_text.grid(row=0,column = 5, columnspan=2, sticky=self.Constants.center)
        self.__activate.grid(row=1,column = 5, columnspan=2, sticky=self.Constants.center)
        self.__outside_label.grid(row=2, column=5, sticky=self.Constants.center)
        self.__inside_label.grid(row=2, column=6, sticky=self.Constants.center)
        self.__outside_value.grid(row=3, column=5, sticky=self.Constants.center)
        self.__inside_value.grid(row=3, column=6, sticky=self.Constants.center)
        self.__bottom_text.grid(row=4, column = 5, columnspan=2, sticky=self.Constants.center)

        for v in range(0, 2):
            self.rowconfigure(v, weight=True)
            self.columnconfigure(v, weight=True)


    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        for column_index in range(5):
            self.grid_columnconfigure(column_index, weight=self.Constants.width//5)

    def __did_tap(self, sender):
        if self.__toogle_handler is None: return
        if sender == "Bedroom One": id = 1
        elif sender == "Bedroom Two": id = 2
        elif sender == "Living room": id = 3
        elif sender == "Dining room": id = 4
        elif sender == "Bathroom": id = 5
        self.__toogle_handler(id)

    def act(self):
        self.__top_text.config(text="Alarma Activa", bg="#000099")
        self.__activate.config(text="Desactivar alarma", bg="red", command=self.deact)
        self.__inside_label.config(text="Dentro de la casa", bg="black", fg="white")
        self.__outside_label.config(text="Fuera de la casa", bg="white", fg="black")
        self.is_active = True

    def deact(self):
        self.__top_text.config(text="Control de Alarma", bg="#666699")
        self.__activate.config(text="Activar alarma", bg="black", command=self.act)
        self.__inside_label.config(text="Desactivada", bg="#666699", fg="black")
        self.__outside_label.config(text="Alarma", bg="#666699", fg="black")
        self.__outside_value.config(text = " ", bg = "#666699")
        self.__inside_value.config(text = " ", bg = "#666699")
        self.is_active = False

    def send_noti_out(self):
        email = send_email
        password = send_password
        msj = """Se encontro movimiento sospechoso fuera de su casa

        mas de 800 lecturas a menos de 50 cm de la entrada

        se ha notificado a la policia"""

        subject = "Alarma fuera de la casa"

        email_msg = "Subject: {} \n\n {}".format(subject, msj)
        smtp = SMTP("smtp.gmail.com", 587)

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        smtp.sendmail(email, "ponx.987@gmail.com", email_msg)

        smtp.quit()
        print("Email sent")

    def manage_outside(self,outs):
        text = "{} cm".format(outs)
        if int(outs) > 150:
            self.__outside_value.config(text = text, bg="green")
        if int(outs) in range(50,149):
            self.__outside_value.config(text = text, bg="yellow")
        if int(outs) < 50:
            self.__outside_value.config(text = text, bg="red")
            self.outside_count += 1
            if self.outside_count > 500 and self.outside_send == False:
                self.send_noti_out()
                self.outside_count = -10000
                self.outside_send = True

    def send_noti_in(self):
        email = send_email
        password = send_password
        msj = """Se encontro movimiento sospechoso dentro de su casa

                  se ha notificado a la policia"""

        subject = "Alarma dentro de la casa"

        email_msg = "Subject: {} \n\n {}".format(subject, msj)
        smtp = SMTP("smtp.gmail.com", 587)

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        smtp.sendmail(email, "ponx.987@gmail.com", email_msg)

        smtp.quit()
        print("Email sent")

    def manage_inside(self,ins):
        move = abs(self.current_pos - int(ins))
        text = "{} cm".format(move)
        if move < 10:
            self.__inside_value.config(text="leve "+text, bg="green")
        if move in range(10,30):
            self.__inside_value.config(text="moderado "+text, bg="yellow")
            self.inside_count += 1
        if move > 30:
            self.__inside_value.config(text="grave " + text, bg="red")
            self.inside_count += 2
            if self.inside_count > 50 and self.inside_send == False:
                self.send_noti_in()
                self.inside_count = -10000
                self.inside_send = True
        self.current_pos = int(ins)

    def sec(self, outs, ins):
       if self.is_active == False:
           pass
       else:
           self.manage_outside(outs)
           self.manage_inside(ins)