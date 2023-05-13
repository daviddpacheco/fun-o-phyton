""""
def dobrar():
    numero = float(input("Digite um numero"))
    resultado = numero * 2
    return resultado
print(' O dobro do numero é: ',dobrar())
"""

"""def somar():
    numero1 = float(input("Digite o primeiro numero da soma"))
    numero2 = float(input("Digite o segundo numero"))
    resultado = numero1 + numero2
    return resultado
print('O resultado da soma é: ', somar())
"""


del fatorial(n)
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input('Digite o numero que vc quer calcular o fatorial; '))

print("O fatorial de", n, "é", fatorial(n))
