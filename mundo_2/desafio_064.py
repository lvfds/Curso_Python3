"""
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quanto o usuário digitar o valor 999, que é a condição de parada.
    No final mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsiderando o flag)

"""

contador_de_vezes_o_usuario_digitou = 0
contador = 1
cancelar_programa = 1
soma_de_todos_os_numeros = 0
while cancelar_programa != 999:
    numero_digitado = int(input(f'Digite o {contador}° número: '))
    if numero_digitado == 999:
        print(f'Foram {contador_de_vezes_o_usuario_digitou} números digitados ao total e a soma deles é = {soma_de_todos_os_numeros}.')
        cancelar_programa = 999
    else:
        cancelar_programa = numero_digitado
        contador_de_vezes_o_usuario_digitou+=1
        soma_de_todos_os_numeros+=numero_digitado
        contador+=1

