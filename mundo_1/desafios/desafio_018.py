# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo_digitado_em_graus_pelo_usuario = int(input('Digite um ângulo qualquer: '))
graus_convertido_em_radianos = math.radians(angulo_digitado_em_graus_pelo_usuario)
radianos_convertido_para_seno = math.cos(graus_convertido_em_radianos)
radianos_convertido_para_cosseno = math.sin(graus_convertido_em_radianos)
radianos_convertidos_para_tangente= math.tan(graus_convertido_em_radianos)
print(f'O valor do seno é {radianos_convertido_para_seno:.2f}.')
print(f'O valor do cosseno é {radianos_convertido_para_cosseno:.2f}.')
print(f'O valor da tangente é {radianos_convertidos_para_tangente:.2f}.')