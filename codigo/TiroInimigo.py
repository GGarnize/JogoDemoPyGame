import pygame

from Config import TIRO_INIMIGO
from codigo.Entidade import Entidade


class TiroInimigo(Entidade):
    def __init__(self, position: tuple):
        super().__init__('projetil', position)
        self.imagem = pygame.image.load('./recurso/projetil.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (8, 5))
        self.imagem = pygame.transform.flip(self.imagem, True, False)
        self.rect = self.imagem.get_rect(topleft=position)

    def mover(self, ):

        self.rect.centerx -= TIRO_INIMIGO

    def atualizar(self):
        self.mover()
