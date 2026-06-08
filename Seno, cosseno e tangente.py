#Seno, cosseno e tangente

from math import sin, cos, tan, radians
angulo = float(input('Insira o valor do ângulo:'))

#Vamos imprimir o seno do ângulo informado:
sen = sin(radians(angulo))
print ('O valor do ângulo é {}º, TEM SENO de {:.2f}'.format (angulo, sen))

#Vamos imprimir o cosseno do ângulo informado:
cos = cos(radians(angulo))
print('O ângulo de {}º tem o COSSENO de {:.2f}' .format(angulo, cos))

#Vamos imprimir a tangente do ângulo informado:
tan = tan(radians(angulo))
print('O ângulo de {}º tem a tangente de {:.2f}'.format(angulo, tan))

