#Calcule o cumprimento da hipotenusa
import math

co = float(input('Insira o valor do cateto oposto:'))
ca = float(input('Insira o valor do cateto adjacente:'))

#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('O valor do cumprimento da hipotenusa é {:.2f}', .format (

hi = math.hypot(co, ca)
print("O valor da hipotenusa é:", hi)
