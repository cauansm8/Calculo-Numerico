import math


def funcao(x):
    y = x - x * math.log(x)
    return y

def f_derivada(x):
    y = - math.log(x)
    return y

def newton():
    
    a = 2
    b = 4
    e = 10**-3

    if funcao(a) == 0:
        print("FIM")
        return a
    
    if funcao(b) == 0:
        print("FIM")
        return b
    
    if funcao(a) * funcao(b) > 0:
        print("o método não pode ser aplicado. FIM.")
        return

    k = 1

    x = (a + b) / 2.

    while (k < itmax):

        x_antigo = x

        x = x_antigo - (funcao(x) / f_derivada(x))

        erro = abs(x - x_antigo) / max(1, abs(x))

        if erro < e:
            break

        k += 1
    
    print(f'x = {x}')
    print(f'iteracoes: {k}')
    print(f'erro: {erro}')

itmax = 4
newton()