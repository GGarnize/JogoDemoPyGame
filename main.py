import random
random.seed(4579677)  # Guilherme Garnizé. Usando o RU como "número mágico" caso precisa usar o random em algum ponto do codigo

from codigo.Jogo import Jogo

if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
