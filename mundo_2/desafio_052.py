# Faça um programa que leia um número inteiro diga se ele é o não um número primo.

numero_digitado_pelo_usuario = int(input('Digite um número qualquer: '))

if numero_digitado_pelo_usuario != 1 and  numero_digitado_pelo_usuario % 2 != 0 and numero_digitado_pelo_usuario % 3 != 0 and numero_digitado_pelo_usuario % 5 != 0 and numero_digitado_pelo_usuario % 7 != 0 or numero_digitado_pelo_usuario == 2:
    print(f'O número {numero_digitado_pelo_usuario} é primo!')
else:
    print(f'O número {numero_digitado_pelo_usuario} não é primo!')