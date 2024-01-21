def define_posicoes(dados_de_posicionamento):
    #inicializo uma lista para alocar as posicoes
    posicoes = []

    #alocando linhas,colunas,orientacao, e tamanho da embarcação
    linha = dados_de_posicionamento['linha']
    coluna = dados_de_posicionamento['coluna']
    orientacao = dados_de_posicionamento['orientacao']
    tamanho = dados_de_posicionamento['tamanho']
    
    #para cada posição do navio
    #se o tamanho for 3 a lista posicoes tera tamanho 3, 4 tera tamanho 4...
    for i in range(tamanho):
        if orientacao == 'vertical':
            #deve-se incrementar a linha
            posicoes.append([linha+i, coluna])
        else:
            #posição == 'horizontal'
            posicoes.append([linha, coluna+i]) 

    return posicoes

def preenche_frota(dados_de_posicionamento,nome_navio,frota):
    posicoes = define_posicoes(dados_de_posicionamento)
    dados_frota = {}
    dados_frota['tipo'] = nome_navio
    dados_frota['posicoes'] = posicoes

    #adicionando o dicionario criado na lista frota
    frota.append(dados_frota)


    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    elif tabuleiro[linha][coluna]==0:
        tabuleiro[linha][coluna]='-'
    return tabuleiro    


   