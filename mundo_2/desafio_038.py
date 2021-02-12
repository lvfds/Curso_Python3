"""
    Escreva um número que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    - O primeiro é maior.
    - O segundo é maior.
    - Não existe valor maior, os dois são iguais.

"""

numero_1 = int(input('Digite o 1° número: '))
numero_2 = int(input('Digite o 2° número: '))

if numero_1 > numero_2:
    print(f'O número {numero_1} é maior do que {numero_2}.')
elif numero_2 > numero_1:
    print(f'O número {numero_2} é maior do que o {numero_1}.')
else:
    print(f'Não existe valor maior, os dois são iguais!')

