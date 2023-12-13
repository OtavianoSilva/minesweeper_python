from minesweeper.game import Game
from time import time

class User():
    def __init__(self, name, birth_date, email, password) -> None:
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.password = password

        self.bast_game = time()
        self.game_history = []

    def save_game(self, game):
        if isinstance(game, Game):
            if game.time > self.bast_game:
                self.bast_game = game
            self.game_history.append(game)
            print('deu certo ae')
        else:
            print("Valor errado para função")