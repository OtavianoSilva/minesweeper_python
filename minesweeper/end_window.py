from minesweeper.game import Game
from os.path import dirname, realpath
from subprocess import call
from time import time
from tkinter import *

class EndWindow(Tk):
    def __init__(self, win: bool, board, current_player) -> None:
        super().__init__()
        self.board = board

        game = Game(self.board.stopwatch.count, self.board.difficulty, current_player, win)
        current_player.save_game(game)

        self.title('Vitória! ' if win else 'Derrota!')
        text: Label = Label(self, text='Você ganhou! ' if win else 'Você perdeu!').pack()
        runtime = Label(self, text=f'Com um tempo de {(self.board.stopwatch.count):.2f} segundos').pack()
        restart_button: Button = Button(self, text='Iniciar um novo jogo: ', command=
                                    self._restart).pack()

        self.mainloop()

    def _restart(self) -> None:
        try:
            self.destroy()
            self.board.destroy()
            call(str(dirname(realpath(__file__))) + '/minesweeper.py' , shell=True)
        except:
            call('minesweeper.exe', shell=True)
        
    def _main(self):
        self.mainloop()
