# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_do_funcionario = float(input('Digite seu salário R$'))
aumento_do_salario = (salario_do_funcionario * 15) / 100
novo_salario_funcionario = salario_do_funcionario + aumento_do_salario
print(f'O seu salário era {salario_do_funcionario}, com o aumento de 15%(R${aumento_do_salario}) seu salário ficou R${novo_salario_funcionario} .')
