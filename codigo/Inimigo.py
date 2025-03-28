from Config import JAN_ALTURA
from codigo.Entidade import Entidade
from codigo.Jogador import GRAVIDADE


class Inimigo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_x = 0
        self.vel_y = 0
        self.no_chao = False

    def move(self):
        self.rect.x -= self.speed_x

        # Aplicando gravidade
        self.vel_y += GRAVIDADE
        self.rect.y += self.vel_y

        # Limitar para não sair da tela (ou checar colisão com chão)
        # Aqui apenas um exemplo de "chão" no final da janela,
        # mas depois faremos a colisão com a entidade "Chao".
        if self.rect.bottom >= JAN_ALTURA:
            self.rect.bottom = JAN_ALTURA
            self.vel_y = 0
            self.no_chao = True