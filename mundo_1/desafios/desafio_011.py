"""
Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,pinta uma área de 2m².

"""
largura_da_parede = float(input('Digite a largura da parede em m²: '))
altura_da_parede = float(input('Digite a altura da parede em m²: '))
area_da_parede = largura_da_parede * altura_da_parede
quantidade_de_litros_de_tinta = area_da_parede / 2
print(f'Com a área da parede de {altura_da_parede}m², será nescessário {quantidade_de_litros_de_tinta}L de tinta.')
