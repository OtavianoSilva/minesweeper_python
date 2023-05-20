from subprocess import call
from time import time
from tkinter import *
from random import randint

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

class Board(Tk):
    def __init__(self, board: list[int], button_size: int, mines_amount: int) -> None:
        super().__init__()
        self.board: list[int] = board
        self.mines_amount: int = mines_amount
        self.flags_amount: int = mines_amount
        self.button_size: int = button_size
        self.start_time: time = time()

        self.x: int = board[1] * button_size
        self.y: int = board[0] * button_size

        self.button_matrix: list[Button] = []
        self.mine_matrix: list[int]      = []
        self.flag_matrix: list[str]      = []

        self.header_frame: Frame = Frame(self, height=70, width=self.y, bg='gray70')
        self.header_frame.pack()
        self.board_game_frame: Frame = Frame(self, height=self.x, width=self.y)
        self.board_game_frame.pack()

        self.title('Minesweeper')
        self.geometry(f'{self.x}x{self.y+70}')

        self._create_header()
        self._create_board()
        self._main()

    def _open_neighbors(self, line: int, column: int) -> None:
        control: set = -1, 0, 1
        for line_control in control:
            for column_control in control:
                if (line == 0 or column == 0) and (line_control == -1 or column_control == -1): continue
                try:
                    neighbor_button: Button = self.button_matrix[line+line_control][column+column_control]
                    if self.flag_matrix[line+line_control][column+column_control] != 'close': continue
                    if self.mine_matrix[line+line_control][column+column_control] < 8:
                        number = self.mine_matrix[line+line_control][column+column_control]
                        self.flag_matrix[line+line_control][column+column_control] = 'open'
                        neighbor_button['text'] = (f'{number}' if number != 0 else '')
                        neighbor_button['bg'] = 'gray85'
                        neighbor_button['font'] =  ('Proggy Square', 12)
                        neighbor_button['fg'] = 'black'
                        if self.mine_matrix[line+line_control][column+column_control] == 0:
                            self._open_neighbors(line+line_control, column+column_control)
                except:
                    continue
        win = True
        for line in self.flag_matrix:
            if 'close' in line:
                win = False
                break
        if win:
            for line_number in range(self.board[0]):
                for column_number in range(self.board[1]):
                    mine_button = self.button_matrix[line_number][column_number]
                    if self.mine_matrix[line_number][column_number] >= 9:
                        mine_button['bg'] = 'green'
                    mine_button['state'] = DISABLED
            win = EndWindow(True, self)

    def _button_action(self, event, target_button: Button, right_click: bool = False) -> None:
        # self.stopwatch.start_cont()

        target_x:int = -1
        target_y:int = -1

        for line_number in range(self.board[1]):
            for column_number in range(self.board[0]):
                if self.button_matrix[line_number][column_number] == target_button:
                    target_x = line_number
                    target_y = column_number

        if right_click and (self.flag_matrix[target_x][target_y] == 'close' or self.flag_matrix[target_x][target_y] == 'mine'):
            self.flag_matrix[target_x][target_y] = 'flag'
            target_button['bg'] = 'blue'
            self._increase_flag_counter()

        elif right_click and self.flag_matrix[target_x][target_y] == 'flag':
            self.flag_matrix[target_x][target_y] = 'close'
            target_button['bg'] = 'gray'
            self._decrease_flag_counter()

        elif self.flag_matrix[target_x][target_y] == 'close' and self.mine_matrix[target_x][target_y] < 8:
            number = self.mine_matrix[target_x][target_y]
            self.flag_matrix[target_x][target_y] = 'open'
            target_button['bg'] = 'gray85'
            target_button['text'] = (f'{number}' if number != 0 else '')
            target_button['font'] =  ('Proggy Square', 12)
            target_button['fg'] = 'black'
            if self.mine_matrix[target_x][target_y] == 0:
                self._open_neighbors(target_x, target_y)

        elif self.mine_matrix[target_x][target_y] > 8 and self.flag_matrix[target_x][target_y] != 'flag':
            for line_number in range(self.board[0]):
                for column_number in range(self.board[1]):
                    mine_button = self.button_matrix[line_number][column_number]
                    if self.mine_matrix[line_number][column_number] >= 9:
                        mine_button['bg'] = 'red'
                    mine_button['state'] = DISABLED
            lose = EndWindow(False, self)

        win = True
        for line in self.flag_matrix:
            if 'close' in line:
                win = False
                break
        if win:
            for line_number in range(self.board[0]):
                for column_number in range(self.board[1]):
                    mine_button = self.button_matrix[line_number][column_number]
                    if self.mine_matrix[line_number][column_number] >= 9:
                        mine_button['bg'] = 'green'
                    mine_button['state'] = DISABLED
                    # self.stopwatch.stop_cont()
            win = EndWindow(True, self)

    def _create_stopwatch(self):
        pass

    def _create_flag_counter(self):
        self.flag_counter_frame: Frame = Frame(self.header_frame, height=50, width=60, bg='gray85')
        self.flag_counter_frame.place(x=10,y=10)

        self.flag_counter_label: Label = Label(self.flag_counter_frame, text=self.flags_amount, font=('Proggy Square', 15), bg='gray85')
        self.flag_counter_label.place(x=17, y=12)

    def _decrease_flag_counter(self):
        self.flags_amount += 1
        self.flag_counter_label.config(text=self.flags_amount)

    def _increase_flag_counter(self):
        self.flags_amount -= 1
        self.flag_counter_label.config(text=self.flags_amount)

    def _create_header(self):
        self._create_stopwatch()
        self._create_flag_counter()

    def _create_mine_matrix(self) -> None:
        for line_number in range(self.board[1]):
            new_mine_line = []
            for column_number in range(self.board[0]):
                new_mine_line.append(0)
            self.mine_matrix.append(new_mine_line)

        for mine in range(self.mines_amount):
            while True:
                mine_x: int = randint(0, self.board[1]-1)
                mine_y: int = randint(0, self.board[0]-1)
                if self.mine_matrix[mine_x][mine_y] < 8:
                    self.mine_matrix[mine_x][mine_y] = 9
                    break

    def _numbers_mine_matrix(self) -> None:
        control: set = (-1, 0, 1)
        for line in range(self.board[1]):
            for column in range(self.board[0]):
                if self.mine_matrix[line][column] > 8:
                    for line_control in control:
                        for column_control in control:
                            if not (line_control == column_control == 0):
                                r, c = line+line_control, column+column_control
                                if (0 <= r < self.board[1]) and (0 <= c < self.board[0]):
                                    self.mine_matrix[r][c] += 1

    def _create_flag_matrix(self) -> None:
        for line_number in range(self.board[1]):
                new_flag_line: list = []
                for column_number in range(self.board[0]):
                    if self.mine_matrix[line_number][column_number] >= 9:
                        new_flag_line.append('mine')
                    else: new_flag_line.append('close')
                self.flag_matrix.append(new_flag_line)

    def _put_buttons_in_frame(self) -> None:
        for line in range(self.board[1]):
            new_button_line: list = []
            for column in range(self.board[0]):
                new_button = Button(self.board_game_frame, text=' ', bg='gray')
            
                new_button.bind('<Button-1>', lambda event, new_button = new_button:
                                self._button_action(event, new_button))
                new_button.bind('<Button-3>', lambda event, new_button = new_button:
                                self._button_action(event, new_button, right_click=True))

                new_button.place(x=line * self.button_size, y=column * self.button_size,
                                height= self.button_size, width= self.button_size)
                new_button_line.append(new_button)
            self.button_matrix.append(new_button_line)

    def _create_board(self) -> None:
        #self.stopwatch = StopwatchWidget(self)
        self._create_mine_matrix()
        self._numbers_mine_matrix()
        self._create_flag_matrix()
        self._put_buttons_in_frame()

    def _main(self):
        self.mainloop()

