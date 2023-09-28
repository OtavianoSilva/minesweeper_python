# Jogo Campo Minado em Python

Este é um jogo de Campo Minado em Python que foi desenvolvido usando a biblioteca Tkinter para a interface gráfica. O jogo consiste em revelar todas as células do campo minado sem acertar nenhuma mina. Se você acertar uma mina, você perde o jogo.
## Como Jogar

    Execute o arquivo minesweeper.py para iniciar o jogo.
    Uma janela de menu será exibida, onde você pode escolher o modo de jogo: Fácil, Médio ou Difícil.
    Clique em uma das opções de modo de jogo para começar.
    O jogo será iniciado, e você verá um tabuleiro com várias células vazias. Clique com o botão esquerdo do mouse em uma célula para revelar seu conteúdo.
    Se você achar que uma célula contém uma mina, clique com o botão direito do mouse nela para colocar uma bandeira.
    O objetivo do jogo é revelar todas as células sem acertar nenhuma mina. Se você clicar em uma mina, o jogo terminará.
    Você pode ganhar o jogo quando todas as células vazias forem reveladas e todas as minas forem marcadas com bandeiras.

## Recursos do Código

O código é organizado em três classes principais:
### 1. Classe Menu

Esta classe representa o menu inicial do jogo. Ela permite ao jogador escolher entre os modos de jogo (Fácil, Médio, Difícil) e fornece exemplos de ações do jogo.

    _create_buttons(): Cria os botões para os modos de jogo.
    _example_mine_action(), _example_flag_action(), _example_number_action(): Funções que ilustram exemplos de ações do jogador.

### 2. Classe Board

Esta classe representa o tabuleiro do jogo e é onde a jogabilidade principal ocorre. Ela lida com a criação do tabuleiro, a geração de minas e números, o controle das ações do jogador e a verificação das condições de vitória ou derrota.

    _create_header(): Cria o cabeçalho do jogo com informações como o contador de bandeiras.
    _create_mine_matrix(): Gera as minas no tabuleiro.
    _numbers_mine_matrix(): Calcula e armazena os números que indicam quantas minas estão adjacentes a cada célula vazia.
    _create_flag_matrix(): Cria uma matriz para rastrear o estado das células (fechadas, abertas, marcadas com bandeira, etc.).
    _put_buttons_in_frame(): Cria os botões do tabuleiro e liga suas ações aos eventos do mouse.
    _button_action(): Lida com as ações do jogador quando ele clica em um botão (revelar, marcar com bandeira, etc.).
    _open_neighbors(): Função recursiva para abrir células vazias adjacentes.
    _check_if_won(): Verifica se o jogador ganhou o jogo e exibe a tela de vitória.

### 3. Classe EndWindow

Esta classe exibe uma janela popup quando o jogador ganha ou perde o jogo. Ela mostra uma mensagem de vitória ou derrota, o tempo decorrido e permite reiniciar o jogo.

    _restart(): Reinicia o jogo quando o jogador clica no botão "Iniciar um novo jogo".

## Como Executar

Para executar o jogo, siga estas etapas:

    Certifique-se de ter o Python instalado em seu sistema.
    Baixe o código-fonte do jogo do repositório no GitHub.
    Navegue até o diretório onde o código está localizado.
    Execute o arquivo minesweeper.py usando o Python.

## Requisitos

Este jogo requer a bibliotecas random, time, subprocess, os e Tkinter que é normalmente incluída na instalação padrão do Python. Certifique-se de ter o Python instalado em seu sistema.
Créditos

Este jogo foi desenvolvido por Otaviano Silva e é distribuído sob a licença Minha licença. Você pode encontrar o código-fonte completo no Neste repositiório.

Aproveite o jogo!
