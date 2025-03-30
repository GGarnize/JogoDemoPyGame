import pygame
from codigo.Pessoa import Pessoa

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
