import pygame
from Config import ALTURA_JANELA, COR_CHAO, LARGURA_JANELA, PLATAFORMA_ALTURA
from codigo.Entidade import Entidade

class Chao(Entidade):
    def __init__(self, chao_loc):
        super().__init__("Chao", (chao_loc, ALTURA_JANELA - PLATAFORMA_ALTURA))
        self.image = pygame.image.load('./recurso/chao_base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_JANELA, PLATAFORMA_ALTURA))
        self.rect = self.image.get_rect(topleft=(chao_loc, ALTURA_JANELA - PLATAFORMA_ALTURA))

    def mover(self, *args, **kwargs):
        pass

    def atualizar(self):
        pass
