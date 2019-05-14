'''
Versão 1.0 baseada na https://github.com/reamat/CalculoNumerico/blob/master/cap_equacao1d/codes/python/metodo_da_bissecao/bissecao.py

Para a função f(x)= x^2−9=0

Apesar de precisar muitas interações (muitos loops) pelo que entendi, com esse método não falha, onde o método Newton falha.
f'(xn)=0   http://www.bessegato.com.br/PUC/cdi_newton.htm


'''
import sys
def FuncBissecao(f, x_L, x_R, eps, return_x_list=False):
    f_L = f(x_L)
    if f_L*f(x_R) > 0:
        print("Erro! A função não possui sinais opostos nos pontos finais do intervalo!")
        sys.exit()
    x_M = float(x_L + x_R)/2.0
    f_M = f(x_M)
    contador_interacao = 1
    if return_x_list:
        x_list = []

    while abs(f_M) > eps:
        if f_L*f_M > 0:
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = float(x_L + x_R)/2
        f_M = f(x_M)
        contador_interacao += 1
        if return_x_list:
            x_list.append(x_M)
    if return_x_list:
        return x_list, contador_interacao
    else:
        return x_M, contador_interacao

def f(x):
    return x**2 - 9

a = 0;   b = 1000

solucao, semInteracoes = FuncBissecao(f, a, b, eps=1.0e-6)

print("Qtd. de interações: %d" % (1 + 2*semInteracoes))
print("A solução é: %f" % (solucao))
