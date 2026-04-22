def mediana(a):
    a.sort()
    qnt = len(a)
    meio = qnt // 2
    meioDiv = (a[meio] + a[meio - 1]) / 2
    
    if qnt % 2 != 0:
        return a[meio]
    else:
        return meioDiv
    
def media(a):
    soma = 0
    qnt = len(a)
    for item in a:
        soma = item + soma
    media = soma / qnt
    return media