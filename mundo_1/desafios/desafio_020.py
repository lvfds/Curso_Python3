# O mesmo professor do desafio anterior quer sortear a ordem de apresentaçãode trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno_1 = input('Digite o nome do(a) 1º(ª) aluno(a): ')
aluno_2 = input('Digite o nome do(a) 2º(ª) aluno(a): ')
aluno_3 = input('Digite o nome do(a) 3º(ª) aluno(a): ')
aluno_4 = input('Digite o nome do(a) 4°(ª) aluno(a): ')

lista_com_os_nomes_dos_alunos = [aluno_1,aluno_2,aluno_3,aluno_4]
shuffle(lista_com_os_nomes_dos_alunos)
print(f'A ordem de apresentação ficou assim: {lista_com_os_nomes_dos_alunos}')