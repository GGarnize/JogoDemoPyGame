import pygame
from Config import COR_PLATAFORMA, LARGURA_JANELA, PLATAFORMA_ALTURA, PLATAFORMA_LARGURA
from codigo.Entidade import Entidade


class Plataforma(Entidade):
    def __init__(self, x, y):
        super().__init__(nome="Plataforma", posicao=(x, y))
        self.image = pygame.image.load('./recurso/chao_base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLATAFORMA_LARGURA, PLATAFORMA_ALTURA))
        self.rect.width = PLATAFORMA_LARGURA
        self.rect.height = PLATAFORMA_ALTURA

    def atualizar(self):
        pass

    def mover(self):
        pass