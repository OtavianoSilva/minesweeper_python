from random import randint
from tkinter import *

# Cada quadrado individual do jogo
class Bloco():
    def __init__(self, master, campo, linha, coluna, complemento, aberto, bandeira):
        if aberto: bandeira = False         # Estar aberto e ter uma bandeira
        else: aberto = False                # Não pode ocorrer ao mesmo tempo

        self.master      =  master          # A que janela ele pertence
        self.campo       =  campo           # a matriz campo que ela pertence
        self.coluna      =  coluna          # sua localizacao com coluna
        self.linha       =  linha           # e linha
        self.complemento =  complemento     # o que há embaixo dele (número ou mina)
        self.aberto      =  aberto          # se o campo já foi aberto
        self.bandeira    =  bandeira        # se foi posto alguma bandeira.

    def define_botao(self):
        # Caso naquele local haja uma mina, só podem ocorrer duas ações:
            if self.complemento == 'M' and self.aberto: self.perder()
            else:
                self.botao = Button(self.master, text=f"{'+' if self.bandeira else f'{self.complemento}' if self.aberto else '   '}", bd=5)
                self.botao.grid(column=self.coluna, row=self.linha)
                if not self.bandeira:
                    self.botao.bind("<Button-1>", self.abrir_bloco)             # perder ao toque esquerdo
                    self.botao.bind("<Button-3>", self.adiciona_bandeira if not self.aberto else None) # marcar com bandeira ao toque direito
                else:
                    self.botao.bind("<Button-3>", self.remove_bandeira)   # caso haja uma bandeira, a unica acao
                                                                          # possivel é remove-la

    def perder(self):
        self.botao.destroy()
        self.master.destroy()
        perdeu = Tk()
        texto = Label(perdeu, text='Você perdeu').pack()
        perdeu.mainloop()

    def abrir_bloco(self, event):
        self.aberto = True
        self.botao.destroy()
        self.define_botao()

    def revela_vizinhos(self, visinhos):
        pass

    def adiciona_bandeira(self, event):
        self.bandeira = True
        self.botao.destroy()
        self.define_botao()
        
    def remove_bandeira(self, event):
        self.bandeira = False
        self.botao.destroy()
        self.define_botao()

    def auto_destruicao(self):
        self.botao.destroy()
        self = None

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
                bloco = Bloco(master, self.campo, l, c, 0, False, False)
                bloco.define_botao()
                linha.append(bloco)
            self.campo.append(linha)

    # Coloca minas aleatorias pelo campo.
    def arma_campo(self):
        for m in range(self.minas): # Não adicionar minas nas bordas para evitar erros
            l, c = randint(1, self.linhas), randint(1, self.colunas)
            self.campo[l][c].complemento = 9

    # Adiciona aos elementos próximos as minas, o número de minas proximas.
    def numera_campo(self):
        controle = [-1, 0, 1]

        for l in range(self.linhas):
            for c in range(self.colunas):

                if self.campo[l][c].complemento >= 9:
                    for cl in controle:     # Caso haja uma mina, soma-se 1 a
                        for cc in controle: # todos os enderecos proximos
                            self.campo[(l+cl)][(c+cc)].complemento += 1

        for l in range(self.linhas+1):
            for c in range(self.colunas+1):
                if l == 0 or c == 0 or l == self.linhas+1 or c == self.colunas+1:
                    self.campo[l][c].auto_destruicao()    # O maior número possível em um
                elif self.campo[l][c].complemento >= 9:   # campo não-mina é 8, por isso
                    self.campo[l][c].complemento = 'M'    # todos os 9s (ou maior) são minas
                
# Responsavel pelo menu principal e inicializar os jogos
class PaginaPrincipal():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Menu CM")

        self.texto = Label(self.principal, text="Bem Vindo ao Campo Minado\nEscolha o modo de jogo:")
        self.texto.pack()

        self.botao = Button(self.principal, text='Easy\n9X9\n(10 minas)', command=lambda: PaginaJogo(self.principal, 9, 9, 10))
        self.botao.pack()
        self.botao = Button(self.principal, text='Medium\n16X16\n(40 minas)', command=lambda: PaginaJogo(self.principal, 16, 16, 40))
        self.botao.pack()
        self.botao = Button(self.principal, text='Hard\n16X30\n(99 minas)', command=lambda: PaginaJogo(self.principal, 16, 30, 99))
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
        self.pagina_jogo.mainloop()
    

pagina = PaginaPrincipal()
