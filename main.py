from tkinter import *
from user.signup import SignUpPage
from user.login import LoginPage

class Menu(Tk):
    
    PADX = 10
    PADY = 15
    FONT = ("TimesNewRoman", "14", "bold")

    def __init__(self) -> None:
        Tk.__init__(self)
        self.title = "Menu"
        self.geometry("350x450")
        self.config(bg='gray60')

        self.main_frame = Frame(self, padx=self.PADX, pady=self.PADY*9, bg='gray60')
        self.main_frame.pack()

        self.label_header = Label(self.main_frame, text="Você...", font=self.FONT, padx=self.PADX, pady=self.PADY, bg='gray60')
        self.label_header.pack()

        self.login_button = Button(self.main_frame, text="Já possuo uma conta", font=self.FONT, padx=self.PADX, pady=self.PADY, bg='gray65')
        self.login_button["command"] = LoginPage
        self.login_button.pack()

        self.sigup_button = Button(self.main_frame, text="Quero me registrar", font=self.FONT, padx=self.PADX, pady=self.PADY, bg='gray65')
        self.sigup_button["command"] = SignUpPage
        self.sigup_button.pack()
        self.mainloop()

if __name__ == '__main__':
    menu = Menu()