# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from emoji import emojize

TEXTO_VERMELHO_COM_NEGRITO = '\033[1;31m'
TEXTO_VERDE_COM_NEGRITO = '\033[1;32m'
LIMPAR_A_COR_DO_TEXTO = '\033[0m'

opcoes_para_escolher = ['Pedra','Papel','Tesoura']
mao_do_usuario = ''
mao_do_computador = choice(opcoes_para_escolher)
numero_digitado_pelo_usuario = 0
opcao_escolhida_pelo_usuario = input("""

ESCOLHA UMA DESSAS OPÇÕES:
1 | Para pedra.
2 | Para papel.
3 | Para tesoura.

Digite aqui sua opção: """)
if opcao_escolhida_pelo_usuario.isnumeric() == True:
    numero_digitado_pelo_usuario = int(opcao_escolhida_pelo_usuario)
    if numero_digitado_pelo_usuario == 1:
        mao_do_usuario = opcoes_para_escolher[0]
    elif numero_digitado_pelo_usuario == 2:
        mao_do_usuario = opcoes_para_escolher[1]
    elif numero_digitado_pelo_usuario == 3:
        mao_do_usuario = opcoes_para_escolher[2]
        if mao_do_usuario == 'Pedra' and mao_do_computador == 'Tesoura':
            print(emojize(
                f'Você escolheu : :fist: e o computador: :v: \n{TEXTO_VERDE_COM_NEGRITO}VOCÊ GANHOU!{LIMPAR_A_COR_DO_TEXTO}',
                use_aliases=True))
        elif mao_do_usuario == 'Tesoura' and mao_do_computador == 'Papel':
            print(emojize(
                f'Você escolheu : :v: e o computador: :hand: \n{TEXTO_VERDE_COM_NEGRITO}VOCÊ GANHOU!{LIMPAR_A_COR_DO_TEXTO}',
                use_aliases=True))
        elif mao_do_usuario == 'Papel' and mao_do_computador == 'Pedra':
            print(emojize(
                f'Você escolheu: :hand: e o computador: :fist: \n{TEXTO_VERDE_COM_NEGRITO}VOCÊ GANHOU!{LIMPAR_A_COR_DO_TEXTO}',
                use_aliases=True))
        elif mao_do_computador == 'Pedra' and mao_do_usuario == 'Tesoura':
            print(emojize(
                f'Você escolheu: :v: e o computador: :fist: \n{TEXTO_VERMELHO_COM_NEGRITO}VOCÊ PERDEU!{LIMPAR_A_COR_DO_TEXTO}',
                use_aliases=True))
        elif mao_do_computador == 'Tesoura' and mao_do_usuario == 'Papel':
            print(emojize(
                f'Você escolheu: :hand: e o computador escolheu: :v: \n{TEXTO_VERMELHO_COM_NEGRITO}VOCÊ PERDEU!{LIMPAR_A_COR_DO_TEXTO}',
                use_aliases=True))
        elif mao_do_computador == 'Papel' and mao_do_usuario == 'Pedra':
            print(emojize(
                f'Você escolheu: :hand: e o computador: :fist: \n{TEXTO_VERMELHO_COM_NEGRITO}VOCÊ PERDEU!{LIMPAR_A_COR_DO_TEXTO}',
                use_aliases=True))
        else:
            if mao_do_usuario == 'Pedra' and mao_do_computador == 'Pedra':
                print(emojize('Você escolheu: :fist: e o computador: :fist: \nEMPATE!', use_aliases=True))
            elif mao_do_usuario == 'Papel' and mao_do_computador == 'Papel':
                print(emojize('Você escolheu: :hand: e o computador: :hand: \nEMPATE!', use_aliases=True))
            else:
                print(emojize('Você escolheu: :v: e o computador: :v: \nEMPATE!', use_aliases=True))
    else:
        print(f'{TEXTO_VERMELHO_COM_NEGRITO}ERRO: O NÚMERO {numero_digitado_pelo_usuario} NÃO É VALIDO COMO OPÇÃO!{LIMPAR_A_COR_DO_TEXTO}')

else:
    print(f'{TEXTO_VERMELHO_COM_NEGRITO}ERRO: O VALOR {opcao_escolhida_pelo_usuario} NÃO É VÁLIDO PARA ESSE JOGUINHO!{LIMPAR_A_COR_DO_TEXTO}')
