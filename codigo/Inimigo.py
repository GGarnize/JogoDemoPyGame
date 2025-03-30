import random

import pygame

from Config import ATRASO_TIRO_INIMIGO
from codigo.Pessoa import Pessoa
from codigo.TiroInimigo import TiroInimigo


class Inimigo(Pessoa):
    def __init__(self, posicao, chao, plataforma, construcao):
        super().__init__(img="inimigo", chao_lista=chao, plataforma_lista=plataforma, construcao_lista=construcao)
        nome_imagem = random.choice(["inimigo", "inimigo2"])
        self.imagem = pygame.image.load(f'./recurso/{nome_imagem}.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.rect = self.imagem.get_rect(topleft=posicao)

    def mover(self):
        pass

    def atualizar(self):
        self.update()

    def tiro(self):
        self.atraso_tiro -= 1
        if self.atraso_tiro <= 0:
            self.atraso_tiro = ATRASO_TIRO_INIMIGO
            return TiroInimigo(position=(self.rect.left + 1, self.rect.top + 20))

