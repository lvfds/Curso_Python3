# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero_digitado = int(input('Digite um número inteiro: '))
if numero_digitado % 2 == 0:
    print(f'O número {numero_digitado} é par!')
else:
    print(f'O número {numero_digitado} é ímpar!')

