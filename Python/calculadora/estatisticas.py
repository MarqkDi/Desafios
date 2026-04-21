def mediana(a):

    listaInt = []
    for item in a:
        listaInt.append(int(item))

    listaInt.sort()
    qnt = len(listaInt)
    meio = qnt // 2
    meioDiv = (listaInt[meio] + listaInt[meio - 1]) / 2
    
    if qnt % 2 != 0:
        return listaInt[meio]
    else:
        return meioDiv