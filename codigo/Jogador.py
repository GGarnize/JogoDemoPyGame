# arquivo: codigo/Jogador.py
import pygame
from Config import ATRASO_TIRO_JOGADOR, LARGURA_JANELA, VELOCIDADE_JOGADOR, ALTURA_JANELA
from codigo.Pessoa import Pessoa
from codigo.TiroJogador import TiroJogador


class Jogador(Pessoa):
    def __init__(self, posicao, chao, plataforma, construcao):
        # "jogador.png" é o nome da imagem
        super().__init__(img="jogador", chao_lista=chao, plataforma_lista=plataforma, construcao_lista=construcao)
        self.image = pygame.image.load('./recurso/jogador.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=posicao)
        # Cria uma area_contato menor do lado direito (reduz 10 pixels)
        self.area_contato_deslocamento = 15
        self.area_contato = pygame.Rect(self.rect.x, self.rect.y, self.rect.width - self.area_contato_deslocamento, self.rect.height)

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= VELOCIDADE_JOGADOR
            self.moverX = -VELOCIDADE_JOGADOR
        elif teclas[pygame.K_RIGHT] and self.rect.x < LARGURA_JANELA - self.rect.width + self.area_contato_deslocamento:
            self.rect.x += VELOCIDADE_JOGADOR
            self.moverX = VELOCIDADE_JOGADOR
        else:
            self.moverX = 0

        if teclas[pygame.K_UP] or teclas[pygame.K_SPACE]:
            self.pular()
        self.area_contato.topleft = self.rect.topleft
        self.gravidade()

    def atualizar(self):
        self.update()

    def tiro(self):
        self.atraso_tiro -= 1
        if self.atraso_tiro <= 0:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_RCTRL]:
                self.atraso_tiro = ATRASO_TIRO_JOGADOR
                return TiroJogador(position=(self.rect.right - 1, self.rect.top + 20))
            else:
                return None
        else:
            return None
