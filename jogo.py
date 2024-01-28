import random
from funcoes import *


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '___________      ___________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
coordenadas_informadas = []
jogando = True
while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    
    linha_jogador = int(input("Escolha a linha para atacar: "))
    while linha_jogador not in range(0, 10):
        print('Linha inválida!')
        linha_jogador = int(input("Escolha a linha para atacar: "))

    coluna_jogador = int(input("Escolha a coluna para atacar: "))
    while coluna_jogador not in range(0, 10):
        print('Coluna inválida!')
        coluna_jogador = int(input("Escolha a coluna para atacar: "))


    atual = []
    atual.append(linha_jogador)
    atual.append(coluna_jogador)
    if atual not in coordenadas_informadas:
        coordenadas_informadas.append(atual)
        jogada = faz_jogada(tabuleiro_oponente, linha_jogador, coluna_jogador)
    else:
        print(f"A posição linha {linha_jogador} e coluna {coluna_jogador} já foi informada anteriormente!")
        print("Linha inválida!")
        print("Coluna inválida!")
    atual = []
    atualizado = afundados(frota_oponente, tabuleiro_oponente)
    if atualizado >= len(frota_oponente):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False


    
    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
    # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
    # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
