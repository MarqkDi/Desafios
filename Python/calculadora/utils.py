def coletarValoresS():
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    return valor1, valor2

def coletarValoresC():
    try:
        valor = int(input('Digite o valor: '))
        return valor
    except ValueError:
        print('Digite apenas números!')
        return None

def valorLog():
    logaritmando = int(input('Qual o logaritmando: '))
    if logaritmando <= 0: 
        return None
    
    base = int(input('Qual a base do logaritmo: '))
    if base <= 1:
        return None
    
    return logaritmando, base

def listaEstatisticas():
    entrada = input('Digite os items separados por espaço: ')
    lista = entrada.split()

    listaFlo = []
    for item in lista:
        try:
            listaFlo.append(float(item))
        except ValueError:
            print('Digite apenas Números!')
            return None

    return listaFlo