import pygame
from Config import PLATAFORMA_ALTURA, PLATAFORMA_LARGURA
from codigo.Entidade import Entidade


class Plataforma(Entidade):
    def __init__(self, x, y, width=PLATAFORMA_LARGURA, height=PLATAFORMA_ALTURA):
        super().__init__(nome="Plataforma", posicao=(x, y))
        self.image = pygame.image.load('./recurso/chao_base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect.width = width
        self.rect.height = height

    def atualizar(self):
        pass

    def mover(self):
        pass