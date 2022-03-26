from biblioteca.interfaces import *
from biblioteca.arquivo import *
from biblioteca.perguntas import *
from time import sleep

nomeArquivo = 'form_estatistica.csv'
verificarArquivo(nomeArquivo)
titulo('FORMULÁRIO COVID')
menu = ('Cadastrar Novo', 'Encerrar')
while True:
    indexSelecionado = exibirMenu(menu)
    if indexSelecionado == 0:
        resposta = []
        #VARIÁVEIS QUALITATIVAS
        genero = ['Masculino', 'Feminino']
        titulo('GÊNERO:')
        resposta.append(variavelQualitativa(genero))
        regiao = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
        titulo('REGIÃO DOMICILIAR:')
        resposta.append(variavelQualitativa(regiao))
        escolaridade = ['Superior', 'Médio', 'Fundamental', 'Básico', 'Sem escolaridade']
        titulo('ESCOLARIDADE:')
        resposta.append(variavelQualitativa(escolaridade))
        titulo('CLASSE ECONÔMICA')
        classeEconomica = ['Baixa', 'Média', 'Alta']
        resposta.append(variavelQualitativa(classeEconomica))
        titulo('POSSUI COMORBIDADE: ')
        comorbidade = ['sim', 'não']
        resposta.append(variavelQualitativa(comorbidade))
        #VARIÁVEIS QUANTITATIVAS
        # qtdDoses = de 1 a 3
        titulo('QUANTIDADE DE DOSES DA VACINA TOMADAS:')
        resposta.append(variavelQuantitativaDiscreta(0, 3))
        # diasExercicioSemanal = de 0 a 7
        titulo('QUANTIDADE DE DIAS QUE PRATICA EXERCÍCIO SEMANALMENTE:')
        resposta.append(variavelQuantitativaDiscreta(0, 7))
        # faixaEtaria = de 0 a 200
        titulo('IDADE: ')
        resposta.append(variavelQuantitativaDiscreta(0, 120))
        # peso = de 0 a 500
        titulo('PESO')
        resposta.append(variavelQuantitativaContinua(0, 200))
        # altura = de 0 a 3
        titulo('ALTURA: ')
        resposta.append(variavelQuantitativaContinua(0, 3))

        print(resposta)

        salvarNoArquivo(resposta, nomeArquivo)
    elif indexSelecionado == 1:
        print('Encerrado!')
        break
    else:
        print('\033[0;31mOpção inválida!\033[m')
    sleep(1)
