"""
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros_por_extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
numero_digitado = int(input('Digite um número entre 0 e 20: '))
while numero_digitado < 0 or numero_digitado > 20:
    numero_digitado = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros_por_extenso[numero_digitado]}.')