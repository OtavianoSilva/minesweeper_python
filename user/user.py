from minesweeper.game import Game
from pickle import *
from time import time

class User():
    def __init__(self, name, birth_date, email, password) -> None:
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.__password = password

        self.bast_game = {
            'easy' :    time(),
            'medium' :  time(),
            'hard' :    time()
        }
        self.game_history = []

    def save_game(self, game):
        if isinstance(game, Game):
            if game.win and game.time < self.bast_game[game.dificulty]:
                self.bast_game[game.dificulty] = game.time
            self.game_history.append(game)
            try:
                with open("usuarios.txt", "rb") as archive:
                    self.data = [x for x in load(archive)]
                    for user in self.data:
                        if user.email == self.email:
                            self.data.remove(user)
                            self.data.append(self)
                            break
                    
                with open("usuarios.txt", "wb") as archive:
                    dump(self.data, archive)
                    self.data = None

            except Exception as error:
                print(f"Erro de : {error}")
 
        else:
            print("Valor errado para função")
    

    def edit_infos(self, name, birth, email, password):
        try:
            with open("usuarios.txt", "rb") as archive:
                self.data = [x for x in load(archive)]
                for user in self.data:
                    if user.email == self.email:
                        self.data.remove(user)

                        self.name = name
                        self.birth_date = birth
                        self.email = email
                        self.__password = password
                        
                        self.data.append(self)
                        break
                
            with open("usuarios.txt", "wb") as archive:
                dump(self.data, archive)
                self.data = None

        except Exception as error:
            print(f"Erro de : {error}")

    def delete(self) -> None:
        try:
            with open("usuarios.txt", "rb") as archive:
                self.data = [x for x in load(archive)]
                for user in self.data:
                    if user.email == self.email:
                        self.data.remove(user)
            with open("usuarios.txt", "wb") as archive:
                dump(self.data, archive)
                self.data = None
        except Exception as error:
            print(f"Erro de : {error}")

    def get_password(self):
        return self.__password