from Config import ENTIDADE_VELOCIDADE, JAN_LARGURA
from codigo.Entidade import Entidade


class ImagemFundo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTIDADE_VELOCIDADE[self.name]
        if self.rect.right <= 0:
            self.rect.left = JAN_LARGURA