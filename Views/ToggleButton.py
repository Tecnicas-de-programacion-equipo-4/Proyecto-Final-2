from tkinter import Label, PhotoImage

class ToggleButton(Label):

    class Constants:
        on_file = "Assets/ON.ppm"
        off_file = "Assets/OFF.ppm"
        event = "<Button-1>"

    def __init__(self, master, room_name, tap_toggle_handler = None, action = None):
        super().__init__(master)
        self.__tap_handler = tap_toggle_handler
        self.__room_name = room_name
        self.__action = action
        self.__state = False
        self.__on_image = PhotoImage(file = self.Constants.on_file)
        self.__off_image = PhotoImage(file = self.Constants.off_file)
        self.__set_image(self.__off_image)
        self.bind(self.Constants.event, self.__toggle)

    def __toggle(self, event):
        self.__state = not self.__state
        image = self.__on_image if self.__state else self.__off_image
        self.__set_image(image)

        if self.__tap_handler is None: return
        self.__tap_handler(self.__state)
        self.__action(self.__room_name)
        print("{}, {}".format(self.__state, self.__room_name))


    def __set_image(self, image):
        self.configure(image = image)
        self.image = image