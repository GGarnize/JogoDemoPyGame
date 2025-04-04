import sys
import pygame
from pygame import Surface

from Config import LARGURA_JANELA, ALTURA_JANELA, OPCOES_MENU
from codigo.Fase import Fase
from codigo.Menu import Menu

class Jogo:
    def __init__(self):
        pygame.init()
        self.janela: Surface = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))

    def executar(self):
        while True:
            menu = Menu(self.janela)
            opcao_menu = menu.executar()
            if opcao_menu in [OPCOES_MENU[0]]:
                fase = Fase(self.janela, "Fase1")
                fase.executar()
            else:
                pygame.quit()
                sys.exit()
