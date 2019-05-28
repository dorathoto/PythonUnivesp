# Programa para gerar estatistica de probabilidade
# Semana 2 - VideoAula 7 - https://www.youtube.com/watch?time_continue=754&v=K1MXYc_89D8
# OBS: Mediana e moda foi feito com a biblioteca statistics do que uma função para verificar (Mediana o item do meio entre todos sorteados) e a moda (item mais comum dos sorteados)

from random import randint
import statistics   # Utilizado para fazer a mediana

# Estatística de quantos números saiu, dado tem 6 faces, 6variaveis
qtdNumero1 = 0
qtdNumero2 = 0
qtdNumero3 = 0
qtdNumero4 = 0
qtdNumero5 = 0
qtdNumero6 = 0

somatoriaValores = 0
EsperancaMedia = 0

variancia = 0
arrayValoresParaMediana = []

# qtdMax será a quantidade máxima a ser jogada
qtdMax = int(
    input('Quantas vezes gostaria de jogar o dado de 6 faces não viciado? '))

# cada repetição estará na variavel interaçã ex:interacao=0 1ª jogada; interacao=1 2ª jogada..etc
for interacao in range(1, qtdMax):

    # RND contém o número gerado aleatóriamente entre 1 e 6
    rnd = randint(1, 6)

    # variavel que soma os valores mesma coisa que (somatoriaValores = somatoriaValores + rnd) ela é igual ao valor dela (antigo) mais o novo random
    somatoriaValores += rnd

    # Calculo de Variancia, inicialmente faço uma temporária Variancia
    # ** é exponenciação em python (fórmula https://drive.google.com/file/d/1x8vP4FuVxfN2PpwnUOxMP-NHBA-PZJdI/preview)
    mediaTemp = somatoriaValores / interacao
    tempvariancia = ((somatoriaValores**2) -
                     (interacao*mediaTemp)**2)/interacao-1
    # Se quiser mostrar o valor em cada interação só descomentar a linha abaixo
    # print(F'{interacao}: {somatoriaValores}/{interacao+1} => {tempvariancia} rnd{rnd}')

    # Vou somando as variancias
    variancia += tempvariancia

    if(rnd == 1):
        qtdNumero1 += 1
    elif(rnd == 2):
        qtdNumero2 += 1
    elif(rnd == 3):
        qtdNumero3 += 1
    elif(rnd == 4):
        qtdNumero4 += 1
    elif(rnd == 5):
        qtdNumero5 += 1
    else:
        qtdNumero6 += 1

    arrayValoresParaMediana.append(rnd)

print('#############################################')
print('###            Estatística Final          ###')
print('###   Qtd. de vezes que cada número saiu  ###')
print('#############################################')

vpercent1 = '{0:.2f}'.format((qtdNumero1/qtdMax)*100)
print(F'Número 01.:  {qtdNumero1} - Porcentagem.: {vpercent1}%')

vpercent2 = '{0:.2f}'.format((qtdNumero2/qtdMax)*100)
print(F'Número 02.:  {qtdNumero2} - Porcentagem.: {vpercent2}%')

vpercent3 = '{0:.2f}'.format((qtdNumero3/qtdMax)*100)
print(F'Número 03.:  {qtdNumero3} - Porcentagem.: {vpercent3}%')

vpercent4 = '{0:.2f}'.format((qtdNumero4/qtdMax)*100)
print(F'Número 04.:  {qtdNumero4} - Porcentagem.: {vpercent4}%')

vpercent5 = '{0:.2f}'.format((qtdNumero5/qtdMax)*100)
print(F'Número 05.:  {qtdNumero5} - Porcentagem.: {vpercent5}%')

vpercent6 = '{0:.2f}'.format((qtdNumero6/qtdMax)*100)
print(F'Número 06.:  {qtdNumero6} - Porcentagem.: {vpercent6}%')

EsperancaMedia = somatoriaValores/qtdMax
print(F'Esperança média.:(teórico: 3.5), real: {EsperancaMedia}')

# PQ ficou negativo ainda é um mistério.
print(F'Variância.:(teórico: 2.9), real: {variancia/qtdMax}')

# https://docs.python.org/3/library/statistics.html#statistics.median
print(F'Mediana: {statistics.median(arrayValoresParaMediana)}')

# Poderia simplesmente verificar as porcentagens qual é mais alta, logo ela é a Moda
print(F'Moda: {statistics.mode(arrayValoresParaMediana)}')
