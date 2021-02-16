# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma_dos_numeros_impares_multiplos_de_tres = 0

for contador in range(1,500):
    if contador % 2 == 1 and contador % 3 == 0:
        soma_dos_numeros_impares_multiplos_de_tres+=contador

print(f'A soma de todos os números ímpares múltiplos de 3 deu: {soma_dos_numeros_impares_multiplos_de_tres}')

