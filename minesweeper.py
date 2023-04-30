from subprocess import call
from tkinter import *
from random import randint

def game_mode(menu: Tk, mode:str) -> None:
    # Define o modo de jogo
    global board, mines_amount
    if mode == 'easy':
        board = [9, 9]
        mines_amount = 10
    elif mode == 'medium':
        board = [16, 16]
        mines_amount = 40
    elif mode == 'hard':
        board = [21, 21]
        mines_amount = 99
    menu.destroy()

def restart(lose_window:Tk) -> None:
        # Reinicia o jogo
        window.destroy()
        lose_window.destroy()
        call('minesweeper.exe', shell=True)

def win_window() -> None:

    # marca todas as minas
    for line_number in range(board[0]):
        for column_number in range(board[1]):
            mine_button = button_matrix[line_number][column_number]
            if mine_matrix[line_number][column_number] >= 9:
                mine_button['bg'] = 'green'
            mine_button['state'] = DISABLED

    # Cria janela da vitória
    win_window: Tk = Tk()
    win_window.title('Vitória! ')
    lose_text: Label = Label(win_window, text='Você ganhou! ').pack()
    restart_button: Button = Button(win_window, text='Iniciar um novo jogo: ', command=
                                    lambda lose_window = win_window: restart(lose_window)).pack()
    win_window.mainloop()

def lose_window() -> None:
    # marca todas as minas
    for line_number in range(board[0]):
        for column_number in range(board[1]):
            mine_button = button_matrix[line_number][column_number]
            if mine_matrix[line_number][column_number] >= 9:
                mine_button['bg'] = 'red'
            mine_button['state'] = DISABLED

    # Cria janela de perda
    lose_window: Tk = Tk()
    lose_window.title('Derrota!')
    lose_text: Label = Label(lose_window, text='Você perdeu! ').pack()
    restart_button: Button = Button(lose_window, text='Iniciar um novo jogo: ', command=
                                    lambda lose_window = lose_window: restart(lose_window)).pack()
    lose_window.mainloop()

def open_neighbors(line: int, column: int) -> None:

    # Função recursiva para abrir os botões vizinhos
    control: set = -1, 0, 1
    for line_control in control:
        for column_control in control:
            if (line == 0 or column == 0) and (line_control == -1 or column_control == -1): continue
            try:
                neighbor_button: Button = button_matrix[line+line_control][column+column_control]
                if flag_matrix[line+line_control][column+column_control] != 'close': continue
                if mine_matrix[line+line_control][column+column_control] < 8:
                    number = mine_matrix[line+line_control][column+column_control]
                    flag_matrix[line+line_control][column+column_control] = 'open'
                    neighbor_button['text'] = (f'{number}' if number != 0 else '')
                    neighbor_button['bg'] = 'gray85'
                    neighbor_button['font'] =  ('Proggy Square', 12)
                    neighbor_button['fg'] = 'black'
                    if mine_matrix[line+line_control][column+column_control] == 0:
                        open_neighbors(line+line_control, column+column_control)
            except:
                continue
    win = True
    for line in flag_matrix:
        if 'close' in line:
            win = False
            break
    if win:
        win_window()

def button_action(event, target_button:Button, right_click: bool = False) -> None:

    target_x:int = -1
    target_y:int = -1

    for line_number in range(board[1]):
        for column_number in range(board[0]):
            if button_matrix[line_number][column_number] == target_button:
                target_x = line_number
                target_y = column_number

    if right_click and (flag_matrix[target_x][target_y] == 'close' or flag_matrix[target_x][target_y] == 'mine'):
        flag_matrix[target_x][target_y] = 'flag'
        target_button['bg'] = 'blue'

    elif right_click and flag_matrix[target_x][target_y] == 'flag':
        flag_matrix[target_x][target_y] = 'close'
        target_button['bg'] = 'gray'

    elif flag_matrix[target_x][target_y] == 'close' and mine_matrix[target_x][target_y] < 8:
        number = mine_matrix[target_x][target_y]
        flag_matrix[target_x][target_y] = 'open'
        target_button['bg'] = 'gray85'
        target_button['text'] = (f'{number}' if number != 0 else '')
        target_button['font'] =  ('Proggy Square', 12)
        target_button['fg'] = 'black'
        if mine_matrix[target_x][target_y] == 0:
            open_neighbors(target_x, target_y)

    elif mine_matrix[target_x][target_y] > 8 and flag_matrix[target_x][target_y] != 'flag':
        lose_window()

    win = True
    for line in flag_matrix:
        if 'close' in line:
            win = False
            break
    if win:
        win_window()


def test_mine(event, target_button: Button) -> None:
    if target_button['bg'] != 'blue':
        target_button['bg'] = 'red'
        target_button['state'] = DISABLED

def test_flag(event, target_button: Button) -> None:
    if target_button['bg'] == 'blue':
        target_button['bg'] = 'gray'
    else: target_button['bg'] = 'blue'

