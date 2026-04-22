def mediana(a):
    a.sort()
    qnt = len(a)
    meio = qnt // 2
    meioDiv = (a[meio] + a[meio - 1]) / 2
    
    if qnt % 2 != 0:
        return a[meio]
    else:
        return meioDiv