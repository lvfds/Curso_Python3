"""
    Faça um programa que leia  o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    Ex: Ana Maria de Sousa
    primeiro = Ana
    último = Sousa

"""

valor_digitado = input('Digite seu nome completo: ')
transformar_valor_digitado_em_lista = valor_digitado.split()
primeiro_nome = transformar_valor_digitado_em_lista[0]
ultimo_nome = transformar_valor_digitado_em_lista[-1]
print(f'Seu primeiro nome é: {primeiro_nome}')
print(f'Seu último nome é: {ultimo_nome}')