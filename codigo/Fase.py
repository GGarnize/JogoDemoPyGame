# arquivo: codigo/Fase.py
import sys
import pygame
from pygame import Surface
from Config import FPS
from codigo.Entidade import Entidade
from codigo.FabricaEntidades import FabricaEntidades

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
            FabricaEntidades.criar_entidade('plataforma', posicao=(300, 300)),
            FabricaEntidades.criar_entidade('plataforma', posicao=(400, 400)),
            FabricaEntidades.criar_entidade('plataforma', posicao=(500, 500))
        ]
        self.lista_entidades.extend(lista_plataforma)
        # Cria o jogador, passando as listas de chão e plataforma para colisão
        self.lista_entidades.append(FabricaEntidades.criar_entidade('jogador', posicao=(10, 50), chao=chao, plataforma=lista_plataforma))

    def executar(self):
        while True:
            self.clock.tick(FPS)
            self.janela.fill((0, 0, 0))
            # Para cada entidade, chamamos mover() e atualizar()
            for ent in self.lista_entidades:
                ent.mover()
                ent.atualizar()
                self.janela.blit(ent.image, ent.rect)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
