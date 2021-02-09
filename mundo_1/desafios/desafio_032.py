# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano_digitado = int(input('Digite um ano qualquer: '))
if ano_digitado %4 == 0:
    print(f'O ano de {ano_digitado} é BISSEXTO.')
else:
    print(f'O ano de {ano_digitado} não é BISSEXTO.')

