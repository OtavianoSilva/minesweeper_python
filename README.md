# Projeto Campo Minado
## Descrição
    Este projeto é uma implementação do clássico jogo Campo Minado em Python, utilizando a biblioteca Tkinter para a interface gráfica. O Campo Minado é um jogo de lógica em que o jogador deve descobrir células em um campo sem acertar as minas escondidas.

## Funcionalidades
### Interface Gráfica:
    O jogo possui uma interface gráfica intuitiva, onde os jogadores podem interagir facilmente com o campo minado.

### Níveis de Dificuldade:
    Oferece diferentes níveis de dificuldade, permitindo aos jogadores escolherem entre iniciante, intermediário e avançado, ajustando o tamanho do campo e o número de minas.
    Marcação de Minas: Os jogadores podem marcar as células suspeitas de conterem minas, facilitando a visualização do campo.

## Como Jogar
### Iniciar o Jogo:
* Execute o programa crie uma conta, ou faça login caso já possua uma, selecione a dificuldade do jogo e se divirta.

* Jogar: Clique nas células para revelar o conteúdo. Se uma mina for acertada, o jogo termina. Caso contrário, continue até revelar todas as células seguras.

* Marcação de Minas: Utilize o botão direito do mouse para marcar as células suspeitas de conterem minas.

* Vitória ou Derrota: O jogo termina quando todas as células seguras são reveladas (vitória) ou quando uma mina é acertada (derrota).

## Requisitos
1. Python 3.x
2. Tkinter (normalmente já vem instalada no Python)

## Instalação e Execução
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


### Da lógica do campo minado:

### Da serialização dos dados:


## Contribuições
