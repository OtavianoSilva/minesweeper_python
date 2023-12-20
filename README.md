# Projeto Campo Minado:
## Descrição:
Este projeto é uma implementação do clássico jogo Campo Minado em Python, utilizando a biblioteca Tkinter para a interface gráfica. O Campo Minado é um jogo de lógica em que o jogador deve descobrir células em um campo sem acertar as minas escondidas.

## Funcionalidades:
### Interface Gráfica:
O jogo possui uma interface gráfica intuitiva, onde os jogadores podem interagir facilmente com o campo minado.

### Níveis de Dificuldade:
Oferece diferentes níveis de dificuldade, permitindo aos jogadores escolherem entre iniciante, intermediário e avançado, ajustando o tamanho do campo e o número de minas.
Marcação de Minas: Os jogadores podem marcar as células suspeitas de conterem minas, facilitando a visualização do campo.

## Como Jogar:
### Iniciar o Jogo:
* Execute o programa crie uma conta, ou faça login caso já possua uma, selecione a dificuldade do jogo e se divirta.

* Jogar: Clique nas células para revelar o conteúdo. Se uma mina for acertada, o jogo termina. Caso contrário, continue até revelar todas as células seguras.

* Marcação de Minas: Utilize o botão direito do mouse para marcar as células suspeitas de conterem minas.

* Vitória ou Derrota: O jogo termina quando todas as células seguras são reveladas (vitória) ou quando uma mina é acertada (derrota).

## Requisitos ( Bibliotecas Python 3.x):
A maioria destas já vem instalada no python, mas caso não podem ser facilmente acessadas atráves do pip install.
1. Tkinter;
2. Random;
3. Time;
4. Pickle;
5. Os;
6. Subprocess.

## Instalação e Execução:
1. Clone o repositório para sua máquina local.
~~~Git
git clone https://github.com/seu-usuario/campo-minado.git
~~~
2. Navegue até o diretório do projeto.

~~~Shell
cd minesweeper_python
~~~
3. Execute o arquivo principal.
~~~Shell
python main.py
~~~

## Estrutura do projeto:

### Fluxo da aplicação:
![Aplication Workflow](minesweeper_python/AplicationWorkFlow.png "Aplication Workflow").

Partindo da pasta principal encontramos 3 arquivos (contando este readme) e duas pastas melhor detalhados adiante.
Os arquivos são respectivamente:
* main.py: Arquivo principal em que o usuario é direcionado para as telas de login ou cadastro, e:
* usuarios.txt: em que são salvos todos os usuários do sistema e todos os jogos registrados por eles.

Na pasta user estão todos os arquivos que gerenciam ou se relacionam diretamente com os usuários, como:

* login.py: que gerencia e valida o acesso dos usuários ao menu principal do jogo;
* profile.py: que permite o usuário editar suas informações, ver seu melhor jogo e deletar sua conta;
* signup.py: que gerencia os registros de novos usuáriose, e;
* user.py: que contem a classe de usuário do sistema, responsavel pelo gerenciamento individual de cada perfil.

A outra pasta é minesweeper, que contem a lógica e sistema pós-login:

* board.py: gêrencia o "tábuleiro" em que o jogo acontece, e todas as lógicas envolvidas nisto;
* end_window.py: é a janela de finalização de cada jogo, informa a vitória ou anúncia a derrota;
* game.py: contém a classe dos registros de cada jogo, se foi ganho e seu tempo de duração;
* menu.py: é o menu do jogo, dá as opções de dificuldade e possibilita o acesso ao perfil e ao ranking, e;
* ranking: que separando pelas dificuldade mostra o top 3 dos melhores jogos de cada categoria.

## Detalalhamento do funcionamento:
### Da interface gráfica:
Todo o sistema roda utilizando a biblioteca tkinter para interfaces gráficas com o paradigma orientado a objetos por meio de herança da classe Tk da biblioteca. Tratando os widgets e objetos que compões as telas como propriedades da classe. Exemplo do arquivo main.py:

~~~Python
...
class Menu(Tk):
    
    # Definições genéricas para evitar repetição.
    FONT = ("TimesNewRoman", "14", "bold")

    def __init__(self) -> None:
        Tk.__init__(self)
        # Definindo propriedades da janela.
        self.title = "Menu"
        self.geometry("350x450")
        self.config(bg='gray60')

        # Definindo objetos dentro da janela.
        self.main_frame = Frame(self, padx=self.PADX, pady=self.PADY*9, bg='gray60')
        self.main_frame.pack()
        ...
