"""
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    - À vista dinheiro/cheque: 10% de desconto.
    - À vista no cartão: 5% de desconto.
    - Em até 2x no cartão: preço normal.
    - 3x ou mais no cartão: 20% de juros.

"""
desconto = 0
texto_vermelho_com_fonte_negrito = '\033[1;31m'
limpar_cor = '\033[0m'

preco_do_produto = float(input('Digite o preço do produto: R$'))
menu_com_as_opcoes = int(input("""

Métodos de pagamento:
- 1 | À vista em dinheiro ou cheque.
- 2 | À vista no cartão.
- 3 | Parcelado no cartão.

Digite aqui a opção de pagamento escolhida: """))
if menu_com_as_opcoes == 1:
    desconto = (preco_do_produto * 10) / 100
    print(f'Como você resolveu pagar em dinheiro/cheque o preço do produto ficou: R${preco_do_produto - desconto:.2f}')
elif menu_com_as_opcoes == 2:
    desconto = (preco_do_produto * 5 ) / 100
    print(f'Como você resolveu pagar à vista no cartão o preço do produto ficou: R${preco_do_produto - desconto:.2f}')
elif menu_com_as_opcoes == 3:
    numero_de_parcelas = int(input('Digite quantas parcelas você quer pagar: '))
    if numero_de_parcelas > 0 and numero_de_parcelas <=2:
        print(f'Você resolveu parcelar em {numero_de_parcelas}x, o preço das parcelas ficaram em R${preco_do_produto / numero_de_parcelas:.2f} e o preço cheio ficou em : R${preco_do_produto:.2f}')
    elif numero_de_parcelas >= 3:
        juros = (preco_do_produto * 20 ) / 100
        print(f'Você resolveu parcelar em {numero_de_parcelas}x, o preço das parcelas ficaram em R${(preco_do_produto + juros ) / numero_de_parcelas:.2f} e o preço cheio ficou em  R${preco_do_produto + juros:.2f}')
    else:
        print(f'{texto_vermelho_com_fonte_negrito}NÃO É POSSÍVEL FAZER ESSE NÚMERO DE PARCELAS!{limpar_cor}')

else:
    print(f'{texto_vermelho_com_fonte_negrito}NÃO FOI RECONHECIDO ESSE TIPO DE PAGAMENTO!{limpar_cor}')