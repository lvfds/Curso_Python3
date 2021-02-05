# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa.

import math
comprimento_cateto_oposto = int(input('Digite o comprimento do cateto oposto: '))
comprimento_cateto_adjacente = int(input('Digite o comprimento do cateto adjacente: '))
calculo_da_hipotenusa = pow(comprimento_cateto_oposto,2) + pow(comprimento_cateto_adjacente,2)
comprimento_da_hipotenusa = math.sqrt(calculo_da_hipotenusa)
print(f'O comprimento da hipotenusa é: {comprimento_da_hipotenusa}.')
