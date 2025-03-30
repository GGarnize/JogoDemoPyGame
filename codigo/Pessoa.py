# arquivo: codigo/Pessoa.py
from abc import ABC, abstractmethod
import pygame
from Config import GRAVIDADE, FORCA_PULO, ALTURA_JANELA

from codigo.Entidade import Entidade

class Pessoa(Entidade, ABC):
    """
    Classe abstrata que agrega a lógica de física, colisões e controle de pulo,
    seguindo o padrão do GUIAPLATAFORMA.
    """
    def __init__(self, img, chao_lista, plataforma_lista):
        super().__init__(nome="Pessoa", posicao=(0, 0))
        self.moverX = 0
        self.moverY = 0
        self.img = img
        # Converter as listas para grupos para usar spritecollide (opcional)
        self.chao_lista = pygame.sprite.Group(chao_lista)
        self.plataforma_lista = pygame.sprite.Group(plataforma_lista)

        # Controle de pulo – inicialmente, não está pulando
        self.pulando = False
        self.caindo = True

        # Adicionando delay para o pulo
        self.delay_pulo = 300  # 300 milissegundos de delay
        self.ultimo_pulo = 0   # tempo do último pulo

    def gravidade(self):
        if self.pulando:
            self.moverY += 3.2

    def pular(self):
        """Tenta iniciar o pulo se o delay tiver passado e o personagem estiver apoiado."""
        tempo_atual = pygame.time.get_ticks()
        if not self.pulando and (tempo_atual - self.ultimo_pulo >= self.delay_pulo):
            self.ultimo_pulo = tempo_atual
            self.velocidade_y = -FORCA_PULO  # ou ajuste o impulso como preferir
            self.pulando = True
            self.caindo = False

    def registrar_pulo(self):
        if self.pulando and not self.caindo:
            self.caindo = True
            self.moverY -= 33

    def registrar_plataforma(self):
        plat_hit_list = pygame.sprite.spritecollide(self, self.plataforma_lista, False)
        for p in plat_hit_list:
            self.pulando = False
            self.moverY = 0
            # Usando a hitbox (se existir) para colisão:
            hit = self.hitbox if hasattr(self, "hitbox") else self.rect
            if hit.bottom <= p.rect.bottom:
                hit.bottom = p.rect.top
                self.rect.bottom = p.rect.top  # sincroniza com o rect principal
            else:
                self.rect.y += 6.4
                self.pulando = True
                self.caindo = True

    def registrar_chao(self):
        ground_hit_list = pygame.sprite.spritecollide(self, self.chao_lista, False)
        for g in ground_hit_list:
            self.moverY = 0
            self.rect.bottom = g.rect.top
            self.pulando = False

    def update(self):
        self.gravidade()
        self.registrar_chao()
        self.registrar_plataforma()
        self.registrar_pulo()
        self.rect.x += self.moverX
        self.rect.y += self.moverY

    @abstractmethod
    def mover(self, *args, **kwargs):
        pass