class StopwatchWidget(Tk):
    def __init__(self, master) -> None:
        self.runing: bool = False

        self.frame: Frame = Frame(master)
        self.frame.pack()
        self.cont_timer: int = 0
        
        self._create_stopwatch()

    def _create_stopwatch(self) -> None:
        self.lable_cont: Label = Label(self.frame, text=self.cont_timer)
        self.lable_cont.pack()

    def start_cont(self) -> None:
        self.runing: bool = True
        self._cont()

    def stop_cont(self) -> None:
        self.runing: bool = False

    def _cont(self) -> None:
        if self.runing:
            self.lable_cont.config(text=self.cont_timer+1)
            self.lable_cont.after(1000, self._cont)

    def _get_conut(self) -> int:
        return self.cont_timer

class EndWindow(Tk):
    def __init__(self, win: bool, board: Board) -> None:
        super().__init__()
        self.board = board

        final_time = (time()-board.start_time) if (time()-board.start_time)/60 < 1 else (time()-board.start_time)/60

        self.title('Vitória! ' if win else 'Derrota!')
        text: Label = Label(self, text='Você ganhou! ' if win else 'Você perdeu!').pack()
        runtime = Label(self, text=f'Com um tempo de {final_time:.2f}'+(' segundos' if final_time/60 < 1 else ' minutos')).pack()
        restart_button: Button = Button(self, text='Iniciar um novo jogo: ', command=
                                    self._restart).pack()

        self.mainloop()

    def _restart(self) -> None:
        try:
            self.destroy()
            self.board.destroy()
            call('minesweeper.py', shell=True)
        except:
            call('minesweeper.exe', shell=True)
        
    def _main(self):
        self.mainloop()

if __name__ == '__main__':
    menu = Menu()