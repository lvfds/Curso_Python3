# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma_dos_numeros_pares = 0
for contador in range(1,7):
    numero_digitado_pelo_usuario = int(input(f'Digite o {contador}° número: '))
    if numero_digitado_pelo_usuario % 2 == 0:
        soma_dos_numeros_pares+=numero_digitado_pelo_usuario

print(f'A soma de todos os números pares foi: {soma_dos_numeros_pares}')

