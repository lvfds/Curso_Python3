"""
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
    - A média de idade do grupo.
    - Qual é o nome do homem mais velho.
    - Quantas mulheres tem menos de 20 anos.
"""
from math import floor

nome_do_homem_mais_velho = ''
idade_do_homem_mais_velho = 0
quantidade_de_mulheres_com_menos_de_20_anos = 0
media_de_idade_do_grupo = 0

for contador in range(1,5):
    nome_do_usuario = input('Digite seu nome: ')
    idade_do_usuario = int(input('Digite sua idade: '))
    sexo_do_usuario = input('Digite seu sexo [M/F]: ')
    media_de_idade_do_grupo+=idade_do_usuario
    if sexo_do_usuario == 'M' or sexo_do_usuario == 'm':
        if idade_do_homem_mais_velho < idade_do_usuario:
            idade_do_homem_mais_velho = idade_do_usuario
            nome_do_homem_mais_velho = nome_do_usuario
    elif sexo_do_usuario == 'F' or sexo_do_usuario == 'f':
        if idade_do_usuario < 20:
            quantidade_de_mulheres_com_menos_de_20_anos+=1

print(f'O nome do homem mais velho é {nome_do_homem_mais_velho}, a idade média do grupo é de {floor(media_de_idade_do_grupo / 4)} anos e possuí {quantidade_de_mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos. ')

