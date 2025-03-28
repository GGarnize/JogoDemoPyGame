import pygame
from pygame import Rect, Surface
from pygame.font import Font

def imprime_texto(janela, texto_tamanho: int, texto: str, texto_cor: tuple, texto_centro_pos: tuple):
    texto_fonte: Font = pygame.font.SysFont(name="Calibri", size=texto_tamanho)
    texto_surf: Surface = texto_fonte.render(texto, True, texto_cor).convert_alpha()
    texto_rect: Rect = texto_surf.get_rect(center=texto_centro_pos)
    janela.blit(source=texto_surf, dest=texto_rect)