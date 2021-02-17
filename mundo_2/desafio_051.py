# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No fiaal mostre os 10 primeiros termos dessa progresão.

from time import sleep
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for contador in range(1,11,):
    print(primeiro_termo)
    primeiro_termo+=razao
    sleep(1)


