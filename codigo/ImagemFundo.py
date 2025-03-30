import pygame

from Config import ALTURA_JANELA, LARGURA_JANELA
from codigo.Entidade import Entidade


class ImagemFundo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.imagem = pygame.image.load(f'recurso/{name}.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JANELA, ALTURA_JANELA))
        self.rect = self.imagem.get_rect(topleft=position)


    def mover(self):
        self.rect.centerx -= 1
        if self.rect.right <= 0:
            self.rect.left = LARGURA_JANELA

    def atualizar(self):
        pass