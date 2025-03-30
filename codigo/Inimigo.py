import pygame
from codigo.Pessoa import Pessoa

class Inimigo(Pessoa):
    def __init__(self, posicao):
        super().__init__("Inimigo", posicao)
        # Cria imagem simples para o inimigo (por exemplo, retângulo azul)
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=posicao)
        self.direcao = 1
        self.velocidade = 3

    def mover(self):
        # Movimento simples horizontal
        self.rect.x += self.velocidade * self.direcao
        # Troca de direção em limites definidos (ajuste conforme o seu nível)
        if self.rect.x > 600 or self.rect.x < 100:
            self.direcao *= -1
        # Aplica gravidade, se necessário (dependendo da mecânica)
        self.aplicar_gravidade()

    def atualizar(self):
        pass
