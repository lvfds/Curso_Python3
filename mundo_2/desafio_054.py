# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas aindam não atingiram a maior idade e quantas já são maiores.

from datetime import datetime

menores_de_idade = 0
maiores_de_idade = 0

for contador in range(1,8):
    ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
    if datetime.now().year - ano_de_nascimento < 21:
        menores_de_idade+=1
    else:
        maiores_de_idade+=1

print(f'No total foram: {maiores_de_idade} maiores de idade e {menores_de_idade} menores de idade.')

