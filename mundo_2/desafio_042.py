"""
    Refaça o DESAFIO 035 dos triângulos, acresentando o recurso de mostrar que tipo de triângulo será formado:
    - Equilátero: todos os lados iguais.
    - Isósceles: dois lados iguais.
    - Escaleno: todos os lados diferentes.

"""

cor_vermelha_com_font_negrito = '\033[1;31m'
limpar_cor = '\033[0m'

lado_1 = float(input('Digite o 1° lado do triângulo: '))
lado_2 = float(input('Digite o 2° lado do triângulo: '))
lado_3 = float(input('Digite o 3° lado do triângulo: '))

if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2:
        if lado_1 == lado_2 and lado_2 == lado_3 and lado_3 == lado_1:
            print(f'Os valores {lado_1}, {lado_2} e {lado_3} são iguais, por isso formam um triângulo Equilátero.')
        elif lado_1 == lado_2 or lado_2 == lado_3 or lado_3 == lado_1:
            print(f'Os valores {lado_1}, {lado_2} e {lado_3} possuí dois lados iguais, por isso formam um triângulo Isósceles.')
        else:
            print(f'Os valores {lado_1}, {lado_2} e {lado_3} são diferentes entre si, por isso formam um triângulo Escaleno!')
else:
    print(f'{cor_vermelha_com_font_negrito}Os valores {lado_1}, {lado_2} e {lado_3} NÃO FORMAM UM TRIÂNGULO!{limpar_cor}')
