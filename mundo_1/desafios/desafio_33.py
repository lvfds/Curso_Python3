# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

maior_numero = -1
menor_numero = 999999999999

numero_digitado_1 = int(input('Digite o 1° número: '))
numero_digitado_2 = int(input('Digite o 2° número: '))
numero_digitado_3 = int(input('Digite o 3° número: '))

if maior_numero < numero_digitado_1:
    maior_numero = numero_digitado_1
if maior_numero < numero_digitado_2:
    maior_numero = numero_digitado_2
if maior_numero < numero_digitado_3:
    maior_numero = numero_digitado_3

if menor_numero > numero_digitado_1:
    menor_numero = numero_digitado_1
if menor_numero > numero_digitado_2:
    menor_numero = numero_digitado_2
if menor_numero > numero_digitado_3:
    menor_numero = numero_digitado_3

print(f'O maior número digitado foi {maior_numero} e o menor número foi {menor_numero}.')

