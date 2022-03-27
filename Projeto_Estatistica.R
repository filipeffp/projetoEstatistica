#Importe o arquivo de texto no Rstudio
dados =  read.csv(
  file = 'C:/Users/filip/PycharmProjects/projetoEstatistica2/form_estatistica.txt',
  sep = ',',
  dec = '.',
  header = TRUE,
  encoding = "UTF-8"
)

#função percentual
porcentagem <- function(percentual) {
  return(table(percentual)/length(percentual)*100)
}

imc <- sort(c(dados$PESO/(dados$ALTURA^2)))

##Obtenha as porcentagens de cada variável qualitativa
porcGenero <- porcentagem(dados$GÊNERO)
porcRegiao <- porcentagem(dados$REGIÃO_DOMICILIAR)
porcEscolaridade <- porcentagem(dados$ESCOLARIDADE)
porcClasse <- porcentagem(dados$CLASSE_ECONÔMICA)
porcComorbidade <- porcentagem(dados$POSSUI_COMORBIDADE)

##Obtenha média, mediana, Q1, Q3, variância e desvio padrão de cada variável
##quantitativa

#médias
mediaDoses <- round(mean(dados$QUANTIDADE_DE_DOSES_DA_VACINA), digits = 2)
mediaExercicios <- round(mean(dados$EXERCÍCIOS_SEMANALMENTE), digits = 2)
mediaIdade <- round(mean(dados$IDADE), digits = 2)
mediaPeso <- round(mean(dados$PESO), digits = 2)
mediaAltura <- round(mean(dados$ALTURA), digits = 2)

#Medianas
medianaDoses <- round(median(dados$QUANTIDADE_DE_DOSES_DA_VACINA), digits = 2)
medianaExercicios <- round(median(dados$EXERCÍCIOS_SEMANALMENTE), digits = 2)
medianaIdade <- round(median(dados$IDADE), digits = 2)
medianaPeso <- round(median(dados$PESO), digits = 2)
medianaAltura <- round(median(dados$ALTURA), digits = 2)

#Quartis Q1
q1Doses <- quantile(dados$QUANTIDADE_DE_DOSES_DA_VACINA, 0.25)
q1Exercicios <- quantile(dados$EXERCÍCIOS_SEMANALMENTE, 0.25)
q1Idade <- quantile(dados$IDADE, 0.25)
q1Peso <- quantile(dados$PESO, 0.25)
q1Altura <- quantile(dados$ALTURA, 0.25)

#Quartis Q3
q3Doses <- quantile(dados$QUANTIDADE_DE_DOSES_DA_VACINA, 0.75)
q3Exercicios <- quantile(dados$EXERCÍCIOS_SEMANALMENTE, 0.75)
q3Idade <- quantile(dados$IDADE, 0.75)
q3Peso <- quantile(dados$PESO, 0.75)
q3Altura <- quantile(dados$ALTURA, 0.75)

#Desvios padrão
desvDoses <- sd(dados$QUANTIDADE_DE_DOSES_DA_VACINA)
desvExercicios <- sd(dados$EXERCÍCIOS_SEMANALMENTE)
desvIdade <- sd(dados$IDADE)
desvPeso <- sd(dados$PESO)
desvAltura <- sd(dados$ALTURA)

#Variâncias
varDoses <- var(dados$QUANTIDADE_DE_DOSES_DA_VACINA)
varExercicios <- var(dados$EXERCÍCIOS_SEMANALMENTE)
varIdade <- var(dados$IDADE)
varPeso <- var(dados$PESO)
varAltura <- var(dados$ALTURA)

##Faça um gráfico para cada variável estudada
#"GÊNERO"
#"REGIÃO_DOMICILIAR"
#"ESCOLARIDADE"
#"CLASSE_ECONÔMICA"
#"POSSUI_COMORBIDADE"
#"QUANTIDADE_DE_DOSES_DA_VACINA"
#"EXERCÍCIOS_SEMANALMENTE"
#"IDADE"
#"PESO"                        
#"ALTURA"

##Utilize, pelo menos uma vez, os seguintes gráficos:
#gráfico de barras
#pizza
#histograma
#box-plot
#gráfico de dispersão

barplot(table(dados$GÊNERO),
        main = "Gêneros dos casos graves de COVID",
        )

pie(table(dados$REGIÃO_DOMICILIAR),
    main = "Região domiciliar \n dos casos graves de COVID",
    )

hist(dados$PESO,
     breaks = ,
     main = "Peso dos casos graves de COVID",
     xlab = "Peso(Kg)",
     ylab = "Casos graves"
     )

boxplot(imc,
        main = "IMC(Peso/Altura²)\ndos casos graves de COVID",
        ylab = 'IMC'
        )

plot(x = dados$PESO, y = dados$EXERCÍCIOS_SEMANALMENTE,
     xlab = "Peso",
     ylab = "Exercícios semanais",
     xlim = c(30, 110),
     ylim = c(0, 7),
     main = "Dispersão de Peso versus Exercícios semanais\ndos casos graves de COVID",
     type = 'p'
)

hist(dados$IDADE,
     main = 'Idades dos casos graves de COVID',
     xlab = 'Faixas de idades',
     ylab = 'Frequência de idades',
     )

barplot(table(dados$POSSUI_COMORBIDADE),
        main = 'Casos graves de COVID com comorbidade',
        ylim = c(0,20),
        ylab = 'pessoas'
        )

barplot(table(dados$ESCOLARIDADE),
        main = 'Escolaridade dos casos graves de COVID',
        ylim = c(0,10),
        ylab = 'Pessoas'
        )

barplot(table(dados$CLASSE_ECONÔMICA),
        main = 'Classe econômica dos casos graves de COVID',
        ylab = 'Pessoas'
        )

barplot(table(dados$QUANTIDADE_DE_DOSES_DA_VACINA),
        main = 'Quantidade de doses de vacina tomadas',
        xlab = 'Doses de vacina',
        ylab = 'Pessoas'
        )