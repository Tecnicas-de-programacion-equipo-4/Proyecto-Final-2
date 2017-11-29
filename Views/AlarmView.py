from tkinter import  N, S, E, W, Label, Button, Frame
from CustomType.View import View
from smtplib import SMTP
from Views.correo import send_email, send_password, reciever

class Alarm(Frame):
    class Constants:
        text_button_back = "Back to Home"
        title = "Security"
        height = 520
        width = 750
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self, parent, change_view_handler=None):
        super().__init__(parent)

        self.__change_view_handler = change_view_handler

        self.is_active = False
        self.current_pos = 0
        self.inside_count = -1
        self.outside_count = 0
        self.inside_send = False
        self.outside_send = False

        self.__top_text = Label(self, text="Alarm Control", bg="#666699", font=("Comic Sans MS", 44))
        self.__activate = Button(self, text="Activate", bg="black", fg="white", command=self.act,
                                 font=("Comic Sans MS", 25))
        self.__outside_label = Label(self, text="Alarm", bg="#666699", font=("Comic Sans MS", 22))
        self.__inside_label = Label(self, text="Deactivated", bg="#666699", font=("Comic Sans MS", 22))
        self.__bottom_text = Label(self, text="You will get a notice if anything happens",
                                   font=("Comic Sans MS", 20))
        self.__outside_value = Label(self, text=" ", font=("Comic Sans MS", 25), bg="#666699")
        self.__inside_value = Label(self, text=" ", font=("Comic Sans MS", 25), bg="#666699")

        self.__top_text.grid(row=0, columnspan=2, sticky=self.Constants.center)
        self.__activate.grid(row=1, columnspan=2, sticky=self.Constants.center)
        self.__outside_label.grid(row=2, column=0, sticky=self.Constants.center)
        self.__inside_label.grid(row=2, column=1, sticky=self.Constants.center)
        self.__outside_value.grid(row=3, column=0, sticky=self.Constants.center)
        self.__inside_value.grid(row=3, column=1, sticky=self.Constants.center)
        self.__bottom_text.grid(row=4, columnspan=2, sticky=self.Constants.center)

        for v in range(0, 2):
            self.rowconfigure(v, weight=True)
            self.columnconfigure(v, weight=True)

        button1 = Button(self, bg = "red", fg = "white", text=self.Constants.text_button_back, command=lambda: self.__did_tap_change_button(View.Main_View))
        button1.grid(row = 5, columnspan = 2, sticky = self.Constants.center)

    def __did_tap_change_button(self, view):
        if self.__change_view_handler is None:
            return
        self.__change_view_handler(view)
        self.Constants.manual_mode = False

    def act(self):
        self.__top_text.config(text="Active", bg="#000099")
        self.__activate.config(text="Deactivate", bg="red", command=self.deact)
        self.__inside_label.config(text="Inside", bg="black", fg="white")
        self.__outside_label.config(text="Outside", bg="white", fg="black")
        self.is_active = True

    def deact(self):
        self.__top_text.config(text="Alarm Control", bg="#666699")
        self.__activate.config(text="Activate", bg="black", command=self.act)
        self.__inside_label.config(text="Deactivated", bg="#666699", fg="black")
        self.__outside_label.config(text="Alarm", bg="#666699", fg="black")
        self.__outside_value.config(text=" ", bg="#666699")
        self.__inside_value.config(text=" ", bg="#666699")
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

        smtp.sendmail(email, reciever, email_msg)

        smtp.quit()
        print("Email sent")

    def manage_outside(self, outs):
        text = "{} cm".format(outs)
        if int(outs) > 150:
            self.__outside_value.config(text=text, bg="green")
        if int(outs) in range(50, 149):
            self.__outside_value.config(text=text, bg="yellow")
        if int(outs) < 50:
            self.__outside_value.config(text=text, bg="red")
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

        smtp.sendmail(email, reciever, email_msg)

        smtp.quit()
        print("Email sent")

    def manage_inside(self, ins):
        move = abs(self.current_pos - int(ins))
        text = "{} cm".format(move)
        if move < 10:
            self.__inside_value.config(text="leve " + text, bg="green")
        if move in range(10, 30):
            self.__inside_value.config(text="moderado " + text, bg="yellow")
            self.inside_count += 1
        if move > 30:
            self.__inside_value.config(text="grave " + text, bg="red")
            self.inside_count += 2
            if self.inside_count > 50 and self.inside_send == False:
                self.send_noti_in()
                self.inside_count = -10000
                self.inside_send = True
        print(self.inside_count)
        self.current_pos = int(ins)

    def sec(self, outs, ins):
        if self.is_active == False:
            pass
        else:
            self.manage_outside(outs)
            self.manage_inside(ins)
