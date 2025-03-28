# arquivo: codigo/Chao.py
from codigo.Entidade import Entidade

class Chao(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Cria uma area de contato com metade da altura do chão, deslocada para a parte inferior
        self.area_contato = self.rect.copy()
        self.area_contato.height = self.rect.height // 2
        self.area_contato.top = self.rect.top + (self.rect.height // 2)

    def move(self):
        # O chão não se move, então não faz nada.
        pass
