"""
    Desenvolva um programa que pergunte a distância de uma viagem em Km.
    calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200km e R$0.45 para viagens mais longas.

"""

distancia_em_km = int(input('Digite a distância em Km da sua viagem: '))
if distancia_em_km <= 200:
    print(f'O valor por Km é R$0.50, sua viagem custará R${distancia_em_km * 0.50:.2f}.')
else:
    print(f'O valor por km é de R$0.45, sua viagem custará R${distancia_em_km * 0.45:.2f}')

