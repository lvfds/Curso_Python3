# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = float(input('Digite o comprimento da 1ª reta: '))
reta_2 = float(input('Digite o comrpimento da 2ª reta: '))
reta_3 = float(input('Digite o comprimento da 3ª reta: '))

if reta_1 + reta_2 > reta_3 and reta_2 + reta_3 > reta_1 and reta_1 + reta_3 > reta_2:
    print(f'Com os comprimentos: {reta_1}, {reta_2} e {reta_3} é possível sim formar um triângulo!')
else:
    print(f'Com os comprimentos: {reta_1}, {reta_2} e {reta_3} não é possível formar um triângulo!')

