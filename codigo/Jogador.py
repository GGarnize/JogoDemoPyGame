# arquivo: codigo/Jogador.py
import pygame
from codigo.Entidade import Entidade
from Config import ENTIDADE_VELOCIDADE, FORCA_PULO, GRAVIDADE, JAN_ALTURA, JAN_LARGURA


class Jogador(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vel_y = 0
        self.no_chao = False

    def move(self):
        """Aplica gravidade, checa teclas e move o jogador."""
        # Leitura de teclas
        teclas = pygame.key.get_pressed()

        # Movimentação horizontal
        if teclas[pygame.K_LEFT] and self.rect.left + 20 > 0:
            self.rect.x -= ENTIDADE_VELOCIDADE[self.name]
        if teclas[pygame.K_RIGHT] and self.rect.right < JAN_LARGURA + 50:
            self.rect.x += ENTIDADE_VELOCIDADE[self.name]

        # Se quiser pular
        if teclas[pygame.K_SPACE] and self.no_chao:
            self.vel_y = -FORCA_PULO
            self.no_chao = False

        # Aplicando gravidade
        self.vel_y += GRAVIDADE
        self.rect.y += self.vel_y

        # Limitar para não sair da tela (ou checar colisão com chão)
        # Aqui apenas um exemplo de "chão" no final da janela,
        # mas depois faremos a colisão com a entidade "Chao".
        if self.rect.bottom >= JAN_ALTURA:
            self.rect.bottom = JAN_ALTURA
            self.vel_y = 0
            self.no_chao = True
