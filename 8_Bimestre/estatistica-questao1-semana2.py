#Cabeçalho da questão
print('-----------------------------------------')
print('Questão 1 - Exercício de apoio - Semana 2')
print('-----------------------------------------')
print('\n')
#Recomendações para os alunos entenderem a resolução
print('- Iniciando a resolução do exercício, relembrar o teorema da probabilidade condicional,')
print('e o teorema do produto quando A e B são eventos independentes')
print('\n')

#Variáveis e valores, respectivamente, das quantidades fornecidas
quantidade_a, quantidade_b, quantidade_c, quantidade_d = 0.4, 0.3, 0.2, 0.1
#Variáveis e valores, respectivamente, do índice de qualidade de cada fornecedor
qualidade_a, qualidade_b, qualidade_c, qualidade_d = 0.8, 0.75, 0.7, 0.6
#Inicializando variáveis de operação que iremos fazer mais pra frente
p_ruim, p_b_interseccao_ruim, p_b_dado_ruim = 0, 0, 0

#Para calcular a porcentagem ruim, basta fazer  quantidade_entrega * (1 - qualidade_N)
#P(RUIM)
p_ruim = (quantidade_a * (1 - qualidade_a))
p_ruim += (quantidade_b * (1 - qualidade_b))
p_ruim += (quantidade_c * (1 - qualidade_c))
p_ruim += (quantidade_d * (1 - qualidade_d))
print('O cálculo da porcentagem das verduras ruins resultou em: %.2f' % (p_ruim))

#Teorema do produto para A e B independentes
#P(FORNECEDORB INTERSECÇÃO RUIM) = P(FORNECEDORB) * P(RUINS DO FORNECEDOR B)
p_b_interseccao_ruim = quantidade_b * (1 - qualidade_b)
print('O cálculo da intersecção resultou em: %.2f' % (p_b_interseccao_ruim))

#Probabilidade Condicional
#P(FORNECEDOR B DADO RUIM) = P(FORNECEDORB INTERSECÇÃO RUIM) / P(RUIM)
p_b_dado_ruim = p_b_interseccao_ruim /p_ruim
print('O resultado final é: %.2f' % (p_b_dado_ruim))