# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco_produto = float(input('Digite o preço do produto R$'))
desconto = (preco_produto*5) / 100
novo_preco_com_desconto = preco_produto - desconto
print(f'Com 5% de desconto (R${desconto:.2f}) o preço do seu produto ficou R${novo_preco_com_desconto:.2f}.')
