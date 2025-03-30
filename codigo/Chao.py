import pygame

from Config import ALTURA_JANELA, LARGURA_JANELA, PLATAFORMA_ALTURA
from codigo.Entidade import Entidade


class Chao(Entidade):
    def __init__(self, chao_loc):
        super().__init__("Chao", (chao_loc, ALTURA_JANELA - PLATAFORMA_ALTURA))
        self.imagem = pygame.image.load('./recurso/chao_base.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JANELA, PLATAFORMA_ALTURA))
        self.rect = self.imagem.get_rect(topleft=(chao_loc, ALTURA_JANELA - PLATAFORMA_ALTURA))

    def mover(self, *args, **kwargs):
        pass

    def atualizar(self):
        pass
