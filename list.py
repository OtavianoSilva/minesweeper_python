from tkinter import *
from pickle import *

class ListPage(Tk):
    PADX = 10
    PADY = 10
    FONT = ("TimesNewRoman", "14", "bold")

    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        try:
            with open("usuarios.txt", "rb") as archive:
                users = [x for x in load(archive)]
                self.Y = len(users) + 1
        except: 
            with open("usuarios.txt", "wb") as archive:
                dump([], archive)
                self.Y = 1

        self.title = "Login"
        self.geometry(f"450x{self.Y*30}")

        self.title = "List"

        with open("usuarios.txt", "rb") as archive:
            users = [x for x in load(archive)]
            for x in users:
                item = Label(self, text=f"{x.name}", font=self.FONT)
                item.pack()
        self.mainloop()

        