def test_number(target_button: Button) -> None:
    target_button['bg'] = 'gray85'
    target_button['text'] = f'{(randint(1, 7))}'
    target_button['font'] =  ('Proggy Square', 12)
    target_button['fg'] = 'black'

while True:

    ### Definições do menu ###
    menu: Tk = Tk()
    menu.title('Menu')
    menu.geometry('300x400')
    menu_text: Label = Label(menu, text='Bem vindo ao campo minado\nEscolha seu modo de jogo:')
    menu_text.pack()

    ### Botões de modo de jogo ###
    easy_button: Button =   Button(menu, text='Easy mode\n9x9\n10 mianas',command=lambda
                                menu= menu,mode = 'easy': game_mode(menu, mode)).pack()
    medium_button: Button = Button(menu, text='Medium mode\n16x16\n40 minas', command=lambda
                                menu= menu,mode = 'medium': game_mode(menu, mode)).pack()
    hard_button: Button =   Button(menu, text='Hard mode\n21x21\n99 minas', command=lambda
                                menu= menu, mode = 'hard': game_mode(menu, mode)).pack()

    ### Detalhes do jogo ###
    example_mine_button: Button = Button(menu, bg='gray')
    example_mine_button.place(x=35, y=250, height= 32, width= 32)
    example_mine_button.bind('<Button-1>', lambda event, button = example_mine_button:
                             test_mine(event, target_button= button))
    example_mine_text: Label = Label(menu, text='Ao tocar com o botão esquerdo\nem uma mina, você perde.')
    example_mine_text.place(x=72, y=250)

    example_flag_button: Button = Button(menu, bg='gray')
    example_flag_button.place(x=35, y=290, height= 32, width= 32)
    example_flag_button.bind('<Button-1>', lambda event, button = example_flag_button:
                             test_mine(event, target_button= button))
    example_flag_button.bind('<Button-3>', lambda event, button = example_flag_button:
                             test_flag(event, target_button= button))
    example_flag_text: Label = Label(menu, text='Ao tocar com o botão direito\numa bandeira bloqueará o bloco')
    example_flag_text.place(x=72, y=290)

    example_number_button: Button = Button(menu, bg='gray')
    example_number_button.place(x=35, y=330, height= 32, width= 32)
    example_number_button["command"] = lambda button = example_number_button: test_number(button)
    example_number_text: Label = Label(menu, text=' E ao tocar com o botão esquerdo\nonde não há mina, o número de minas\npróximas é revelado')
    example_number_text.place(x=72, y=330)


    menu.mainloop()

    ### Definições do jogo ###
    button_size: int = 32
    x:int = board[1] * button_size # padronizar x para linha
    y:int = board[0] * button_size # e y para colunas

    ### Definições Tk ###
    global window
    window: Tk = Tk()
    window.title('Minesweeper')
    window.geometry(f'{x}x{y}')

    ### Matrizes ###
    button_matrix:list[Button] = [] # Armazena todos os botões
    mine_matrix:list[int] = []      # Armazena as posições das minas e os númros
    flag_matrix:list[str] = []      # Armazena as posições das bandeiras e botões abertos

    # cria matriz das minas
    for line_number in range(board[1]):
            new_mine_line = []
            for column_number in range(board[0]):
                new_mine_line.append(0)
            mine_matrix.append(new_mine_line)
    del new_mine_line

    # arma matriz das minas
    for mine in range(mines_amount):
        while True:
            mine_x: int = randint(0, board[1]-1)
            mine_y: int = randint(0, board[0]-1)
            if mine_matrix[mine_x][mine_y] < 8:
                mine_matrix[mine_x][mine_y] = 9
                break

    # Adiciona os números de proximidade de minas
    control: set = (-1, 0, 1)
    for line in range(board[1]):
        for column in range(board[0]):
            if mine_matrix[line][column] > 8:
                for line_control in control:
                    for column_control in control:
                        if not (line_control == column_control == 0):
                            r, c = line+line_control, column+column_control
                            # Ter certeza que ambos os valores r e c são válidos
                            if (0 <= r < board[1]) and (0 <= c < board[0]):
                                mine_matrix[r][c] += 1

    # Cria matriz das bandeiras
    for line_number in range(board[1]):
            new_flag_line: list = []
            for column_number in range(board[0]):
                if mine_matrix[line_number][column_number] >= 9:
                    new_flag_line.append('mine')
                else: new_flag_line.append('close')
            flag_matrix.append(new_flag_line)
    del new_flag_line

    # Cria matriz com todos os botões
    for line in range(board[1]):
        new_button_line: list = []
        for column in range(board[0]):
            new_button = Button(window,text=' ', bg='gray')
        
            new_button.bind('<Button-1>', lambda event, new_button = new_button:
                            button_action(event, new_button))
            new_button.bind('<Button-3>', lambda event, new_button = new_button:
                            button_action(event, new_button, right_click=True))

            new_button.place(x=line * button_size, y=column * button_size,
                            height= button_size, width= button_size)
            new_button_line.append(new_button)
        button_matrix.append(new_button_line)

    window.mainloop()
    break
