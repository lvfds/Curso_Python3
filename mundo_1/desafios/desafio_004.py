# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo_digitado_pelo_usuario = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo_digitado_pelo_usuario)}')
print(f'Só tem espaços? {algo_digitado_pelo_usuario.isspace()}')
print(f'É um número? {algo_digitado_pelo_usuario.isnumeric()}')
print(f'É alfabético? {algo_digitado_pelo_usuario.isalpha()}')
print(f'É alfanúmerico? {algo_digitado_pelo_usuario.isalnum()}')
print(f'Está em maísculas? {algo_digitado_pelo_usuario.isupper()}')
print(f'Está em minúsculas? {algo_digitado_pelo_usuario.islower()}')
print(f'Está capitalizada? {algo_digitado_pelo_usuario.istitle()}')