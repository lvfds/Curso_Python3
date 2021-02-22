# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.

from time import sleep
contador = 1
continuar_fatorial = 1
primeiro_termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
while contador <=10:
    if contador == 10:
        print(primeiro_termo)
    else:
        print(primeiro_termo,end=' → ')
        sleep(1)
        primeiro_termo+=razao
    contador+=1

contador = 1


while continuar_fatorial != 0:
    continuar_fatorial = int(input('Digite qualquer maior que 0 para ver mais esse fatorial: '))
    contador = 1
    while contador <= continuar_fatorial:
        if contador == continuar_fatorial:
            print(primeiro_termo)
        else:
            print(primeiro_termo,end=' → ')
            sleep(1)
            primeiro_termo+=razao
        contador+=1

