from Config import ALTURA_JANELA, LARGURA_JANELA, PLATAFORMA_ALTURA, PLATAFORMA_LARGURA
from codigo.Chao import Chao
from codigo.ImagemFundo import ImagemFundo
from codigo.Inimigo import Inimigo
from codigo.Jogador import Jogador
from codigo.Plataforma import Plataforma


class FabricaEntidades:
    @staticmethod
    def criar_entidade(tipo, **kwargs):
        if tipo == "Fase1_":
            lista_fundos = []
            for i in range(5):
                lista_fundos.append(ImagemFundo(f'Fase1_{i + 1}', (0, 0)))
                lista_fundos.append(ImagemFundo(f'Fase1_{i + 1}', (LARGURA_JANELA, 0)))
            return lista_fundos
        if tipo == "jogador":
            return Jogador(posicao=kwargs.get("posicao", (10, ALTURA_JANELA - PLATAFORMA_ALTURA)),
                           chao=kwargs.get("chao", []),
                           plataforma=kwargs.get("plataforma", []),
                           construcao=kwargs.get("construcao", []),
                           )
        elif tipo == "inimigo":
            return Inimigo(posicao=kwargs.get("posicao", (300, 50)),
                           chao=kwargs.get("chao", []),
                           plataforma=kwargs.get("plataforma", []),
                           construcao=kwargs.get("construcao", []))

        elif tipo == "plataforma":
            posicao = kwargs.get("posicao", (100, 200))
            tamanho = (kwargs.get("width", PLATAFORMA_LARGURA), kwargs.get("height", PLATAFORMA_ALTURA))
            imagem = (kwargs.get("imagem_custom", "chao_base"))
            return Plataforma(posicao[0], posicao[1], tamanho[0], tamanho[1], imagem)
        elif tipo == "chao":
            lista_chao = []
            chao = 0
            while chao <= (LARGURA_JANELA / PLATAFORMA_LARGURA) + PLATAFORMA_LARGURA:
               lista_chao.append(Chao(chao * PLATAFORMA_LARGURA))
               chao += 1
            return lista_chao
        else:
            return None
