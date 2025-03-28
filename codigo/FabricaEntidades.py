# arquivo: codigo/FabricaEntidades.py
import random
from Config import JAN_LARGURA, JAN_ALTURA
from codigo.ImagemFundo import ImagemFundo
from codigo.Jogador import Jogador
from codigo.Chao import Chao
from codigo.Inimigo import Inimigo

class FabricaEntidades:

    @staticmethod
    def cria_entidade(entidade_nome):
        match entidade_nome:
            case 'Fase1_':
                lista_fundos = []
                for i in range(5):
                    lista_fundos.append(ImagemFundo(f'Fase1_{i + 1}', (0, 0)))
                    lista_fundos.append(ImagemFundo(f'Fase1_{i + 1}', (JAN_LARGURA, 0)))
                return lista_fundos

            case 'Jogador':
                return [Jogador('Jogador', (10, 50))]

            case 'Chao':
                return [Chao('chao_base', (0, JAN_ALTURA - 35))]

            case 'Inimigo':
                return [Inimigo('Inimigo', (JAN_LARGURA - 170 ,50))]

            case _:
                return []
