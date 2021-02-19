# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai ter tentar adivinhar até acertar, mostrando no final quantos palpites foram nescessários para vencer.

from random import randint

numero_de_tentativas_do_usuario = 0
numero_pensado_pelo_computador = randint(1,10)
numero_escolhido_pelo_usuario = -1
TEXTO_VERMELHO_COM_NEGRITO = ('\033[1;31m')
TEXTO_VERDE_COM_NEGRITO = ('\033[1;32m')
LIMPAR_COR_TEXTO = ('\033[0m')

while numero_escolhido_pelo_usuario != numero_pensado_pelo_computador:
    numero_escolhido_pelo_usuario = int(input('Digite o número que eu estou pensando: '))
    if numero_escolhido_pelo_usuario != numero_pensado_pelo_computador:
        numero_de_tentativas_do_usuario+=1
        print(f'{TEXTO_VERMELHO_COM_NEGRITO}VOCÊ ERROU, TENTE NOVAMENTE!{LIMPAR_COR_TEXTO}')
    else:
        print(f'{TEXTO_VERDE_COM_NEGRITO}VOCÊ ACERTOU!{LIMPAR_COR_TEXTO} O NÚMERO ERA {numero_pensado_pelo_computador}. VOCÊ PRECISOU DE {numero_de_tentativas_do_usuario} TENTATIVAS PARA ACERTAR.')

