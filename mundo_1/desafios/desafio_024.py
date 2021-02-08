# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

nome_digitado = input('Digite um nome de qualquer cidade: ')
nome_da_cidade = nome_digitado.upper().split()
if 'SANTO' in nome_da_cidade[0]:
    print(f'{" ".join(nome_da_cidade)} começa com SANTO no nome!')
else:
    print(f'{" ".join(nome_da_cidade)} não começa com SANTO no nome!')

