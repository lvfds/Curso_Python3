"""
    A confederação nacional de natação precisa de um programa que leia o ano de nascimento de atleta e mostre sua categoria, de acordo com a idade:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 20 anos: SÊNIOR
    - Acima: MASTER

"""

categoria_dos_atletas_lista = ['MIRIM','INFANTIL','JUNIOR','SÊNIOR','MASTER']
categoria_dos_atletas = ''

from datetime import datetime

prefixo_do_modulo = datetime.now()
ano_atual = prefixo_do_modulo.year
ano_de_nascimento_usuario = int(input('Digite o seu ano de nascimento: '))
if ano_atual - ano_de_nascimento_usuario <=9:
    categoria_dos_atletas = categoria_dos_atletas_lista[0]
elif ano_atual - ano_de_nascimento_usuario >=10 and ano_atual - ano_de_nascimento_usuario <=14:
    categoria_dos_atletas = categoria_dos_atletas_lista[1]
elif ano_atual -  ano_de_nascimento_usuario <= 19 and ano_atual - ano_de_nascimento_usuario < 20:
    categoria_dos_atletas = categoria_dos_atletas_lista[2]
elif ano_atual - ano_de_nascimento_usuario == 20:
    categoria_dos_atletas = categoria_dos_atletas_lista[3]
else:
    categoria_dos_atletas = categoria_dos_atletas_lista[4]

print(f'De acordo com sua idade {ano_atual - ano_de_nascimento_usuario} anos sua categoria é {categoria_dos_atletas}.')

