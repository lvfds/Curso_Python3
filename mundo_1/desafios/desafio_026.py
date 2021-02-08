"""
    Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra 'A'.
    - Em que posição ela aparece a primeira vez.
    - Em que posição ela aparece pela última vez.

"""

frase_digitada = input('Digite uma frase: ')
print(f'A palavra "A" aparece: {frase_digitada.upper().count("A")} vezes.')
print(f'A posição do primeiro "A" é: {frase_digitada.upper().index("A")}')
print(f'A posição do último "A" é: {frase_digitada.upper().rindex("A")}')
