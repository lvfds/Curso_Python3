"""
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada km acima do limite.

"""

velocidade_do_carro = int(input('Digite a velocidade do carro: '))
if velocidade_do_carro <= 80:
    print(f'Você está à {velocidade_do_carro}Km/h, está dentro da velocidade permitida.')
else:
    multa = (velocidade_do_carro - 80) * 7.00
    print(f'Com {velocidade_do_carro}Km/h você ultrapassou a velocidade limite, então foi multado em R${multa:.2f}.')

