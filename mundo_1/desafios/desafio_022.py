"""
Crie um programa que leia um nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas.
    - O nome com todas as letras minúsculas.
    - Quantas letras tem ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome.

"""

nome_completo_usuario = input('Digite o seu nome completo: ')
primeiro_nome = nome_completo_usuario.split()
print(f'O seu nome com todas as letras maiúsculas: {nome_completo_usuario.upper()}.')
print(f'O seu nome com todas as letras minúsculas: {nome_completo_usuario.lower()}.')
print(f'O seu nome tem {len(nome_completo_usuario.replace(" ",""))} letras sem espaços.')
print(f'O seu primeiro nome tem {len(primeiro_nome[0])} letras.')
