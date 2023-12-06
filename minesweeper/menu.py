from tkinter import *
from random import randint
from minesweeper.board import Board

class Menu(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Menu')
        self.geometry('300x400')
        self.config(bg='gray60')
        
        self._create_buttons()
        self._create_examples()
        self._main()

    def _create_board(self, mode):
        if mode == 'easy':
            board = [9, 9]
            button_size = 32
            mines_amount = 10
            self.destroy()
            game = Board(board, button_size, mines_amount)
        elif mode == 'medium':
            board = [16, 16]
            button_size = 32
            mines_amount = 40
            self.destroy()
            game = Board(board, button_size, mines_amount)
        elif mode == 'hard':
            board = [26, 26]
            button_size = 26
            mines_amount = 99
            self.destroy()
            game = Board(board, button_size, mines_amount)

    def _create_buttons(self):

        menu_text: Label = Label(self, text='Bem vindo ao campo minado\nEscolha seu modo de jogo:', bg='gray60')
        menu_text.pack()

        easy_button: Button =   Button(self, text='Easy mode\n9x9\n10 mianas', bg='gray65',command=lambda
                                menu= self, mode = 'easy': self._create_board(mode)).pack()
        medium_button: Button = Button(self, text='Medium mode\n16x16\n40 minas', bg='gray65', command=lambda
                                menu= self, mode = 'medium': self._create_board(mode)).pack()
        hard_button: Button =   Button(self, text='Hard mode\n26x26\n99 minas', bg='gray65', command=lambda
                                menu= self, mode = 'hard': self._create_board(mode)).pack()
        
    def _example_mine_action(self, event, target_button: Button) -> None:
        if target_button['bg'] != 'blue':
            target_button['bg'] = 'red'
            target_button['state'] = DISABLED

    def _example_flag_action(self, event, target_button: Button) -> None:
        if target_button['bg'] == 'blue':
            target_button['bg'] = 'gray'
        else: target_button['bg'] = 'blue'

    def _example_number_action(self, target_button: Button) -> None:
        target_button['bg'] = 'gray85'
        target_button['text'] = f'{(randint(1, 7))}'
        target_button['font'] =  ('Proggy Square', 12)
        target_button['fg'] = 'black'

    def _create_examples(self):
        example_mine_button: Button = Button(self, bg='gray')
        example_mine_button.place(x=35, y=250, height= 32, width= 32)
        example_mine_button.bind('<Button-1>', lambda event, button = example_mine_button:
                                self._example_mine_action(event, target_button= button))
        example_mine_text: Label = Label(self, text='Ao tocar com o botão esquerdo\nem uma mina, você perde.', bg='gray60')
        example_mine_text.place(x=72, y=250)

        example_flag_button: Button = Button(self, bg='gray')
        example_flag_button.place(x=35, y=290, height= 32, width= 32)
        example_flag_button.bind('<Button-1>', lambda event, button = example_flag_button:
                                self._example_mine_action(event= event, target_button= button))
        example_flag_button.bind('<Button-3>', lambda event, button = example_flag_button:
                                self._example_flag_action(event= event, target_button= button))
        example_flag_text: Label = Label(self, text='Ao tocar com o botão direito\numa bandeira bloqueará o bloco', bg='gray60')
        example_flag_text.place(x=72, y=290)

        example_number_button: Button = Button(self, bg='gray')
        example_number_button.place(x=35, y=330, height= 32, width= 32)
        example_number_button["command"] = lambda button = example_number_button: self._example_number_action(button)
        example_number_text: Label = Label(self, text=' E ao tocar com o botão esquerdo\nonde não há mina, o número de minas\npróximas é revelado', bg='gray60')
        example_number_text.place(x=72, y=330)
    
    def _main(self):
        self.mainloop()