...
~~~

Em todos os arquivos que possuem alguma leitur de dados, como nas telas de cadastro e login, as entradas se não com o componenete Entry da própria biblioteca, exempo da entrada e extração deste dado no arquivo signup.py:

~~~Python
...
def __init__(self, *args, **kwargs) -> None:
    ...
    self.password_frame = Frame(self, padx=self.PADX, pady=self.PADY, bg=self.BG)
    self.password_frame.pack()

    # Objeto que recebe a senha digitada.
    self.password_label = Label(self.password_frame, text="Senha", font=self.FONT, bg=self.BG)
    self.password_label.pack(side=LEFT)

    self.password_entry = Entry(self.password_frame, show='*')
    self.password_entry.pack(side=LEFT)
    ...
...
~~~

~~~Python
...
def validate(self) -> None:
    ...
    # Extração e comparação da senha com a senha de confirmação.
    elif self.password_entry.get() != self.conf_password_entry.get():
    self.messages_label["text"] = "As senhas não batem"
    ...
...
~~~

Também é utulizada a lógica disponibilizda pela biblioteca de poder alocar componentes a um frame, então manipular o frame e de efeito cascata afetar o que nele está contido, como no arquivo profile.py:
Um frame é criado mostrando algumas informações do usuário:

~~~Python
...
def __init__(self, current_player) -> None:
    ...
    self.main_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
    self.main_frame.pack()

    # Perceba que o master do Label é o Frame recém criado.
    self.title_label = Label(self.main_frame, text="Perfil do usuário:", font=self.FONT, bg=self.BG)
    self.title_label.pack()
    ...
...
~~~

Para então, quando o usuário interagir com está tela, evitando que outra janela seja aberta, este frame é destruído (levando junto tudo nele contido) e um novo é criado:

~~~Python
...
def set_edit_frame(self) -> None:
        # Removendo da tela o frame antigo.
        self.main_frame.destroy()

        # Criando um novo para adicionar novos objetos.
        name_entry_text = StringVar(self)
        name_entry_text.set(self.current_player.name)
        ...
...
~~~

O campo minado também funciona com objetos tkinter, a parte principal do campo, por exemplos são botões que mudam de cor, estado e chamam diferentes funções utilizando a propriede bind dos objetos tk que controla o que acontece com diferentes entradas (como por bandeiras com botão direito e abrir o campo com o esquerdo):

~~~Python
...
# Função que cria os botões e os coloca no campo para jogar.
def _put_buttons_in_frame(self) -> None:
    for line in range(self.board[1]):
        new_button_line: list = []
        for column in range(self.board[0]):
            new_button = Button(self.board_game_frame, text=' ', bg='gray')
        
            # Controle da entrada esquerda.
            new_button.bind('<Button-1>', lambda event, new_button = new_button:
                            self._button_action(event, new_button))
            # Controle da entrada direita.
            new_button.bind('<Button-3>', lambda event, new_button = new_button:
                            self._button_action(event, new_button, right_click=True))

            new_button.place(x=line * self.button_size, y=column * self.button_size,
                            height= self.button_size, width= self.button_size)
            new_button_line.append(new_button)
        self.button_matrix.append(new_button_line)
...
~~~

### Da lógica do campo minado:
Os arquivos do campo minado estão todos na pasta minesweeper, e eles desenpenham diferentes papéis no funcionamento do jogo, antes do jogo começar o usuáio escolhe a dificuldade do jogo (tamanho do campo e número de minas) na tela de Menu que logo inicializa o jogo:

~~~Python
...
def _create_board(self, mode):
    if mode == 'easy':
        board = [9, 9]
        button_size = 32
        mines_amount = 10
        # Cria um campo com as características selecionadas.
        game = Board(board, button_size, mines_amount, mode, self.current_player)
    ...
...
~~~

Board é o arquivo principal do jogo ele possuí uma classe hómonoma e se reponsábiliza por inicializar, e gerencia o fluxo do jogo, detalhado a seguir:

