# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

numero_de_dias_alugado = int(input('Digite quantos dias foram alugado o carro: '))
numero_de_km_rodados = float(input('Digite quantos km foram rodados: '))
preco_por_dia_alugado = 60 * numero_de_dias_alugado
preco_por_km_rodado = numero_de_km_rodados * 0.15
preco_final = preco_por_dia_alugado + preco_por_km_rodado
print(f'O total a pagar é R${preco_final:.2f}.')
