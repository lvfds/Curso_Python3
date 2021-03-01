"""
    Faça um programa que jogue par ou ímpar com o computador.
    O jogo só será interropido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
"""

from unidecode import unidecode
from time import sleep
from random import randint

continuar_programa = True
numero_de_vitorias_consecutivas = 0
TEXTO_EM_VERMELHO_EM_NEGRITO = ('\033[1;31m')
TEXTO_VERDE_EM_NEGRITO = ('\033[1;32m')
FORMATAR_FONTE = ('\033[0m')

print('-'*29)
print(f'{"| VAMOS JOGAR PAR OU ÍMPAR! |":^30}')
print('-'*29)

while continuar_programa == True:
    numero_digitado = int(input('Digite um número: '))
    opcao_escolhida = input('Par ou Ímpar? [P/Í] ').strip().upper()[0]
    opcao_escolhida = unidecode(opcao_escolhida)
    numero_gerado = randint(0,5)
    if opcao_escolhida == 'P' and (numero_digitado +  numero_gerado)%2 == 0:
        print(f'{TEXTO_VERDE_EM_NEGRITO}VOCÊ VENCEU!{FORMATAR_FONTE}')
        print(f'Você jogou {numero_digitado} e o computador {numero_gerado}. No total deu {numero_digitado+numero_gerado}. É PAR!')
        numero_de_vitorias_consecutivas+=1
        sleep(1)
    elif opcao_escolhida == 'I' and (numero_digitado + numero_gerado)%2 == 1:
        print(f'{TEXTO_VERDE_EM_NEGRITO}VOCÊ VENCEU!{FORMATAR_FONTE}')
        print(f'Você jogou {numero_digitado} e o computador {numero_gerado}. No total deu {numero_digitado+numero_gerado}. É ÍMPAR!')
        numero_de_vitorias_consecutivas+=1
    elif opcao_escolhida != 'P' and opcao_escolhida != 'I':
            print(f'{TEXTO_EM_VERMELHO_EM_NEGRITO}O VALOR {opcao_escolhida} NÃO FOI RECONHECIDO! TENTE NOVAMENTE!{FORMATAR_FONTE}')
    else:
        print(f'{TEXTO_EM_VERMELHO_EM_NEGRITO}VOCÊ PERDEU!{FORMATAR_FONTE}')
        opcao_do_pc = ''
        if opcao_escolhida == 'P':
            opcao_do_pc = 'ÍMPAR'
        else:
            opcao_do_pc = 'PAR'
        print(f'Você jogou {numero_digitado} e o computador {numero_gerado}. No total deu {numero_digitado+numero_gerado}. É {opcao_do_pc} ')
        break

print(f'{TEXTO_EM_VERMELHO_EM_NEGRITO}GAME OVER! você venceu {numero_de_vitorias_consecutivas} vezes.')

