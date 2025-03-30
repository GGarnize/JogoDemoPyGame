# arquivo: codigo/Jogador.py
import pygame
from Config import VELOCIDADE_JOGADOR, ALTURA_JANELA
from codigo.Pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, posicao, chao, plataforma):
        # "jogador.png" é o nome da imagem
        super().__init__(img="jogador", chao_lista=chao, plataforma_lista=plataforma)
        self.image = pygame.image.load('./recurso/jogador.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=posicao)
        # Cria uma hitbox menor do lado direito (reduz 10 pixels)
        self.hitbox_offset = 10
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width - self.hitbox_offset, self.rect.height)

    def mover(self):
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

        # Sempre atualiza a hitbox para que acompanhe o rect:
        self.hitbox.topleft = self.rect.topleft

        self.gravidade()

    def update(self):
        self.update()  # Chama a atualização de física definida na classe Pessoa
