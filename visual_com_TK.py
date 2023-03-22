from campo_minado import *
from tkinter import *
from tkinter.ttk import *

# Responsável por gerenciar os botões como objetos TK.
class BotaoTK():
    def __init__(self, master: Tk, bloco: Bloco) -> None:
        self.master:        Tk              = master    # A janela a qual o botão pertence,
        self.bloco:         Bloco           = bloco     # o bloco referenciado

    ### Métodos do Botao ###
    # Cria o botão como objeto Button
    def cria_botao_visual(self) -> None:
        imagem = self.define_imagem()        

        self.botao = Button(self.master, image=imagem)
        self.botao.grid(column=self.bloco.coluna, row=self.bloco.linha+1)
        if not self.bloco.bandeira:
            self.botao.bind('<Button-1>', self.revela_botao)            # Ao toque direito, abre o botão,
            self.botao.bind('<Button-3>', self.adiciona_bandeira_botao) # ao toque esquerdo, adiciona bandeira.
        else:                                                           # E caso já tenha banderia, ao toque
            self.botao.bind('<Button-3>', self.remove_bandeira_botao)   # esquerdo, a remove.

    def define_imagem(self) -> Image:                                   # Define qual a imagem que deve
        if self.bloco.bandeira:                                         # ser apresentada no botão
            controle: str = 'bandeira.png'
        elif self.bloco.conteudo >= 9 and self.bloco.aberto:
            controle: str = 'mina.png'
        elif self.bloco.aberto and self.bloco.conteudo != 0:
            controle: str = f'{self.bloco.conteudo}.png'
        elif self.bloco.aberto:
            controle: str = 'aberto.png'
        else: controle: str = 'campo.png'

        # Define a imagem, seguindo as condições acima
        imagem = PhotoImage(file=f'imagens/{controle}').subsample(30, 30)
        figura = Label(self.master, image=imagem)
        figura.image = imagem
        return imagem

    # Todos recebem o paramentro 'event' pela funcionalidade da função bind
    def revela_botao(self, event) -> cria_botao_visual:
        self.botao.destroy()
        self.bloco.revela()
        return self.cria_botao_visual()

    def adiciona_bandeira_botao(self, event) -> cria_botao_visual:
        self.botao.destroy()    # destruir é importante para recria-lo em seguida
        self.bloco.adiciona_bandeira()
        return self.cria_botao_visual()

    def remove_bandeira_botao(self, event) -> cria_botao_visual:
        self.botao.destroy()
        self.bloco.remove_bandeira()
        return self.cria_botao_visual() # O return pode causar recursão, caso de erro, é aqui

# Gerencia a apresentação visual do campo com TK
class CampoTK(Campo):
    def __init__(self, linhas: int, colunas: int, minas: int) -> None:
        super().__init__(linhas, colunas, minas)
        self.cria_campo()

        ### Propriedades da janela campo ###
        self.janela_campo:    Tk  = Tk()
        self.janela_campo.title('Campo Minado')
        self.janela_campo.iconbitmap('imagens/soriso.ico')

        self.contador_bandeiras()
        self.cria_campo_visual()

    ### Métodos do campo ###
    def contador_bandeiras(self) -> None:

        imagem: PhotoImage  = PhotoImage(file='imagens/bandeira.png').subsample(46, 46)
        figura: Label       = Label(self.janela_campo, image=imagem)
        figura.image = imagem

        lable_bandeiras = Label(self.janela_campo, text=f'{self.minas}', image=imagem, compound=RIGHT,
                                font=('Arial', 10)).grid(column=1, row=0, pady=6)

    def cria_campo_visual(self) -> None:

        for bloco in self.campo.values():               # Um a um passa pelos blocos
            botoes = BotaoTK(self.janela_campo, bloco)  # criando seu objeto tk equivalente
            botoes.cria_botao_visual()
        
        self.janela_campo.mainloop()

class JanelaPerdaTK():
    def __init__(self) -> None:
        self.janela_perda:    Tk  = Tk()
        self.janela_perda.title('Perda')
        self.janela_perda.iconbitmap('imagens/triste.ico')


class MenuTK():
    def __init__(self) -> None:
        self.janela_menu:   Tk      =   Tk()
        texto:              Label   =   Label(self.janela_menu,
                                              text='Escolha seu modo de jogo:').pack()

        ### Propriedades da janela menu ###
        self.janela_menu.title("Menu")
        self.janela_menu.geometry('400x600+50+50')
        self.janela_menu.resizable(False, False)
        self.janela_menu.iconbitmap('imagens/soriso.ico')

        ### Botões que inicializam os jogos ###
        botao_facil = Button(self.janela_menu, text='fácil\n9x9 10 minas',
                            command= lambda: self.inicia_jogo(9,9,10)).pack()
        botao_medio = Button(self.janela_menu, text='Medio\n16x16 30 minas',
                            command= lambda: self.inicia_jogo(16,16,40)).pack()
        botao_dificil = Button(self.janela_menu, text='Dificil\n16x30 99 minas',
                            command= lambda: self.inicia_jogo(16,30,99)).pack()

        self.janela_menu.mainloop()

    ### Métodos do menu ###
    def inicia_jogo(self, l: int, c: int, m: int) -> None:
        self.janela_menu.destroy()
        CampoTK(l, c, m)

if __name__ == "__main__": 
    menu = MenuTK()
