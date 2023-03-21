from tkinter import *
from campo_minado import *

# Responsável por gerenciar os botões como objetos TK.
class BotaoTK():
    def __init__(self, master: Tk, bloco: Bloco) -> None:
        self.master:        Tk              = master    # A janela a qual o botão pertence,
        self.bloco:         Bloco           = bloco     # o bloco referenciado
        self.cores:         dict[str / int] = {         # grade de possiveis conteúdos
            'aberto'  :     'gray',                     # do botão, e sua representação.
            'fechado' :     'white',
            'mina'    :     'red',
            'bandeira':     'yellow',
            1         :     'blue',
            2         :     'green',
            3         :     'red',
            4         :     'purple',                   # Ps.:
            5         :     'maroon',                   # Toda a apresentação visual é um espelho
            6         :     'turquoise',                # do botão pelo qual a classe se baseia
            7         :     'black',
            8         :     'gray',
        }

    # Cria o botão como objeto Button
    def cria_botao_visual(self) -> None:
        self.botao = Button(self.master, text='+' if self.bloco.bandeira else f'{bloco.conteudo}' if self.bloco.aberto else '  ')
        self.botao.grid(column=self.bloco.coluna, row=self.bloco.linha)
        if not self.bloco.bandeira:
            self.botao.bind('<Button-1>', self.revela_botao)            # Ao toque direito, abre o botão,
            self.botao.bind('<Button-3>', self.adiciona_bandeira_botao) # ao toque esquerdo, adiciona bandeira.
        else:                                                           # E caso já tenha banderia, ao toque
            self.botao.bind('<Button-3>', self.remove_bandeira_botao)   # esquerdo, a remove.

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
class CampoTK():
    def __init__(self) -> None:

        self.janela = Tk()
        self.janela.title('Campo Minado')
        self.janela.geometry(f'{9*self.largura_bloco+4}x{9*self.altura_bloco+100}')
        self.frame = Frame(self.janela)
        self.frame.pack()


        self.janela.mainloop()


bloco = Bloco(9, 9, 0, False, False)
janela = Tk()
teste = BotaoTK(janela, bloco)
teste.cria_botao_visual()
janela.mainloop()