from Config import LARGURA_JANELA
from codigo.Entidade import Entidade
from codigo.Inimigo import Inimigo
from codigo.Jogador import Jogador
from codigo.Plataforma import Plataforma
from codigo.TiroInimigo import TiroInimigo
from codigo.TiroJogador import TiroJogador


class MediadorEntidades:
    @staticmethod
    def __verificar_colisao_janela(ent: Entidade):
        if isinstance(ent, TiroInimigo):
            if ent.rect.right < 0:
                ent.vida = 0
        if isinstance(ent, TiroJogador):
            if ent.rect.left > LARGURA_JANELA:
                ent.vida = 0

    @staticmethod
    def __verificar_colisao_entidade(ent1: Entidade, ent2: Entidade):
        interacao_valida = False
        if isinstance(ent1, Inimigo) and isinstance(ent2, TiroJogador):
            interacao_valida = True
        elif isinstance(ent1, TiroJogador) and isinstance(ent2, Inimigo):
            interacao_valida = True
        elif isinstance(ent1, Jogador) and isinstance(ent2, TiroInimigo):
            interacao_valida = True
        elif isinstance(ent1, TiroInimigo) and isinstance(ent2, Jogador):
            interacao_valida = True

        if interacao_valida:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.vida -= ent2.dano
                ent2.vida -= ent1.dano

    @staticmethod
    def verificar_colisao(lista_entidades: list[Entidade]):
        for i in range(len(lista_entidades)):
            entidade1 = lista_entidades[i]
            MediadorEntidades.__verificar_colisao_janela(entidade1)
            for j in range(i + 1, len(lista_entidades)):
                entidade2 = lista_entidades[j]
                MediadorEntidades.__verificar_colisao_entidade(entidade1, entidade2)

    @staticmethod
    def verificar_vida(lista_entidades: list[Entidade]):
        for entidade in lista_entidades:
            if entidade.vida <= 0:
                lista_entidades.remove(entidade)

    @staticmethod
    def verificar_fim_fase(lista_entidades: list) -> str | bool:
        jogadores = [e for e in lista_entidades if isinstance(e, Jogador)]
        inimigos = [e for e in lista_entidades if isinstance(e, Inimigo)]
        construcao = [e for e in lista_entidades if isinstance(e, Plataforma) and e.nome == 'Casa']
        if not jogadores:
            return 'perdeu'
        jogador = jogadores[0]
        for casa in construcao:
            if jogador.rect.colliderect(casa.rect) and not inimigos:
                return 'ganhou'
        return False