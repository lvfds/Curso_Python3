# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere: US$1.00 = R$3.27

quantidade_de_reais = float(input('Digite quantos R$ você tem: '))
reais_convertidos_em_dolares = quantidade_de_reais / 3.27
print(f'Com R${quantidade_de_reais} você poderá comprar US${reais_convertidos_em_dolares:.2f}.')