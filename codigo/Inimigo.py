import pygame

from Config import ATRASO_TIRO_INIMIGO
from codigo.Pessoa import Pessoa
from codigo.TiroInimigo import TiroInimigo


class Inimigo(Pessoa):
    def __init__(self, posicao, chao, plataforma, construcao):
        super().__init__(img="inimigo", chao_lista=chao, plataforma_lista=plataforma, construcao_lista=construcao)
        # Cria imagem simples para o inimigo (por exemplo, retângulo azul)
        self.image = pygame.image.load('./recurso/Inimigo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=posicao)

    def mover(self):
        # Aplica gravidade, se necessário (dependendo da mecânica)
        pass

    def atualizar(self):
        self.update()

    def tiro(self):
        self.atraso_tiro -= 1
        if self.atraso_tiro <= 0:
            self.atraso_tiro = ATRASO_TIRO_INIMIGO
            return TiroInimigo(position=(self.rect.left + 1, self.rect.top + 20))

