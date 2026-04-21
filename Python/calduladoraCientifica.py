import math
#Estudo independente em python
#Data: 21/04/26
exit = 'N'
print(f'{'Bem-Vindo à Calculadora':=^50}')
print('Feito por: MarqkDi')
print('=' * 50)
while exit == 'N':
    print('1 - Calculadora Simples')
    print('2 - Calculadora Científica')
    escolhaCalc = int(input('Escolha o tipo de calculadora: '))
    if escolhaCalc == 1:
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Divisão Inteira')
        print('6 - Potenciação')
        escolhaSOp = int(input('Qual tipo de operação deseja?: '))
        def coletarValores():
            valor1 = float(input('Digite o primeiro valor: '))
            valor2 = float(input('Digite o segundo valor: '))
            return valor1, valor2
        def soma(a,b):
            return a + b
        def sub(a,b):
            return a - b
        def mult(a,b):
            return a * b
        def div(a,b):
            return a / b
        def divInt(a,b):
            return a // b
        def poten(a,b):
            return a ** b
        if escolhaSOp == 1:
            v1, v2 = coletarValores()
            resultado = soma(v1, v2)
            print(f'O resultado da soma é: {resultado:.2f}')
        elif escolhaSOp == 2:
            v1, v2 = coletarValores
            resultado = sub(v1, v2)
            print(f'O resultado da subtração é: {resultado:.2f}')
        elif escolhaSOp == 3:
            v1, v2 = coletarValores
            resultado = mult(v1, v2)
            print(f'O resultado da multiplicação é: {resultado:.2f}')
        elif escolhaSOp == 4:
            v1, v2 = coletarValores
            resultado = div(v1, v2)
            print(f'O resultado da divisão é: {resultado:.2f} \nCom um resto de {v1 % v2}')
        elif escolhaSOp == 5:
            v1, v2 = coletarValores
            resultado = divInt(v1, v2)
            print(f'O resultado da divisão inteira é: {resultado}')
        elif escolhaSOp == 6:
            v1, v2 = coletarValores
            resultado = poten(v1, v2)
            print(f'O resultado da potenciação é: {resultado:.2f}')
    elif escolhaCalc == 2:
        print('1 - Raiz quadrada')
        print('2 - Logaritmo')
        print('3 - Fatorial')
        print('4 - Máximo divisor comum')
        print('5 - Mínimo múltiplo comum')
        print('6 - Cosseno')
        print('7 - Seno')
        print('8 - Tangente')
        escolhaCOp = int(input('Qual tipo de operação deseja?: '))
    else:
        print('Escolha inválida!')
    exit = input('Deseja fechar a aplicação?(Y/N) ').upper()