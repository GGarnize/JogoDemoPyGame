# arquivo: codigo/Jogador.py
import pygame
from Config import VELOCIDADE_JOGADOR, ALTURA_JANELA
from codigo.Pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, posicao, chao, plataforma):
        # Aqui, "jogador.png" é o nome da imagem base para o jogador
        super().__init__(img="jogador", chao_lista=chao, plataforma_lista=plataforma)
        # Ajusta a imagem e a posição inicial conforme necessário
        self.image = pygame.image.load('./recurso/jogador.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=posicao)

    def mover(self):
        """Controla o movimento do jogador baseado no input."""
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= VELOCIDADE_JOGADOR
            self.moverX = -VELOCIDADE_JOGADOR
        elif teclas[pygame.K_RIGHT]:
            self.rect.x += VELOCIDADE_JOGADOR
            self.moverX = VELOCIDADE_JOGADOR
        else:
            self.moverX = 0
        if teclas[pygame.K_UP] or teclas[pygame.K_SPACE]:
            self.pular()
