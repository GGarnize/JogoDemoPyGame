import sys

import pygame

from Config import JAN_LARGURA, JAN_ALTURA, MENU_OPCOES
from codigo.Fase import Fase
from codigo.Menu import Menu


class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(JAN_LARGURA, JAN_ALTURA))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPCOES[0], MENU_OPCOES[1], MENU_OPCOES[2]]:
                fase = Fase(self.window, 'Fase1')
                fase_return = fase.run()
                if fase_return:
                    fase = Fase(self.window, 'Fase2')
                    fase_return = fase.run()
                    if fase_return:
                        pass

            elif menu_return == MENU_OPCOES[3]:
                pass
            elif menu_return == MENU_OPCOES[4]:
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()