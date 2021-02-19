# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

FONTE_VERMELHA_COM_NEGRITO = '\033[1;31m'
LIMPAR_A_COR_DA_FONTE = '\033[0m'
sexo_da_pessoa = ''

while sexo_da_pessoa != 'M' and sexo_da_pessoa != 'F':
    sexo_da_pessoa = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if sexo_da_pessoa == 'M':
        print('Você é do sexo masculino!')
    elif sexo_da_pessoa == 'F':
        print('Você é do sexo feminino!')
    else:
        print(f'{FONTE_VERMELHA_COM_NEGRITO}ERRO! VOCÊ DIGITOU {sexo_da_pessoa} que é um SEXO INVÁLIDO!{LIMPAR_A_COR_DA_FONTE}')

