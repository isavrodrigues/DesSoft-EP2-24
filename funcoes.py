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