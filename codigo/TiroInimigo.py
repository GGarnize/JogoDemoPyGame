import pygame

from Config import TIRO_INIMIGO
from codigo.Entidade import Entidade


class TiroInimigo(Entidade):
    def __init__(self, position: tuple):
        super().__init__('projetil', position)
        self.image = pygame.image.load('./recurso/projetil.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (8, 5))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(topleft=position)

    def mover(self, ):

        self.rect.centerx -= TIRO_INIMIGO

    def atualizar(self):
        self.mover()
