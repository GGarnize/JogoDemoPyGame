from abc import ABC, abstractmethod

import pygame

from Config import FORCA_PULO, GRAVIDADE, ATRASO_PULO
from codigo.Entidade import Entidade


class Pessoa(Entidade, ABC):
    def __init__(self, img, chao_lista, plataforma_lista, construcao_lista):
        super().__init__(nome="Pessoa", posicao=(0, 0))
        self.velocidade_y = None
        self.moverX = 0
        self.moverY = 0
        self.img = img

        self.chao_lista = pygame.sprite.Group(chao_lista)
        self.plataforma_lista = pygame.sprite.Group(plataforma_lista)
        self.construcao_lista = pygame.sprite.Group(construcao_lista)

        self.pulando = True
        self.caindo = True

        self.atraso_pulo = ATRASO_PULO
        self.ultimo_pulo = 0

        self.atraso_tiro = 0


    def gravidade(self):
        if self.pulando:
            self.moverY += GRAVIDADE

    def pular(self):
        tempo_atual = pygame.time.get_ticks()
        if not self.pulando and (tempo_atual - self.ultimo_pulo >= self.atraso_pulo):
            self.ultimo_pulo = tempo_atual
            self.velocidade_y = -FORCA_PULO
            self.pulando = True
            self.caindo = False

    def registrar_pulo(self):
        if self.pulando and not self.caindo:
            self.caindo = True
            self.moverY -= FORCA_PULO

    def registrar_plataforma(self):
        plat_acerto_lista = pygame.sprite.spritecollide(self, self.plataforma_lista, False)
        for p in plat_acerto_lista:
            self.pulando = False
            self.moverY = 0
            hit = self.area_contato if hasattr(self, "area_contato") else self.rect
            if (hit.bottom <= p.rect.bottom
                    or (hit.bottom >= p.rect.bottom and hit.centery <= p.rect.centery)):
                hit.bottom = p.rect.top
                self.rect.bottom = p.rect.top
            else:
                self.rect.y += 6.4
                self.pulando = True
                self.caindo = True

    def registrar_construcao(self):
        pass


    def registrar_chao(self):
        chao_acerto_lista = pygame.sprite.spritecollide(self, self.chao_lista, False)
        for g in chao_acerto_lista:
            self.moverY = 0
            self.rect.bottom = g.rect.top
            self.pulando = False

    def movimento(self):
        if self.moverX < 0:
            self.pulando = True
        if self.moverX > 0:
            self.pulando = True

    def update(self):
        self.movimento()
        self.gravidade()
        self.registrar_chao()
        self.registrar_plataforma()
        self.registrar_construcao()
        self.registrar_pulo()
        self.rect.x += self.moverX
        self.rect.y += self.moverY

    @abstractmethod
    def mover(self, *args, **kwargs):
        pass

    @abstractmethod
    def tiro(self):
        pass
