# c) Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um acréstimo de 8 \por cento de imposto:

p = float(input('digite o valor de um número produto'))
vf = p + (p * 8/100)
print ("O valor final do produto, acrescido do valor do imposto é:", vf)
