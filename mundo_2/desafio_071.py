"""
    Crie um programa que simule o funcionamento de um caixa eletrônico.
    no início, pergunte ao usuário qual será valor o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

cedulas_de_50 = cedulas_de_20 = cedulas_de_10 = cedulas_de_1 = 0

print('-'*30)
print(f'{"BANCO CEV":^30}')
print('-'*30)
valor_para_ser_sacado = int(input('Digite o valor que você quer sacar: '))
while valor_para_ser_sacado > 0:
    if valor_para_ser_sacado >= 50:
        valor_para_ser_sacado = valor_para_ser_sacado - 50
        cedulas_de_50+=1
    elif valor_para_ser_sacado >= 20:
        valor_para_ser_sacado = valor_para_ser_sacado - 20
        cedulas_de_20+=1
    elif valor_para_ser_sacado >= 10:
        valor_para_ser_sacado = valor_para_ser_sacado - 10
        cedulas_de_10+=1
    elif valor_para_ser_sacado >= 1:
        valor_para_ser_sacado = valor_para_ser_sacado - 1
        cedulas_de_1 +=1

while cedulas_de_50 > 0:
    print(f'Total de {cedulas_de_50} cédulas de R$50.')
    break
while cedulas_de_20 > 0:
    print(f'Total de {cedulas_de_20} cédulas de R$20.')
    break
while cedulas_de_10 > 0:
    print(f'Total de {cedulas_de_10} cédulas de R$10.')
    break
while cedulas_de_1 > 0:
    print(f'Total de {cedulas_de_1} cédulas de R$1.')
    break
