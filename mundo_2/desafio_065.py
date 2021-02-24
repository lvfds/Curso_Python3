"""
    Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média de entre todos os valores e qual foi o maior e menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar mais valores.

"""

continuar_o_programa = True
maior_numero_digitado = 0
menor_numero_digitado = 0
contador = 0
quantidade_de_numeros_digitados = 0
soma_de_todos_os_numeros_digitados = 0

while continuar_o_programa == True:
    contador += 1
    numero_digitado = int(input(f'Digite o {contador}° número: '))
    if contador == 1:
        maior_numero_digitado = numero_digitado
        menor_numero_digitado = numero_digitado
    else:
        if maior_numero_digitado < numero_digitado:
             maior_numero_digitado = numero_digitado
        elif menor_numero_digitado > numero_digitado:
            menor_numero_digitado = numero_digitado
    soma_de_todos_os_numeros_digitados+=numero_digitado
    quantidade_de_numeros_digitados+=1
    opcao_escolhida_pelo_usuario = input('Você quer continuar [S/N]? ').upper().strip()
    if opcao_escolhida_pelo_usuario != 'S':
        media_dos_numeros_digitados = soma_de_todos_os_numeros_digitados / quantidade_de_numeros_digitados
        continuar_o_programa = False
        if maior_numero_digitado == menor_numero_digitado and contador == 1:
            print(f'A média do {quantidade_de_numeros_digitados} número digitado é: {media_dos_numeros_digitados} e não há maior valor pois {maior_numero_digitado} e {menor_numero_digitado} são iguais!')
        elif maior_numero_digitado == menor_numero_digitado and contador > 1:
            print(f'A média dos {quantidade_de_numeros_digitados} números digitados é: {media_dos_numeros_digitados} e não há maior valor pois {maior_numero_digitado} e {menor_numero_digitado} são iguais!')
        else:
            print(f'A média dos {quantidade_de_numeros_digitados} números digitados é: {media_dos_numeros_digitados}. {maior_numero_digitado} é maior número e {menor_numero_digitado} é o menor número digitado.')

