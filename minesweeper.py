from tkinter import *
from random import randint

### Definições ###

def game_mode(menu: Tk, mode:str):
    global board, mines_amount
    if mode == 'easy':
        board = [9, 9]
        mines_amount = 10
    elif mode == 'medium':
        board = [16, 16]
        mines_amount = 40
    elif mode == 'hard':
        board = [16, 32]
        mines_amount = 99
    menu.destroy()

def lose() -> None:
    for line_number in range(board[0]):
        for column_number in range(board[1]):
            if mine_matrix[line_number][column_number] > 9:
                mine_button = button_matrix[line_number][column_number]
                mine_button['bg'] = 'red'
            else: 
                mine_button = button_matrix[line_number][column_number]
            mine_button['state'] = DISABLED

    lose_window = Tk()
    lose_text = Label(lose_window, text='Você perdeu! ').pack()
    lose_window.mainloop()

def open_neighbors(line: int, column: int) -> None:
    # Função recursiva para abrir os botões vizinhos
    control = -1, 0, 1
    for line_control in control:
        for column_control in control:
            if (line == 0 or column == 0) and (line_control == -1 or column_control == -1): continue
            try:
                neighbor_button = button_matrix[line+line_control][column+column_control]
                if flag_matrix[line+line_control][column+column_control] != 'close': continue
                if mine_matrix[line+line_control][column+column_control] < 8:
                    flag_matrix[line+line_control][column+column_control] = 'open'
                    neighbor_button['text'] = f'{mine_matrix[line+line_control][column+column_control]}'
                    neighbor_button['bg'] = 'gray70'
                    neighbor_button['font'] =  ('Proggy Square', 12)
                    neighbor_button['fg'] = 'white'
                    if mine_matrix[line+line_control][column+column_control] == 0:
                        open_neighbors(line+line_control, column+column_control)
            except:
                continue

def button_action(event, target_button:Button, right_click: bool = False) -> None:
    target_x:int = -1
    target_y:int = -1

    for line_number in range(board[0]):
        for column_number in range(board[1]):
            if button_matrix[line_number][column_number] == target_button:
                target_x = line_number
                target_y = column_number

    if right_click and flag_matrix[target_x][target_y] == 'close':
        flag_matrix[target_x][target_y] = 'flag'
        target_button['bg'] = 'blue'

    elif right_click and flag_matrix[target_x][target_y] == 'flag':
        flag_matrix[target_x][target_y] = 'close'
        target_button['bg'] = 'gray'

    elif flag_matrix[target_x][target_y] == 'close' and mine_matrix[target_x][target_y] < 8:
        flag_matrix[target_x][target_y] = 'open'
        target_button['bg'] = 'gray70'
        target_button['text'] = f'{mine_matrix[target_x][target_y]}'
        target_button['font'] =  ('Proggy Square', 12)
        target_button['fg'] = 'white'
        if mine_matrix[target_x][target_y] == 0:
            open_neighbors(target_x, target_y)

    elif mine_matrix[target_x][target_y] > 8 and flag_matrix[target_x][target_y] != 'flag':
        lose()

    print(f'{target_x}, {target_y}')


### Menu de seleção ###

menu: Tk = Tk()
menu_text: Label = Label(menu, text='Bem vindo ao campo minado\nEscolha seu modo de jogo:')
menu_text.pack()

easy_button: Button = Button(menu, text='Easy mode\n9x9\n10 mianas',command=lambda
                             menu= menu,mode = 'easy': game_mode(menu, mode)).pack()
medium_button: Button = Button(menu, text='Medium mode\n16x16\n40 minas', command=lambda
                               menu= menu,mode = 'medium': game_mode(menu, mode)).pack()
hard_button: Button = Button(menu, text='Hard mode\n16x30\n99 minas', command=lambda
                             menu= menu, mode = 'hard': game_mode(menu, mode)).pack()

menu.mainloop()

# Definições do jogo
button_size: int = 32
x:int = board[1] * button_size # padronizar x para linha
y:int = board[0] * button_size # e y para colunas

# Definições Tk
window: Tk = Tk()
window.geometry(f'{x}x{y}')

# Matrizes
button_matrix:list = [] # Armazena todos os botões
mine_matrix:list = [] # Armazena as posições das minas e os númros
flag_matrix:list = [] # Armazena as posições das bandeiras e botões abertos

#cria matriz das minas
for line_number in range(board[0]):
        new_mine_line = []
        for column_number in range(board[1]):
            new_mine_line.append(0)
        mine_matrix.append(new_mine_line)
del new_mine_line

# arma matriz das minas
for mine in range(mines_amount):
    while True:
        mine_x = randint(0, board[0]-1)
        mine_y = randint(0, board[1]-1)
        if mine_matrix[mine_x][mine_y] < 8:
            mine_matrix[mine_x][mine_y] = 9
            break

# Adiciona os números de proximidade de minas
control = -1, 0, 1
for line in range(board[1]):
    for column in range(board[0]):
        if mine_matrix[line][column] > 8:
            for line_control in control:
                for column_control in control:
                    if (line == 0 or column == 0) and (line_control == -1 or column_control == -1): continue
                    try: mine_matrix[line+line_control][column+column_control] += 1
                    except: pass
del control

# Cria matriz das bandeiras
for line_number in range(board[0]):
        new_flag_line = []
        for column_number in range(board[1]):
            new_flag_line.append('close')
        flag_matrix.append(new_flag_line)
del new_flag_line

# Cria matriz com todos os botões
for line in range(board[0]):
    new_button_line = []
    for column in range(board[1]):
        new_button = Button(window,text=' ', bg='gray')
    
        new_button.bind('<Button-1>', lambda event, new_button = new_button:
                        button_action(event, new_button))
        new_button.bind('<Button-3>', lambda event, new_button = new_button:
                        button_action(event, new_button, right_click=True))

        new_button.place(x=column * button_size, y=line * button_size,
                         height= button_size, width= button_size)
        new_button_line.append(new_button)
    button_matrix.append(new_button_line)

for x in range(0, board[0]):
    print(mine_matrix[x])

window.mainloop()
