"""
    Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.

"""

from time import sleep

opcao_escolhida_pelo_usuario = 0
numero_1 = int(input('Digite o 1° número: '))
numero_2 = int(input('Digite o 2° número: '))

while opcao_escolhida_pelo_usuario > -1:
    print("""
    MENU DE OPÇÕES:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """)
    opcao_escolhida_pelo_usuario = int(input('Digite uma das opções a cima: '))
    if opcao_escolhida_pelo_usuario == 1:
        print(f'A soma de {numero_1} + {numero_2}  = {numero_1+numero_2}')
        sleep(2.5)
    elif opcao_escolhida_pelo_usuario == 2:
        print(f'A multiplicação de {numero_1} x {numero_2} = {numero_1*numero_2}')
        sleep(2.5)
    elif opcao_escolhida_pelo_usuario == 3:
        if numero_1 > numero_2:
            print(f'O número {numero_1} é maior do que o número {numero_2}.')
            sleep(2.5)
        elif numero_2 > numero_1:
            print(f'O número {numero_2} é maior do que o número {numero_1}.')
            sleep(2.5)
        else:
            print(f'O número {numero_1} é igual ao {numero_2}, por isso não possuí o maior valor.')
            sleep(2.5)
    elif opcao_escolhida_pelo_usuario == 4:
        numero_1 = int(input('Digite o 1° número: '))
        numero_2  = int(input('Digite o 2° número: '))
        sleep(2.5)
    elif opcao_escolhida_pelo_usuario == 5:
        print('Saindo do programa ...')
        sleep(2.5)
        break
    else:
        TEXTO_VERMELHO_COM_NEGRITO = ('\033[1;31m')
        LIMPAR_FORMATACAO_TEXTO = ('\033[0m')
        print(f'{TEXTO_VERMELHO_COM_NEGRITO}ERRO! O NÚMERO {opcao_escolhida_pelo_usuario} NÃO FOI RECONHECIDO!{LIMPAR_FORMATACAO_TEXTO}')
        sleep(2.5)

