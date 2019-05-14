'''
Semana 1 e 2
Probabilidade Condicional

P(A | B) -> Probabilidade condicional de A dado B, ou seja, probabilidade do evento A ocorrer, dado que ocorreu o evento B
P(A, B) -> Como já vimos, é a probabilidade dos dois eventos ocorrerem
P(A) e P(B) -> Também, como já vimos, é a probabilidade de cada evento acontecer
Para eventos dependentes, o cálculo é o seguinte:

P(A | B) = P(A, B)/P(B)

E algumas vezes, passamos P(B) para o outro lado da igualdade, e a equação fica assim:

P(A, B) = P(A | B) × P(B)

Vejamos um exemplo e um pouco de código. Consideremos um dado. Seja o primeiro evento tirar um número ímpar e o segundo tirar um 5 ou 6 no dado. Vamos calcular a probabilidade de A dado B.

P(A | B) = ??

P(A) = 3/6

P(B) = 2/6

P(A, B) = 2/6 × 3/6 = 0, 16666 ou 16, 66 %, ou ainda 1/6 – Este resultado equivale a nossa única possibilidade, que é o número 5.
'''

from fractions import Fraction

# Probabilidade do evento A: dado ser ímpar
probabilidade_impar = 3/6
# Probabilidade do evento B: dado ser 5 ou 6
probabilidade_5_ou_6 = 2/6
# Probabilidade dos dois eventos
probabilidade_ambos = probabilidade_impar * probabilidade_5_ou_6
print(probabilidade_ambos)

print(Fraction(probabilidade_ambos).limit_denominator())


# Probabilidade de A dado B igual a P(A,B) / P(B)
probabilidade_a_dado_b = probabilidade_ambos / probabilidade_5_ou_6
print(probabilidade_a_dado_b)

print(Fraction(probabilidade_a_dado_b).limit_denominator())
