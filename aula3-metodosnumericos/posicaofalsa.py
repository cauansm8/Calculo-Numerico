import math

def f(x):
    y = x - x * math.log(x)
    return y

def posicaofalsa():

    a = 2
    b = 4
    x = a
    e = 10**-3
    
    if f(a) == 0:
        print("FIM")
        return a
    
    if f(b) == 0:
        print("FIM")
        return b
    
    if f(a) * f(b) > 0:
        print("o método não pode ser aplicado. FIM.")
        return

    k = 1

    while (k < itmax):
        x_k = (a * f(b) - b * f(a)) / (f(b) - f(a))

        erro = abs(b-a) / max(1, abs(b))

        if abs(b - a) / max(1, abs(b)) < e:
            break

        elif f(a) * f(x_k) < 0:
            b = x_k

        else:
            a = x_k

        k += 1
    
    print(f'x = {x_k}')
    print(f'iteracoes: {k}')
    print(f'erro: {erro}')


itmax = 4
posicaofalsa()