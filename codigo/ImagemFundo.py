import pygame

from Config import ALTURA_JANELA, LARGURA_JANELA
from codigo.Entidade import Entidade


class ImagemFundo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image = pygame.image.load(f'recurso/{name}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_JANELA, ALTURA_JANELA))
        self.rect = self.image.get_rect(topleft=position)


    def mover(self):
        self.rect.centerx -= 1
        if self.rect.right <= 0:
            self.rect.left = LARGURA_JANELA

    def atualizar(self):
        pass