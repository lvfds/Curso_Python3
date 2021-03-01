"""
    Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar.
    No final, mostre:
    A)  Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$1000.
    C) Qual é o nome do produto mais barato.

"""
total_gasto_na_compra = 0
produtos_que_passam_de_mil = 0
nome_produto_mais_barato = ''
preco_do_produto_mais_barato = 0
continuar_programa = True
contador = 1

print('-'*30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print(f'-'*30)

while continuar_programa == True:
    nome_produto = input('Digite o nome do produto: ').strip()
    preco_do_produto = float(input('Digite o preço do produto: R$'))
    if preco_do_produto > 1000:
        produtos_que_passam_de_mil+=1
    elif contador == 1:
        nome_produto_mais_barato = nome_produto
        preco_do_produto_mais_barato = preco_do_produto
        contador+=1
    elif contador > 1:
        if preco_do_produto < preco_do_produto_mais_barato:
            preco_do_produto_mais_barato = preco_do_produto
            nome_produto_mais_barato = nome_produto
            contador+=1
    total_gasto_na_compra+=preco_do_produto
    opcao_do_usuario = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while opcao_do_usuario != 'S' and opcao_do_usuario != 'N':
        opcao_do_usuario = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if opcao_do_usuario != 'S':
        break

print(f'O total da compra foi R${total_gasto_na_compra:.2f}')
print(f'Temos {produtos_que_passam_de_mil} produtos que passam de R$1000.00.')
print(f'O produto mais barato foi {nome_produto_mais_barato} que custa {preco_do_produto_mais_barato:.2f}')
