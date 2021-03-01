"""
    Crie um programa que leia a idade e o sexo de várias pessoas.
    A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
    No final, mostre:
    A) Quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadrastrados.
    C) Quantas mulheres tem menos de 20 anos.

"""
continuar_programa = True
pessoas_com_mais_de_18_anos = 0
quantidade_de_homens_cadrastrados = 0
quantidade_de_mulheres_com_menos_de_20_anos = 0
while continuar_programa == True:

    print('-'*32)
    print(f'{"CADRASTRE UMA PESSOA":^32}')
    print('-'*32)
    idade_da_pessoa = int(input('Digite sua idade: '))
    if idade_da_pessoa >= 18:
        pessoas_com_mais_de_18_anos+=1
    sexo_da_pessoa = input('Digite seu sexo [M/F]: ').strip().upper()[0]
    if sexo_da_pessoa == 'M':
        quantidade_de_homens_cadrastrados+=1
    elif sexo_da_pessoa == 'F' and idade_da_pessoa < 20:
        quantidade_de_mulheres_com_menos_de_20_anos+=1
    while sexo_da_pessoa != 'M' and sexo_da_pessoa != 'F':
        sexo_da_pessoa = input('Digite seu sexo [M/F]: ').strip().upper()[0]
    deseja_continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if deseja_continuar != 'S':
        break
    while deseja_continuar != 'S'  and deseja_continuar != 'N':
        deseja_continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    print('-'*32)
print(f'Total de pessoas com mais de 18 anos: {pessoas_com_mais_de_18_anos}')
print(f'Ao todos temos {quantidade_de_homens_cadrastrados} homens cadatrados.')
print(f'E temos {quantidade_de_mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos.')