# C
import pygame

C_LARANJA = (255, 128, 0)
C_AMARELO = (255, 255, 128)
C_BRANCO = (255, 255, 255)
C_VERDE = (0, 128, 0)
C_CIANO = (0, 128, 128)

# E
EVENTO_INIMIGO = pygame.USEREVENT + 1
EVENTO_TIMEOUT = pygame.USEREVENT + 2
ENTIDADE_VELOCIDADE = {
    'Fase1_1': 0,
    'Fase1_2': 3,
    'Fase1_3': 2,
    'Fase1_4': 2,
    'Fase1_5': 1,
    'Fase2_1': 0,
    'Fase2_2': 1,
    'Fase2_3': 2,
    'Fase2_4': 3,
    'Fase2_5': 4,
    'Jogador': 3,
    'JogadorTiro': 1,
    'Inimigo': 1,
    'InimigoTiro': 5
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}

#F
FORCA_PULO = 15

#G
GRAVIDADE = 1

#J
JAN_LARGURA = 576
JAN_ALTURA = 324

# M
MENU_OPCOES = ('Novo Jogo',
               'Pontuação',
               'Fechar')
#N
NASCIMENTO_INTERVALO = 4000

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# T
TIMEOUT_STEP = 100  # 100ms
TEMPO_FASE = 20000  # 20s

# S
SCORE_POS = {'Title': (JAN_LARGURA / 2, 50),
             'EnterName': (JAN_LARGURA / 2, 80),
             'Label': (JAN_LARGURA / 2, 90),
             'Name': (JAN_LARGURA / 2, 110),
             0: (JAN_LARGURA / 2, 110),
             1: (JAN_LARGURA / 2, 130),
             2: (JAN_LARGURA / 2, 150),
             3: (JAN_LARGURA / 2, 170),
             4: (JAN_LARGURA / 2, 190),
             5: (JAN_LARGURA / 2, 210),
             6: (JAN_LARGURA / 2, 230),
             7: (JAN_LARGURA / 2, 250),
             8: (JAN_LARGURA / 2, 270),
             9: (JAN_LARGURA / 2, 290),
             }
