"""
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do peso.
    - Entre 18.5 e 25: Peso ideal.
    - Entre 25 e 30: Sobrepeso.
    - Entre 30 e 40: Obesidade.
    - Acima de 40: Obsidade mórbida.

"""
cor_vermelha_fonte_negrito = '\033[1;31m'
limpa_cor = '\033[0m'

peso_em_kg_usuario = float(input('Digite o seu peso: '))
altura_usuario = float(input('Digite a sua altura:  '))

imc = peso_em_kg_usuario / (altura_usuario * altura_usuario)
if imc < 18.5:
    print(f'Seu IMC deu {imc:.2f}, então você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC deu {imc:.2f}, então você está com o PESO IDEAL.')
elif imc >=25 and imc   <= 30:
    print(f'Seu IMC deu {imc:.2f}, então você está com SOBREPRESO.')
elif imc >=30 and imc <=40:
    print(f'{cor_vermelha_fonte_negrito}PERIGO! SEU IMC DEU {imc:.2f}, VOCÊ ESTÁ COM OBESIDADE!{limpa_cor}')
else:
    print(f'{cor_vermelha_fonte_negrito}PERIGO! SEU IMC DEU {imc:.2f}, VOCÊ ESTÁ COM OBESIDADE MÓRBIDA!{limpa_cor}')

