"""

    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo ela não pode exceder 30% do salário ou então o empréstimo será negado.

"""
cor_vermelha = '\033[41;30m'
remover_cor = '\033[0m'
cor_verde = '\033[42;30m'

valor_da_casa = float(input('Digite o valor da casa R$'))
salario_do_comprador = float(input('Digite o valor do seu salário R$'))
quantos_anos_vai_pagar = int(input('Digite quantos anos vai querer pagar a casa: '))

valor_da_prestacao = valor_da_casa / (quantos_anos_vai_pagar * 12)
trinta_porcento_do_salario = (salario_do_comprador * 30) / 100
if valor_da_prestacao > trinta_porcento_do_salario:
    print(f'{cor_vermelha}EMPRÉSTIMO NEGADO!{remover_cor} O valor da prestação seria de R${valor_da_prestacao:.2f} que ultrapaça 30% do seu salário que é de R${trinta_porcento_do_salario:.2f}.')
else:
    print(f'{cor_verde}EMPRÉSTIMO APROVADO!{remover_cor} O valor da sua prestação ficou em R${valor_da_prestacao:.2f} durante {quantos_anos_vai_pagar} anos.')