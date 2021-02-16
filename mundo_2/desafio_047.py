# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep
for contador in range(1,50):
    if contador % 2 == 0:
        print(f'Estou no número: {contador}')
        sleep(1)

