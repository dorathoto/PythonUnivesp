'''
Para a função f(x)= x^2−9=0

f(xn)−f(xn−1)/xn−xn−1
Método secante é igual ao Newton, mas não precisamos utilizar a derivada, com isso precisamos de mais interações.
'''
def FuncSecante(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    contador_interacao = 0
    while abs(f_x1) > eps and contador_interacao < 100:
        denominador = float(f_x1 - f_x0)/(x1 - x0)
        x = x1 - float(f_x1)/denominador
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        contador_interacao += 1
    # Aqui, uma solução é encontrada ou muitas iterações
    if abs(f_x1) > eps:
        contador_interacao = -1
    return x, contador_interacao

def f(x):
    return x**2 - 9
x0 = 1000;   x1 = x0 - 1

solucao, semInteracoes = FuncSecante(f, x0, x1, eps=1.0e-6)

if semInteracoes > 0:    # Solução encontrada
    print("Qtd. de interações: %d" % (2 + semInteracoes))
    print("A solução é: %f" % (solucao))
else:
    print("Solução não encontrada")