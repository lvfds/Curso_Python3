"""

    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se já passou o tempo do alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""

from datetime import datetime

cor_do_texto_vermelho = '\033[1;31m'
limpar_cor = '\033[0m'

prefixo_modulo = datetime.now()
ano_atual = prefixo_modulo.year
ano_de_nascimento_usuario = int(input('Digite o seu ano de nascimento: '))
if ano_atual - ano_de_nascimento_usuario == 18:
    print(f'Você tem {ano_atual - ano_de_nascimento_usuario} anos, está na hora de se alistar!')
elif ano_atual - ano_de_nascimento_usuario < 18:
    print(f'Você tem {ano_atual - ano_de_nascimento_usuario} anos, ainda faltam { 18 -(ano_atual - ano_de_nascimento_usuario) } anos para poder se alistar!')
else:
    print(f'{cor_do_texto_vermelho}VOCÊ TEM {ano_atual - ano_de_nascimento_usuario} ANOS, JÁ SE PASSOU {(ano_atual - ano_de_nascimento_usuario) - 18} ANOS DO PRAZO PARA SE ALISTAR!{limpar_cor}')

