# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: 6.127, O número 6.127 tem a parte inteira 6.

import math 

numero_real = float(input('Digite um número real: '))
print(f'O número {numero_real} tem a parte inteira {math.floor(numero_real)}.')


