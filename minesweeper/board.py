from tkinter import *
from random import randint
from minesweeper.end_window import EndWindow
from minesweeper.stopwatch import Stopwatch

class Board(Tk):
    def __init__(self, board: list[int], button_size: int, mines_amount: int, mode:str, player: object) -> None:
        super().__init__()

        self.stopwatch      = Stopwatch(self.update_counter_label)
        self.current_player = player
        self.difficulty     = mode

        self.board: list[int]   = board
        self.mines_amount: int  = mines_amount
        self.flags_amount: int  = mines_amount
        self.button_size: int   = button_size

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

    def _check_if_won(self):
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
            self.stopwatch.stop_count()
            return EndWindow(True, self, self.current_player)

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
        self._check_if_won()

    def _button_action(self, event, target_button: Button, right_click: bool = False) -> None:

        if not self.stopwatch.is_counting: self.stopwatch.start_count()

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
            self._decrease_flag_counter()

        elif right_click and self.flag_matrix[target_x][target_y] == 'flag':
            self.flag_matrix[target_x][target_y] = 'close'
            target_button['bg'] = 'gray'
            self._increase_flag_counter()

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
            self.stopwatch.stop_count()
            lose = EndWindow(False, self, self.current_player)

        self._check_if_won()

    def update_counter_label(self, number: int) -> None:
        if isinstance(number, int): self.time_counter_label.config(text=str(number))

    def _create_stopwatch(self) -> None:
        self.stopwatch_frame: Frame = Frame(self.header_frame, height=50, width=60, bg='gray85')
        self.stopwatch_frame.place(x=110, y=10)

        self.time_counter_label: Label = Label(self.header_frame, text=str(0), font=('Proggy Square', 15), bg='gray85')
        self.time_counter_label.place(x=130, y=25)

    def _create_flag_counter(self) -> None:
        self.flag_counter_frame: Frame = Frame(self.header_frame, height=50, width=60, bg='gray85')
        self.flag_counter_frame.place(x=10,y=10)

        self.flag_counter_label: Label = Label(self.flag_counter_frame, text=self.flags_amount, font=('Proggy Square', 15), bg='gray85')
        self.flag_counter_label.place(x=17, y=12)

    def _decrease_flag_counter(self) -> None:
        self.flags_amount -= 1
        self.flag_counter_label.config(text=self.flags_amount)

    def _increase_flag_counter(self) -> None:
        self.flags_amount += 1
        self.flag_counter_label.config(text=self.flags_amount)

    def _create_header(self) -> None:
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
        self._create_mine_matrix()
        self._numbers_mine_matrix()
        self._create_flag_matrix()
        self._put_buttons_in_frame()

    def _main(self):
        self.mainloop()
