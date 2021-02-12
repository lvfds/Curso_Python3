"""

    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    - 1 para binário.
    - 2 para octal.
    - 3 para hexadecimal.


"""
cor_vermelha = '\033[1;31m'
limpar_cor = '\033[0m'
numero_inteiro = int(input('Digite um número: '))
numero_escolhido_para_a_base_de_conversao = int(input("""
Escolha qual será a base de conversão:
- 1 para binário.
- 2 para octal.
- 3 para hexadecimal

Digite aqui: """))

if numero_escolhido_para_a_base_de_conversao == 1:
    print('A base escolhida foi binário!')
    print(f'O número {numero_inteiro} convertido para binário ficou assim: {bin(numero_inteiro)[2:]}. ')
elif numero_escolhido_para_a_base_de_conversao == 2:
    print('A base escolhida foi octal!')
    print(f'O número {numero_inteiro} convertido para octal ficou assim: {oct(numero_inteiro)[2:]}.')
elif numero_escolhido_para_a_base_de_conversao == 3:
    print('A base escolhida foi hexadecimal!')
    print(f'O número {numero_inteiro} convertido para hexadecimal ficou assim: {hex(numero_inteiro)[2:]}')
else:
    print(f'{cor_vermelha}ERRO! ESSA BASE DE CONVERSÃO NÃO FOI RECONHECIDA!{limpar_cor}')

