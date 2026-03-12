import math


def funcao(x):
    y = x - x * math.log(x)
    return y

def secante():
    
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

    x0 = a
    x1 = b

    while (k < itmax):

        x = x1 - ((x1 - x0) * funcao(x1)) / (funcao(x1) - funcao(x0))

        erro = abs(x - x1) / max(1, abs(x))

        if erro < e:
            break

        x0 = x1
        x1 = x

        k += 1
    
    print(f'x = {x}')
    print(f'iteracoes: {k}')
    print(f'erro: {erro}')

itmax = 4
secante()
