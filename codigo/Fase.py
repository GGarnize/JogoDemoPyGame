# arquivo: codigo/Fase.py
import sys
from msilib.schema import Media

import pygame
from pygame import Surface

from Config import FPS
from codigo.Entidade import Entidade
from codigo.FabricaEntidades import FabricaEntidades
from codigo.Inimigo import Inimigo
from codigo.Jogador import Jogador
from codigo.MediadorEntidades import MediadorEntidades


class Fase:
    def __init__(self, janela, nome_fase):
        self.janela: Surface = janela
        self.nome_fase = nome_fase
        self.clock = pygame.time.Clock()
        self.lista_entidades: list[Entidade] = []
        # Cria fundo (exemplo, se houver ImagemFundo)
        self.lista_entidades.extend(FabricaEntidades.criar_entidade(self.nome_fase + '_'))
        # Cria o chão
        chao = FabricaEntidades.criar_entidade('chao')
        self.lista_entidades.extend(chao)
        # Cria algumas plataformas
        lista_plataforma = [
            FabricaEntidades.criar_entidade('plataforma', posicao=(500, 500), width=300),
            FabricaEntidades.criar_entidade('plataforma', posicao=(0, 420), width=425),
            FabricaEntidades.criar_entidade('plataforma', posicao=(100, 320), width=150),
            FabricaEntidades.criar_entidade('plataforma', posicao=(250, 260), width=150),
            FabricaEntidades.criar_entidade('plataforma', posicao=(400, 200), width=150),
            FabricaEntidades.criar_entidade('plataforma', posicao=(600, 95), width=200),
            FabricaEntidades.criar_entidade('plataforma', posicao=(0, 95), width=430),
        ]
        self.lista_entidades.extend(lista_plataforma)
        lista_construcao = [
            FabricaEntidades.criar_entidade('plataforma', posicao=(0, 10), width=120, height=90, imagem_custom='casa2'),
        ]
        self.lista_entidades.extend(lista_construcao)
        # Cria o jogador, passando as listas de chão e plataforma para colisão
        self.lista_entidades.append(FabricaEntidades.criar_entidade('jogador',
                                                                    posicao=(10, 560),
                                                                    chao=chao,
                                                                    plataforma=lista_plataforma,
                                                                    construcao=lista_construcao))
        self.lista_entidades.append(FabricaEntidades.criar_entidade('inimigo',
                                                                    posicao=(700, 40),
                                                                    chao=chao,
                                                                    plataforma=lista_plataforma,
                                                                    construcao=lista_construcao))

    def executar(self):
        while True:
            self.clock.tick(FPS)
            self.janela.fill((0, 0, 0))
            # Para cada entidade, chamamos mover() e atualizar()
            for ent in self.lista_entidades:
                self.janela.blit(source=ent.image, dest=ent.rect)
                ent.mover()
                ent.atualizar()
                if isinstance(ent, (Jogador, Inimigo)):
                    tiro = ent.tiro()
                    if tiro is not None:
                        self.lista_entidades.append(tiro)


            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            MediadorEntidades.verificar_colisao(lista_entidades=self.lista_entidades)
            MediadorEntidades.verificar_vida(self.lista_entidades)
