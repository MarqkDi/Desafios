def raizQuadrada(a, precisao = 0.0001, max_iteracao = 1000):

    inicio = 0
    fim = a
    iteracao = 0

    while (fim - inicio) > precisao and iteracao < max_iteracao:
        meio = (inicio + fim) / 2

        if meio * meio < a:
            inicio = meio
        else:
            fim = meio

        iteracao += 1

    return (inicio + fim) / 2

def fatorial(a):
    if a < 0:
        return None

    resultado = 1
    for i in range(a, 1, -1):
        resultado *= i 
    return resultado

def log(a, b):
    for i in range(a):
        calc = b ** i
        if calc == a:
            resultado = i
            return resultado
    return None