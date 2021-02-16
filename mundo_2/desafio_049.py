# Refaça o DEAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

from time import sleep
numero_escolhido_pelo_usuario = int(input('Digite o número para ver sua tabela: '))
for contador in range(1,11):
    print(f'O número {numero_escolhido_pelo_usuario} x {contador:2} = {numero_escolhido_pelo_usuario*contador}')
    sleep(1)

