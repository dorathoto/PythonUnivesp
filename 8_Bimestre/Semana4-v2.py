''' Como foi conversado bastante sobre ferramentas utilizei bibliotecas para os calculos
Porém poderia se ter feito manualmente já que a lista é pequena.
Utilizado o Panda, biblioteca mais famosa para Estatística em python
https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1

Recomendo executar pelo Spyder https://www.spyder-ide.org/
Manual básico spyder-https://panda.ime.usp.br/panda/static/data/python/spyder.pdf
'''

import pandas as pd

tabela = [63, 50, 57, 56, 68, 82, 75, 95, 47, 75, 95, 47, 75, 95, 47, 63, 50, 57, 56, 68, 82, 75, 95, 47,
          61, 76, 61, 52, 63, 80, 80, 68, 72, 64, 77]
palavras = ["chocolate", "chocolate", "chocolate", "biscoito", "biscoito",
            "cafe", "suco", "feijao", "arroz"]

exemploPanda = pd.Series(tabela)
exemploPandaPalavras = pd.Series(palavras)


# Média pelo Panda
print('Média.: ', exemploPanda.mean())

# Exemplo Mediana by Panda
print('Mediana..: ', exemploPanda.median())

print('Quartil..: ', exemploPanda.quantile())
print('Q1.......: ', exemploPanda.quantile(q=0.25))
print('----  Quartil - Q1,Q2,Q3 -----')
print(exemploPanda.quantile([0.25, 0.5, 0.75]))
print('----  Moda  -----')
print(exemploPanda.mode())
print('Moda strings: ', exemploPandaPalavras.mode())
print('---------------')
print('Amplitude (max - min).: ', exemploPanda.max() - exemploPanda.min())


print('Variancia.....: ', exemploPanda.var())
print('Desvio Padrão.: ', exemploPanda.std())
