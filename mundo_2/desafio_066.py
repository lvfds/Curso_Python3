"""

    Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada.
    No final mostre quantos números foram digitados e qual foi a soma entres.(desconsiderando o flag)

"""

contador = 0
quantidade_de_numeros_digitados = 0
soma_de_todos_os_numeros_digitados = 0
continuar_programa = True
while continuar_programa == True:
    contador+=1
    numero_digitado = int(input(f'Digite o {contador}° número (digite 999 para parar o programa): '))
    if numero_digitado == 999:
        break
    soma_de_todos_os_numeros_digitados+=numero_digitado
    quantidade_de_numeros_digitados+=1
print(f'A soma dos {quantidade_de_numeros_digitados} números digitados foi {soma_de_todos_os_numeros_digitados}.')

