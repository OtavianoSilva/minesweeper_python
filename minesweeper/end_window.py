from os.path import dirname, realpath
from subprocess import call
from time import time
from tkinter import *

class EndWindow(Tk):
    def __init__(self, win: bool, board) -> None:
        super().__init__()
        self.board = board

        final_time = (time()-board.start_time)

        self.title('Vitória! ' if win else 'Derrota!')
        text: Label = Label(self, text='Você ganhou! ' if win else 'Você perdeu!').pack()
        runtime = Label(self, text=f'Com um tempo de {(final_time/60):.2f} minutos').pack()
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
