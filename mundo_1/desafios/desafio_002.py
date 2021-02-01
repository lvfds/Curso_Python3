# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia_de_nascimento = int(input('Digite o dia que você nasceu: '))
mes_de_nascimento = input('Digite o mês que você nasceu [OBS: O nome do mês, não o número.]: ')
ano_de_nascimento = int(input('Digite o ano que você nasceu: '))

print(f'Você nasceu no dia {dia_de_nascimento} do mês de {mes_de_nascimento} do ano de {ano_de_nascimento}. Correto?')