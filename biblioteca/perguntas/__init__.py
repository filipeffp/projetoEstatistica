from biblioteca.interfaces import *


def variavelQualitativa(lista):
    '''
    #Recebe uma lista de valores a serem exibidos e retorna uma string correspondente ao item selecionado na lista
    :param lista: lista com itens a serem exibidos
    :return: retorna o objeto do tipo string selecionado na lista
    '''
    valor = str(lista[exibirMenu(lista)])
    #print(f'valor de valor === {valor}')
    return valor


def variavelQuantitativaContinua(min, max):
    '''
    #Recebe dois inteiros e retorna uma string correspondente a um valor float variando entre o parâmetro
    min e o parâmetro max
    :param min: limite inferior
    :param max: limite superior
    :return: string correspondente ao float selecionado
    '''
    valor = str(validarFloat(min, max))
    return valor


def variavelQuantitativaDiscreta(min, max):
    '''
        #Recebe dois inteiros e retorna uma string correspondente a um valor inteiro variando entre o
        parâmetrovmin e o parâmetro max
        :param min: limite inferior
        :param max: limite superior
        :return: string correspondente ao inteiro selecionado
        '''
    valor = str(validarInt(min, max))
    return valor
