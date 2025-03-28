# arquivo: codigo/Fase.py
import sys
import pygame
from pygame import Surface

from Config import EVENTO_INIMIGO, TEMPO_FASE
from codigo.Entidade import Entidade
from codigo.FabricaEntidades import FabricaEntidades

class Fase:
    def __init__(self, janela: Surface, nome: str):
        self.tempo = TEMPO_FASE
        self.janela = janela
        self.nome = nome

        self.lista_entidades: list[Entidade] = []

        # Cria fundos (parallax)
        self.lista_entidades.extend(FabricaEntidades.cria_entidade(self.nome + '_'))

        # Cria chão
        self.lista_entidades.extend(FabricaEntidades.cria_entidade('Chao'))

        # Cria jogador
        self.lista_entidades.extend(FabricaEntidades.cria_entidade('Jogador'))

        # Cria 1 inimigo só pra testar
        self.lista_entidades.extend(FabricaEntidades.cria_entidade('Inimigo'))

    def run(self):
        pygame.mixer_music.load(f'./recurso/{self.nome}.mp3')
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.janela.fill((0, 0, 0))  # Limpa a tela com preto

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENTO_INIMIGO:
                    pass  # Lógica de inimigo, se quiser

            # Primeiro move as entidades
            for ent in self.lista_entidades:
                ent.move()

            # Depois trata colisões específicas (Jogador vs Chao)
            self.verifica_colisoes()

            # Desenha as entidades na tela
            for ent in self.lista_entidades:
                self.janela.blit(ent.surf, ent.rect)

            pygame.display.flip()

# Trecho do arquivo: codigo/Fase.py
    def verifica_colisoes(self):
        jogadores = [e for e in self.lista_entidades if e.name.startswith("Jogador")]
        chao_lista = [c for c in self.lista_entidades if c.name.startswith("chao_base")]
        inimigos = [i for i in self.lista_entidades if i.name.startswith("Inimigo")]

        for jogador in jogadores:
            for chao in chao_lista:
                if jogador.rect.colliderect(chao.area_contato):
                    jogador.rect.bottom = chao.area_contato.top
                    if hasattr(jogador, 'vel_y'):
                        jogador.vel_y = 0
                    if hasattr(jogador, 'no_chao'):
                        jogador.no_chao = True

            for inimigo in inimigos:
                for chao in chao_lista:
                    if inimigo.rect.colliderect(chao.area_contato):
                        inimigo.rect.bottom = chao.area_contato.top
                        if hasattr(inimigo, 'vel_y'):
                            inimigo.vel_y = 0
                        if hasattr(inimigo, 'no_chao'):
                            inimigo.no_chao = True
