"""
    Faça um programa que leia um  número de 0 a 9999 e mostre na tela cada um dos digitos separados.
    Ex:
    Digite um número: 1834
    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1

"""

numero_digitado = input('Digite um número: ')

if len(numero_digitado) == 1:
    print(f'Unidade: {numero_digitado[0]}')
else:
    if len(numero_digitado) == 2:
        print(f'Unidade: {numero_digitado[1]}')
        print(f'Dezena: {numero_digitado[0]}')
    elif len(numero_digitado) == 3:
        print(f'Unidade: {numero_digitado[2]}')
        print(f'Dezena: {numero_digitado[1]}')
        print(f'Centena: {numero_digitado[0]}')
    elif len(numero_digitado) == 4:
        print(f'Unidade: {numero_digitado[3]}')
        print(f'Dezena: {numero_digitado[2]}')
        print(f'Centena: {numero_digitado[1]}')
        print(f'Milhar: {numero_digitado[0]}')

