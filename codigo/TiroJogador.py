import pygame

from Config import TIRO_JOGADOR
from codigo.Entidade import Entidade


class TiroJogador(Entidade):
    def __init__(self, position: tuple):
        super().__init__('projetil', position)
        self.image = pygame.image.load('./recurso/projetil.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (8, 5))
        self.rect = self.image.get_rect(topleft=position)

    def mover(self, ):
        self.rect.centerx += TIRO_JOGADOR

    def atualizar(self):
        self.mover()
