def converterd_b(n):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    binario = int(binario)
    return binario
def converterb_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal


print("Digite a opção desejada:\n1 - Decimal em binário:\n2 - Binário em decimal")
opc = int(input("Digite a opção: "))
if opc==1:
    numeroD = int(input("Digite o número decimal: "))
    print(f"O número na base 10 {numeroD} em binário (base 2) é: {converterd_b(numeroD)}")