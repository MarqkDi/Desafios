import numpy as np
def raizQuadrada(a):
    for i in np.arange(0, a + 1, 1e-6):
        if abs(i * i - a) < 0.001:
            return i
    return None

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