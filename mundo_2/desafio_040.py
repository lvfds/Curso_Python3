"""
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 5.0:
        REPROVADO
    - Média entre 5.0 e 6.9:
        RECUPERAÇÃO
    - Média 7.0 ou superior:
        APROVADO

"""

cor_vermelha = '\033[1;31m'
cor_verde = '\033[1;32m'
cor_magenta = '\033[1;35m'
limpar_cores = '\033[0m'

nota_1 = float(input('Digite a sua 1ª nota: '))
nota_2 = float(input('Digite a sua 2ª nota: '))
media = (nota_1 + nota_2) / 2

mensagem_final = [f'{cor_verde}SUA MÉDIA É {media}, VOCÊ ESTÁ APROVADO(A)!{limpar_cores}',f'{cor_vermelha}SUA MÉDIA É {media}, VOCÊ ESTÁ REPROVADO(A)!{limpar_cores}',f'{cor_magenta}SUA MÉDIA É DE {media}, VOCÊ ESTÁ DE RECUPERAÇÃO!{limpar_cores}']

if media >= 7.0:
    print(mensagem_final[0])
elif media < 5.0:
    print(mensagem_final[1])
else:
    print(mensagem_final[2])

