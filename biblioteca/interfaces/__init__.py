import random


def linha(tam=56):
    '''
    #retorna caracteres a serem exibidos na tela
    :param tam: quantidade de caracteres a serem repetidos
    :return: string com os caracteres repetidos
    '''
    return '-' * tam


def titulo(txt):
    '''
    #Imprime um título no tela
    :param txt: texto a ser exibido no título
    :return:
    '''
    print(linha())
    print(f'\033[0;31m{txt.center(56)}\033[m')
    print(linha())


def validarOpcaoLista(texto, lista):
    '''
    #Recebe um texto e uma lista e retorna um index escolhido da lista
    :param texto: texto a ser exibido
    :param lista: lista de itens a serem exibidos
    :return: index da lista
    '''
    while True:
        try:
            opcao = int(input(texto))
            if not 1 <= opcao <= len(lista):
                raise ValueError
        except (TypeError, ValueError):
            print('\033[0;31mOpção Inválida!\033[m')
        else:
            print(f'\033[0;32mVocê digitou: {lista[opcao-1]}\033[m')
            return opcao-1


def validarFloat(min, max):
    '''
    #Recebe os parâmetros min e max do tipo inteiro e retorna um valor do tipo float entre min e max
    :param min: parâmetro limíte inferior
    :param max: parâmetro limite superior
    :return: valor tipo float válido
    '''
    while True:
        try:
            entrada = float(input(f'Digite um valor entre {min} e {max}: ').strip().replace(',','.'))
            if not min <= entrada <= max:
                raise ValueError
        except (TypeError, ValueError):
            print('\033[0;31mEntrada Inválida!\033[m')
        else:
            print(f'\033[0;32mVocê digitou: {entrada}\033[m')
            return entrada


def validarInt(min, max):
    '''
    #Recebe os parâmetros min e max do tipo inteiro e retorna um valor do tipo float entre min e max
    :param min: parâmetro limíte inferior
    :param max: parâmetro limite superior
    :return: valor tipo float válido
    '''
    while True:
        try:
            entrada = int(input(f'Digite um valor entre {min} e {max}: ').strip())
            if not min <= entrada <= max:
                raise ValueError
        except (TypeError, ValueError):
            print('\033[0;31mEntrada Inválida!\033[m')
        else:
            print(f'\033[0;32mVocê digitou: {entrada}\033[m')
            return entrada


def exibirMenu(lista):
    '''
    #Recebe uma lista, exibe os itens da lista e retorna a opção selecionada
    :param lista: lista de itens a exibir
    :return: inteiro selecionado
    '''
    titulo('Selecione uma opção:')
    count = 1
    for item in lista:
        print(f'{count} - {item}')
        count += 1
    print(linha())
    indexSelecao = validarOpcaoLista('Opção: ', lista)
    return indexSelecao
