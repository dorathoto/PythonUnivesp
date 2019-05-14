###############################################
# Referência: https://www.vooo.pro/insights/6-passos-faceis-para-aprender-o-algoritmo-naive-bayes-com-o-codigo-em-python/


# A probabilidade de uma pessoa ter certa doença A é de 1% consequentemente, a probabilidade de não ter a doença é de 99%
probabilidade_doenca = 0.01
probabilidade_nao_doenca = 1 - probabilidade_doenca

# Um teste T para detectar a doença não é 100% confiável, detectando a doença em pessoas não doentes e não detectando em pessoas doentes

# O teste detecta a doença em pessoas doentes em 90% dos casos e não detecta a doença em pessoas doentes em 10% dos casos
prob_teste_pos_e_doenca = 0.9
prob_teste_neg_e_doenca = 0.1

# O teste detecta a doença em pessoas não doentes em 5% dos casos e não detecta a doença em pessoas não doentes em 95% dos casos
prob_teste_pos_e_nao_doenca = 0.05
prob_teste_neg_e_nao_doenca = 0.95

# Verdadeiro positivo: chance de ter a doença e o teste dar positivo
prob_verdadeiro_positivo = probabilidade_doenca * prob_teste_pos_e_doenca
# Verdadeiro negativo: chance de não ter a doença e o teste dar negativo
prob_verdadeiro_negativo = probabilidade_nao_doenca * prob_teste_neg_e_nao_doenca
# Falso positivo: chance de não ter a doença e o teste dar positivo
prob_falso_positivo = probabilidade_nao_doenca * prob_teste_pos_e_nao_doenca
# Falso negativo: chance de ter a doença e o teste dar negativo
prob_falso_negativo = probabilidade_doenca * prob_teste_neg_e_doenca

# Fizemos o teste e o resultado foi positivo. Qual a chance de eu ter a doença?
# Teorema de Bayes: P(D|A) = (P(A|D) * P(D)) / (P(A|D) * P(D) + P(A|¬D) * P(¬D))
# P(D|A) = Probabilidade de doença dado um teste positivo. É o que desejamos calcular
# P(A|D) = Probabilidade do teste ser positivo se você tem a doença -> 90%
# P(D) = Probabilidade de ter a doença -> 1%
# P(A|¬D) = Probabilidade do teste ser positivo e você não ter a doença -> 5%
# P(¬D) = Probabilidade de não ter a doença -> 99%


P_A_D = prob_teste_pos_e_doenca
P_D = probabilidade_doenca
P_A_ND = prob_teste_pos_e_nao_doenca
P_ND = probabilidade_nao_doenca
prob_doente_dado_positivo = (P_A_D * P_D) / (P_A_D * P_D + P_A_ND * P_ND)
print(prob_doente_dado_positivo)
