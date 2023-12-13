from tkinter import *

class Profile(Tk):
    
    PADX = 10
    PADY = 15
    FONT = ("TimesNewRoman", "14", "bold")
    BG = "gray60"

    def __init__(self, current_player) -> None:
        Tk.__init__(self)

        self.current_player = current_player

        self.title = "Profile"
        self.geometry("350x450")
        self.config(bg='gray60')

        self.main_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.main_frame.pack()

        self.title_label = Label(self.main_frame, text="Perfil do usuário:", font=self.FONT, bg=self.BG)
        self.title_label.pack()

        self.name_label = Label(self.main_frame, text=f"{self.current_player.name}", font=self.FONT, bg=self.BG)
        self.name_label.pack()
