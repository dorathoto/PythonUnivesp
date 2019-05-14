# Programa para gerar estatistica de probabilidade
# OBS: Número aleatório em programação não é realmente aleatório, verifique sorteando números baixo como 20 e depois altos como 999999

# Importando biblioteca de Random
from random import randint

# Estatística de quantos números saiu, dado tem 6 faces, 6variaveis
qtdNumero1 = 0
qtdNumero2 = 0
qtdNumero3 = 0
qtdNumero4 = 0
qtdNumero5 = 0
qtdNumero6 = 0


qtdMax = int(
    input('Quantas vezes gostaria de jogar o dado de 6 faces não viciado? '))

for interacao in range(qtdMax):
    rnd = randint(1, 6)

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
