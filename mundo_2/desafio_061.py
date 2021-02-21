# Refaça o DESAFIO 051, lendo o primeiro termo e a ração de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

from time import sleep
contador = 1
primeiro_termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
while contador <=10:
    if contador == 10:
        print(primeiro_termo)
    else:
        print(primeiro_termo, end=' → ')
        sleep(1)
    primeiro_termo += razao
    contador+=1

