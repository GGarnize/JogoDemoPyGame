import pygame

from Config import TIRO_JOGADOR
from codigo.Entidade import Entidade


class TiroJogador(Entidade):
    def __init__(self, position: tuple):
        super().__init__('projetil', position)
        self.imagem = pygame.image.load('./recurso/projetil.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (8, 5))
        self.rect = self.imagem.get_rect(topleft=position)

    def mover(self, ):
        self.rect.centerx += TIRO_JOGADOR

    def atualizar(self):
        self.mover()
