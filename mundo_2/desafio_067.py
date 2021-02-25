"""

    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    O programa será interrompido quando o número solicitado for negativo.

"""
from time import sleep
contador = 0
contador2 = 0
continuar_o_programa = True

while continuar_o_programa == True:
    contador+=1
    numero_digitado = int(input(f'Digite o {contador}° número para fazer sua tabuada(digite um valor negativo para parar): '))
    if numero_digitado >=0:
        contador2+=1
        print('=-='*30)
        while contador2<=10:
            print(f'{numero_digitado:2}  x {contador2:2} = {numero_digitado*contador2:2}')
            contador2+=1
            sleep(1)
        contador2 = 0
        print('=-='*30)
    else:
        print('Finalizando o programa...')
        sleep(1)
        break

