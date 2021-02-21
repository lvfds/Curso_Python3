"""
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
    Ex:
    5! = 5x4x3x2x1 = 120

"""
from math import factorial
contador = 0
numero_digitado = int(input('Digite um número fatorial: '))
numero_original = numero_digitado
print(f'{numero_digitado}! = ',end='')
while numero_digitado >= contador:
    if numero_digitado == 0:
        print(f'{numero_digitado} = {factorial(numero_original)}', end='')
    else:
        print(f'{numero_digitado} X ', end='')
    numero_digitado-=1

