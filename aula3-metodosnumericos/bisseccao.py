import math


def funcao(x):
    y = x - x * math.log(x)
    return y

def bissecao():
    
    a = 2
    b = 4
    x = a
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

    while (k < itmax):
        x_k = (a + b) / 2.0

        erro = abs(b-a) / max(1, abs(b))

        if abs(b - a) / max(1, abs(b)) < e:
            break

        elif funcao(a) * funcao(x_k) < 0:
            b = x_k

        else:
            a = x_k

        k += 1
    
    print(f'x = {x_k}')
    print(f'iteracoes: {k}')
    print(f'erro: {erro}')

itmax = 4
bissecao()