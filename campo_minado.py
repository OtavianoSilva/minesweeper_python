from random import randint
from tkinter import *

# Cada quadrado individual do jogo
class Bloco():
    def __init__(self, master, linha, coluna, complemento, aberto, bandeira):
        if aberto: bandeira = False         # Estar aberto e ter uma bandeira
        else: aberto = False                # Não pode ocorrer ao mesmo tempo

        self.master      =  master          # A que janela ele pertence
        self.coluna      =  coluna          # sua localizacao com coluna
        self.linha       =  linha           # e linha
        self.complemento =  complemento     # o que há embaixo dele (número ou mina)
        self.aberto      =  aberto          # se o campo já foi aberto
        self.bandeira    =  bandeira        # se foi posto alguma bandeira.

    def define_botao(self):
        # Caso naquele local haja uma mina, só podem ocorrer duas ações:
        if self.complemento == 'M':
            self.botao = Button(self.master, text=f'   ', bd=5)
            self.botao.grid(column=self.coluna, row=self.linha)
            self.botao.bind("<Button-1>", self.perder)            # perder ao toque esquerdo
            self.botao.bind("<Button-3>", self.adiciona_bandeira) # marcar com bandeira ao toque direito

        
        # Caso não seja uma mina:
        else:
            self.botao = Button(self.master, text=f"{self.complemento if self.aberto else '   '}", bd=5)
            self.botao.grid(column=self.coluna, row=self.linha)
            self.botao.bind("<Button-1>", self.abrir)             # abrir o bloco ao toque esquerdo
            self.botao.bind("<Button-3>", self.adiciona_bandeira) # marcar com bandeira ao toque direito  
    
    def perder(self, event):
        self.master.destroy()
        perdeu = Tk()
        texto = Label(perdeu, text='Você perdeu').pack()
        perdeu.mainloop()
        

    def abrir(self, event):
        self.aberto = True
        self.define_botao()

    def adiciona_bandeira(self, event):
        pass
        

# Responsavel por toda a criacao e administacao do jogo
class CampoMinado():
    def __init__(self, linhas, colunas, minas):
        # Tratando as entradas para evitar futuros erros
        if linhas < 9 or colunas < 9 or minas < 1 or minas > (linhas*colunas):
            raise Exception('Valor de parametro inválido.')
        
        self.linhas = linhas
        self.colunas = colunas
        self.minas = minas
        self.campo = []

    # Cria uma matriz com todos os elementos sendo um objeto tipo Bloco.
    def cria_campo(self, master):
        for l in range(self.linhas+1):      # Crio a matriz um edereço maior para
            linha = []                      # evitar problemas com indexacao.
            for c in range(self.colunas+1): 
                bloco = Bloco(master, l, c, 0, False, False)
                bloco.define_botao()
                linha.append(bloco)
            self.campo.append(linha)

    # Coloca minas aleatorias pelo campo.
    def arma_campo(self):
        for m in range(self.minas): # Não adicionar minas nas bordas para evitar erros
            l, c = randint(1, self.linhas-2), randint(1, self.colunas-2)
            self.campo[l][c].complemento = 9

    # Adiciona aos elementos próximos as minas, o número de minas proximas.
    def numera_campo(self):
        controle = [-1, 0, 1]

        for l in range(self.linhas-1):
            for c in range(self.colunas-1):

                if self.campo[l][c].complemento >= 9:
                    for cl in controle:     # Caso haja uma mina, soma-se 1 a
                        for cc in controle: # todos os enderecos proximos
                            self.campo[(l+cl)][(c+cc)].complemento += 1
        
        for l in range(self.linhas):
            for c in range(self.colunas):               # O maior número possível em um
                if self.campo[l][c].complemento >= 9:   # campo não-mina é 8, por isso
                    self.campo[l][c].complemento = 'M'  # todos os 9s (ou maior) são minas

# Responsavel pelo menu principal e inicializar os jogos
class PaginaPrincipal():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Menu CM")

        self.texto = Label(self.principal, text="Bem Vindo ao Campo Minado\nEscolha o modo de jogo:")
        self.texto.pack()

        self.botao = Button(self.principal, text='Easy\n9X9\n(16 minas)', command=lambda: PaginaJogo(self.principal, 9, 9, 16))
        self.botao.pack()
        self.botao = Button(self.principal, text='Medium\n16X16\n(40 minas)', command=lambda: PaginaJogo(self.principal, 16, 16, 40))
        self.botao.pack()
        self.botao = Button(self.principal, text='Hard\n24X24\n(200 minas)', command=lambda: PaginaJogo(self.principal, 24, 24, 100))
        self.botao.pack()

        self.principal.mainloop()

# Resposavel por gerenciar a parte visual de cada jogo
class PaginaJogo(CampoMinado):
    def __init__(self, master, linhas, colunas, minas):
        super().__init__(linhas, colunas, minas)
        master.destroy()
        self.pagina_jogo = Tk()
        self.pagina_jogo.title("Campo Minado")
        self.cria_campo(self.pagina_jogo)
        self.arma_campo()
        self.numera_campo()

        self.cria_campo_visual()

    def cria_campo_visual(self):
        while True:
            self.pagina_jogo.mainloop()
    

pagina = PaginaPrincipal()