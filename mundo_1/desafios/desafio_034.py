"""
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1250.00, calcule um aumento de 10%.
    Para inferiores ou iguais o aumento é de 15%.

"""

salario_funcionario = float(input('Digite seu salário: '))
if salario_funcionario < 1250.00:
    aumento_salario = (salario_funcionario * 15) / 100
    novo_salario_com_aumento = salario_funcionario + aumento_salario
    print(f'O seu salário R${salario_funcionario:.2f} ganhou 15% de aumento, foi adicionado R${aumento_salario:.2f}. Seu novo salário é de R${novo_salario_com_aumento:.2f}.')
else:
    aumento_salario = (salario_funcionario * 10) / 100
    novo_salario_com_aumento = salario_funcionario + aumento_salario
    print(f'O seu salário R${salario_funcionario:.2f} ganhou 10% de aumento, foi adicionado R${aumento_salario:.2f}. Seu novo salário é de R${novo_salario_com_aumento:.2f}.')

