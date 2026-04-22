#Estudo independente em python
#Data: 21/04/26
from simples import soma, mult, sub, div, divInt, poten
from cientifica import raizQuadrada, fatorial, log
from estatisticas import mediana, media
from utils import coletarValoresS, coletarValoresC, valorLog, listaEstatisticas

sair = 'N'

print(f'{"Bem-Vindo à Calculadora":=^50}')
print('Feito por: MarqkDi')
print('=' * 50)

while sair == 'N':
    print('1 - Calculadora Simples \n2 - Calculadora Científica \n3 - Estatisticas \n0 - Sair')
    print('')
    escolhaCalc = int(input('Escolha uma opção: '))
    print('')

    #Parte da Simples
    if escolhaCalc == 1:
        print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Divisão Inteira\n6 - Potenciação')
        print('')
        escolhaSOp = int(input('Qual tipo de operação deseja?: '))
        print('')

        if escolhaSOp not in [1, 2, 3, 4, 5, 6]:
            print('Opção inválida')
            continue

        v1, v2 = coletarValoresS()

        if escolhaSOp == 1: resultado = soma(v1, v2)
        elif escolhaSOp == 2: resultado = sub(v1, v2)
        elif escolhaSOp == 3: resultado = mult(v1, v2)
        elif escolhaSOp == 4: resultado = div(v1, v2)
        elif escolhaSOp == 5: resultado = divInt(v1, v2)
        elif escolhaSOp == 6: resultado = poten(v1, v2)

        if resultado is None:
            print('Erro: divisão por zero!')
        else:
            print(f'Resultado: {resultado:.2f}')

    #Parte da Cientifica 
    elif escolhaCalc == 2:

        print('1 - Raiz quadrada \n2 - Logaritmo \n3 - Fatorial \n4 - Máximo divisor comum \n5 - Mínimo múltiplo comum \n6 - Cosseno \n7 - Seno \n8 - Tangente')
        print('')
        escolhaCOp = int(input('Qual tipo de operação deseja?: '))
        print('')

        if escolhaCOp not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print('Opção inválida')
            continue

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
        
        elif escolhaCOp == 4:
            print('Em trabalho')

        elif escolhaCOp == 5:
            print('Em trabalho')
        
        elif escolhaCOp == 6:
            print('Em trabalho')

        elif escolhaCOp == 7:
            print('Em trabalho')

        elif escolhaCOp == 8:
            print('Em trabalho')
    
    #Parte das Estatisticas
    elif escolhaCalc == 3:
        
        print('1 - Mediana \n2 - Moda \n3 - Media')
        print('')
        escolhaEOp = int(input('Escolha a operação que deseja: '))
        print('')

        if escolhaEOp not in [1, 2, 3]:
            print('Opção inválida')
            continue

        lista = listaEstatisticas()

        if escolhaEOp == 1:
            if lista is not None:
                resultado = mediana(lista)
                print(f'A mediana da lista é: {resultado:.2f}')
            else: 
                print('Digite apenas números!')
        
        elif escolhaEOp == 2:
            print('Em trabalho')

        elif escolhaEOp == 3:
            resultado = media(lista)
            print(f'A média é: {resultado:.2f}')
    
    #Fechamento da aplicação no menu
    elif escolhaCalc == 0: 
        print('Você será sempre Bem-Vindo de volta!')
        break

    #Verificação da escolha
    else:
        print('Opção inválida!')
        continue
    
    #Escolha de fechamento da aplicação
    while True:
        print('')
        sair = input('Deseja fechar a aplicação?(Y/N) ').upper()

        if sair == 'Y':
            break
        elif sair == 'N':
            break
        else:
            print('Escolha inválida')