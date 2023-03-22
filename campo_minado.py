from random import randint
from tkinter import *

# Responsável pelo controle de cada bloco individual
class Bloco():
    def __init__(self,  linha: int, coluna:int, conteudo:int,
                 aberto:bool, bandeira:bool) -> None:
        if aberto: self.remove_bandeira()          # Estar aberto e ter uma bandeira
        else: aberto = False                       # Não pode ocorrer ao mesmo tempo

        self.coluna:    int     =  coluna          # Sua localizacao com coluna
        self.linha:     int     =  linha           # e linha corespondente
        self.conteudo:  int     =  conteudo        # o que há embaixo dele (número ou mina)
        self.aberto:    bool    =  aberto          # se o campo já foi aberto
        self.bandeira:  bool    =  bandeira        # se foi posto alguma bandeira.

    ### Métodos do bloco ###
    def revela(self) -> None:                      # Abre um bloco antes fechado
        if not self.aberto and not self.bandeira:  # Caso haja uma baneira o bloco
            self.aberto = True                     # não pode ser aberto.

    def adiciona_bandeira(self) -> None:           # Adiciona uma bandeira
        if not self.bandeira and not self.aberto:  # Caso o bloco esteja aberto, 
            self.bandeira = True                   # não pode adicionar bandeira.
    
    def remove_bandeira(self) -> None:             # Caso haja uma bandeira, ele
        if self.bandeira:                          # a remove.
            self.bandeira = False

    def index(self) -> list:                       # Retorna o endereço deste bloco
        return [self.linha, self.coluna]           # em linha e coluna.

# Responsável pelo gerenciamento do campo
class Campo():
    def __init__(self, linhas:int, colunas:int, minas:int) -> None:

        self.linhas:        int        = linhas     # Quantidade de linhas,
        self.colunas:       int        = colunas    # colunas e
        self.minas:         int        = minas      # minas no campo
        self.campo:   dict[str, Bloco] = {}         # o próprio campo.

    ### Métodos do campo ###
    def define_campo(self) -> dict:                 # Cria o campo com blocos
        for l in range(self.linhas):                # genéricos.
            for c in range(self.colunas):
                self.campo[f'{l}, {c}'] = Bloco(l, c, 0, False, False)
        return self.campo
    
    def arma_campo(self) -> dict:                   # Adiciona minas randomicamente
        for mina in range(self.minas):              # pelo campo.
            l, c = randint(0,self.linhas-1), randint(0, self.colunas-1)
            local: Bloco = self.campo[f'{l}, {c}']

            while local.conteudo == 9:
                l, c = randint(0,self.linhas-1), randint(0, self.colunas-1)
                local = self.campo[f'{l}, {c}']

            else: local.conteudo = 9
        
        return self.campo
    
    def numera_campo(self) -> dict:                 # Númera os campos de acordo
        controle: set = -1, 0, 1                    # com a quantidade de minas
        for bloco in self.campo.values():           # próximas.
            if bloco.conteudo >= 9:
                endereco = bloco.index()
                for l in controle:
                    for c in controle:
                        try: self.campo[f'{endereco[0]+l}, {endereco[1]+c}'].conteudo += 1
                        except: continue
        return self.campo
    
    def revela_vizinhos(self):
        pass

    def cria_campo(self) -> None:
        self.define_campo()
        self.arma_campo()
        self.numera_campo()
