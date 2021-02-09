"""
    Escreva um programa que faça  o computador 'Pensar' em um número inteiro entre 0 e 5
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

"""
from random import randint

numero_gerado_aleatoriamente = randint(0,5)
numero_digitado_pelo_usuario = int(input('Adivinhe qual número estou pensando, uma dica: é entre 0 e 5! '))

if numero_digitado_pelo_usuario == numero_gerado_aleatoriamente:
    print(f'VOCÊ ACERTOU! O número que estava pensando era mesmo o {numero_gerado_aleatoriamente}!')
else:
    print(f'Você errou! O número que pensei era {numero_gerado_aleatoriamente}')

