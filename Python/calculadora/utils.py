def coletarValoresS():
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    return valor1, valor2

def coletarValoresC():
    valor = int(input('Diite o valor: '))
    return valor

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

    listaInt = []
    for item in lista:
        try:
            listaInt.append(int(item))
        except ValueError:
            return None

    return listaInt