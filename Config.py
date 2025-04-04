import pygame
#Info trabalho:
DEV="Guilherme Garnizé"
RU=4579677
# Cores
COR_TEXTO_MENU = [(255, 255, 0), (255, 255, 255)]
COR_FUNDO_MENU = (0, 0, 128)
COR_PLATAFORMA = (0, 255, 0)
COR_CHAO = (139, 69, 19)
COR_LARANJA = (255, 128, 0)
COR_AMARELO = (255, 255, 128)
COR_BRANCO = (255, 255, 255)
COR_VERDE = (0, 128, 0)
COR_CIANO = (0, 128, 128)

# Dimensões da janela
LARGURA_JANELA = 800
ALTURA_JANELA = 600
PLATAFORMA_ALTURA = 20
PLATAFORMA_LARGURA = 100

#LOCALIZACOES
CHAO_LOCALIZACAO = []

# Opções de menu
OPCOES_MENU = ["Começar!", "Sair"]

# Parâmetros de física
GRAVIDADE = 3.2
FORCA_PULO = 40
VELOCIDADE_JOGADOR = 5
TIRO_INIMIGO = 2
TIRO_JOGADOR = 3
ATRASO_TIRO_INIMIGO = 100
ATRASO_TIRO_JOGADOR = 20

# Outras constantes
ATRASO_PULO = 400 #ms
FPS = 45
