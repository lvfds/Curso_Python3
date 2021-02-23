"""
    Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
    Ex:
    0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

"""
from time import sleep
valor_digitado = int(input('Digite um número para fazer sua sequência de Fibonacci: '))

contador = 0
numero_anterior_1 = -1
numero_anterior_2 = 1
while contador <= valor_digitado:
    numero_fibonacci = numero_anterior_1 + numero_anterior_2
    if contador == valor_digitado:
        sleep(1)
        print(f'{numero_fibonacci} → FIM')
    else:
        print(numero_fibonacci,end=' → ')
        numero_anterior_1 = numero_anterior_2
        numero_anterior_2 = numero_fibonacci
        sleep(1)
    contador+=1
