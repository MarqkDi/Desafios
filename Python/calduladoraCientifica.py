#Estudo independente em python
#Data: 21/04/26
import numpy as np
exit = 'N'
print(f'{'Bem-Vindo à Calculadora':=^50}')
print('Feito por: MarqkDi')
print('=' * 50)

# Funções
def coletarValores():
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    return valor1, valor2

# Calculadora Simples
def soma(a,b): return a + b
def sub(a,b): return a - b
def mult(a,b): return a * b
def div(a,b): return a / b if b != 0 else None
def divInt(a,b): return a // b if b != 0 else None
def poten(a,b): return a ** b

#Calculadora Científica
def raizQuadrada(a):
    for i in np.arange(0, a + 1, 0.00001):
        if abs(i * i - a) < 0.001:
            return i
    return None

while exit == 'N':
    print('1 - Calculadora Simples')
    print('2 - Calculadora Científica')
    escolhaCalc = int(input('Escolha o tipo de calculadora: '))
    if escolhaCalc == 1:
        print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Divisão Inteira\n6 - Potenciação')
        escolhaSOp = int(input('Qual tipo de operação deseja?: '))

        v1, v2 = coletarValores()

        if escolhaSOp == 1: resultado = soma(v1, v2)
        elif escolhaSOp == 2: resultado = sub(v1, v2)
        elif escolhaSOp == 3: resultado = mult(v1, v2)
        elif escolhaSOp == 4: resultado = div(v1, v2)
        elif escolhaSOp == 5: resultado = divInt(v1, v2)
        elif escolhaSOp == 6: resultado = poten(v1, v2)
        else:
            print('Opção inválida')
            continue

        if resultado is None:
            print('Erro: divisão por zero!')
        else:
            print(f'Resultado: {resultado:.2f}')
        
    elif escolhaCalc == 2:

        print('1 - Raiz quadrada \n2 - Logaritmo \n3 - Fatorial \n4 - Máximo divisor comum \n5 - Mínimo múltiplo comum \n6 - Cosseno \n7 - Seno \n8 - Tangente')
        escolhaCOp = int(input('Qual tipo de operação deseja?: '))

        if escolhaCOp == 1:

            valRQ = float(input('Digite o valor que deseja descobrir a Raiz Quadrada: '))
            resultado = raizQuadrada(valRQ)

            if resultado is not None:
                print(f'A Raiz aproximada é: {resultado:.2f}')
            else:
                print('Resultado não encontrado')
    else:
        print('Escolha inválida!')
    
    #Escolha de fechamento da aplicação
    while True:
        exit = input('Deseja fechar a aplicação?(Y/N) ').upper()

        if exit == 'Y':
            break
        elif exit == 'N':
            break
        else:
            print('Escolha inválida')