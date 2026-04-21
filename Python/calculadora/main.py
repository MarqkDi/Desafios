#Estudo independente em python
#Data: 21/04/26
from simples import soma, mult, sub, div, divInt, poten
from cientifica import raizQuadrada, fatorial, log
from utils import coletarValoresS, coletarValoresC, valorLog

exit = 'N'

print(f'{'Bem-Vindo à Calculadora':=^50}')
print('Feito por: MarqkDi')
print('=' * 50)

while exit == 'N':
    print('1 - Calculadora Simples')
    print('2 - Calculadora Científica')
    escolhaCalc = int(input('Escolha o tipo de calculadora: '))
    if escolhaCalc == 1:
        print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Divisão Inteira\n6 - Potenciação')
        escolhaSOp = int(input('Qual tipo de operação deseja?: '))

        v1, v2 = coletarValoresS()

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
            v1 = coletarValoresC()
            resultado = raizQuadrada(v1)
            if resultado is not None:
                print(f'A Raiz aproximada é: {resultado:.2f}')
            else:
                print('Resultado não encontrado')

        elif escolhaCOp == 2:
            valores = valorLog()
            if valores is not None:
                logaritmando, base = valores
                resultado = log(logaritmando, base)
                if resultado is not None:
                    print(f'O logaritmo exato é: {resultado}')
                else:
                    print('Resultado não encontrado (Não é exato)!')
            
        elif escolhaCOp == 3:
            v1 = coletarValoresC()
            resultado = fatorial(v1)
            if resultado is not None:
                print(f'{v1}! é igual à: {resultado}')
            else:
                print('Valor inválido!')

    else:
        print('Opção inválida!')
        continue
    
    #Escolha de fechamento da aplicação
    while True:
        exit = input('Deseja fechar a aplicação?(Y/N) ').upper()

        if exit == 'Y':
            break
        elif exit == 'N':
            break
        else:
            print('Escolha inválida')