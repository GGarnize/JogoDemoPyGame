# arquivo: codigo/Pessoa.py
from abc import ABC, abstractmethod
import pygame
from codigo.Entidade import Entidade

class Pessoa(Entidade, ABC):
    """
    Classe abstrata que agrega a lógica de física, colisões e controle de pulo,
    seguindo o padrão do GUIAPLATAFORMA.
    Recebe as listas de chão e plataformas (e opcionalmente inimigos e loot) para colisões.
    """
    def __init__(self, img, chao_lista, plataforma_lista):
        super().__init__(nome="Pessoa", posicao=(0, 0))
        # Atributos de controle
        self.moverX = 0   # movimento horizontal acumulado
        self.moverY = 0   # movimento vertical acumulado
        self.img = img
        self.chao_lista = pygame.sprite.Group(chao_lista)
        self.plataforma_lista = pygame.sprite.Group(plataforma_lista)

        # Código de pulo (inicialmente, está no ar)
        self.pulando = True
        self.caindo = True

    def gravidade(self):
        """Aplica a gravidade – se estiver pulando, incrementa o movimento vertical."""
        if self.pulando:
            self.moverY += 3.2

    def pular(self):
        """Inicia o pulo se o personagem não estiver já pulando."""
        if not self.pulando:
            self.caindo = False
            self.pulando = True

    def registrar_pulo(self):
        """Registra o impulso do pulo: se estiver pulando e não caindo, aplica um impulso."""
        if self.pulando and not self.caindo:
            self.caindo = True
            self.moverY -= 33

    def registrar_plataforma(self):
        """Detecta colisões com plataformas usando sprite collide e ajusta a posição.
           Se o personagem estiver caindo e o seu bottom estiver próximo do top da plataforma,
           posiciona-o exatamente sobre ela."""
        plat_colisao_lista = pygame.sprite.spritecollide(self, self.plataforma_lista, False)
        for p in plat_colisao_lista:
            # Ao colidir, interrompe o pulo
            self.pulando = False
            self.moverY = 0
            # Se a parte inferior do personagem estiver próximo do topo da plataforma
            if self.rect.bottom <= p.rect.bottom or self.rect.centery + 1 <= p.rect.bottom:
                self.rect.bottom = p.rect.top
            else:
                self.rect.y += 6.4
                self.pulando = True
                self.caindo = True

    def registrar_chao(self):
        """Detecta colisão com o chão e ajusta a posição."""
        chao_colisao_lista = pygame.sprite.spritecollide(self, self.chao_lista, False)
        for g in chao_colisao_lista:
            self.moverY = 0
            self.rect.bottom = g.rect.top
            self.pulando = False  # Para o pulo


    def movement(self):
        if self.moverX < 0:
            self.pulando = True
        if self.moverX > 0:
            self.pulando = True
            

    def atualizar(self):
        """
        Atualiza o estado do personagem:
         - Executa a animação de movimento.
         - Verifica colisões com chão e plataformas.
         - Trata a queda fora da tela.
         - Registra o pulo (impulso).
         - Atualiza a posição com os movimentos acumulados.
        """
        self.gravidade()
        self.movement()
        self.mover()
        self.registrar_chao()
        self.registrar_plataforma()
        self.registrar_pulo()
        self.rect.x += self.moverX
        self.rect.y += self.moverY
