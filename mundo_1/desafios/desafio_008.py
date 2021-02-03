# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_em_metros = int(input('Digite o valor em metros(m): '))
valor_em_centimetros = valor_em_metros * 100
valor_em_milimetros = valor_em_metros * 1000
print(f'O valor {valor_em_metros}m convertido para centímetros é {valor_em_centimetros}, convertido para milímetros é {valor_em_milimetros}.')