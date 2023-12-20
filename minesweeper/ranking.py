from tkinter import *
from pickle import *

class Ranking(Tk):
    
    PADX = 10
    PADY = 15
    FONT = ("TimesNewRoman", "14", "bold")
    BG = "gray60"

    def __init__(self, current_player) -> None:
        Tk.__init__(self)

        self.geometry("350x450")
        self.config(bg='gray60')

        self.current_player = current_player

        self.buttons_frame = Frame(self, bg='gray60', padx=self.PADX,pady=self.PADY*8)
        self.buttons_frame.pack()

        self.rank_easy_button = Button(self.buttons_frame, text="Rank Easy games", font=self.FONT, bg=self.BG)
        self.rank_easy_button["command"] = lambda mode = "easy": self.show_rank(mode)
        self.rank_easy_button.pack()

        self.rank_medium_button = Button (self.buttons_frame, text="Rank Medium games", font=self.FONT, bg=self.BG)
        self.rank_medium_button["command"] = lambda mode = "medium": self.show_rank(mode)
        self.rank_medium_button.pack()

        self.rank_hard_button = Button(self.buttons_frame, text="Rank Hard games", font=self.FONT, bg=self.BG)
        self.rank_hard_button["command"] = lambda mode = "hard": self.show_rank(mode)
        self.rank_hard_button.pack()

    def show_rank(self, mode:str) -> None:
        self.buttons_frame.destroy()
        self.rank_frame = Frame(self,bg='gray60', padx=self.PADX,pady=self.PADY*8)
        self.rank_frame.pack()

        self.title_label = Label(self.rank_frame, text=f"Melhores jogos {mode}", bg=self.BG)

        try:
            with open("usuarios.txt", "rb") as archive:
                users = [x for x in load(archive)]
                bast_game = self.current_player
                length = 3 if len(users) > 3 else len(users)
                for x in range(length):
                    bast_game = min(users, key=lambda user: user.bast_game[mode])
                    bast_game_label = Label(self.rank_frame, text=f"{bast_game.name} - {self.current_player.bast_game[mode]:.2f} minutos" if self.current_player.bast_game[mode] < 100000 else "Sem dados",
                                            font=self.FONT, bg=self.BG)
                    bast_game_label.pack()
                    users.remove(bast_game)
        except Exception as error:
            print(f"Erro de {error}")   
