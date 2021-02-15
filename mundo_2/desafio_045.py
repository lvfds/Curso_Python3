# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from emoji import emojize

# Cores do texto:
TEXTO_VERMELHO_EM_NEGRITO = '\033[1;31m'
TEXTO_VERDE_EM_NEGRITO = '\033[1;32m'
LIMPAR_COR_DA_FONTE = '\033[0m'

# Listas com os dados mais importantes:
opcoes_do_jogo = ['PEDRA','PAPEL','TESOURA']
emojis_das_maos = [emojize(':fist:',use_aliases=True),emojize(':hand:',use_aliases=True),emojize(':v:',use_aliases=True)]

# Mãos dos jogadores
mao_do_computador = choice(opcoes_do_jogo)
mao_do_jogador = ''

opcao_valida = False

print(f"""
Escolha uma dessas opções:
[ 1 ] para jogar {emojis_das_maos[0]}.
[ 2 ] para jogar {emojis_das_maos[1]}.
[ 3 ] para jogar {emojis_das_maos[2]}.
""")
opcao_escolhida_pelo_usuario = input('Digite a opção escolhida: ')
if opcao_escolhida_pelo_usuario.isnumeric() != True:
    print(f'{TEXTO_VERMELHO_EM_NEGRITO}ERRO: O VALOR {opcao_escolhida_pelo_usuario} É INVÁLIDO PARA O JOGO!{LIMPAR_COR_DA_FONTE}')
elif opcao_escolhida_pelo_usuario.isnumeric() == True and int(opcao_escolhida_pelo_usuario) > 0 and int(opcao_escolhida_pelo_usuario) <=3:
    opcao_valida = True
    if int(opcao_escolhida_pelo_usuario) == 1:
        mao_do_jogador = opcoes_do_jogo[0]
    elif int(opcao_escolhida_pelo_usuario) == 2:
        mao_do_jogador = opcoes_do_jogo[1]
    elif int(opcao_escolhida_pelo_usuario) == 3:
        mao_do_jogador = opcoes_do_jogo[2]
else:
    print(f'{TEXTO_VERMELHO_EM_NEGRITO}ERRO: O NÚMERO {opcao_escolhida_pelo_usuario} É UMA OPÇÃO INVÁLIDA!{LIMPAR_COR_DA_FONTE}')

if opcao_valida == True:
    if mao_do_jogador == 'PEDRA' and mao_do_computador == 'TESOURA':
        print(
            f'{emojis_das_maos[0]} x {emojis_das_maos[2]}. {TEXTO_VERDE_EM_NEGRITO}VOCÊ GANHOU!{LIMPAR_COR_DA_FONTE}')
    elif mao_do_jogador == 'PAPEL' and mao_do_computador == 'PEDRA':
        print(
            f'{emojis_das_maos[1]} x {emojis_das_maos[0]}. {TEXTO_VERDE_EM_NEGRITO}VOCÊ GANHOU!{LIMPAR_COR_DA_FONTE}')
    elif mao_do_jogador == 'TESOURA' and mao_do_computador == 'PAPEL':
        print(
            f'{emojis_das_maos[2]} x {emojis_das_maos[1]}. {TEXTO_VERDE_EM_NEGRITO}VOCÊ GANHOU!{LIMPAR_COR_DA_FONTE}')
        # Vitória da máquina
    elif mao_do_computador == 'PEDRA' and mao_do_jogador == 'TESOURA':
        print(
            f'{emojis_das_maos[0]} x {emojis_das_maos[2]}. {TEXTO_VERMELHO_EM_NEGRITO}VOCÊ PERDEU!{LIMPAR_COR_DA_FONTE}')
    elif mao_do_computador == 'PAPEL' and mao_do_jogador == 'PEDRA':
        print(
            f'{emojis_das_maos[1]} x {emojis_das_maos[0]}. {TEXTO_VERMELHO_EM_NEGRITO}VOCÊ PERDEU!{LIMPAR_COR_DA_FONTE}')
    elif mao_do_computador == 'TESOURA' and mao_do_jogador == 'PAPEL':
        print(
            f'{emojis_das_maos[2]} x {emojis_das_maos[1]}. {TEXTO_VERMELHO_EM_NEGRITO}VOCÊ PERDEU!{LIMPAR_COR_DA_FONTE}')
    elif mao_do_computador == 'PEDRA' and mao_do_jogador == 'PEDRA' or mao_do_jogador == 'PEDRA' and mao_do_computador == 'PEDRA':
        print(f'{emojis_das_maos[0]} x {emojis_das_maos[0]}. EMPATE!')
    elif mao_do_computador == 'PAPEL' and mao_do_jogador == 'PAPEL' or mao_do_jogador == 'PAPEL' and mao_do_computador == 'PAPEL':
        print(f'{emojis_das_maos[1]} x {emojis_das_maos[1]}. EMPATE!')
    else:
        print(f'{emojis_das_maos[2]} x {emojis_das_maos[2]}. EMPATE!')

