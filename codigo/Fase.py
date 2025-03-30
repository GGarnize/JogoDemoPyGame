import sys

import pygame
from pygame import Surface

from Config import ALTURA_JANELA, COR_BRANCO, DEV, FPS, LARGURA_JANELA, RU
from codigo.Entidade import Entidade
from codigo.FabricaEntidades import FabricaEntidades
from codigo.MediadorEntidades import MediadorEntidades
from codigo.Util import imprimir_texto


class Fase:
    def __init__(self, janela, nome_fase):
        self.janela: Surface = janela
        self.nome_fase = nome_fase
        self.clock = pygame.time.Clock()
        self.lista_entidades: list[Entidade] = []
        # Cria fundo
        self.lista_entidades.extend(FabricaEntidades.criar_entidade(self.nome_fase + '_'))
        # Cria o chão
        chao = FabricaEntidades.criar_entidade('chao')
        self.lista_entidades.extend(chao)
        # Cria plataformas
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
            FabricaEntidades.criar_entidade('plataforma', nome='Casa', posicao=(0, 10), width=120, height=90,
                                            imagem_custom='casa2'),
        ]
        self.lista_entidades.extend(lista_construcao)
        # Cria o jogador
        self.lista_entidades.append(FabricaEntidades.criar_entidade('jogador',
                                                                    posicao=(10, 560),
                                                                    chao=chao,
                                                                    plataforma=lista_plataforma,
                                                                    construcao=lista_construcao))
        # Cria um inimigo
        inimigo_posicoes = [(700, 40), (500, 150), (311,210), (175,270), (661, 450)]
        for posicao in inimigo_posicoes:
            self.lista_entidades.append(FabricaEntidades.criar_entidade('inimigo',
                                                                        posicao=posicao,
                                                                        chao=chao,
                                                                        plataforma=lista_plataforma,
                                                                        construcao=lista_construcao))

    def executar(self):
        while True:
            self.clock.tick(FPS)
            self.janela.fill((0, 0, 0))
            for ent in self.lista_entidades:
                self.janela.blit(ent.imagem, ent.rect)
                ent.mover()
                ent.atualizar()
                if hasattr(ent, "tiro"):
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
            status_partida = MediadorEntidades.verificar_fim_fase(self.lista_entidades)
            if status_partida:
                self.exibir_popup(status_partida)
                return

    def exibir_popup(self, sucesso, duracao=2000):
        if sucesso == 'ganhou':
            mensagem = "Você mandou bala!!"
        elif sucesso == 'perdeu':
            mensagem = "Você tomou bala!"
        else:
            mensagem = "Fim da Fase!"

        popup = pygame.Surface((LARGURA_JANELA, ALTURA_JANELA))
        popup.set_alpha(200)
        popup.fill((0, 0, 0))
        self.janela.blit(popup, (0, 0))
        imprimir_texto(superficie=self.janela, texto=mensagem, tamanho=64, cor=COR_BRANCO,
                       posicao=(LARGURA_JANELA // 2, ALTURA_JANELA // 2))
        imprimir_texto(superficie=self.janela, texto=f"By: {DEV}. RU={RU}", tamanho=13, cor=COR_BRANCO,
                       posicao=(120, ALTURA_JANELA - 20))
        pygame.display.flip()
        pygame.time.delay(duracao)
