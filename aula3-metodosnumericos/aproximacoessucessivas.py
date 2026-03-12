import math

def f(x):
    y = x - x * math.log(x)
    return y

def phi_de_x(x):
    y = x / math.log(x)
    return y

def aprox_sucessivas():
    
    a = 2
    b = 4
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

    x = (b + a) / 2.

    k = 1
    while (k < itmax):
        x_antigo = x

        x = phi_de_x(x)

        erro = abs(x - x_antigo) / max(1, abs(x))

        if erro < e:
            break

        k += 1


    print(f'x = {x}')
    print(f'iteracoes: {k}')
    print(f'erro: {erro}')


itmax = 4
aprox_sucessivas()