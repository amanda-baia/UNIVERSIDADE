#e) Construa um algoritmo que receba a altura em metros, e o peso de uma pessoa. Calcule, então, o Índice de Massa Corporal, o IMC:

h = float(input('digite a altura em metros: '))
p = float(input('digite a peso em kg: '))

IMC = p/(h*h)
print ("O valor do IMC é:", IMC)
