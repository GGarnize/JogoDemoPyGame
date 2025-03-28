import pygame
from pygame import Rect, Surface
from pygame.font import Font

from Config import C_AMARELO, C_BRANCO, C_LARANJA, JAN_LARGURA, MENU_OPCOES
from codigo.Util import imprime_texto


class Menu:
    def __init__(self, janela):
        self.janela = janela
        self.surf = pygame.image.load('./recurso/Menu_Fundo.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_opcao = 0
        pygame.mixer_music.load('./recurso/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.janela.blit(source=self.surf, dest=self.rect)
            imprime_texto(self.janela, 50, "Se mantenha", C_LARANJA, ((JAN_LARGURA / 2), 70))
            imprime_texto(self.janela, 50, "calmo", C_LARANJA, ((JAN_LARGURA / 2), 120))
            for i in range(len(MENU_OPCOES)):
                if i == menu_opcao:
                    imprime_texto(self.janela, 20, MENU_OPCOES[i], C_AMARELO, ((JAN_LARGURA / 2), 200 + 25 * i))
                else:
                    imprime_texto(self.janela, 20, MENU_OPCOES[i], C_BRANCO, ((JAN_LARGURA / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_opcao < len(MENU_OPCOES) - 1:
                            menu_opcao += 1
                        else:
                            menu_opcao = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_opcao > 0:
                            menu_opcao -= 1
                        else:
                            menu_opcao = len(MENU_OPCOES) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPCOES[menu_opcao]
