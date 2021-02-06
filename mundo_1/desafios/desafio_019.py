# um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno_1 = input('Digite o nome do(a) 1º(ª) aluno(a): ')
aluno_2 = input('Digite o nome do(a) 2°(ª) aluno(a): ')
aluno_3 = input('Digite o nome do(a) 3º(ª) aluno(a): ')
aluno_4 = input('Digite o nome do(a) 4°(ª) aluno(a): ')

lista_com_os_nomes_dos_alunos = [aluno_1,aluno_2,aluno_3,aluno_4]

print(f'O(A) aluno(a) escolhido(a) foi: {random.choice(lista_com_os_nomes_dos_alunos)}.')