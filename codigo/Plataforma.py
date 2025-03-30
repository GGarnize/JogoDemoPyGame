import pygame
from Config import PLATAFORMA_ALTURA, PLATAFORMA_LARGURA
from codigo.Entidade import Entidade


class Plataforma(Entidade):
    def __init__(self, nome, x, y, width=PLATAFORMA_LARGURA, height=PLATAFORMA_ALTURA, imagem='chao_base'):
        super().__init__(nome=nome, posicao=(x, y))
        self.imagem = pygame.image.load(f'./recurso/{imagem}.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (width, height))
        self.rect.width = width
        self.rect.height = height

    def atualizar(self):
        pass

    def mover(self):
        pass