Logo no método construtor da classe já são inicializadas diversas váriveis de controle que servirão mais tarde para as lógicas do jogo, como uma matriz de bandeiras que armazena se os campos estão abertos/descobertos ou com bandeira, também a matriz numérica que armazena as posições das minas e os números que devem aparecer quando o usuário abre aquele determinado espaço. Junto disto outros aspectos do jogo como a inicialização do timer, assim como os contadores de minas e tamanho dos componentes.

~~~Python
    ...
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
    ...
~~~

Para a funcionálidade do código é utilizado, por exemplo, a biblioteca random para aleatorizar a colocação das minas no tabuleiro do jogo:

~~~Python
    ...
    for mine in range(self.mines_amount):
    while True:
        mine_x: int = randint(0, self.board[1]-1)
        mine_y: int = randint(0, self.board[0]-1)
        if self.mine_matrix[mine_x][mine_y] < 8:
            self.mine_matrix[mine_x][mine_y] = 9
            break
    ...
~~~

Por último no quesito lógicas do jogo, na função que gerência o processo de abrir mais de um bloco quando o usuário clica, foi utilizado recursão para encadear a abertura a todos os blocos possíveis:

~~~Python
...
def _open_neighbors(self, line: int, column: int) -> None:
        control: set = -1, 0, 1
        for line_control in control:
            for column_control in control:
                if (line == 0 or column == 0) and (line_control == -1 or column_control == -1): continue
                ...
                        # Chama a própia função para todas as posições próximas.
                        if self.mine_matrix[line+line_control][column+column_control] == 0:
                            self._open_neighbors(line+line_control, column+column_control)
                        ...
~~~

O último envolvido no jogo é o End_window que aparece quando o usuário ganha ou perde e ainda mostra seu tempo.

### Da serialização dos dados:
Isto acontece em vários níveis e em vários arquivos, mas, tudo é serializado e salvo no mesmo arquivo "usuarios.txt" utilizando os métodos da biblioteca pickle, exemplo no arquivo signup, em que os usuários são registrados, tomando os cuidados de se exitem ou não usuários prévios. A lista de usuários é resgatada, um novo é adicionado então ela é escrita novamente, essa sinuca de bico é realizada para manter a integridade dos dados.

~~~Python
def save(self, user: User) -> None:
    try:
        # Resgata os dados armazenados.
        with open("usuarios.txt", "rb") as archive:
            self.data = load(archive)
            self.data.append(user)

    except EOFError:
        with open("usuarios.txt", "wb") as archive:
            dump(self.data, archive)

    # Reescreve o arquivo com o novo usuário.
    with open("usuarios.txt", "wb") as archive:
            dump(self.data, archive)
    self.messages_label["text"] = "Usuário cadastrado"
~~~

Todos os usuários salvos, tal qual os jogos realizados por eles são armazenados como objetos (suas definições esão respectivamente nos arquivos user.py e game.py) em que o objeto dos usuários possuí um dicionário para armazenar os melhores jogos de cada categôria e mais genéricamente uma lista para todos os outros jogos. Isto, na tela de End_window é criado uma instância de game que é logo associada a seu usuároi e gerenciado no próprio objeto:

~~~Python
def save_game(self, game):
    ...
    # Faz a verificação dos melhores jogos.
    if game.win and game.time < self.bast_game[game.dificulty]:
        self.bast_game[game.dificulty] = game.time
    self.game_history.append(game)
    try:
        ...
        # Salva os dados do usuário com o acrecio de do jogo.
        with open("usuarios.txt", "wb") as archive:
            dump(self.data, archive)
            self.data = None
        ...
    ...
~~~

Seguindo esta ordem de responsábilizar o objeto por ele mesmo, a janela profile (perfil) pode editar o usuário corrente ou deleta-lo, que novamente, acontece tudo dentro do próprio objeto:

~~~Python
def edit_infos(self, name, birth, email, password):
    ...

def delete(self) -> None:
    ...

# O atributo da senha é privado.
def get_password(self):
    return self.__password
~~~

Na página de ranking há uma busca precisa nos dados para traser os usuários e os jogos com menor tempo em uma determinada dificuldade de jogo, resolvido com uma lista, função min(), lambda e algumas remoções:

~~~Python
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
~~~

## Contribuições:
Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença:
Eu que fiz, mas pode usar. <3
