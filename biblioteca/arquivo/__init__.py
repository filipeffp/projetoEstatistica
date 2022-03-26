def criarArquivo(arquivo):
    '''
    #Cria um arquivo com cabeçalho
    :param arquivo:
    :return:
    '''
    try:
        arq = open(arquivo, 'wt+')
        arq.close()
    except:
        print(f'Não foi possível criar o arquivo!{arquivo}')
    else:
        lista = ['GÊNERO','REGIÃO_DOMICILIAR','ESCOLARIDADE','CLASSE_ECONÔMICA','POSSUI_COMORBIDADE',
                 'QUANTIDADE_DE_DOSES_DA_VACINA','EXERCÍCIOS_SEMANALMENTE','IDADE',
                 'PESO','ALTURA']
        salvarNoArquivo(lista,arquivo)
        print(f'Arquivo {arquivo} criado com sucesso!')


def verificarArquivo(arquivo):
    '''
    #Verifica se o arquivo recebido como parâmetro existe, caso não exista ele é criado.
    :param arquivo:
    :return:
    '''
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        criarArquivo(arquivo)


def salvarNoArquivo(lista, arquivo):
    '''
    #Recebe uma lista e um objeto do tipo arquivo do tipo txt e salva os itens da lista por linha
    :param lista: lista com obetos tipo texto
    :param arquivo: arquivo do tipo texto
    :return:
    '''
    with open(arquivo, 'a', newline='', encoding='utf-8') as arquivo:
        for c in range(0, len(lista)):
            if c < len(lista) - 1:
                arquivo.write(lista[c] + ',')
            else:
                arquivo.write(lista[c])
        arquivo.write('\n')
