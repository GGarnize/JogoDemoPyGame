import pygame
from pygame import Surface

from Config import ALTURA_JANELA, COR_AMARELO, COR_BRANCO, COR_FUNDO_MENU, COR_LARANJA, DEV, LARGURA_JANELA, OPCOES_MENU
from codigo.Util import imprimir_texto


class Menu:
    def __init__(self, janela: Surface):
        self.janela: Surface = janela
        self.surf = pygame.image.load('./recurso/Menu_Fundo.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (LARGURA_JANELA, ALTURA_JANELA))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.fundo = pygame.Surface(janela.get_size())
        self.fundo.fill(COR_FUNDO_MENU)

    def executar(self):
        pygame.mixer_music.load('./recurso/Menu.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.12)
        opcao_selecionada = 0
        executando = True
        clock = pygame.time.Clock()
        while executando:
            clock.tick(60)
            self.janela.blit(source=self.surf, dest=self.rect)
            imprimir_texto(superficie=self.janela, texto="Se mantenha", tamanho=50, cor=COR_LARANJA,
                           posicao=((LARGURA_JANELA / 2), 70))
            imprimir_texto(superficie=self.janela, texto="calmo", tamanho=48, cor=COR_LARANJA,
                           posicao=((LARGURA_JANELA / 2), 120))
            for i in range(len(OPCOES_MENU)):
                if i == opcao_selecionada:
                    imprimir_texto(superficie=self.janela, texto=f'> {OPCOES_MENU[i]}', tamanho=31, cor=COR_AMARELO,
                                   posicao=((LARGURA_JANELA / 2), (ALTURA_JANELA - 150) + 35 * i))
                else:
                    imprimir_texto(superficie=self.janela, texto=OPCOES_MENU[i], tamanho=30, cor=COR_BRANCO,
                                   posicao=((LARGURA_JANELA / 2), (ALTURA_JANELA - 150) + 35 * i))
            imprimir_texto(superficie=self.janela, texto="Feito por: " + DEV, tamanho=13, cor=COR_BRANCO,
                           posicao=(100, ALTURA_JANELA - 20))
            imprimir_texto(superficie=self.janela, texto="Movimento: Setas", tamanho=13, cor=COR_BRANCO,
                           posicao=(65, ALTURA_JANELA - 80))
            imprimir_texto(superficie=self.janela, texto="Pulo: Seta Cima ou Espaço", tamanho=13, cor=COR_BRANCO,
                           posicao=(90, ALTURA_JANELA - 60))
            imprimir_texto(superficie=self.janela, texto="Tiro: Ctrl", tamanho=13, cor=COR_BRANCO,
                           posicao=(39, ALTURA_JANELA - 40))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        opcao_selecionada = (opcao_selecionada + 1) % len(OPCOES_MENU)
                    elif evento.key == pygame.K_UP:
                        opcao_selecionada = (opcao_selecionada - 1) % len(OPCOES_MENU)
                    elif evento.key == pygame.K_RETURN:
                        return OPCOES_MENU[opcao_selecionada]
