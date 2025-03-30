from abc import ABC, abstractmethod
import pygame

class Entidade(ABC, pygame.sprite.Sprite):
    def __init__(self, nome: str, posicao: tuple):
        super().__init__()
        self.nome = nome
        self.image = None  # Será definida nas classes concretas
        self.rect = pygame.Rect(posicao[0], posicao[1], 0, 0)
        self.vida = 3
        self.dano = 1

    @abstractmethod
    def mover(self, *args, **kwargs):
        pass

    @abstractmethod
    def atualizar(self):
        pass
