# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
nome_usuario = input('Digite o seu nome: ')
if 'SILVA' in nome_usuario.upper():
    print(f'Seu nome: {nome_usuario}, tem SILVA no nome!')
else:
    print(f'Seu nome: {nome_usuario}, não tem SILVA no nome!')