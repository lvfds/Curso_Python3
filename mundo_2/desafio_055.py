# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0

for contador in range(1,6):
    peso_digitado_pelo_usuario = float(input(f'Digite o peso do {contador}° usuário: '))
    if contador == 1:
        maior_peso = peso_digitado_pelo_usuario
        menor_peso = peso_digitado_pelo_usuario
    elif peso_digitado_pelo_usuario > maior_peso:
        maior_peso = peso_digitado_pelo_usuario
    elif peso_digitado_pelo_usuario < menor_peso:
        menor_peso = peso_digitado_pelo_usuario

print(f'O maior peso foi de {maior_peso}Kg e o menor foi {menor_peso}Kg.')

