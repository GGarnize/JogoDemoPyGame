import pygame
from pygame import Surface


def imprimir_texto(superficie: Surface, texto: str, tamanho: int, cor: tuple, posicao: tuple):
    fonte = pygame.font.SysFont("Comic Sans MS", tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    rect_texto = texto_renderizado.get_rect(center=posicao)
    superficie.blit(texto_renderizado, rect_texto)
