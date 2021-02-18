# Crie um programa que leia uma frase qualquer e diga se é um palíndomo, desconsiderando os espaços. Ex: APOS A SOPA.

frase_digitada_pelo_usuario = input('Digite uma frase: ').strip()
formatar_frase = frase_digitada_pelo_usuario.replace(' ','').lower()
if formatar_frase[::-1] == formatar_frase:
    print(f'A frase: {frase_digitada_pelo_usuario} é um palíndomo!')
else:
    print(f'A frase: {frase_digitada_pelo_usuario} não é um palíndomo!')

